import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_470nf_queue import PART, reviewed_recipe


def test_selected_identity_and_scaled_geometry():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1, 1, .78125]
    assert '1.25 mm' in recipe['appearance_status']
    changed = copy.deepcopy(record); changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['dimensions_mm']['height'] = .8
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
