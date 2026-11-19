import copy
import pytest
from kicad_agents.display_render_wurth_8x6_5_example_queue import REFERENCE, reviewed_recipe


def sample():
    return {'name_proper': 'Capacitor 220 uF 10 V Electrolytic 8 mm diameter x 6.5 mm tall',
            'dimensions_mm': {'length': 8., 'width': 8.}, 'manufacturers': [], 'distributors': [],
            'kicad': {'machine_solder': '', 'symbol': ''}}


def test_example_preserves_reference_and_discloses_missing_data():
    recipes = {REFERENCE: {'family': 'aluminum_capacitor', 'model': {'metal_top_marking': True}, 'marking': {}}}
    before = copy.deepcopy(recipes)
    result = reviewed_recipe(sample(), recipes, 'a'*64)
    assert result['marking']['text'] == '221\n10V'
    assert result['model']['expected_bounds_mm'] == [9.5, 8.3, 6.5]
    assert 'not a selected procurement part' in result['appearance_status']
    assert 'date line' in result['marking']['appearance_status']
    assert recipes == before


def test_newly_selected_supplier_requires_new_review():
    record = sample()
    record['manufacturer'] = 'Würth'
    with pytest.raises(ValueError, match='review again'):
        reviewed_recipe(record, {}, 'a'*64)
