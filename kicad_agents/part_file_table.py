"""Build the part README's Markdown file table from published local files."""

from collections import defaultdict
from html import escape
import os
from pathlib import Path, PurePosixPath
from urllib.parse import quote


TABLE_START = "<!-- oomp-part-file-table -->"
TABLE_END = "<!-- /oomp-part-file-table -->"
IMAGE_FORMATS = (".svg", ".png", ".webp", ".jpg", ".jpeg", ".gif")

# Keep related views together and give the short catalogue identifiers context.
DIAGRAMS = {
    "square_pins": ("Pinout drawing", "Pin names and positions on the part."),
    "assembly": ("Assembly", "Component placement drawing."),
    "assembly_pins": ("Assembly pinout", "Placement drawing with the pins marked."),
    "top": ("Top view", "Package seen from above."),
    "bottom": ("Bottom view", "Package seen from below."),
    "side": ("Side view", "Package profile."),
    "outline": ("Outline", "External shape of the part."),
    "dimensioned": ("Dimensions", "Package outline with dimension arrows."),
    "dimensioned_titles": ("Dimensions with labels", "Labelled package measurements."),
    "square": ("Square summary", "Component identification card."),
    "square_schematic": ("Square schematic", "Schematic symbol on an identification card."),
    "part_id": ("Part ID", "Drawing labelled with the OOMP catalogue ID."),
    "md5_6_alpha": ("MD5 alpha", "Drawing labelled with the short OOMP code."),
    "bip_39_3_word": ("BIP 39 words", "Drawing labelled with the three-word identifier."),
    "schematic": ("Schematic", "Electrical symbol for the part."),
    "schematic_pins": ("Schematic pinout", "Electrical symbol with pin labels."),
    "schematic_part_id": ("Schematic with part ID", "Symbol labelled with the OOMP catalogue ID."),
    "schematic_md5_6_alpha": ("Schematic with MD5 alpha", "Symbol labelled with the short OOMP code."),
    "schematic_bip_39_3_word": ("Schematic with BIP 39 words", "Symbol labelled with the three-word identifier."),
    "contact_sheet": ("Diagram contact sheet", "Component drawings together in one image."),
}

TITLES = {
    "data/display_render/render": "Studio render",
    "data/display_render/manifest": "Studio render sources and recipe",
    "data/model_3d_render": "Reference model render",
    "data/model_3d": "Reference CAD model",
    "data/model_3d_body": "Insulator mesh",
    "data/model_3d_pins": "Contact mesh",
    "data/model_3d_arrangement": "Three-strip assembly render",
    "data/model_3d_3_strip": "Three-strip assembly model",
    "data/model_3d_3_strip_body": "Three-strip insulator mesh",
    "data/model_3d_3_strip_pins": "Three-strip contact mesh",
    "data/model_3d_source": "Reference model sources",
    "data/datasheet": "Manufacturer or supplier datasheet",
    "data/kicad/contact_sheet": "KiCad symbol and footprint overview",
    "data/kicad/README": "KiCad library guide",
    "data/kicad/manifest": "KiCad availability and source masters",
    "data/kicad/LICENSE": "KiCad asset licence",
    "generator_label": "Generator label",
    "label_drawer_3x2": "Large drawer label",
    "label_drawer_1_5x1": "Small drawer label",
    "data/label_drawer": "Drawer label data",
    "data/label_oomp": "OOMP label",
    "working": "Part definition and build recipe",
    "web": "Web catalogue file index",
}


def _row_details(stem, files):
    path = PurePosixPath(stem)
    title = TITLES.get(stem, path.name.replace("_", " ").capitalize())
    if stem.startswith("data/working_svg_"):
        key = path.name.removeprefix("working_svg_")
        title, description = DIAGRAMS.get(key, (key.replace("_", " ").capitalize(), ""))
        rank = list(DIAGRAMS).index(key) if key in DIAGRAMS else len(DIAGRAMS)
        return (1, rank), title, description

    if stem.startswith("data/kicad/"):
        if "previous_generated" in path.parts:
            kind = {".kicad_mod": "footprint", ".kicad_sym": "symbol"}.get(files[0].suffix, "asset")
            title = f"Archived KiCad {kind}"
        elif any(f.suffix == ".kicad_sym" for f in files):
            title = "KiCad symbol library"
        elif path.parent.name in ("machine_solder", "hand_solder"):
            method = "Machine-solder" if path.parent.name == "machine_solder" else "Hand-solder"
            title = f"{method} footprint guide" if path.name == "README" else f"{method} footprint"
        elif path.name.startswith("kicad_footprint_"):
            view = path.name.removeprefix("kicad_footprint_")
            method = "Hand-solder" if view.startswith("hand_solder") else "Machine-solder"
            qualifiers = []
            if "bare" in view:
                qualifiers.append("without silkscreen")
            if "square" in view:
                qualifiers.append("square view")
            if "3d" in view:
                qualifiers.append("3D view")
            title = f"{method} footprint" + (f" ({', '.join(qualifiers)})" if qualifiers else " drawing")
        elif path.name.startswith("kicad_symbol_"):
            title = "KiCad symbol, " + path.name.removeprefix("kicad_symbol_").replace("_square", " (square view)").replace("_", " ")
        return (2, stem), title, ""

    if stem == "data/display_render/render":
        return (0, stem), title, ""
    if stem.startswith(("data/display_render/", "data/model_3d")):
        return (3, stem), title, ""
    return (4, stem), title, ""


def file_table(paths):
    """One row per view or resource, with alternate formats in the same cell."""
    groups = defaultdict(list)
    previews = {}
    for name in sorted(paths):
        path = PurePosixPath(name)
        if name == "README.md" or path.suffix in {".tmp", ".pyc"}:
            continue
        if "__pycache__" in path.parts or any(piece.startswith(".") for piece in path.parts):
            continue
        stem = str(path.with_suffix(""))
        if name.endswith("_300.png"):
            stem = stem.removesuffix("_300")
            previews[stem] = name
        elif name == "data/display_render/preview.webp":
            stem = "data/display_render/render"
            previews[stem] = name
        groups[stem].append(path)

    rows = []
    for stem, files in groups.items():
        order, title, description = _row_details(stem, files)
        safe_title = escape(title, quote=True).replace("|", "&#124;")
        images = [str(f) for f in files if f.suffix.lower() in IMAGE_FORMATS]
        preview = previews.get(stem) or next(iter(images), None)
        image = "—"
        if preview:
            image = f'<img src="{quote(preview)}" alt="{safe_title}" width="160">'
        links = []
        for f in sorted(files, key=lambda f: (str(f) == previews.get(stem), f.suffix != ".svg", str(f))):
            label = f.suffix.removeprefix(".").upper() or f.name
            if str(f) == previews.get(stem):
                label = "Preview"
            links.append(f"[{label}]({quote(str(f))})")
        text = f"**{safe_title}**"
        if description:
            text += f"<br>{description}"
        rows.append((order, f"| {text} | {image} | {' · '.join(links)} |"))
    return "\n".join(["| Image type | Image | Link |", "| --- | :---: | --- |",
                      *(row for _, row in sorted(rows))])


def local_files(directory):
    directory = Path(directory)
    return {(Path(folder) / name).relative_to(directory).as_posix()
            for folder, _, files in os.walk(directory) for name in files}


def fill_file_table(page, paths):
    """The final publishing action sees files produced after the Jinja action."""
    if not page.is_file():
        return
    original = page.read_text(encoding="utf-8")
    prefix, start, rest = original.partition(TABLE_START)
    _, end, suffix = rest.partition(TABLE_END)
    if start and end:
        updated = f"{prefix}{start}\n\n{file_table(paths)}\n\n{end}{suffix}"
        if original != updated:
            page.write_text(updated, encoding="utf-8")
