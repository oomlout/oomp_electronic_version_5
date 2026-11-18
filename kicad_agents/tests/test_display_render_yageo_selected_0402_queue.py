import copy
import json
from pathlib import Path
import pytest
import yaml
from kicad_agents.display_render_yageo_selected_0402_queue import reviewed_recipe


def test_reference_and_selected_identity_are_disclosed_and_guarded():
    part = 'electronic_resistor_0402_2400_ohm'
    record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    recipe = reviewed_recipe(part, record, recipes, 'hash')
    assert recipe['represented_mpn'] == 'RC0402JR-072K4L'
    assert 'identity and appearance are unverified' in recipe['appearance_status']
    assert 'interchangeability' in recipe['appearance_status']
    for field in ('identity', 'listing', 'value', 'tolerance', 'footprint'):
        changed = copy.deepcopy(record)
        if field == 'identity': changed['part_number_manufacturer'] = 'other'
        if field == 'listing': changed['distributors'][0]['part_number'] = 'other'
        if field == 'value': changed['distributors'][0]['product_name'] = 'other ±5%'
        if field == 'tolerance': changed['electrical'] = {'tolerance': '2%'}
        if field == 'footprint': changed['kicad']['machine_solder'] = 'other'
        with pytest.raises(ValueError): reviewed_recipe(part, changed, recipes, 'hash')
