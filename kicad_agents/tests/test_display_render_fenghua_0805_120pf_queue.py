import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_120pf_queue import PART, reviewed_recipe


def test_selected_fenghua_and_dimensions_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1, 1, .64]
    assert recipe['marking']['policy'] == 'unmarked_illustration'
    for field, value in [('part_number_manufacturer', 'different'), ('dimensions_mm', {'length': 2, 'width': 1.25, 'height': .65})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(changed, recipes, 'test')
