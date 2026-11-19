import copy
import pytest
from kicad_agents.display_render_radial_km_10x17_pilot_queue import REFERENCE, reviewed_recipe


def record():
    return {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': 'KM477M035G17RR0VH2FP0',
            'part_number_lcsc': 'C2064', 'electrical': {'capacitance': '470 uF', 'rated_voltage': '35 V',
            'pin_spacing': '5.0 mm', 'polarized': True}, 'dimensions_mm': {'length': 10., 'width': 10., 'height': 17.},
            'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'}}


def test_reviewed_recipe_does_not_modify_reference():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'model': {}, 'marking': {}}}
    before = copy.deepcopy(recipes)
    result = reviewed_recipe(record(), recipes, 'a' * 64)
    assert recipes == before
    assert result['model']['radial_stretch']['extra_height'] == 7
    assert result['marking']['text'] == '470uF\n35V\nKM 105C'
    assert 'temperature' in result['appearance_status']


@pytest.mark.parametrize('field,value', [('capacitance', '47 uF'), ('rated_voltage', '50 V'),
                                          ('pin_spacing', '3.5 mm'), ('polarized', False)])
def test_identity_mismatch_is_rejected(field, value):
    item = record()
    item['electrical'][field] = value
    with pytest.raises(ValueError, match='identity'):
        reviewed_recipe(item, {}, 'a' * 64)
