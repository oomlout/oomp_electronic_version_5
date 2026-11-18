import json
from pathlib import Path

import pytest

from kicad_agents.display_render_uniroyal_five_percent_queue import reviewed_recipe


@pytest.fixture
def recipes():
    return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))


@pytest.mark.parametrize(('size', 'value', 'mpn', 'footprint', 'mark'), [
    ('0603', '220', '0603WAJ0221T5E', 'R_0603_1608Metric', '221'),
    ('0805', '180', '0805W8J0181T5E', 'R_0805_2012Metric', '181'),
    ('1206', '1', '1206W4J010JT5E', 'R_1206_3216Metric', '1R0'),
])
def test_reviewed_5_percent_marking_and_identity(size, value, mpn, footprint, mark, recipes):
    part = f'electronic_resistor_{size}_{value}_ohm_5_percent'
    record = {'manufacturer': 'UNI-ROYAL(Uniroyal Elec)', 'part_number_manufacturer': mpn,
              'manufacturers': [{'manufacturer': 'UNI-ROYAL', 'part_number': mpn}],
              'kicad': {'machine_solder': 'Resistor_SMD:' + footprint},
              'oomp_datasheet_common_with': 'electronic_resistor_0402_0_ohm'}
    recipe = reviewed_recipe(part, record, recipes)
    assert recipe['marking']['text'] == mark
    assert not recipe['marking'].get('underline')
    for invalid in ({**record, 'part_number_manufacturer': mpn.replace('J', 'F', 1)},
                    {**record, 'manufacturers': []}, {**record, 'oomp_datasheet_common_with': None}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, invalid, recipes)
