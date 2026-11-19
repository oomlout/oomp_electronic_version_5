import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_0805_y5v_unverified_queue as q


@pytest.mark.parametrize('part', list(q.PARTS))
def test_y5v_identity_and_unknown_height_are_explicit(part):
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(part, record, recipes, sha)
    assert 'actual thickness is unverified' in recipe['appearance_status']
    changed = copy.deepcopy(record)
    changed['electrical']['dielectric'] = 'X7R'
    with pytest.raises(ValueError, match='dielectric'):
        q.reviewed_recipe(part, changed, recipes, sha)
