import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_batch02_queue import PARTS, NO_ELECTRICAL, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_reviewed_identity_and_record_changes(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'test')
    assert recipe['represented_mpn'] == PARTS[part][0]
    assert recipe['marking']['policy'] == 'unmarked_illustration'
    assert ('lacks electrical fields' in recipe['appearance_status']) == (part in NO_ELECTRICAL)
    changed = copy.deepcopy(record)
    changed['dimensions_mm']['height'] = 0.65
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record)
    changed['electrical'] = {'capacitance': 'wrong'}
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
