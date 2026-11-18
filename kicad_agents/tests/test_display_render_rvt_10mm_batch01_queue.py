import copy
import json
import pytest
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_rvt_10mm_batch01_queue import PARTS, reviewed_recipe
from kicad_agents.package_markings import marking_text

@pytest.mark.parametrize('part', list(PARTS))
def test_rvt_10mm_identity_polarity_and_marking(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'evidence')
    assert marking_text(recipe['marking']) == PARTS[part][4]
    for field, value in [('rated_voltage', '999 V'), ('capacitance', '999 uF'), ('polarized', False)]:
        changed = copy.deepcopy(record)
        changed['electrical'][field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'evidence')
