import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_10nf_queue import PART, reviewed_recipe


def test_selected_identity_and_model_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(record, recipes, 'test')
    assert result['model']['expected_bounds_mm'] == [3.2, 1.6, 1.6]
    assert result['model']['display_scale_xyz'] == [1, 1, .5]
    changed = copy.deepcopy(record); changed['dimensions_mm']['height'] = 1.6
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError):
        reviewed_recipe(changed, recipes, 'test')
