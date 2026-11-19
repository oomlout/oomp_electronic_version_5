import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_22uf_10v_queue as q


def test_exact_x5r_part_and_full_height_guard():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert recipe['represented_mpn'] == '1206X226K100NT'
    assert not recipe['model'].get('display_scale_xyz')
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError, match='rating'):
        q.reviewed_recipe(changed, recipes, sha)
