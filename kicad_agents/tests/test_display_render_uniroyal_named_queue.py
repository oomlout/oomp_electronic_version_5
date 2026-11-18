import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_uniroyal_named_queue import reviewed_recipe


def test_reviewed_generic_and_variant_require_matching_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part, expected in (
        ('electronic_resistor_1206_6_8_ohm', '6R8'),
        ('electronic_resistor_1206_270_ohm_uni_royal_uniroyal_elec_1206w4f2700t5e', '2700'),
    ):
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes)
        assert recipe['marking']['text'] == expected
        assert recipe['marking']['evidence']['source_record'] == f'parts_source/{part}/working.yaml'
        conflict = copy.deepcopy(record)
        conflict['electrical'] = {'tolerance': '±10%'}
        with pytest.raises(ValueError):
            reviewed_recipe(part, conflict, recipes)
        conflict = copy.deepcopy(record)
        conflict['part_number_manufacturer'] = 'unknown'
        with pytest.raises(ValueError):
            reviewed_recipe(part, conflict, recipes)


def test_supplier_description_can_confirm_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    part = 'electronic_resistor_1206_510_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(part, record, recipes)['marking']['text'] == '511'
    record['distributors'][0]['product_name'] = '510Ω ±1%'
    with pytest.raises(ValueError):
        reviewed_recipe(part, record, recipes)
