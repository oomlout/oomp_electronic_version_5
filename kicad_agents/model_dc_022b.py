"""Build and render the nominal DC-022B socket in millimetres."""
import argparse
from collections import defaultdict
import json
import math
from pathlib import Path
from tempfile import TemporaryDirectory

from working_oomp_populate_connector_dc_022b import PART, SOURCE


def build():
    """Return PBT and metal solids along the socket axis, front face at x=0."""
    import cadquery as cq

    def cylinder(x, length, radius):
        return cq.Workplane("YZ", origin=(x, 0, 0)).circle(radius).extrude(length)

    def ring(x, length, outer, inner):
        return cq.Workplane("YZ", origin=(x, 0, 0)).circle(outer).circle(inner).extrude(length)

    front = ring(.55, 3.45, 5, 2.8)
    # Pitch is visible as annular grooves. Actual helical thread form is omitted.
    profile = [(4, 0), (4, 4)]
    for i in range(5):
        start = 4 + i
        profile.extend([(start + .26, 3.56), (start + .65, 3.56), (start + 1, 4)])
    profile.extend([(9, 3.98), (12, 3.98), (12, 0)])
    shank = cq.Workplane("XY").polyline(profile).close().revolve(360, (0, 0), (1, 0))
    flats = cq.Workplane("XY").box(10, 9, 6.8).translate((8, 0, 0))
    shank = shank.intersect(flats).cut(cylinder(3.9, 6, 2.8))
    socket_body = front.union(shank)
    bezel = ring(0, .55, 4.45, 2.8).union(ring(.55, .8, 3.15, 2.8))
    pin = cylinder(1.15, 8.75, 1.05).edges("<X").fillet(.22)
    nut_diameter = 22 / math.sqrt(3)
    nut = (cq.Workplane("YZ", origin=(4.2, 0, 0)).polygon(6, nut_diameter)
           .extrude(2).cut(cylinder(4.1, 2.2, 4.02)))
    lugs = []
    for length, y in [(4.5, 2.65), (5.8, -2.65)]:
        plane = cq.Workplane("XZ", origin=(12, y + .4, 0))
        lug = (plane.moveTo(-.15, -1.1).lineTo(length - 1.1, -1.1)
               .threePointArc((length, 0), (length - 1.1, 1.1))
               .lineTo(-.15, 1.1).close().extrude(.8))
        hole = cq.Workplane("XZ", origin=(12 + length - 1.1, y + .5, 0)).circle(.52).extrude(1)
        lugs.append(lug.cut(hole))
    spring = cq.Workplane("XY").box(4, .45, 1.35).translate((6.4, -2.54, 0))
    return {
        "coating": [socket_body.val()],
        "termination": [item.val() for item in (bezel, pin, nut, spring, *lugs)],
    }


def mesh(solids):
    import numpy as np

    groups = defaultdict(lambda: {"vertices": [], "normals": [], "triangles": []})
    for role, shapes in solids.items():
        group = groups[role]
        for shape in shapes:
            if not shape.isValid() or not shape.Solids():
                raise ValueError(f"Invalid solid in {role}")
            for face in shape.Faces():
                vertices, triangles = face.tessellate(.015, .1)
                offset = len(group["vertices"])
                group["vertices"].extend(v.toTuple() for v in vertices)
                group["normals"].extend(face.normalAt(v).toTuple() for v in vertices)
                group["triangles"].extend(tuple(offset + i for i in face) for face in triangles)
    vertices = np.asarray([v for group in groups.values() for v in group["vertices"]])
    return groups, vertices.min(axis=0), vertices.max(axis=0)


def render(output, pixels, samples):
    import numpy as np
    from PIL import Image
    from kicad_agents import display_render as studio

    source_pdf = SOURCE / "datasheet.pdf"
    document_hash = studio.digest(source_pdf)
    groups, lower, upper = mesh(build())
    if not np.allclose(upper - lower, [17.8, 22 / math.sqrt(3), 11], atol=.025):
        raise ValueError(f"Unexpected assembled model envelope: {upper - lower}")
    output.mkdir(parents=True, exist_ok=True)
    scene = json.loads(studio.STUDIO.read_text(encoding="utf-8"))
    scene["framing_margin"] = .12
    settings = {}
    views = {
        "model_3d_render.png": [-2.3, -1.65, 1.45],
        "model_3d_rear.png": [2.1, -1.60, 1.65],
    }
    for name, direction in views.items():
        with TemporaryDirectory(prefix="dc-022b-") as folder:
            scratch = Path(folder)
            studio.create_textures({}, "", upper - lower, scratch)
            image, detail = studio.render_scene(
                groups, lower, upper, {"disable_bump_for": ["termination"]},
                dict(scene, camera_direction=direction), scratch, pixels, samples,
            )
            if detail["nonfinite_pixels_repaired"]:
                raise ValueError("Render contains nonfinite pixels")
            Image.fromarray(image).save(output / name, optimize=True)
            settings[name] = {"camera": direction, "sha256": studio.digest(output / name), **detail}
            print(f"Rendered {name} in {detail['seconds']} s", flush=True)
    manifest = {
        "part_id": PART, "purpose": "display_only", "units": "mm",
        "datasheet_sha256": document_hash, "datasheet_page": 1,
        "model_source": "kicad_agents/model_dc_022b.py",
        "model_sha256": studio.digest(__file__), "studio_sha256": studio.digest(studio.STUDIO),
        "renderer_sha256": studio.digest(studio.__file__),
        "bounds_mm_including_nut": (upper - lower).tolist(),
        "limits": "Thread grooves, internal spring and lug hole detail are approximate. "
                  "The catalogue plug specification determines the displayed centre pin. Finishes are illustrative.",
        "views": settings,
    }
    (output / "model_3d_source.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SOURCE)
    parser.add_argument("--pixels", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=64)
    args = parser.parse_args()
    render(args.output, args.pixels, args.samples)
