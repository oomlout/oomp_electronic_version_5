import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0402_batch01_queue import PARTS, NO_ELECTRICAL, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_selected_part_and_geometry_guard(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['represented_mpn'] == PARTS[part][0]
    assert result['model']['expected_bounds_mm'] == [1, .5, .5]
    assert ('lacks electrical fields' in result['appearance_status']) == (part in NO_ELECTRICAL)
    changed = copy.deepcopy(record); changed['dimensions_mm']['height'] = .8
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['electrical'] = {'rated_voltage': 'wrong'}
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
