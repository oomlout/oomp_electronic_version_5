import copy
import json

import pytest
import yaml

from kicad_agents.display_render_remaining_carbon_queue import ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part,bands,package', [
    ('electronic_resistor_quarter_watt_through_hole_39_ohm', ['orange', 'white', 'black', 'gold'], 'din0207_horizontal_7_62mm'),
    ('electronic_resistor_quarter_watt_through_hole_39000_ohm', ['orange', 'white', 'orange', 'gold'], 'din0204_horizontal_7_62mm'),
])
def test_source_guard_and_marking(part, bands, package):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['bands'] == bands
    assert result['package'] == package
    assert 'truncated' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = 'different resistor'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
