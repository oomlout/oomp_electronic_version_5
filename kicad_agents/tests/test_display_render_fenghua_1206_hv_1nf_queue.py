import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_hv_1nf_queue as q


@pytest.mark.parametrize('part', list(q.PARTS))
def test_hv_exact_identity_and_voltage(part):
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(part, record, recipes, sha)
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .5]
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '10 V'
    with pytest.raises(ValueError, match='rating'):
        q.reviewed_recipe(part, changed, recipes, sha)
