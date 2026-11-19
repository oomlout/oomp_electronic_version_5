import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_fenghua_1206_12pf_height_queue as q


def test_discrepant_height_is_disclosed_and_part_is_checked():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .5]
    assert 'secondary listing reports 1.6 mm' in recipe['appearance_status']
    changed = copy.deepcopy(record)
    changed['electrical']['capacitance'] = '22 pF'
    with pytest.raises(ValueError, match='capacitance'):
        q.reviewed_recipe(changed, recipes, sha)
