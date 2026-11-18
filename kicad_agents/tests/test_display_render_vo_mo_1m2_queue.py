import copy
import json

import pytest
import yaml

from kicad_agents.display_render_vo_mo_1m2_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_selected_value_rating_and_colour_code():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['brown', 'red', 'green', 'gold']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('1.2MΩ', '1MΩ')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
