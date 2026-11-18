import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_batch01_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_identity_and_geometry_guard(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['marking']['policy'] == 'unmarked_illustration'
    assert result['model']['expected_bounds_mm'] == [2.0, 1.25, 1.25]
    altered = copy.deepcopy(record)
    altered['part_number_manufacturer'] = 'different'
    with pytest.raises(ValueError):
        reviewed_recipe(part, altered, recipes, 'test')
    altered = copy.deepcopy(record)
    altered['dimensions_mm']['height'] = 0.65
    with pytest.raises(ValueError):
        reviewed_recipe(part, altered, recipes, 'test')


def test_electrical_changes_are_rejected():
    part = list(PARTS)[-1]
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    record['electrical']['rated_voltage'] = '50 V'
    with pytest.raises(ValueError):
        reviewed_recipe(part, record, {}, 'test')
