import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_ac0402_queue import reviewed_recipe, PART


def test_exact_identity_and_conflicting_rating():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    record = yaml.safe_load((Path('parts_source') / PART / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(PART, record, recipes, 'hash')['marking']['policy'] == 'none'
    for key, value in [('part_number_manufacturer', 'AC0402FR-076M8L'),
                       ('kicad', {'machine_solder': 'wrong'}),
                       ('electrical', {'tolerance': '1%'}),
                       ('electrical', {'tolerance': '1.5%'})]:
        changed = copy.deepcopy(record)
        changed[key] = value
        with pytest.raises(ValueError):
            reviewed_recipe(PART, changed, recipes, 'hash')
