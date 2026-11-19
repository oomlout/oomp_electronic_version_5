import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_generic_0603_2200pf_queue as q


def test_generic_example_preserves_unselected_procurement():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    original = copy.deepcopy(record)
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert record == original
    assert recipe['represented_mpn'] == '0603B222K500NT'
    assert 'without a selected supplier or voltage' in recipe['appearance_status']
    record['manufacturers'] = [{'part_number': 'chosen'}]
    with pytest.raises(ValueError, match='procurement'):
        q.reviewed_recipe(record, recipes, sha)
