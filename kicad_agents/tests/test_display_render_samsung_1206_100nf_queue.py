import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_1206_100nf_queue import PART, reviewed_recipe


def test_selected_part_and_missing_electrical_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1, 1, .53125]
    assert 'source record lacks electrical fields' in recipe['appearance_status']
    changed = copy.deepcopy(record); changed['electrical'] = {'rated_voltage': '100 V'}
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['part_number_manufacturer'] = 'changed'
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
