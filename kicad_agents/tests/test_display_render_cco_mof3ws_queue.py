import copy
import json

import pytest
import yaml

from kicad_agents.display_render_cco_mof3ws_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_large_package_rating_and_identity(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['bands'][-1] == 'gold'
    assert 'DIN0516' in result['model']['relative_path']
    assert '3 W' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('3W', '250mW')
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
