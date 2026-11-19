import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_1nf_queue as q
from kicad_agents import display_render_fenghua_1206_c0g_table_queue as table
from kicad_agents import display_render_fenghua_1206_c0g_table_02_queue as table02
from kicad_agents import display_render_fenghua_1206_x7r_table_queue as x7r
from kicad_agents import display_render_fenghua_1206_low_c0g_table_queue as low


def test_exact_part_and_height_are_reviewed():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert recipe['represented_mpn'] == '1206CG102J500NT'
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, 0.5]
    changed = copy.deepcopy(record)
    changed['electrical']['capacitance'] = '10 nF'
    with pytest.raises(ValueError, match='capacitance'):
        q.reviewed_recipe(changed, recipes, sha)


@pytest.mark.parametrize('part', list(table.PARTS))
def test_series_table_recipe_guards_identity(part):
    recipes = json.loads(table.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((table.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((table.ROOT / table.EVIDENCE).read_bytes()).hexdigest()
    recipe = table.reviewed_recipe(part, record, recipes, sha)
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, 0.5]
    assert 'series table' in recipe['appearance_status']
    record['part_number_manufacturer'] = 'unreviewed'
    with pytest.raises(ValueError, match='identity'):
        table.reviewed_recipe(part, record, recipes, sha)


@pytest.mark.parametrize('part', list(table02.PARTS))
def test_series_table_batch02_rejects_changed_part(part):
    recipes = json.loads(table02.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((table02.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((table02.ROOT / table02.EVIDENCE).read_bytes()).hexdigest()
    recipe = table02.reviewed_recipe(part, record, recipes, sha)
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, 0.5]
    record['electrical']['rated_voltage'] = '100 V'
    with pytest.raises(ValueError, match='rated_voltage'):
        table02.reviewed_recipe(part, record, recipes, sha)


@pytest.mark.parametrize('part', list(x7r.PARTS))
def test_x7r_table_requires_exact_dielectric_and_identity(part):
    recipes = json.loads(x7r.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((x7r.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((x7r.ROOT / x7r.EVIDENCE).read_bytes()).hexdigest()
    recipe = x7r.reviewed_recipe(part, record, recipes, sha)
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, 0.5]
    record['electrical']['dielectric'] = 'C0G'
    with pytest.raises(ValueError, match='dielectric'):
        x7r.reviewed_recipe(part, record, recipes, sha)


@pytest.mark.parametrize('part', list(low.PARTS))
def test_low_c0g_preserves_missing_tolerance_and_rejects_mismatch(part):
    recipes = json.loads(low.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((low.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((low.ROOT / low.EVIDENCE).read_bytes()).hexdigest()
    before = copy.deepcopy(record)
    recipe = low.reviewed_recipe(part, record, recipes, sha)
    assert record == before
    assert 'omits tolerance' in recipe['appearance_status']
    record['electrical']['tolerance'] = '5 pF'
    with pytest.raises(ValueError, match='tolerance'):
        low.reviewed_recipe(part, record, recipes, sha)
