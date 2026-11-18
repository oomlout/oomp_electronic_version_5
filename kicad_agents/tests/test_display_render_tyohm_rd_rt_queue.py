import copy
import json

import pytest
import yaml

from kicad_agents.display_render_tyohm_rd_rt_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part,expected', [
    ('electronic_resistor_quarter_watt_through_hole_5600000_ohm', ['green', 'blue', 'green', 'gold']),
    ('electronic_resistor_quarter_watt_through_hole_2200000_ohm', ['red', 'red', 'green', 'gold']),
])
def test_reviewed_identity_and_value_guards(part, expected):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['bands'] == expected
    assert 'DIN0207' in result['model']['relative_path']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('±5%', '±1%')
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
