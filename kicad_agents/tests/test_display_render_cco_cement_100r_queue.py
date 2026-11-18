import copy
import json

import pytest
import yaml

from kicad_agents.display_render_cco_cement_100r_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe
from kicad_agents.package_markings import marking_text


def test_cement_identity_rating_and_illustrative_marking():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert marking_text(result['marking']) == '100Ω 5W'
    assert 'unverified' in result['marking']['appearance_status']
    assert '5 W' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('5W', '2W')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    missing = dict(result['marking']); missing.pop('appearance_status')
    with pytest.raises(ValueError):
        marking_text(missing)
