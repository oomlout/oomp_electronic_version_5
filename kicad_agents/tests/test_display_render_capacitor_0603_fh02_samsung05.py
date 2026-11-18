import copy
import json

import pytest
import yaml

from kicad_agents.display_render_fenghua_0603_batch02_queue import PARTS as FENGHUA, reviewed_recipe as fenghua_recipe
from kicad_agents.display_render_samsung_0603_batch05_queue import PARTS as SAMSUNG, NO_ELECTRICAL, ROOT, RECIPE_FILE, reviewed_recipe as samsung_recipe


@pytest.mark.parametrize('part', [*FENGHUA, *SAMSUNG])
def test_reviewed_identity_and_limitations(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    make = fenghua_recipe if part in FENGHUA else samsung_recipe
    result = make(part, record, recipes, 'test')
    assert result['marking']['policy'] == 'unmarked_illustration'
    assert 'not been verified' in result['marking']['appearance_status']
    if part in NO_ELECTRICAL:
        assert 'lacks electrical fields' in result['appearance_status']
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        make(part, changed, recipes, 'test')
