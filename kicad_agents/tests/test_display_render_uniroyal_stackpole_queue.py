import copy
import json

import pytest
import yaml

from kicad_agents.display_render_uniroyal_stackpole_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part,expected,model', [
    ('electronic_resistor_quarter_watt_through_hole_2700000_ohm', ['red', 'violet', 'black', 'yellow', 'brown'], 'DIN0207'),
    ('electronic_resistor_quarter_watt_through_hole_8200000_ohm', ['grey', 'red', 'green', 'gold'], 'DIN0309'),
])
def test_reviewed_identity_and_value_guards(part, expected, model):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['bands'] == expected
    assert model in result['model']['relative_path']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = 'different part'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
