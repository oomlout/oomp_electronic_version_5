import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_1206_batch01_queue import PARTS, NO_ELECTRICAL, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_selected_part_guard_and_missing_fields(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'test')
    assert recipe['represented_mpn'] == PARTS[part][0]
    assert 'display_scale_xyz' not in recipe['model']
    assert ('lacks electrical fields' in recipe['appearance_status']) == (part in NO_ELECTRICAL)
    changed = copy.deepcopy(record); changed['dimensions_mm']['height'] = .8
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['electrical'] = {'rated_voltage': 'wrong'}
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
