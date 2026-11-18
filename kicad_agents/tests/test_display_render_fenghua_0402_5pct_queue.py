import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_fenghua_0402_5pct_queue import reviewed_recipe


def test_identity_value_footprint_and_tolerance():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part in ('electronic_resistor_0402_36_ohm', 'electronic_resistor_0402_82000_ohm_5_percent'):
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        assert reviewed_recipe(part, record, recipes, 'hash')['marking']['policy'] == 'none'
        for field, value in [('part_number_manufacturer', 'RS-02K360JT'),
                             ('electrical', {'tolerance': '1%'}),
                             ('kicad', {'machine_solder': 'wrong'})]:
            changed = copy.deepcopy(record)
            changed[field] = value
            with pytest.raises(ValueError):
                reviewed_recipe(part, changed, recipes, 'hash')
    for part in ('electronic_resistor_0402_24000_ohm', 'electronic_resistor_0402_91000_ohm'):
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        assert reviewed_recipe(part, record, recipes, 'hash')['marking']['policy'] == 'none'
        record['electrical']['tolerance'] = '+-1% (F)'
        with pytest.raises(ValueError, match='tolerance'):
            reviewed_recipe(part, record, recipes, 'hash')
