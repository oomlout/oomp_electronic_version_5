import copy
import pytest
from kicad_agents.display_render_tdk_1210_68uf_example_queue import REFERENCE, reviewed_recipe


def sample():
    return {'name_proper': 'Capacitor 68 uF 1210', 'dimensions_mm': {'length': 10., 'width': 5.},
            'kicad': {'machine_solder': 'Capacitor_SMD:C_1210_3225Metric'}, 'manufacturers': [], 'distributors': []}


def test_generic_example_discloses_conflict_and_preserves_reference():
    recipes = {REFERENCE: {'family': 'chip_capacitor', 'model': {'expected_bounds_mm': [3.2, 2.5, 2.5]},
                           'marking': {'policy': 'unmarked_illustration'}}}
    before = copy.deepcopy(recipes)
    result = reviewed_recipe(sample(), recipes, 'a'*64)
    assert result['model']['display_scale_xyz'] == [1., 1., .8]
    assert 'dimension conflict' in result['appearance_status']
    assert 'not an asserted rating' in result['appearance_status']
    assert recipes == before


def test_new_procurement_identity_requires_new_review():
    item = sample()
    item['part_number_manufacturer'] = 'something else'
    with pytest.raises(ValueError, match='review again'):
        reviewed_recipe(item, {}, 'a'*64)
