import copy
import importlib
import json
import pytest
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

MODULES = ['rvt_4mm_batch01', 'rvt_5mm_batch01', 'rvt_6_3mm_batch01',
           'rvt_6_3x5_4', 'rvt_8mm_batch01', 'rvt_10mm_batch01']

@pytest.mark.parametrize('module', MODULES)
def test_source_guards_reject_wrong_identity_and_footprint(module):
    queue = importlib.import_module('kicad_agents.display_render_' + module + '_queue')
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    part = next(iter(queue.PARTS))
    record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
    queue.reviewed_recipe(part, record, recipes, 'evidence')
    for field in ('part_number_manufacturer', 'part_number_lcsc', 'footprint', 'dimensions'):
        changed = copy.deepcopy(record)
        if field == 'footprint': changed['kicad']['machine_solder'] = 'wrong'
        elif field == 'dimensions': changed['dimensions_mm']['height'] = 999
        else: changed[field] = 'wrong'
        with pytest.raises(ValueError): queue.reviewed_recipe(part, changed, recipes, 'evidence')
