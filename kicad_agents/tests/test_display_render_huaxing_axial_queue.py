import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_huaxing_axial_queue import reviewed_recipe


def test_five_band_identity_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    part = 'electronic_resistor_quarter_watt_through_hole_2200_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'hash')
    assert recipe['marking']['bands'] == ['red', 'red', 'black', 'brown', 'brown']
    assert 'specification states blue' in recipe['appearance_status']
    for field, value in [('part_number_manufacturer', 'MF1/4W-2.2KΩ±5%T52'),
                         ('electrical', {'tolerance': '5%'}),
                         ('kicad', {'machine_solder': 'wrong'})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_quarter_watt_through_hole_3300_ohm', record, recipes, 'hash')
