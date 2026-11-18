import copy
import json

import pytest
import yaml

from kicad_agents.display_render_cco_cf1_6w_2k4_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe


def test_selected_rating_and_small_four_band_package():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['marking']['bands'] == ['red', 'yellow', 'red', 'gold']
    assert 'DIN0204' in result['model']['relative_path']
    assert '167 mW' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('167mW', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
