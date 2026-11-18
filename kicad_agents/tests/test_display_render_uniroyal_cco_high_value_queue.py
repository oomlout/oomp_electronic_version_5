import copy
import json

import pytest
import yaml

from kicad_agents.display_render_uniroyal_cco_high_value_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part,expected,model', [
    ('electronic_resistor_quarter_watt_through_hole_6800000_ohm', ['blue', 'grey', 'black', 'yellow', 'brown'], 'DIN0516'),
    ('electronic_resistor_quarter_watt_through_hole_820000_ohm', ['grey', 'red', 'black', 'orange', 'red'], 'DIN0207'),
])
def test_identity_value_and_package_guards(part, expected, model):
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
