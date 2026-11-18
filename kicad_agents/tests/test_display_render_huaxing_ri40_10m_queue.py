import copy
import json

import pytest
import yaml

from kicad_agents.display_render_huaxing_ri40_10m_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_huaxing_10m_identity_rating_and_tolerance():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['brown', 'black', 'black', 'green', 'red']
    assert result['package'] == 'din0414_horizontal_15_24mm'
    assert '1 W' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('1W', '2W')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
