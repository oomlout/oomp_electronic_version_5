from pathlib import Path

import pytest
from PIL import Image

from kicad_agents.display_render import create_textures, find_font, repair_nonfinite_pixels


@pytest.fixture
def marking():
    try:
        find_font('arialbd.ttf')
    except FileNotFoundError:
        pytest.skip('Reviewed marking font is not installed on this machine')
    return {'font_file': 'arialbd.ttf', 'maximum_width_mm': .76, 'maximum_height_mm': .32}


def test_underlined_marking_has_a_continuous_line_below_the_text(tmp_path, marking):
    create_textures({**marking, 'underline': True}, '333', [1.6, .8, .45], tmp_path)
    image = Image.open(tmp_path / 'marking.png').convert('L')
    bounds = image.getbbox()
    assert bounds is not None
    left, top, right, bottom = bounds
    # The last interior row contains one continuous stroke spanning the glyph width.
    line = [image.getpixel((x, bottom - 2)) for x in range(left + 2, right - 2)]
    assert line and min(line) > 200
    assert right - left < image.width * .7 and bottom - top < image.height * .75


def test_middle_character_underline_is_short_and_centered(tmp_path, marking):
    create_textures({**marking, 'underline_character': 1}, '223', [1.6, .8, .45], tmp_path)
    image = Image.open(tmp_path / 'marking.png').convert('L')
    left, top, right, bottom = image.getbbox()
    ink = [x for x in range(left, right) if image.getpixel((x, bottom - 2)) > 180]
    assert ink and max(ink) - min(ink) < (right - left) * .5
    assert abs((min(ink) + max(ink)) / 2 - (left + right) / 2) < (right - left) * .1
    with pytest.raises(ValueError, match='Character underline'):
        create_textures({**marking, 'underline_character': 3}, '223', [1.6, .8, .45], tmp_path)


def test_rotated_array_marking_fits_physical_coating(tmp_path, marking):
    options = {**marking, 'rotation_degrees': 90, 'maximum_width_mm': 1.1, 'maximum_height_mm': .32}
    create_textures(options, '332', [1., 2., .35], tmp_path)
    image = Image.open(tmp_path / 'marking.png').convert('L')
    left, top, right, bottom = image.getbbox()
    physical_x = (right-left) / image.width
    physical_y = (bottom-top) * 2 / image.height
    assert physical_x <= .33 and physical_y <= 1.11 and physical_y > physical_x
    with pytest.raises(ValueError, match='rotation'):
        create_textures({**options, 'rotation_degrees': 45}, '332', [1., 2., .35], tmp_path)


def test_multiline_text_renders_without_float_image_dimensions(tmp_path, marking):
    create_textures(marking, 'ABC\n123', [1.6, .8, .45], tmp_path)
    assert Image.open(tmp_path / 'marking.png').getbbox() is not None
    with pytest.raises(ValueError, match='single line'):
        create_textures({**marking, 'underline': True}, 'ABC\n123', [1.6, .8, .45], tmp_path)


def test_isolated_nonfinite_pixel_is_repaired_but_widespread_failure_is_rejected():
    import numpy as np
    image = np.ones((20, 20, 3), dtype='float32')
    image[10, 10, 1] = float('nan')
    repaired, count = repair_nonfinite_pixels(image)
    assert count == 1 and np.isfinite(repaired).all()
    assert np.allclose(repaired[10, 10], [1, 1, 1], atol=.02)
    image[:5, 0, :] = float('inf')
    with pytest.raises(ValueError, match='non-finite'):
        repair_nonfinite_pixels(image)


def test_cluster_of_nonfinite_samples_uses_valid_neighbours():
    import numpy as np
    image = np.full((500, 500, 3), .6, dtype='float32')
    image[100:103, 100:103] = float('nan')
    repaired, count = repair_nonfinite_pixels(image)
    assert count == 9 and np.isfinite(repaired).all()
    assert np.allclose(repaired[100:103, 100:103], .6)
