"""Assemble a contact sheet from already rendered component images.

This reads final images only; it does not invoke a renderer or catalogue generator.
"""
import argparse
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def create_contact_sheet(parts, output, tile=660, columns=None):
    if not parts:
        raise ValueError('Select at least one exact part and its label')
    if columns is not None and columns < 1:
        raise ValueError('Columns must be a positive integer')
    images = []
    for part_id, label in parts:
        if not re.fullmatch(r'electronic_[a-z0-9_]+', part_id):
            raise ValueError(f'Invalid exact component ID: {part_id}')
        path = ROOT / 'parts' / part_id / 'data/display_render/render.png'
        with Image.open(path) as source:
            image = source.convert('RGB')
            image.thumbnail((tile, tile), Image.Resampling.LANCZOS)
            images.append((image, label))
    margin = 20
    columns = min(columns or len(images), len(images))
    rows = (len(images) + columns - 1) // columns
    row_height = tile + 100
    canvas = Image.new('RGB', (columns * (tile + margin) + margin, rows * row_height), '#f4f4f2')
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype('arialbd.ttf', 25)
    except OSError:
        font = ImageFont.load_default(size=25)
    for index, (image, label) in enumerate(images):
        x = margin + (index % columns) * (tile + margin)
        y = (index // columns) * row_height
        canvas.paste(image, (x + (tile-image.width)//2, y + margin + (tile-image.height)//2))
        # Deliberately fail rather than silently clip a misleading label.
        if draw.textbbox((0, 0), label, font=font)[2] > tile:
            raise ValueError(f'Contact sheet label is too long: {label}')
        draw.text((x, y + tile + 38), label, font=font, fill='#20252a')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--part', nargs=2, action='append', metavar=('EXACT_ID', 'LABEL'), required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--columns', type=int, help='Number of columns; defaults to one row')
    args = parser.parse_args()
    print(create_contact_sheet(args.part, args.output, columns=args.columns))


if __name__ == '__main__':
    main()
