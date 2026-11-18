import copy
import json

import pytest
import yaml

from kicad_agents.display_render_huaxing_mf1_8w_68k_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_smaller_package_and_source_rating_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['blue', 'grey', 'black', 'red', 'brown']
    assert 'DIN0204' in result['model']['relative_path']
    assert '125 mW' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('125mW', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
