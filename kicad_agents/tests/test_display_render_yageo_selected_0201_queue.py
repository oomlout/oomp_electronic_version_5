import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_yageo_selected_0201_queue import PARTS, reviewed_recipe


@pytest.mark.parametrize('part', PARTS)
def test_selected_reference_guards_identity_and_discloses_reference(part):
    manufacturer, selected, lcsc, value, reference, tolerance = PARTS[part]
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'hash')
    assert recipe['represented_mpn'] == reference
    assert selected in recipe['appearance_status'] and manufacturer in recipe['appearance_status']
    assert 'unverified' in recipe['appearance_status'] and 'interchangeability' in recipe['appearance_status']
    for mutate in ('identity', 'listing', 'value', 'tolerance', 'footprint'):
        changed = copy.deepcopy(record)
        if mutate == 'identity': changed['part_number_manufacturer'] = 'different'
        if mutate == 'listing': changed['distributors'][0]['part_number'] = 'different'
        if mutate == 'value': changed['distributors'][0]['product_name'] = changed['distributors'][0]['product_name'].replace(value, 'other value')
        if mutate == 'tolerance': changed['electrical'] = {'tolerance': '2%'}
        if mutate == 'footprint': changed['kicad']['machine_solder'] = 'other'
        with pytest.raises(ValueError): reviewed_recipe(part, changed, recipes, 'hash')
