import json
from pathlib import Path

import pytest

from kicad_agents.display_render_uniroyal_array_queue import reviewed_recipe


@pytest.mark.parametrize(('value', 'mpn', 'mark'), [('10000', '4D03WGJ0103T5E', '103'),
                                                     ('0', '4D03WGJ0000T5E', '0')])
def test_array_codes_and_source_checks(value, mpn, mark):
    pilot = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))[
        'electronic_resistor_0603_10000_ohm']
    part = f'electronic_resistor_array_4_x_0603_convex_{value}_ohm_8_pin'
    record = {'manufacturer': 'UNI-ROYAL', 'part_number_manufacturer': mpn,
              'manufacturers': [{'manufacturer': 'UNI-ROYAL', 'part_number': mpn}],
              'oomp_datasheet_common_with': 'electronic_resistor_array_4_x_0402_convex_47000_ohm_8_pin',
              'kicad': {'machine_solder': 'Resistor_SMD:R_Array_Convex_4x0603', 'symbol': 'Device:R_Pack04'}}
    recipe = reviewed_recipe(part, record, pilot, 'evidence-hash')
    assert recipe['marking']['text'] == mark
    assert recipe['marking']['rotation_degrees'] == 90
    split = {**record, 'kicad': {**record['kicad'], 'symbol': 'Device:R_Pack04_Split'}}
    assert reviewed_recipe(part, split, pilot, 'evidence-hash')['marking']['text'] == mark
    for invalid in ({**record, 'manufacturers': []}, {**record, 'oomp_datasheet_common_with': None},
                    {**record, 'kicad': {'machine_solder': 'wrong'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, invalid, pilot, 'evidence-hash')
