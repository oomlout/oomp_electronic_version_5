import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_yc124_queue import PART, reviewed_recipe


def test_exact_selected_array_and_guards():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    record = yaml.safe_load((Path('parts_source') / PART / 'working.yaml').read_text(encoding='utf8'))
    assert reviewed_recipe(PART, record, recipes, 'hash')['marking']['text'] == '103'
    for field, value in [('part_number_manufacturer', 'YC124-FR-0710KL'),
                         ('distributors', []), ('electrical', {'tolerance': '1%'}), ('kicad', {'machine_solder': 'wrong'}),
                         ('dimensions_mm', {'length': 10})]:
        changed = copy.deepcopy(record)
        changed[field] = value
        with pytest.raises(ValueError):
            reviewed_recipe(PART, changed, recipes, 'hash')
