"""Roboclick action that renders a part's KiCad symbol and footprints.

Uses kicad-cli to plot the per-part symbol library (one SVG per unit) and each
soldering footprint variant in a full view and a bare pads-plus-fab view, then
Inkscape rasterizes them the same way the rest of the OOMP pipeline does. Every
symbol unit and footprint plot also gets a square variant (``*_square.svg``/
``*.png``) re-canvasd onto a centred white square so webpage grids can show
them without long thin strips. Footprints that embed a 3D model are additionally
written out as a STEP file and a 3/4-view PNG rendered from a courtyard-sized
board. Finishes with a labelled contact sheet so the whole set can be reviewed
in one image. Parts without KiCad masters are reported and skipped; parts with
masters fail loudly when rendering breaks.
"""

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
repository_root_text = str(REPOSITORY_ROOT)
if repository_root_text in sys.path:
    sys.path.remove(repository_root_text)
sys.path.insert(0, repository_root_text)

from kicad_agents import kicad_sexpr as sx
from kicad_agents.contact_sheet import build_contact_sheet
from kicad_agents.kicad_cli import find_kicad_cli
from kicad_agents.run_error_report import log_run_error

SYMBOL_FILE_SUFFIX = ".kicad_sym"
FOOTPRINT_VARIANTS = ["machine_solder", "hand_solder"]
EXPORT_WIDTH_PX = 800
# Square variants: the shorter axis is padded until the canvas is square, with
# this factor of breathing room around the drawing so webpage grids show the
# part without it touching the card edges.
SQUARE_PAD_FACTOR = 1.08
EXPORT_SQUARE_WIDTH_PX = 800

# Bare footprint render: copper pads plus the fab-layer body outline, i.e. the
# physical component and its pads without silkscreen marks or reference text.
FOOTPRINT_BARE_LAYERS = "F.Cu,F.Fab"
# The 3D board is a courtyard-sized slab so the component sits on believable
# PCB without a full sheet of empty substrate.
BOARD_OUTLINE_MARGIN_MM = 2.0
BOARD_OUTLINE_FALLBACK_MM = 10.0
RENDER_ROTATE = "-30,0,40"
RENDER_ZOOM = "0.85"
RENDER_WIDTH_PX = 800
RENDER_HEIGHT_PX = 600
# kicad-cli's 3D renderer jitters a few anti-aliased pixels between runs, so a
# re-render within this per-channel tolerance of the stored PNG keeps the
# stored bytes; only a genuinely different render replaces the file.
RENDER_JITTER_TOLERANCE = 24

def find_inkscape():
    explicit = str(os.environ.get("INKSCAPE") or "").strip()
    if explicit:
        return explicit
    discovered = shutil.which("inkscape")
    if discovered:
        return discovered
    program_files = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
    candidate = program_files / "Inkscape" / "bin" / "inkscape.exe"
    if candidate.is_file():
        return str(candidate)
    return "inkscape"


def write_changed(path, content):
    path = Path(path)
    data = content if isinstance(content, bytes) else content.encode("utf-8")
    if not path.is_file() or path.read_bytes() != data:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def is_outdated(destination, sources):
    destination = Path(destination)
    if not destination.is_file():
        return True
    destination_time = destination.stat().st_mtime
    for source in sources:
        if Path(source).stat().st_mtime > destination_time:
            return True
    return False


def run_command(command):
    completed = subprocess.run(
        [str(argument) for argument in command],
        capture_output=True,
        text=True,
        timeout=600,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {' '.join(str(a) for a in command)}\n"
            f"{completed.stdout.strip()}\n{completed.stderr.strip()}"
        )
    return completed.stdout


def normalize_svg(svg_text):
    """Drop kicad-cli's export timestamp so repeated plots stay byte-identical."""
    import re

    return re.sub(r" date \d{4}-\d{2}-\d{2}T[\d:]+", "", svg_text)


def symbol_name_for_part(symbol_file, part_id):
    library = sx.parse(symbol_file.read_text(encoding="utf-8"))
    root_names = [str(child[1]) for child in sx.children(library, "symbol")]
    if part_id in root_names:
        return part_id
    if len(root_names) == 1:
        return root_names[0]
    raise ValueError(
        f"No symbol named '{part_id}' in {symbol_file} (found {root_names})."
    )


def render_symbol(kicad_cli, kicad_directory, symbol_file, part_id, regenerate):
    """Plot each unit of the part's symbol; return the exported SVG paths."""
    symbol_name = symbol_name_for_part(symbol_file, part_id)
    with tempfile.TemporaryDirectory(prefix="oomp_kicad_render_sym_") as temporary:
        export_directory = Path(temporary) / "svg"
        export_directory.mkdir()
        run_command(
            [
                kicad_cli,
                "sym",
                "export",
                "svg",
                "-o",
                export_directory,
                "-s",
                symbol_name,
                symbol_file,
            ]
        )
        unit_svgs = sorted(export_directory.glob("*.svg"))
        if not unit_svgs:
            raise RuntimeError(f"kicad-cli plotted no symbol units for '{symbol_name}'.")

        exported = []
        for unit_number, unit_svg in enumerate(unit_svgs, start=1):
            destination = kicad_directory / f"kicad_symbol_unit_{unit_number}.svg"
            if regenerate or is_outdated(destination, [symbol_file]):
                write_changed(destination, normalize_svg(unit_svg.read_text(encoding="utf-8")))
            exported.append(destination)
        # Drop stale unit renders when a regeneration produced fewer units.
        unit_number = len(unit_svgs) + 1
        while (kicad_directory / f"kicad_symbol_unit_{unit_number}.svg").is_file():
            (kicad_directory / f"kicad_symbol_unit_{unit_number}.svg").unlink()
            unit_number += 1
        return exported


def strip_footprint_caption(svg_text, footprint_name):
    """Drop the caption kicad-cli plots under every footprint.

    The plotter draws the footprint name as invisible <text> plus a stroked
    vector copy; both widen the canvas far past the pads. Field texts such as
    REF** and the part mark are real content and stay.
    """
    import re

    escaped_name = re.escape(footprint_name)
    pattern = (
        rf"<text[^>]*>{escaped_name}</text>\s*"
        rf'<g class="stroked-text"><desc>{escaped_name}</desc>.*?</g>\s*'
    )
    stripped, count = re.subn(pattern, "", svg_text, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(
            f"Expected one caption for '{footprint_name}' in the plotted footprint, found {count}."
        )
    return stripped


def render_footprint(kicad_cli, kicad_directory, footprint_file, variant_name, part_id, regenerate):
    """Plot one footprint variant; kicad-cli needs a .pretty library directory."""
    with tempfile.TemporaryDirectory(prefix="oomp_kicad_render_fp_") as temporary:
        library = Path(temporary) / f"{part_id}.pretty"
        library.mkdir()
        shutil.copyfile(footprint_file, library / footprint_file.name)
        export_directory = Path(temporary) / "svg"
        export_directory.mkdir()
        run_command(
            [
                kicad_cli,
                "fp",
                "export",
                "svg",
                "-o",
                export_directory,
                library,
            ]
        )
        exported_svgs = sorted(export_directory.glob("*.svg"))
        if not exported_svgs:
            raise RuntimeError(
                f"kicad-cli plotted no footprint for variant '{variant_name}'."
            )
        destination = kicad_directory / f"kicad_footprint_{variant_name}.svg"
        if regenerate or is_outdated(destination, [footprint_file]):
            svg_text = exported_svgs[0].read_text(encoding="utf-8")
            svg_text = normalize_svg(strip_footprint_caption(svg_text, footprint_file.stem))
            write_changed(destination, svg_text)
        return destination


def normalize_step(step_text):
    """Freeze the export timestamp in the STEP header for byte-stable output."""
    import re

    return re.sub(
        r"(FILE_NAME\('[^']*',')[^']*'",
        r"\g<1>1970-01-01T00:00:00'",
        step_text,
        count=1,
    )


def footprint_bounding_box(footprint_text):
    """Courtyard bounding box in mm, falling back to pads, then a fixed square."""
    import re

    coordinates = []
    for line in footprint_text.splitlines():
        if 'F.CrtYd' in line:
            match = re.search(r"\(start ([-\d.]+) ([-\d.]+)\) \(end ([-\d.]+) ([-\d.]+)\)", line)
            if match:
                coordinates.extend(
                    [
                        (float(match.group(1)), float(match.group(2))),
                        (float(match.group(3)), float(match.group(4))),
                    ]
                )
    if not coordinates:
        for line in footprint_text.splitlines():
            if "(pad " not in line:
                continue
            match = re.search(r"\(at ([-\d.]+) ([-\d.]+)", line)
            if match:
                coordinates.append((float(match.group(1)), float(match.group(2))))
    if not coordinates:
        reach = BOARD_OUTLINE_FALLBACK_MM
        return (-reach, -reach, reach, reach)
    xs = [point[0] for point in coordinates]
    ys = [point[1] for point in coordinates]
    margin = BOARD_OUTLINE_MARGIN_MM
    return (min(xs) - margin, min(ys) - margin, max(xs) + margin, max(ys) + margin)


BOARD_TEMPLATE = """(kicad_pcb (version 20221018) (generator oomp)
  (general (thickness 1.6))
  (paper "A4")
  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (44 "Edge.Cuts" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
  )
  (setup (pad_to_mask_clearance 0))
  (gr_rect (start {x0} {y0}) (end {x1} {y1}) (stroke (width 0.05) (type solid)) (fill none) (layer "Edge.Cuts"))
{footprint}
)
"""


def build_render_board(footprint_file):
    """A minimal board holding just this footprint, sized to its courtyard."""
    footprint_text = footprint_file.read_text(encoding="utf-8").strip()
    if "\n  (at " not in footprint_text:
        footprint_text = footprint_text.replace(
            '(layer "F.Cu")', '(layer "F.Cu")\n  (at 0 0)', 1
        )
    x0, y0, x1, y1 = footprint_bounding_box(footprint_text)
    return BOARD_TEMPLATE.format(
        x0=f"{x0:.4f}", y0=f"{y0:.4f}", x1=f"{x1:.4f}", y1=f"{y1:.4f}", footprint=footprint_text
    )


def strip_all_text(svg_text):
    """Remove every text element and its stroked vector copy.

    Bare renders are meant to show only the physical component: pads, body
    outline, courtyard. KiCad plots each text as an invisible <text> plus a
    stroked <g class="stroked-text"> copy; the two are not always adjacent (a
    rotate wrapper can sit between), so both are removed independently.
    """
    import re

    svg_text = re.sub(r'<g class="stroked-text">.*?</g>\s*', "", svg_text, flags=re.DOTALL)
    return re.sub(r"<text[^>]*>.*?</text>\s*", "", svg_text, flags=re.DOTALL)


def render_footprint_bare(kicad_cli, kicad_directory, footprint_file, variant_name, regenerate):
    """Plot pads plus fab outline only, so silkscreen marks stay out of the way."""
    with tempfile.TemporaryDirectory(prefix="oomp_kicad_render_bare_") as temporary:
        library = Path(temporary) / f"{footprint_file.stem}.pretty"
        library.mkdir()
        shutil.copyfile(footprint_file, library / footprint_file.name)
        export_directory = Path(temporary) / "svg"
        export_directory.mkdir()
        run_command(
            [
                kicad_cli,
                "fp",
                "export",
                "svg",
                "-o",
                export_directory,
                "--layers",
                FOOTPRINT_BARE_LAYERS,
                library,
            ]
        )
        exported_svgs = sorted(export_directory.glob("*.svg"))
        if not exported_svgs:
            raise RuntimeError(
                f"kicad-cli plotted no bare footprint for variant '{variant_name}'."
            )
        destination = kicad_directory / f"kicad_footprint_{variant_name}_bare.svg"
        if regenerate or is_outdated(destination, [footprint_file]):
            svg_text = exported_svgs[0].read_text(encoding="utf-8")
            svg_text = normalize_svg(strip_all_text(svg_text))
            write_changed(destination, svg_text)
        return destination


def footprint_model_reference(footprint_file):
    """The first embedded 3D model path, or None when the footprint has none."""
    import re

    match = re.search(r'\(model "([^"]+)"', footprint_file.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def render_looks_identical(existing_path, candidate_path, tolerance=RENDER_JITTER_TOLERANCE):
    """True when two rasters differ only by renderer jitter (small per-channel deltas)."""
    from PIL import Image, ImageChops

    existing = Image.open(existing_path).convert("RGB")
    candidate = Image.open(candidate_path).convert("RGB")
    if existing.size != candidate.size:
        return False
    extrema = ImageChops.difference(existing, candidate).getextrema()
    return all(high <= tolerance for _, high in extrema)


def step_entity_keys(step_text):
    """Canonical multiset of STEP entity records, ignoring ids and ordering.

    OpenCASCADE writes the colour/presentation block in a hash-dependent
    order with shifting entity numbers, so raw bytes alternate between runs
    even though the exported model is identical.
    """
    import re

    data_match = re.search(r"^DATA;(.*?)^ENDSEC;", step_text, flags=re.DOTALL | re.MULTILINE)
    if data_match is None:
        raise ValueError("STEP file has no DATA section.")
    records = []
    current = []
    depth = 0
    for line in data_match.group(1).splitlines():
        if not current and not line.lstrip().startswith("#"):
            continue
        current.append(line)
        depth += line.count("(") - line.count(")")
        if depth <= 0 and line.rstrip().endswith(";"):
            record = "\n".join(current)
            record = re.sub(r"^#\d+\s*=\s*", "", record)
            record = re.sub(r"#\d+", "#", record)
            records.append(record)
            current = []
            depth = 0
    if current:
        raise ValueError("STEP entity records did not parse cleanly.")
    return sorted(records)


def step_models_equivalent(existing_path, candidate_text):
    """True when a fresh STEP export is the same model as the stored one."""
    try:
        existing_keys = step_entity_keys(Path(existing_path).read_text(encoding="utf-8"))
        candidate_keys = step_entity_keys(candidate_text)
    except (ValueError, OSError):
        return False
    return existing_keys == candidate_keys


def render_footprint_3d(kicad_cli, kicad_directory, footprint_file, variant_name, regenerate):
    """Export the footprint (with its 3D model) as STEP and a 3/4-view PNG."""
    board_text = build_render_board(footprint_file)
    step_destination = kicad_directory / f"kicad_footprint_{variant_name}.step"
    png_destination = kicad_directory / f"kicad_footprint_{variant_name}_3d.png"
    if not regenerate and not is_outdated(step_destination, [footprint_file]) and not is_outdated(
        png_destination, [footprint_file]
    ):
        return step_destination, png_destination

    with tempfile.TemporaryDirectory(prefix="oomp_kicad_render_3d_") as temporary:
        board_path = Path(temporary) / f"{footprint_file.stem}_render.kicad_pcb"
        board_path.write_text(board_text, encoding="utf-8")
        run_command(
            [
                kicad_cli,
                "pcb",
                "export",
                "step",
                "--include-pads",
                "-o",
                Path(temporary) / "model.step",
                board_path,
            ]
        )
        step_text = normalize_step((Path(temporary) / "model.step").read_text(encoding="utf-8"))
        if step_destination.is_file() and step_models_equivalent(step_destination, step_text):
            # Keep the stored bytes: entity numbering and presentation-block
            # order jitter between exports of an unchanged model, and
            # rewriting would churn git on every forced regeneration.
            pass
        else:
            write_changed(step_destination, step_text)
        run_command(
            [
                kicad_cli,
                "pcb",
                "render",
                "-o",
                Path(temporary) / "render.png",
                "--side",
                "top",
                "--rotate",
                RENDER_ROTATE,
                "--zoom",
                RENDER_ZOOM,
                "--width",
                str(RENDER_WIDTH_PX),
                "--height",
                str(RENDER_HEIGHT_PX),
                "--background",
                "transparent",
                board_path,
            ]
        )
        render_path = Path(temporary) / "render.png"
        if not render_path.is_file():
            raise RuntimeError(f"kicad-cli produced no 3D render for variant '{variant_name}'.")
        flatten_png_onto_white(render_path)
        if png_destination.is_file() and render_looks_identical(png_destination, render_path):
            # Keep the stored bytes: the renderer jitters slightly between runs
            # and rewriting would churn git on every forced regeneration.
            pass
        else:
            write_changed(png_destination, render_path.read_bytes())
    return step_destination, png_destination


def flatten_png_onto_white(png_path):
    """Existing OOMP rasters are white-background RGB; match them so the renders
    stay legible on dark README themes."""
    from PIL import Image

    rendered = Image.open(png_path).convert("RGBA")
    background = Image.new("RGBA", rendered.size, (255, 255, 255, 255))
    background.alpha_composite(rendered)
    background.convert("RGB").save(png_path)


def svg_to_png(svg_path, inkscape):
    png_path = svg_path.with_suffix(".png")
    if not is_outdated(png_path, [svg_path]):
        return png_path
    run_command(
        [
            inkscape,
            svg_path,
            "--export-filename",
            png_path,
            "--export-area-drawing",
            "--export-margin=8",
            f"--export-width={EXPORT_WIDTH_PX}",
        ]
    )
    if not png_path.is_file():
        raise RuntimeError(f"Inkscape did not create {png_path}.")
    flatten_png_onto_white(png_path)
    return png_path


def square_svg_text(svg_text):
    """Re-canvas a kicad-cli plot onto a centred white square.

    kicad-cli fits the canvas to the drawing, so a 0402 symbol plots as a long
    thin strip. The plot itself is untouched; only the page grows on its short
    axis until it is square, with a white ground behind the drawing.
    """
    import re

    match = re.search(
        r'width="([\d.]+)mm"\s+height="([\d.]+)mm"\s+'
        r'viewBox="([-\d.]+)\s+([-\d.]+)\s+([\d.]+)\s+([\d.]+)"',
        svg_text,
    )
    if match is None:
        raise ValueError("kicad-cli plot is missing width/height/viewBox attributes.")
    width, height = float(match.group(1)), float(match.group(2))
    origin_x, origin_y = float(match.group(3)), float(match.group(4))
    side = max(width, height) * SQUARE_PAD_FACTOR
    new_origin_x = origin_x - (side - width) / 2
    new_origin_y = origin_y - (side - height) / 2
    replacement = (
        f'width="{side:.4f}mm" height="{side:.4f}mm" '
        f'viewBox="{new_origin_x:.4f} {new_origin_y:.4f} {side:.4f} {side:.4f}"'
    )
    squared = svg_text[: match.start()] + replacement + svg_text[match.end() :]
    background = (
        f'<rect x="{new_origin_x:.4f}" y="{new_origin_y:.4f}" width="{side:.4f}" '
        f'height="{side:.4f}" style="fill:#FFFFFF;fill-opacity:1"/>'
    )
    desc_match = re.search(r"<desc>[^<]*</desc>", squared)
    if desc_match is None:
        raise ValueError("kicad-cli plot has no <desc> element to anchor the background.")
    insertion = desc_match.end()
    return squared[:insertion] + "\n  " + background + squared[insertion:]


def render_square_variant(svg_path, inkscape, regenerate):
    """Write the *_square.svg / *.png web-display variant next to a plot."""
    destination = svg_path.with_name(f"{svg_path.stem}_square{svg_path.suffix}")
    if regenerate or is_outdated(destination, [svg_path]):
        write_changed(destination, square_svg_text(svg_path.read_text(encoding="utf-8")))
    png_path = destination.with_suffix(".png")
    if is_outdated(png_path, [destination]):
        run_command(
            [
                inkscape,
                destination,
                "--export-filename",
                png_path,
                "--export-area-page",
                f"--export-width={EXPORT_SQUARE_WIDTH_PX}",
                f"--export-height={EXPORT_SQUARE_WIDTH_PX}",
            ]
        )
        if not png_path.is_file():
            raise RuntimeError(f"Inkscape did not create {png_path}.")
        flatten_png_onto_white(png_path)
    return destination


def build(details):
    part_directory = Path(details.get("directory", "")).resolve()
    part_id = str(details.get("part_id", "")).strip()
    if part_id == "":
        part_id = part_directory.name
    kicad_directory = part_directory / "data" / "kicad"
    if not kicad_directory.is_dir():
        raise FileNotFoundError(
            f"No KiCad data to render for {part_id}: {kicad_directory} is missing."
        )
    regenerate = details.get("regenerate_pngs", False) in [True, "true", "True", "1", "yes"]

    kicad_cli = find_kicad_cli()
    inkscape = find_inkscape()

    symbol_files = sorted(kicad_directory.glob(f"*{SYMBOL_FILE_SUFFIX}"))
    cells = []
    if symbol_files:
        symbol_svg_paths = render_symbol(
            kicad_cli, kicad_directory, symbol_files[0], part_id, regenerate
        )
        for unit_number, symbol_svg in enumerate(symbol_svg_paths, start=1):
            png_path = svg_to_png(symbol_svg, inkscape)
            render_square_variant(symbol_svg, inkscape, regenerate)
            cells.append((f"Symbol unit {unit_number}", png_path))

    footprint_files = {}
    for variant in FOOTPRINT_VARIANTS:
        variant_directory = kicad_directory / variant
        if not variant_directory.is_dir():
            continue
        variant_files = sorted(variant_directory.glob("*.kicad_mod"))
        if variant_files:
            footprint_files[variant] = variant_files[0]

    if "machine_solder" in footprint_files and "hand_solder" in footprint_files:
        if footprint_files["machine_solder"].read_bytes() == footprint_files["hand_solder"].read_bytes():
            footprint_files.pop("hand_solder")
            identical_hand_solder = True
        else:
            identical_hand_solder = False
    else:
        identical_hand_solder = False

    rendered_models = set()
    for variant, footprint_file in footprint_files.items():
        variant_label = variant.replace("_", " ")
        identical_note = " (hand solder identical)" if variant == "machine_solder" and identical_hand_solder else ""

        footprint_svg = render_footprint(
            kicad_cli, kicad_directory, footprint_file, variant, part_id, regenerate
        )
        footprint_png = svg_to_png(footprint_svg, inkscape)
        render_square_variant(footprint_svg, inkscape, regenerate)
        cells.append((f"Footprint {variant_label}{identical_note}", footprint_png))

        bare_svg = render_footprint_bare(
            kicad_cli, kicad_directory, footprint_file, variant, regenerate
        )
        render_square_variant(bare_svg, inkscape, regenerate)
        cells.append(
            (
                f"Footprint {variant_label}, no silkscreen",
                svg_to_png(bare_svg, inkscape),
            )
        )

        # The 3D model belongs to the package, not the pad set, so variants
        # sharing one model reference share one STEP and render.
        model_reference = footprint_model_reference(footprint_file)
        if model_reference is None or model_reference in rendered_models:
            continue
        rendered_models.add(model_reference)
        _, render_png = render_footprint_3d(
            kicad_cli, kicad_directory, footprint_file, variant, regenerate
        )
        cells.append((f"3D render, {variant_label}", render_png))

    if not cells:
        raise FileNotFoundError(f"No KiCad symbol or footprint files found for {part_id}.")

    contact_sheet = kicad_directory / "contact_sheet.png"
    if regenerate or is_outdated(contact_sheet, [png_path for _, png_path in cells]):
        build_contact_sheet(part_id, cells, contact_sheet)
    if not contact_sheet.is_file():
        raise RuntimeError(f"Contact sheet was not created: {contact_sheet}.")
    print(
        f"rendered {len(symbol_files)} symbol library with {len(cells)} views "
        f"and contact sheet for {part_id}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Render one part's KiCad symbol and footprints to SVG, PNG, and a contact sheet."
    )
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    try:
        build(json.loads(arguments.kwargs))
    except Exception as error:
        log_run_error("kicad_render_action", error)
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
