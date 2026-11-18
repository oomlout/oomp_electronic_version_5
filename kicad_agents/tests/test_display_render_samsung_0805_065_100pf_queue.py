import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_065_100pf_queue import PART, reviewed_recipe


def test_thin_selected_part_and_height_discrepancy():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1, 1, .52]
    assert 'source lists 1.25 mm height' in recipe['appearance_status']
    changed = copy.deepcopy(record)
    changed['dimensions_mm']['height'] = .65
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    changed = copy.deepcopy(record)
    changed['electrical']['dielectric'] = 'X7R'
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
