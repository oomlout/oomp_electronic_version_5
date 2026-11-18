import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_ralec_0603_queue import PART, reviewed_recipe


def test_59_ohm_eiaj_marking_and_identity():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    record = yaml.safe_load((Path('parts_source') / PART / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(PART, record, recipes, 'hash')['marking']['text'] == '75X'
    for field, value in [('part_number_manufacturer', 'RTT0359R0JTP'),
                         ('electrical', {'tolerance': '5%'}),
                         ('kicad', {'machine_solder': 'wrong'})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(PART, changed, recipes, 'hash')
