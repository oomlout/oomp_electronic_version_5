import copy
import json

import pytest
import yaml

from kicad_agents.display_render_samsung_0603_batch04_queue import PARTS, NO_ELECTRICAL, ROOT, RECIPE_FILE, reviewed_recipe


@pytest.mark.parametrize('part', PARTS)
def test_identity_source_omissions_and_conflicts(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['policy'] == 'unmarked_illustration'
    if part in NO_ELECTRICAL:
        assert 'lacks electrical fields' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['electrical'] = {'rated_voltage': '12 V'}
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
