import copy
import pytest
from kicad_agents.display_render_radial_km_6x11_pilot_queue import REFERENCE, reviewed_recipe


def sample():
    return {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': 'KM106M100E11RR0VH2FP0',
            'part_number_lcsc': 'C2029', 'electrical': {'capacitance': '10 uF', 'rated_voltage': '100 V',
            'pin_spacing': '2.5 mm', 'polarized': True}, 'dimensions_mm': {'length': 6.3, 'width': 6.3, 'height': 11.},
            'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D6.3mm_P2.50mm'}}


def test_reviewed_geometry_and_marking():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'model': {}, 'marking': {}}}
    original = copy.deepcopy(recipes)
    recipe = reviewed_recipe(sample(), recipes, 'a' * 64)
    assert recipe['model']['radial_stretch']['extra_height'] == 4.7
    assert recipe['marking']['text'] == '10uF\n100V\nKM 105C'
    assert recipes == original


def test_wrong_voltage_is_rejected():
    record = sample()
    record['electrical']['rated_voltage'] = '10 V'
    with pytest.raises(ValueError, match='Identity'):
        reviewed_recipe(record, {}, 'a' * 64)
