"""Build drawing-based Harwin M20 reference STEP models and preview PNGs."""

import argparse
import hashlib
import math
from pathlib import Path
from tempfile import TemporaryDirectory

import cadquery as cq
import yaml

from working_oomp_populate_connector_crimp_data import MODEL_ASSETS, PARTS


ROOT = Path(__file__).resolve().parents[1]
STEP_NAME, RENDER_NAME, RECORD_NAME = MODEL_ASSETS


def housing_model(row):
    """Use drawing pitch and outer dimensions with simplified cavity geometry."""
    dimensions = row["dimensions_mm"]
    length, depth, height = (dimensions[key] for key in ("length", "width", "height"))
    housing = cq.Workplane("XY").box(length, depth, height, centered=(True, False, False))
    housing = housing.edges("|Y").chamfer(0.09)
    for index in range(row["positions"]):
        x = 2.54 * (index - (row["positions"] - 1) / 2)
        center = (x, 0, height / 2)
        # The drawing shows a flared mating opening and wider rear socket cavity.
        # Aperture sizes, depths and edge breaks below are illustrative.
        entry = cq.Workplane("XZ", origin=center).workplane(offset=0.01).rect(1.85, 1.85)
        entry = entry.workplane(offset=-0.48).rect(0.95, 0.95).loft()
        throat = cq.Workplane("XZ", origin=center).rect(0.95, 0.95).extrude(-depth)
        rear = cq.Workplane("XZ", origin=(x, depth + 0.01, height / 2))
        rear = rear.rect(1.76, 1.76).extrude(7.4)
        housing = housing.cut(entry).cut(throat).cut(rear)
    return housing.val()


def contact_model(row):
    """Sketch a socket, connecting strip and uncrimped wings as one solid."""
    length = row["dimensions_mm"]["length"]
    thickness = 0.20  # Illustrative sheet thickness.
    socket = cq.Workplane("XY").box(4.5, 1.65, 1.50, centered=(False, True, False))
    bore = cq.Workplane("XY").box(4.52, 1.00, 1.02, centered=(False, True, False))
    socket = socket.cut(bore.translate((-0.01, 0, 0.22)))
    slot = cq.Workplane("XY").box(2.2, 0.68, 0.52, centered=(False, True, False))
    socket = socket.cut(slot.translate((0.60, 0, 1.12)))
    strip = cq.Workplane("XY").box(length - 4.45, 0.95, thickness, centered=(False, True, False))
    contact = socket.union(strip.translate((4.45, 0, 0)))
    # Width and height at X-X and Y-Y come from Harwin's section dimensions.
    # The wing wall shape and longitudinal transitions are simplified.
    for start, span, width, height in ((6.0, 2.4, 1.70, 1.70), (length - 1.70, 1.70, 2.30, 2.60)):
        half = width / 2
        bottom = 0.54
        outline = [
            (-half, height), (-bottom, 0), (bottom, 0), (half, height),
            (half - thickness, height), (bottom - 0.15, thickness),
            (-bottom + 0.15, thickness), (-half + thickness, height),
        ]
        wings = cq.Workplane("YZ", origin=(start, 0, 0)).polyline(outline).close().extrude(span)
        contact = contact.union(wings)
    return contact.val()


def verify_solid(shape, row):
    bounds = shape.BoundingBox()
    actual = (bounds.xlen, bounds.ylen, bounds.zlen)
    expected = tuple(row["dimensions_mm"][key] for key in ("length", "width", "height"))
    if len(shape.Solids()) != 1 or not shape.isValid() or shape.Volume() <= 0:
        raise ValueError(f"{row['mpn']} must be one valid, nonempty solid")
    if not all(math.isclose(a, b, abs_tol=0.005) for a, b in zip(actual, expected)):
        raise ValueError(f"{row['mpn']} STEP envelope {actual} differs from {expected}")


def generate(row, render_only=False, *, model_builder=None, drawing=None, generator=None,
             render_options=None):
    from kicad_agents.crimp_studio import render_studio

    source_dir = ROOT / "parts_source" / row["id"]
    drawing = drawing or source_dir / "datasheet.pdf"
    if not drawing.is_file():
        raise FileNotFoundError(f"Review the local drawing for {row['mpn']} before generating a model")
    housing = row["role"] == "cable_housing"
    with TemporaryDirectory(prefix="model-", dir=source_dir) as scratch:
        output = Path(scratch)
        step_path = source_dir / STEP_NAME if render_only else output / STEP_NAME
        if not render_only:
            builder = model_builder or (housing_model if housing else contact_model)
            shape = builder(row)
            verify_solid(shape, row)
            cq.exporters.export(shape, str(step_path))
        reloaded = cq.importers.importStep(str(step_path)).val()
        verify_solid(reloaded, row)
        render_record = render_studio(reloaded, row, output / RENDER_NAME, **(render_options or {}))
        record = {
            "mpn": row["mpn"],
            "source": "OOMP drawing-based reference model",
            "drawing_url": row["datasheet_url"],
            "drawing_sha256": hashlib.sha256(drawing.read_bytes()).hexdigest(),
            "dimensions_mm": row["dimensions_mm"],
            "limitations": ("Simplified cavity, taper and retention geometry." if housing
                            else "Simplified stamped profile, crimp wings and socket. Spring and latch geometry are omitted."),
            "generator": generator or "kicad_agents/crimp_3d.py",
            "render": render_record,
        }
        if housing:
            record.update(positions=row["positions"], pitch_mm=row.get("pitch_mm", 2.54))
        if row.get("pdf_page"):
            record["drawing_pdf_page"] = row["pdf_page"]
        (output / RECORD_NAME).write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
        for name in (RENDER_NAME, RECORD_NAME) if render_only else MODEL_ASSETS:
            (output / name).replace(source_dir / name)
    print(f"{row['mpn']}: verified STEP and rendered studio preview")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choices = {row["mpn"]: row for row in PARTS}
    parser.add_argument("mpns", nargs="+", metavar="MPN", help="Exact Harwin MPNs from the connector table")
    parser.add_argument("--render-only", action="store_true", help="Render the existing source STEP")
    args = parser.parse_args()
    for mpn in args.mpns:
        if mpn.upper() not in choices:
            parser.error(f"No verified connector definition for {mpn}")
    for mpn in dict.fromkeys(mpn.upper() for mpn in args.mpns):
        generate(choices[mpn], render_only=args.render_only)


if __name__ == "__main__":
    main()
