"""Shared labelled contact-sheet builder for the OOMP Roboclick render actions.

Both diagram stages finish by composing their renders into one review image:
``component_svg_action`` for the OOMP drawing set and ``kicad_render_action``
for the KiCad symbol/footprint/3D set. Cells are (label, png_path) pairs laid
out on a white grid with wrapped labels so neighbouring cells never overlap.
"""

import math
from pathlib import Path

CELL_IMAGE_WIDTH = 460
CELL_IMAGE_HEIGHT = 340
CELL_LABEL_HEIGHT = 68
CELL_BORDER = 1
CELL_PADDING = 16
SHEET_COLUMNS = 3
SHEET_MARGIN = 24
SHEET_GUTTER = 24
SHEET_HEADER_HEIGHT = 64
TEXT_COLOR = (34, 34, 34)
BORDER_COLOR = (203, 203, 203)
HEADER_TEXT_COLOR = (68, 68, 68)


def load_font(size):
    from PIL import ImageFont

    font_names = ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_label(draw, position, text, font, max_width):
    """Draw a label, wrapping to the cell width so neighbours never overlap."""
    line_height = getattr(font, "size", 20) + 6
    lines = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if current and draw.textlength(candidate, font=font) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    for offset, line in enumerate(lines[:3]):
        draw.text(
            (position[0], position[1] + offset * line_height),
            line,
            fill=TEXT_COLOR,
            font=font,
        )


def build_contact_sheet(part_id, cells, destination, title="KiCad symbol and footprint renders"):
    """Compose the labelled renders into one review image."""
    from PIL import Image, ImageDraw

    title_font = load_font(30)
    label_font = load_font(20)
    cell_width = CELL_IMAGE_WIDTH + 2 * CELL_PADDING + 2 * CELL_BORDER
    cell_height = (
        CELL_IMAGE_HEIGHT + CELL_LABEL_HEIGHT + 2 * CELL_PADDING + 2 * CELL_BORDER
    )
    cell_count = len(cells)
    columns = min(SHEET_COLUMNS, cell_count)
    rows = math.ceil(cell_count / columns)
    sheet_width = 2 * SHEET_MARGIN + columns * cell_width + (columns - 1) * SHEET_GUTTER
    sheet_height = (
        SHEET_HEADER_HEIGHT
        + 2 * SHEET_MARGIN
        + rows * cell_height
        + (rows - 1) * SHEET_GUTTER
    )
    sheet = Image.new("RGB", (sheet_width, sheet_height), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (SHEET_MARGIN, SHEET_MARGIN // 2),
        f"{part_id} - {title}",
        fill=HEADER_TEXT_COLOR,
        font=title_font,
    )

    for index, (label, png_path) in enumerate(cells):
        column = index % columns
        row = index // columns
        cell_left = SHEET_MARGIN + column * (cell_width + SHEET_GUTTER)
        cell_top = SHEET_HEADER_HEIGHT + SHEET_MARGIN + row * (cell_height + SHEET_GUTTER)
        draw.rectangle(
            [
                cell_left,
                cell_top,
                cell_left + cell_width - 1,
                cell_top + cell_height - 1,
            ],
            outline=BORDER_COLOR,
            width=CELL_BORDER,
        )
        image_left = cell_left + CELL_PADDING + CELL_BORDER
        image_top = cell_top + CELL_PADDING + CELL_BORDER
        image = Image.open(png_path).convert("RGB")
        image.thumbnail((CELL_IMAGE_WIDTH, CELL_IMAGE_HEIGHT))
        draw.rectangle(
            [
                image_left,
                image_top,
                image_left + CELL_IMAGE_WIDTH - 1,
                image_top + CELL_IMAGE_HEIGHT - 1,
            ],
            fill=(255, 255, 255),
        )
        paste_x = image_left + (CELL_IMAGE_WIDTH - image.width) // 2
        paste_y = image_top + (CELL_IMAGE_HEIGHT - image.height) // 2
        sheet.paste(image, (paste_x, paste_y))
        draw_label(
            draw,
            (image_left + 4, image_top + CELL_IMAGE_HEIGHT + 10),
            label,
            label_font,
            CELL_IMAGE_WIDTH - 8,
        )

    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination, format="PNG")


def is_outdated(destination, sources):
    """True when the sheet is missing or any source image is newer."""
    destination = Path(destination)
    if not destination.is_file():
        return True
    destination_time = destination.stat().st_mtime
    for source in sources:
        if Path(source).stat().st_mtime > destination_time:
            return True
    return False
