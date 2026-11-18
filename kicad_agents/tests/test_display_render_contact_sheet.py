from pathlib import Path

import pytest
from PIL import Image

from kicad_agents import display_render_contact_sheet as sheet


def test_contact_sheet_supports_a_review_grid(tmp_path, monkeypatch):
    monkeypatch.setattr(sheet, 'ROOT', tmp_path)
    parts = []
    for index in range(3):
        part = f'electronic_part_{index}'
        folder = tmp_path/'parts'/part/'data/display_render'
        folder.mkdir(parents=True)
        Image.new('RGB', (80, 80), (40*index, 20, 30)).save(folder/'render.png')
        parts.append((part, str(index)))
    output = tmp_path/'review.png'
    sheet.create_contact_sheet(parts, output, tile=100, columns=2)
    with Image.open(output) as image:
        assert image.size == (260, 400)
        assert image.getpixel((70, 70)) == (0, 20, 30)
        assert image.getpixel((190, 70)) == (40, 20, 30)
        assert image.getpixel((70, 270)) == (80, 20, 30)


def test_contact_sheet_rejects_untrusted_ids_and_bad_column_count(tmp_path):
    with pytest.raises(ValueError, match='Invalid exact'):
        sheet.create_contact_sheet([('../outside', 'bad')], tmp_path/'out.png')
    with pytest.raises(ValueError, match='positive'):
        sheet.create_contact_sheet([('electronic_part', 'x')], tmp_path/'out.png', columns=0)
