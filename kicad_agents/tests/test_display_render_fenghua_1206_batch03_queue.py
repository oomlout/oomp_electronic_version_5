import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch03_queue import PARTS, MISSING_TOLERANCE, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_selected_part_and_changed_rating(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'test')
    assert recipe['represented_mpn'] == PARTS[part][0]
    assert ('source record omits tolerance' in recipe['appearance_status']) == (part == MISSING_TOLERANCE)
    changed = copy.deepcopy(record); changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['electrical']['tolerance'] = 'wrong'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
