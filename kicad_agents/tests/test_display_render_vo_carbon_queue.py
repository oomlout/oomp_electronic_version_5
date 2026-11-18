import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_vo_carbon_queue import reviewed_recipe


def test_four_band_identity_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    part = 'electronic_resistor_quarter_watt_through_hole_2700_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'hash')
    assert recipe['marking']['bands'] == ['red', 'violet', 'red', 'gold']
    assert 'not verified' in recipe['marking']['appearance_status']
    for field, value in [('part_number_manufacturer', 'CR1/4W-2K7±1%-ST26'),
                         ('electrical', {'tolerance': '1%'}),
                         ('kicad', {'machine_solder': 'wrong'})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_quarter_watt_through_hole_27000_ohm', record, recipes, 'hash')
