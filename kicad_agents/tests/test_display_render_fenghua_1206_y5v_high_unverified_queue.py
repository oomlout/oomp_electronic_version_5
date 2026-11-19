import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_y5v_high_unverified_queue as q


@pytest.mark.parametrize('part', list(q.PARTS))
def test_exact_high_value_identity_and_unverified_height(part):
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(part, record, recipes, sha)
    assert 'actual thickness is unverified' in recipe['appearance_status']
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '99 V'
    with pytest.raises(ValueError, match='rating'):
        q.reviewed_recipe(part, changed, recipes, sha)
