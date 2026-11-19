import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_taj_r_pilot_queue as q
from kicad_agents.package_markings import marking_text


def test_r_case_marking_and_identity_guard():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert marking_text(recipe['marking']) == 'J\n106'
    assert recipe['model']['display_scale_xyz'] == [2.05/2.0, 1.3/1.2, 1.0]
    changed = copy.deepcopy(record)
    changed['electrical']['polarized'] = False
    with pytest.raises(ValueError, match='polarity'):
        q.reviewed_recipe(changed, recipes, sha)
