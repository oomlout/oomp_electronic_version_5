import copy
import json

import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_10uf_queue import PART, reviewed_recipe


def test_recipe_matches_selected_part_and_discloses_illustration():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['expected_bounds_mm'] == [2.0, 1.25, 1.25]
    assert recipe['marking']['policy'] == 'unmarked_illustration'
    assert 'not been verified' in recipe['marking']['appearance_status']


@pytest.mark.parametrize('field,value', [('rated_voltage', '25 V'), ('capacitance', '1 uF'), ('dielectric', 'X7R')])
def test_changed_electrical_spec_rejected(field, value):
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    record = copy.deepcopy(record)
    record['electrical'][field] = value
    with pytest.raises(ValueError):
        reviewed_recipe(record, {}, 'test')
