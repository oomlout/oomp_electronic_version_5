import copy
import json

import pytest
import yaml

from kicad_agents.display_render_yageo_0603_100nf_queue import PART, ROOT, RECIPE_FILE, reviewed_recipe
from kicad_agents.package_markings import marking_text


def test_selected_capacitor_and_unverified_marking_disclosure():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert marking_text(result['marking']) == ''
    assert 'not been verified' in result['marking']['appearance_status']
    changed = copy.deepcopy(record)
    changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace('50V', '25V')
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
