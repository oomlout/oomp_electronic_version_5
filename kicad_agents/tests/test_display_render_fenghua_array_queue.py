from decimal import Decimal

import pytest

from kicad_agents.display_render_fenghua_array_queue import resistance, reviewed_recipe


@pytest.mark.parametrize(('code', 'ohms'), [('332', 3300), ('203', 20000), ('3R0', 3)])
def test_network_value_codes(code, ohms):
    assert resistance(code) == Decimal(ohms)


def test_network_requires_exact_value_manufacturer_and_four_resistor_footprint():
    part = 'electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin'
    record = {'manufacturer': 'FH (Guangdong Fenghua Advanced Tech)',
              'part_number_manufacturer': 'RC-MT08W332JT',
              'manufacturers': [{'manufacturer': 'FH (Guangdong Fenghua Advanced Tech)',
                                 'part_number': 'RC-MT08W332JT'}],
              'kicad': {'machine_solder': 'Resistor_SMD:R_Array_Convex_4x0402', 'symbol': 'Device:R_Pack04'}}
    pilot = {'family': 'chip_resistor', 'model': {}}
    recipe = reviewed_recipe(part, record, pilot, 'evidence-hash')
    assert recipe['marking']['text'] == '332'
    assert recipe['marking']['rotation_degrees'] == 90
    assert recipe['model']['license'].startswith('GPL-3.0-or-later')
    for change in ({**record, 'part_number_manufacturer': 'RC-MT08W333JT'},
                   {**record, 'manufacturers': []},
                   {**record, 'kicad': {'machine_solder': 'wrong', 'symbol': 'Device:R_Pack04'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, change, pilot, 'evidence-hash')


def test_larger_network_uses_its_local_manufacturer_evidence():
    part = 'electronic_resistor_array_4_x_0603_convex_1500_ohm_8_pin'
    mpn = 'RC-ML08W152JT'
    record = {'manufacturer': 'FH (Guangdong Fenghua Advanced Tech)', 'part_number_manufacturer': mpn,
              'manufacturers': [{'manufacturer': 'FH (Guangdong Fenghua Advanced Tech)', 'part_number': mpn}],
              'oomp_datasheet_common_with': 'electronic_resistor_array_4_x_0402_convex_0_ohm_8_pin',
              'kicad': {'machine_solder': 'Resistor_SMD:R_Array_Convex_4x0603', 'symbol': 'Device:R_Pack04'}}
    recipe = reviewed_recipe(part, record, {'family': 'chip_resistor', 'model': {}}, 'evidence-hash')
    assert recipe['marking']['text'] == '152'
    assert recipe['marking']['evidence']['file'].endswith('/datasheet.pdf')
    assert recipe['model']['expected_bounds_mm'] == [1.6, 3.2, .5]
