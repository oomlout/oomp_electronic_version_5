import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_low_unlisted_queue as q


@pytest.mark.parametrize('part', list(q.PARTS))
def test_low_unlisted_discloses_limits_and_preserves_source(part):
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    original = copy.deepcopy(record)
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(part, record, recipes, sha)
    assert record == original
    assert 'actual thickness is unverified' in recipe['appearance_status']
    assert 'source record omits tolerance' in recipe['appearance_status']
    record['electrical']['rated_voltage'] = '10 V'
    with pytest.raises(ValueError, match='rated_voltage'):
        q.reviewed_recipe(part, record, recipes, sha)
