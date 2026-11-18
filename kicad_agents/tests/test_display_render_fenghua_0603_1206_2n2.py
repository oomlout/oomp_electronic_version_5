import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch05_queue import PARTS, NO_ELECTRICAL, reviewed_recipe as reviewed_0603
from kicad_agents.display_render_fenghua_1206_2n2_queue import PART as PART_1206, reviewed_recipe as reviewed_1206


@pytest.mark.parametrize('part', list(PARTS))
def test_0603_identity_and_missing_fields(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_0603(part, record, recipes, 'test')
    assert result['represented_mpn'] == PARTS[part][0]
    assert ('lacks electrical fields' in result['appearance_status']) == (part in NO_ELECTRICAL)
    changed = copy.deepcopy(record); changed['electrical'] = {'rated_voltage': 'wrong'}
    with pytest.raises(ValueError):
        reviewed_0603(part, changed, recipes, 'test')


def test_1206_identity_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART_1206 / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    result = reviewed_1206(record, recipes, 'test')
    assert result['model']['display_scale_xyz'] == [1, 1, .5]
    record['electrical']['rated_voltage'] = 'wrong'
    with pytest.raises(ValueError):
        reviewed_1206(record, recipes, 'test')
