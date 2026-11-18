import numpy as np
import pytest

from kicad_agents.display_render_axial_composite import band_masks, compose


def test_axial_composite_identifies_five_regions_and_colours_them():
    black = np.full((500, 1000, 3), 40, dtype='uint8')
    white = black.copy()
    for x in (100, 250, 400, 550, 700):
        white[100:200, x:x+80] = 210
    masks = band_masks(black, white)
    assert len(masks) == 5
    out = compose(black, white, ['red', 'green', 'blue', 'yellow', 'brown'])
    assert out[150, 130, 0] > out[150, 130, 1]
    assert out[150, 280, 1] > out[150, 280, 0]
    assert out[150, 430, 2] > out[150, 430, 0]
    assert np.array_equal(out[20, 20], black[20, 20])
    with pytest.raises(ValueError, match='expected'):
        band_masks(black, black)


def test_four_band_calibration_keeps_all_stripes():
    black = np.full((500, 1000, 3), 40, dtype='uint8')
    white = black.copy()
    for x in (100, 250, 400, 700):
        white[100:200, x:x+80] = 210
    masks = band_masks(black, white, 4)
    assert len(masks) == 4
    out = compose(black, white, ['red', 'green', 'blue', 'gold'])
    assert out[150, 130, 0] > out[150, 130, 1]
    assert out[150, 280, 1] > out[150, 280, 0]
    assert out[150, 430, 2] > out[150, 430, 0]
    assert np.array_equal(out[20, 20], black[20, 20])
