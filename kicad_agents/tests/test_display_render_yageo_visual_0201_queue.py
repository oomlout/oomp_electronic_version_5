import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_visual_0201_queue import PARTS, reviewed_recipe


def test_references_are_explicit_and_selected_identity_is_guarded():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    for part, (selected, reference, _) in PARTS.items():
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, 'hash')
        assert recipe['represented_mpn'] == reference
        assert selected in recipe['appearance_status'] and 'unverified' in recipe['appearance_status']
        changed = copy.deepcopy(record)
        changed['part_number_manufacturer'] = 'different'
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
        changed = copy.deepcopy(record)
        changed['distributors'] = []
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
        changed = copy.deepcopy(record)
        changed['electrical'] = {'tolerance': '2%'}
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash')
