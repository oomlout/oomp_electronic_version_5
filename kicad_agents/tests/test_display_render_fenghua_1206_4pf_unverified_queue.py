import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_4pf_unverified_queue as q


def test_4pf_identity_and_missing_tolerance_are_guarded():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    original = copy.deepcopy(record)
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert record == original
    assert 'actual thickness is unverified' in recipe['appearance_status']
    assert 'source record omits tolerance' in recipe['appearance_status']
    record['electrical']['tolerance'] = '5%'
    with pytest.raises(ValueError, match='tolerance'):
        q.reviewed_recipe(record, recipes, sha)
