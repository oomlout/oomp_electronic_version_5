import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_fenghua_array_jumper_queue import PART, reviewed_recipe


def test_jumper_marking_and_identity_guards():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    record = yaml.safe_load((Path('parts_source') / PART / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(PART, record, recipes, 'hash')['marking']['text'] == '0'
    for field, value in [('part_number_manufacturer', 'RC-MT08W100JT'),
                         ('electrical', {'elements': 4, 'terminals': 8, 'resistance': '1Ω'}),
                         ('kicad', {'machine_solder': 'wrong'})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(PART, changed, recipes, 'hash')
