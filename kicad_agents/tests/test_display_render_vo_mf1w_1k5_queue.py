import copy
import json

import pytest
import yaml

from kicad_agents.display_render_vo_mf1w_1k5_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_selected_rating_and_code():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['brown', 'green', 'black', 'brown', 'brown']
    assert 'DIN0414' in result['model']['relative_path']
    assert '1 W' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('1W', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
