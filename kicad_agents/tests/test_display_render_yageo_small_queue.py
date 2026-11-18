from decimal import Decimal

import pytest

from kicad_agents.display_render_yageo_small_queue import resistance, reviewed_recipe


@pytest.mark.parametrize(('code', 'ohms'), [('1ML', None), ('1M', 1000000), ('1K5', 1500),
                                             ('150K', 150000), ('68R', 68), ('2M2', 2200000)])
def test_resistance_notation(code, ohms):
    if ohms is None:
        with pytest.raises(ValueError):
            resistance(code)
    else:
        assert resistance(code) == Decimal(ohms)


def test_recipe_requires_matching_series_value_footprint_and_supplier():
    part = 'electronic_resistor_0201_1500_ohm'
    record = {'manufacturer': 'YAGEO', 'part_number_manufacturer': 'RC0201FR-071K5L',
              'manufacturers': [{'manufacturer': 'YAGEO', 'part_number': 'RC0201FR-071K5L'}],
              'kicad': {'machine_solder': 'Resistor_SMD:R_0201_0603Metric'}}
    pilot = {'family': 'chip_resistor', 'marking': {'policy': 'uniroyal_0603_e96'}, 'model': {}}
    recipe = reviewed_recipe(part, record, pilot, 'evidence-hash')
    assert recipe['marking']['policy'] == 'none'
    assert recipe['model']['expected_bounds_mm'] == [.6, .3, .23]
    for changed in ({**record, 'part_number_manufacturer': 'RC0201FR-072K2L'},
                    {**record, 'part_number_manufacturer': 'AF0201FR-071K5L'},
                    {**record, 'manufacturers': []},
                    {**record, 'kicad': {'machine_solder': 'wrong'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, pilot, 'evidence-hash')
