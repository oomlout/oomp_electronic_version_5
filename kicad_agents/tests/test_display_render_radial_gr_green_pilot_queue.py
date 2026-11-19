import copy
import pytest
from kicad_agents.display_render_radial_gr_green_pilot_queue import REFERENCE, reviewed_recipe


def sample():
    return {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': 'GR108M010F12RR0VL4FP0',
            'part_number_lcsc': 'C3299', 'electrical': {'capacitance': '1000 uF', 'rated_voltage': '10 V',
            'pin_spacing': '3.5 mm', 'polarized': True}, 'dimensions_mm': {'length': 8., 'width': 8., 'height': 12.},
            'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm'}}


def test_exact_green_gold_part_and_reference_unchanged():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor',
               'model': {'radial_stretch': {'extra_height': 4.}}, 'marking': {}}}
    before = copy.deepcopy(recipes)
    result = reviewed_recipe(sample(), recipes, 'a'*64)
    assert result['radial_palette'] == 'green_gold'
    assert result['marking']['text'] == '1000uF\n10V\nGR 105C'
    assert recipes == before


def test_wrong_part_is_rejected():
    record = sample()
    record['electrical']['rated_voltage'] = '16 V'
    with pytest.raises(ValueError, match='Identity'):
        reviewed_recipe(record, {}, 'a'*64)
