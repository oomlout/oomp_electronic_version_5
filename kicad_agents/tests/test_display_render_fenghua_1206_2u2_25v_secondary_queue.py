import copy
import json
import pytest
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_2u2_25v_secondary_queue import PART, SOURCE, reviewed_recipe
from working_oomp_populate_display_render import unmarked_visual_recipe

def test_exact_rating_and_reuse_geometry_are_guarded():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'evidence')
    assert unmarked_visual_recipe(recipe) == unmarked_visual_recipe(recipes[SOURCE])
    assert 'manufacturer drawing was not independently accessed' in recipe['appearance_status']
    for field, value in [('rated_voltage', '50 V'), ('dielectric', 'X7R'), ('capacitance', '2.2 nF')]:
        changed = copy.deepcopy(record)
        changed['electrical'][field] = value
        with pytest.raises(ValueError): reviewed_recipe(changed, recipes, 'evidence')
