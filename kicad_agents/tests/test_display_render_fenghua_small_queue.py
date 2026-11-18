from decimal import Decimal

import pytest

from kicad_agents.display_render_fenghua_small_queue import resistance, reviewed_recipe


@pytest.mark.parametrize(('code', 'ohms'), [('1023', 102000), ('1202', 12000), ('12R0', 12),
                                             ('82R0', 82), ('2000', 200)])
def test_resistance_notation(code, ohms):
    assert resistance(code) == Decimal(ohms)


def test_recipe_rejects_mismatched_series_identity_and_footprint():
    part = 'electronic_resistor_0201_102000_ohm'
    record = {'manufacturer': 'FH', 'part_number_manufacturer': 'RC-01W1023FT',
              'manufacturers': [{'manufacturer': 'FH', 'part_number': 'RC-01W1023FT'}],
              'kicad': {'machine_solder': 'Resistor_SMD:R_0201_0603Metric'}}
    pilot = {'family': 'chip_resistor', 'marking': {'policy': 'uniroyal_0603_e96'}, 'model': {}}
    assert reviewed_recipe(part, record, pilot, 'hash')['marking']['policy'] == 'none'
    for changed in ({**record, 'part_number_manufacturer': 'RC-01W1202FT'},
                    {**record, 'part_number_manufacturer': 'RHC-01U106JT'},
                    {**record, 'manufacturers': []},
                    {**record, 'kicad': {'machine_solder': 'wrong'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, pilot, 'hash')
