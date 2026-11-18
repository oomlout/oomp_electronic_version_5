import copy
import json
import hashlib
import pytest
import yaml

from kicad_agents import display_render_radial_km_220uf_queue as queue
from kicad_agents import display_render_radial_km_4_7uf_queue as high_voltage_queue


def test_reviewed_recipe_uses_exact_part_and_rejects_changed_voltage():
    recipes = json.loads(queue.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((queue.ROOT / 'parts_source' / queue.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((queue.ROOT / queue.EVIDENCE).read_bytes()).hexdigest()
    recipe = queue.reviewed_recipe(record, recipes, sha)
    assert recipe['marking']['text'] == '220uF\n35V\nKM 105C'
    assert recipe['represented_mpn'] == 'KM227M035F12RR0VH2FP0'
    assert recipe['marking']['evidence']['sha256'] == sha
    changed = copy.deepcopy(record)
    changed['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError, match='identity'):
        queue.reviewed_recipe(changed, recipes, sha)


def test_high_voltage_recipe_requires_exact_polarized_part():
    recipes = json.loads(high_voltage_queue.RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((high_voltage_queue.ROOT / 'parts_source' / high_voltage_queue.PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((high_voltage_queue.ROOT / high_voltage_queue.EVIDENCE).read_bytes()).hexdigest()
    recipe = high_voltage_queue.reviewed_recipe(record, recipes, sha)
    assert recipe['marking']['text'] == '4.7uF\n250V\nKM 105C'
    assert recipe['represented_mpn'] == 'KM475M250F12RR0VH2FP0'
    record['electrical']['polarized'] = False
    with pytest.raises(ValueError, match='identity'):
        high_voltage_queue.reviewed_recipe(record, recipes, sha)
