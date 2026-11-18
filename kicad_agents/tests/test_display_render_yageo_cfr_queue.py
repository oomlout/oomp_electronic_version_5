import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_cfr_queue import reviewed_recipe


def test_four_band_identity_value_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    part = 'electronic_resistor_quarter_watt_through_hole_1800000_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(part, record, recipes, 'hash')['marking']['bands'] == ['brown', 'grey', 'green', 'gold']
    for field, value in [('part_number_manufacturer', 'CFR-25FT-52-1M8'),
                         ('electrical', {'tolerance': '1%'}),
                         ('kicad', {'machine_solder': 'wrong'})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_quarter_watt_through_hole_180000_ohm', record, recipes, 'hash')
