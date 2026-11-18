import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_generic_array_0402_queue import PARTS, reviewed_recipe


def test_array_reference_and_source_guards():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part, (reference, mark) in PARTS.items():
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, 'hash')
        assert recipe['represented_mpn'] == reference and recipe['marking']['text'] == mark
        assert 'no selected manufacturer or tolerance' in recipe['appearance_status']
        for field, value in [('manufacturer', 'new supplier'), ('electrical', {'tolerance': '1%'}),
                             ('kicad', {'machine_solder': 'wrong'}), ('dimensions_mm', {'length': 10})]:
            changed = copy.deepcopy(record)
            changed[field] = value
            with pytest.raises(ValueError):
                reviewed_recipe(part, changed, recipes, 'hash')
