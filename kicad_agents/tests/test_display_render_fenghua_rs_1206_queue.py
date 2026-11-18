import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_fenghua_rs_1206_queue import reviewed_recipe


def test_strict_selected_supplier_and_marking():
    part = 'electronic_resistor_1206_110_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    assert reviewed_recipe(part, record, recipes, 'hash')['marking']['text'] == '111'
    for field, value in [('part_number_manufacturer', 'RS-06K112JT'),
                         ('electrical', {'tolerance': '1%'}),
                         ('kicad', {'machine_solder': 'wrong'}),
                         ('manufacturer', 'other')]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
