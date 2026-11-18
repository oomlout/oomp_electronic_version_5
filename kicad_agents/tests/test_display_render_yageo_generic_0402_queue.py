import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_generic_0402_queue import PARTS, reviewed_recipe


def test_unsourced_generic_parts_and_change_guards():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part, reference in PARTS.items():
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, 'hash')
        assert recipe['represented_mpn'] == reference
        assert 'no selected manufacturer or tolerance' in recipe['appearance_status']
        for field, value in [('manufacturer', 'new supplier'), ('electrical', {'tolerance': '5%'}),
                             ('kicad', {'machine_solder': 'wrong'})]:
            changed = copy.deepcopy(record)
            changed[field] = value
            with pytest.raises(ValueError):
                reviewed_recipe(part, changed, recipes, 'hash')
