import copy
import json
from pathlib import Path

import pytest
import yaml

from kicad_agents.display_render_cco_axial_queue import EVIDENCE, reviewed_recipe
from working_oomp_populate_lcsc_research_data import LCSC_RESEARCH


@pytest.mark.parametrize('evidence', [EVIDENCE, EVIDENCE.with_name('DISPLAY_RENDER_CCO_MF_IDENTITIES_02.json')])
def test_reviewed_supplier_identities_and_marking(evidence):
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
    entries = json.loads(evidence.read_text(encoding='utf8'))['records']
    identities = {entry['part_id']: entry for entry in entries}
    for entry in entries:
        part = entry['part_id']
        record = yaml.safe_load((Path('parts_source') / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, 'hash', identities, evidence)
        assert recipe['represented_mpn'] == entry['mpn']
        assert recipe['marking']['evidence']['file'] == evidence.as_posix()
        assert recipe['marking']['bands'][-1] == 'brown'
        assert LCSC_RESEARCH[part]['part_number_manufacturer'] == entry['mpn']
        changed = copy.deepcopy(record)
        changed['part_number_manufacturer'] = 'T'
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash', identities)
        changed = copy.deepcopy(record)
        changed['electrical'] = {'tolerance': '5%'}
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, recipes, 'hash', identities)
