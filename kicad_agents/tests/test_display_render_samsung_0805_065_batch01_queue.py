import copy
import json
import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_065_batch01_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', list(PARTS))
def test_reviewed_identity_and_discrepancy(part):
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1, 1, .52]
    assert 'source lists 1.25 mm height' in recipe['appearance_status']
    for key in ('part_number_manufacturer', 'dimensions_mm'):
        changed = copy.deepcopy(record)
        changed[key] = 'changed' if key == 'part_number_manufacturer' else {'length': 2, 'width': 1.25, 'height': .65}
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'test')
