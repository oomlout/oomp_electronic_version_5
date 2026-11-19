import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_0805_33nf_table_queue as q
from kicad_agents import display_render_fenghua_0805_36pf_queue as q36


def test_exact_0805_part_and_height_guard():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert recipe['represented_mpn'] == '0805B333K500NT'
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .64]
    changed = copy.deepcopy(record)
    changed['dimensions_mm']['height'] = 1.25
    with pytest.raises(ValueError, match='dimensions'):
        q.reviewed_recipe(changed, recipes, sha)


def test_36pf_discloses_unverified_height_and_checks_identity():
    recipes = json.loads(q36.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q36.ROOT / 'parts_source' / q36.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q36.ROOT / q36.EVIDENCE).read_bytes()).hexdigest()
    recipe = q36.reviewed_recipe(record, recipes, sha)
    assert 'actual thickness is unverified' in recipe['appearance_status']
    record['part_number_manufacturer'] = 'other'
    with pytest.raises(ValueError, match='identity'):
        q36.reviewed_recipe(record, recipes, sha)
