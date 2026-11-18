import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch03_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_selected_part_ratings_and_dimensions(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'test')
    assert recipe['represented_mpn'] == PARTS[part][0]
    assert recipe['model']['display_scale_xyz'] == [1, 1, .64]
    changed = copy.deepcopy(record); changed['dimensions_mm']['height'] = .65
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['electrical']['dielectric'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
