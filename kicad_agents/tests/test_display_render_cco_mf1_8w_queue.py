import copy
import json

import pytest
import yaml

from kicad_agents.display_render_cco_mf1_8w_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_small_package_rating_and_identity(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['bands'][-1] == 'brown'
    assert 'DIN0204' in result['model']['relative_path']
    assert '125 mW' in result['appearance_status']
    bad = copy.deepcopy(record)
    bad['distributors'][0]['product_name'] = bad['distributors'][0]['product_name'].replace('125mW', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(part, bad, recipes, 'test')
