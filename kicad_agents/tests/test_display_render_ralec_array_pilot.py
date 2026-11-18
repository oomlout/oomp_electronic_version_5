import json
from pathlib import Path

import pytest

from kicad_agents.display_render_ralec_array_pilot import reviewed_recipe


def test_ralec_exact_identity_and_geometry():
    pilot = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))[
        'electronic_resistor_array_4_x_0603_convex_10000_ohm_8_pin']
    record = {'manufacturer': 'RALEC', 'part_number_manufacturer': 'RTA03-4D303JTP',
              'manufacturers': [{'manufacturer': 'RALEC', 'part_number': 'RTA03-4D303JTP'}],
              'kicad': {'machine_solder': 'Resistor_SMD:R_Array_Convex_4x0603', 'symbol': 'Device:R_Pack04'}}
    recipe = reviewed_recipe(record, pilot, 'evidence-hash')
    assert recipe['marking']['text'] == '303'
    assert recipe['marking']['evidence']['page'] == 14
    with pytest.raises(ValueError):
        reviewed_recipe({**record, 'part_number_manufacturer': 'RTA03-4D304JTP'}, pilot, 'evidence-hash')
