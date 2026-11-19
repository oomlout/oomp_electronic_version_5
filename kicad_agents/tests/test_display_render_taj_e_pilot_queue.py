import copy
import hashlib
import json
import pytest
import yaml
from kicad_agents import display_render_taj_e_pilot_queue as q
from kicad_agents import display_render_taj_e_batch01_queue as batch
from kicad_agents.package_markings import marking_text


def test_e_pilot_checks_part_and_positive_polarity():
    recipes = json.loads(q.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((q.ROOT / 'parts_source' / q.PILOT / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((q.ROOT / q.EVIDENCE).read_bytes()).hexdigest()
    recipe = q.reviewed_recipe(record, recipes, sha)
    assert marking_text(recipe['marking']) == '227 C'
    assert recipe['model']['display_scale_xyz'] == [73/76, 43/46, 41/43]
    changed = copy.deepcopy(record)
    changed['electrical']['polarized'] = False
    with pytest.raises(ValueError, match='polarity'):
        q.reviewed_recipe(changed, recipes, sha)


@pytest.mark.parametrize('part', list(batch.PARTS))
def test_e_batch_requires_exact_identity_and_voltage(part):
    recipes = json.loads(batch.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((batch.ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((batch.ROOT / batch.EVIDENCE).read_bytes()).hexdigest()
    recipe = batch.reviewed_recipe(part, record, recipes, sha)
    assert marking_text(recipe['marking']) == batch.PARTS[part][-1]
    record['electrical']['rated_voltage'] = '99 V'
    with pytest.raises(ValueError, match='rating'):
        batch.reviewed_recipe(part, record, recipes, sha)
