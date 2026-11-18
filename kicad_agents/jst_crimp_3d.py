"""Generate verified reference STEP and studio renders for JST cable parts."""
import argparse

import cadquery as cq

from kicad_agents.crimp_3d import generate
from working_oomp_populate_connector_crimp_data import MODEL_ASSETS
from working_oomp_populate_connector_jst_cable_data import FAMILIES, PARTS, PDF_OWNERS, SOURCE_ROOT


def _box(length, depth, height, y=0, z=0, x=0):
    return (cq.Workplane("XY").box(length, depth, height, centered=(True, False, False))
            .translate((x, y, z)))


def housing_model(row):
    length, depth, height = (row["dimensions_mm"][key] for key in ("length", "width", "height"))
    family = row["family"]
    count, pitch = row["positions"], row["pitch_mm"]
    # The broad wire-entry flange is full width. The SH variant with
    # protrusions keeps its two ears at this end. PH and XH have a stepped body.
    flange_depth = {"sh": 1, "gh": 0.72, "ph": 0.8, "xh": 0.7}[family]
    inset = 1 if row["protrusions"] else {"sh": 0, "gh": 0.23, "ph": 0.27, "xh": 0.31}[family]
    undercut = {"sh": 0.28, "gh": 0.78, "ph": 0.38, "xh": 0.36}[family]
    body = _box(length - 2 * inset, depth - flange_depth + 0.08, height - undercut,
                z=undercut / 2)
    flange = _box(length, flange_depth, height, y=depth - flange_depth).edges("|Z").chamfer(0.05)
    part = body.union(flange)
    if family == "gh":
        latch = _box(length - 2.25, depth * 0.72, 0.62, depth * 0.16, height - 0.62)
        part = part.union(latch.edges("|Y").chamfer(0.1))
    aperture, aperture_z, tunnel_z = {
        "sh": (0.43, 0.55, 0.98), "gh": (0.49, 0.58, 1.22),
        "ph": (0.86, 1.02, 1.75), "xh": (0.96, 1.02, 2.2),
    }[family]
    cutters = []
    for index in range(count):
        x = pitch * (index - (count - 1) / 2)
        # Clearance steps and tapered openings reproduce the drawing's
        # visible shape. Their unlabelled dimensions are reference estimates.
        center_z = height * (0.58 if family == "xh" else 0.50)
        opening = cq.Workplane("XZ", origin=(x, -0.01, center_z))
        opening = (opening.rect(aperture * 1.25, aperture_z * 1.22)
                   .workplane(offset=-0.36).rect(aperture, aperture_z).loft())
        throat = _box(aperture, depth + 0.02, aperture_z, -0.01, center_z - aperture_z / 2, x)
        rear = _box(aperture * 1.57, depth * 0.58, tunnel_z,
                    depth * 0.43, center_z - tunnel_z / 2, x)
        cutters.extend((opening.val(), throat.val(), rear.val()))
        if family in ("sh", "ph"):
            slot = _box(aperture * 0.73, depth * 0.47, height * 0.22,
                        depth * 0.12, height * 0.81, x)
            cutters.append(slot.val())
        if family == "xh":
            recess = _box(aperture * 0.82, 0.62, 0.38, -0.01, 0.70, x)
            cutters.append(recess.val())
    # Cut the whole row at once so long housings do not repeatedly rebuild
    # all of the already-cut boundary faces.
    part = cq.Workplane("XY").newObject([part.val().cut(*cutters)])
    if family == "xh":
        for x in (-length / 2 + 0.8, length / 2 - 0.8):
            rib = _box(0.46, depth * 0.64, undercut / 2 + 0.10, depth * 0.15,
                       height - undercut / 2 - 0.10, x)
            part = part.union(rib)
    return part.val()


def contact_model(row):
    length, width, height = (row["dimensions_mm"][key] for key in ("length", "width", "height"))
    thickness = width * 0.13
    socket_width = width * 0.82
    socket_height = 0.55 if row["family"] == "gh" else height * 0.70
    socket_length = length * (0.46 if row["family"] == "gh" else 0.32)
    lip = cq.Workplane("XY").box(socket_length, socket_width, socket_height,
                               centered=(False, True, False))
    lip = lip.edges("|X").fillet(thickness * 0.55)
    bore = cq.Workplane("XY").box(socket_length + 0.02, socket_width - 2 * thickness,
                                socket_height - 2 * thickness, centered=(False, True, False))
    lip = lip.cut(bore.translate((-0.01, 0, thickness)))
    part = lip.union(_box(length - socket_length + 0.04, width * 0.45, thickness)
                     .translate(((length + socket_length - 0.04) / 2, -width * 0.225, 0)))
    for start, end, half_width, wing_height in (
        (length * 0.46, length * 0.65, width * 0.44, height * 0.73),
        (length * 0.76, length, width / 2, height),
    ):
        base = width * 0.20
        outline = [
            (-half_width, wing_height), (-base, 0), (base, 0), (half_width, wing_height),
            (half_width - thickness, wing_height), (base - thickness / 2, thickness),
            (-base + thickness / 2, thickness), (-half_width + thickness, wing_height),
        ]
        wings = cq.Workplane("YZ", origin=(start, 0, 0)).polyline(outline).close()
        part = part.union(wings.extrude(end - start))
    return part.val()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("selection", nargs="+", help="Exact MPNs, SH/GH/PH/XH, or all")
    parser.add_argument("--missing-only", action="store_true", help="Skip complete source assets")
    args = parser.parse_args()
    names = {name.upper() for name in args.selection}
    choices = {row["mpn"] for row in PARTS} | {"ALL"} | {family.upper() for family in FAMILIES}
    if names - choices:
        parser.error(f"Unknown JST selection: {', '.join(sorted(names - choices))}")
    for row in PARTS:
        if not names.intersection({"ALL", row["family"].upper(), row["mpn"]}):
            continue
        source = SOURCE_ROOT / row["id"]
        if args.missing_only and all((source / name).is_file() for name in MODEL_ASSETS):
            continue
        source.mkdir(exist_ok=True)
        drawing = SOURCE_ROOT / PDF_OWNERS[row["family"]] / "datasheet.pdf"
        builder = housing_model if row["role"] == "cable_housing" else contact_model
        generate(row, model_builder=builder, drawing=drawing, generator="kicad_agents/jst_crimp_3d.py",
                 render_options={"samples": 32, "resolution": 768})


if __name__ == "__main__":
    main()
