import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_2kv_1nf_queue as q


def test_2kv_example_preserves_missing_electrical_data():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    before = copy.deepcopy(record)
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert record == before
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .78125]
    assert 'source record omits electrical fields' in recipe['appearance_status']
    record['electrical'] = {'rated_voltage': '1 kV'}
    with pytest.raises(ValueError, match='electrical state'):
        q.reviewed_recipe(record, recipes, sha)
