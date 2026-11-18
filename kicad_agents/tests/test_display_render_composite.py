import numpy as np
import pytest

from kicad_agents.display_render_composite import composite, forward_tone, inverse_tone, read_recipe


def test_tone_mapping_round_trip_and_composite_endpoints():
    values = np.array([.1, .3, .5, .7, .9], dtype='float32')
    assert np.allclose(forward_tone(inverse_tone(values)), values, atol=1e-5)
    body = np.full((2, 2, 3), 60, dtype='float32')
    ink = np.full((2, 2, 3), 180, dtype='float32')
    result = composite(body, ink, np.array([[0, 1], [.5, 0]], dtype='float32'))
    assert np.all(result[0, 0] == 60)
    assert np.all(result[0, 1] == 180)
    assert np.all((result[1, 0] > 60) & (result[1, 0] < 180))


def test_compositor_accepts_reviewed_packages_and_rejects_unmarked_small_package():
    for part in ('electronic_resistor_0603_1000_ohm', 'electronic_resistor_0603_102000_ohm',
                 'electronic_resistor_0805_1000_ohm',
                 'electronic_resistor_1206_1000_ohm'):
        assert read_recipe(part)['family'] == 'chip_resistor'
    assert read_recipe('electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin')['family'] == 'chip_resistor_array'
    assert read_recipe('electronic_resistor_array_4_x_0603_convex_10000_ohm_8_pin')['family'] == 'chip_resistor_array'
    with pytest.raises(ValueError, match='reviewed only'):
        read_recipe('electronic_resistor_0402_1000_ohm')
