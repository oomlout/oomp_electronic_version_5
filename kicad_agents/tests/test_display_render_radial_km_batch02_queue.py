import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_radial_km_batch02_queue as q


@pytest.mark.parametrize('part', list(q.PARTS))
def test_radial_batch_identity_and_voltage_guard(part):
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(part, record, recipes, sha)
    assert recipe['marking']['text'] == q.PARTS[part][-1]
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '99 V'
    with pytest.raises(ValueError, match='ratings'):
        q.reviewed_recipe(part, changed, recipes, sha)
