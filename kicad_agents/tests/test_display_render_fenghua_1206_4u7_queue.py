import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_4u7_queue import PART, reviewed_recipe


def test_selected_identity_and_missing_fields():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert 'lacks electrical fields' in result['appearance_status']
    assert 'display_scale_xyz' not in result['model']
    changed = copy.deepcopy(record); changed['electrical'] = {'rated_voltage': '25 V'}
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['part_number_manufacturer'] = 'changed'
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
