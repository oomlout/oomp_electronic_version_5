import copy
import json

import pytest
import yaml

from kicad_agents.display_render_fenghua_0603_batch01_queue import PARTS, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part', PARTS)
def test_source_identity_and_illustration(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['policy'] == 'unmarked_illustration'
    assert 'not been verified' in result['marking']['appearance_status']
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
