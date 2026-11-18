import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_ralec_small_queue import reviewed_recipe


def test_unmarked_size_value_identity_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part in ('electronic_resistor_0201_1800000_ohm', 'electronic_resistor_0402_8_2_ohm'):
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        assert reviewed_recipe(part, record, recipes, 'hash')['marking']['policy'] == 'none'
        for field, value in [('part_number_manufacturer', 'wrong'),
                             ('electrical', {'tolerance': '2%'}),
                             ('kicad', {'machine_solder': 'wrong'})]:
            changed = copy.deepcopy(record)
            changed[field] = value
            with pytest.raises(ValueError):
                reviewed_recipe(part, changed, recipes, 'hash')
