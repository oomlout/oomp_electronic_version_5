import copy
import pytest

from kicad_agents.display_render_radial_ks_pilot_queue import REFERENCE, reviewed_recipe


def sample():
    return {'manufacturer': 'CX(Dongguan Chengxing Elec)',
            'part_number_manufacturer': 'KS336M016C07RR0VH2FP0', 'part_number_lcsc': 'C3314',
            'electrical': {'capacitance': '33 uF', 'rated_voltage': '16 V',
                           'pin_spacing': '1.5 mm', 'polarized': True},
            'dimensions_mm': {'length': 4., 'width': 4., 'height': 7.},
            'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D4.0mm_P1.50mm'}}


def test_recipe_matches_reviewed_can_and_keeps_reference_unchanged():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'model': {}, 'marking': {}}}
    original = copy.deepcopy(recipes)
    recipe = reviewed_recipe(sample(), recipes, 'a' * 64)
    assert recipes == original
    assert recipe['model']['radial_stretch']['extra_height'] == 3
    assert recipe['model']['flat_top']['radius'] == 1.4
    assert recipe['marking']['text'] == '33uF\n16V\nKS 105C'
    assert recipe['marking']['evidence']['sha256'] == 'a' * 64


@pytest.mark.parametrize('field,value', [('capacitance', '330 uF'), ('rated_voltage', '25 V'),
                                          ('pin_spacing', '2 mm'), ('polarized', False)])
def test_rejects_mismatched_part(field, value):
    record = sample()
    record['electrical'][field] = value
    with pytest.raises(ValueError, match='identity'):
        reviewed_recipe(record, {}, 'a' * 64)
