import copy
import json

import pytest
import yaml

from kicad_agents.display_render_samsung_0603_batch01_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe
from working_oomp_populate_display_render import unmarked_visual_recipe


@pytest.mark.parametrize('part', PARTS)
def test_selected_identity_and_blank_illustration(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    r = reviewed_recipe(part, record, recipes, 'test')
    assert r['marking']['policy'] == 'unmarked_illustration'
    assert 'not been verified' in r['marking']['appearance_status']
    unmarked_visual_recipe(r)
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record)
    changed['dimensions_mm']['width'] = 1.2
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
