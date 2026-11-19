import copy
import pytest
from kicad_agents.display_render_radial_km_10x20_pilot_queue import REFERENCE, reviewed_recipe


def sample():
    return {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': 'KM228M016G20RR0VH2FP0',
            'part_number_lcsc': 'C3328', 'electrical': {'capacitance': '2200 uF', 'rated_voltage': '16 V',
            'pin_spacing': '5.0 mm', 'polarized': True}, 'dimensions_mm': {'length': 10., 'width': 10., 'height': 20.},
            'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'}}


def test_tall_can_recipe_preserves_reference():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'represented_mpn': 'KM477M035G17RR0VH2FP0',
               'model': {'radial_stretch': {'extra_height': 7.}}, 'marking': {}}}
    original = copy.deepcopy(recipes)
    result = reviewed_recipe(sample(), recipes, 'a' * 64)
    assert recipes == original
    assert result['model']['radial_stretch']['extra_height'] == 10.
    assert result['marking']['text'] == '2200uF\n16V\nKM 105C'
    assert 'temperature' in result['appearance_status']


def test_changed_polarity_is_rejected():
    record = sample()
    record['electrical']['polarized'] = False
    with pytest.raises(ValueError, match='Identity'):
        reviewed_recipe(record, {}, 'a' * 64)
