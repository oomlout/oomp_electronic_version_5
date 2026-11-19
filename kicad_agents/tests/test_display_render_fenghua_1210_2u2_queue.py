import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1210_2u2_queue as q


def test_1210_part_and_geometry_guards():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert recipe['model']['expected_bounds_mm'] == [3.2, 2.5, 2.5]
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .64]
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError, match='ratings'):
        q.reviewed_recipe(changed, recipes, sha)
