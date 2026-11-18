import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch06_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_missing_tolerance_and_changed_fields(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_recipe(part, record, recipes, 'test')
    assert 'source record omits tolerance' in result['appearance_status']
    assert 'tolerance' not in record['electrical']
    changed = copy.deepcopy(record); changed['electrical']['tolerance'] = '±0.5 pF'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
    changed = copy.deepcopy(record); changed['part_number_manufacturer'] = 'changed'
    with pytest.raises(ValueError):
        reviewed_recipe(part, changed, recipes, 'test')
