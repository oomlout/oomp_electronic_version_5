import copy
import json

import pytest
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_taj_a_batch01_queue import PARTS, reviewed_recipe
from kicad_agents.display_render_taj_a_batch02_queue import PARTS as PARTS_02, reviewed_recipe as reviewed_recipe_02
from kicad_agents.display_render_taj_a_batch03_queue import PARTS as PARTS_03, reviewed_recipe as reviewed_recipe_03
from kicad_agents.display_render_taj_a_batch04_queue import PARTS as PARTS_04, reviewed_recipe as reviewed_recipe_04
from kicad_agents.display_render_taj_b_batch01_queue import PARTS as B_PARTS, reviewed_recipe as reviewed_b_recipe
from kicad_agents.display_render_taj_b_batch02_queue import PARTS as B_PARTS_02, reviewed_recipe as reviewed_b_recipe_02
from kicad_agents.display_render_taj_b_batch03_queue import PARTS as B_PARTS_03, reviewed_recipe as reviewed_b_recipe_03
from kicad_agents.package_markings import marking_text


@pytest.mark.parametrize('part', list(PARTS))
def test_taj_recipes_match_reviewed_parts_and_markings(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'evidence-hash')
    mpn, _, _, volts, code = PARTS[part]
    assert recipe['represented_mpn'] == mpn
    assert marking_text(recipe['marking']).startswith(code + ' ')
    assert recipe['marking']['rated_voltage_v'] == volts
    changed = copy.deepcopy(record)
    changed['electrical']['polarized'] = False
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_recipe(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(PARTS_02))
def test_second_taj_batch_rejects_wrong_voltage(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe_02(part, record, recipes, 'evidence-hash')
    assert recipe['represented_mpn'] == PARTS_02[part][0]
    assert marking_text(recipe['marking']).startswith(PARTS_02[part][4] + ' ')
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '999 V'
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_recipe_02(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(PARTS_03))
def test_taj_fractional_voltage_code_and_identity(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe_03(part, record, recipes, 'evidence-hash')
    _, _, _, volts, code = PARTS_03[part]
    letter = {'6.3': 'J', '10': 'A', '20': 'D'}[volts]
    assert marking_text(recipe['marking']) == f'{code} {letter}'
    changed = copy.deepcopy(record)
    changed['part_number_manufacturer'] = 'TAJA000K999RNJ'
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_recipe_03(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(PARTS_04))
def test_taj_tolerance_variants_and_incomplete_generic_source(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe_04(part, record, recipes, 'evidence-hash')
    mpn, _, _, volts, code = PARTS_04[part]
    assert recipe['represented_mpn'] == mpn
    assert marking_text(recipe['marking']) == f"{code} { {'10': 'A', '16': 'C'}[volts] }"
    changed = copy.deepcopy(record)
    changed['part_number_lcsc'] = 'wrong'
    with pytest.raises(ValueError):
        reviewed_recipe_04(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(B_PARTS))
def test_taj_b_case_rejects_wrong_package(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_b_recipe(part, record, recipes, 'evidence-hash')
    assert recipe['marking']['case'] == 'B'
    assert recipe['model']['expected_bounds_mm'] == [3.5, 2.8, 2.1]
    changed = copy.deepcopy(record)
    changed['electrical']['case_size'] = 'CASE-A-3216-18'
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_b_recipe(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(B_PARTS_02))
def test_taj_b_case_tolerance_and_voltage_variants(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_b_recipe_02(part, record, recipes, 'evidence-hash')
    _, _, _, volts, code = B_PARTS_02[part]
    assert marking_text(recipe['marking']) == f"{code} { {'4': 'G', '6.3': 'J', '10': 'A'}[volts] }"
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '999 V'
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_b_recipe_02(part, changed, recipes, 'evidence-hash')


@pytest.mark.parametrize('part', list(B_PARTS_03))
def test_taj_b_third_batch_rejects_changed_capacitance(part):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_b_recipe_03(part, record, recipes, 'evidence-hash')
    assert recipe['represented_mpn'] == B_PARTS_03[part][0]
    assert marking_text(recipe['marking']).startswith(B_PARTS_03[part][4] + ' ')
    changed = copy.deepcopy(record)
    changed['electrical']['capacitance'] = '999 uF'
    with pytest.raises(ValueError, match='identity, ratings or package'):
        reviewed_b_recipe_03(part, changed, recipes, 'evidence-hash')
