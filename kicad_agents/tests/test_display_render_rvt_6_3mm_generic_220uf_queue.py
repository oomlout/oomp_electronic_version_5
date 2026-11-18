import copy
import json
import pytest
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_rvt_6_3mm_generic_220uf_queue import PART, reviewed_recipe
from kicad_agents.package_markings import marking_text

def test_generic_example_preserves_procurement_and_rejects_changed_identity():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    before = copy.deepcopy(record)
    recipe = reviewed_recipe(record, recipes, 'evidence')
    assert record == before
    assert recipe['represented_mpn'] == 'RVT1A221M0607'
    assert marking_text(recipe['marking']) == '220\n10V'
    assert 'without a selected supplier' in recipe['appearance_status']
    for field, value in [('name_proper', 'wrong'), ('lcsc_research_status', 'selected'), ('manufacturers', [{'manufacturer': 'Other'}])]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError): reviewed_recipe(changed, recipes, 'evidence')
