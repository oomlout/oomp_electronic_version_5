import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch05_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_guarded_identity_and_dimensions(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert result['represented_mpn'] == PARTS[part][0]
    assert result['model']['display_scale_xyz'] == [1, 1, .64]
    altered = copy.deepcopy(record); altered['part_number_manufacturer'] = 'changed'
    with pytest.raises(ValueError):
        reviewed_recipe(part, altered, recipes, 'test')
    altered = copy.deepcopy(record); altered['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError):
        reviewed_recipe(part, altered, recipes, 'test')
