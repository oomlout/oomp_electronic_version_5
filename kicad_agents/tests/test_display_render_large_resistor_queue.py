import json
from pathlib import Path

import pytest

from kicad_agents.display_render_large_resistor_queue import reviewed_recipe


@pytest.fixture
def pilot():
    return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))[
        'electronic_resistor_0603_10000_ohm']


@pytest.fixture
def source():
    return {'manufacturer': 'UNI-ROYAL', 'part_number_manufacturer': '0805W8F1001T5E',
            'manufacturers': [{'manufacturer': 'UNI-ROYAL', 'part_number': '0805W8F1001T5E'}],
            'kicad': {'machine_solder': 'Resistor_SMD:R_0805_2012Metric'}}


def test_0805_one_percent_has_documented_four_digit_code(source, pilot):
    recipe = reviewed_recipe('electronic_resistor_0805_1000_ohm', source, pilot)
    assert recipe['marking']['text'] == '1001'
    assert recipe['marking']['evidence']['page'] == 3
    assert recipe['model']['expected_bounds_mm'] == [2., 1.2, .45]


def test_zero_ohm_is_marked_zero_not_four_zeroes(source, pilot):
    source['part_number_manufacturer'] = '0805W8F0000T5E'
    source['manufacturers'][0]['part_number'] = '0805W8F0000T5E'
    recipe = reviewed_recipe('electronic_resistor_0805_0_ohm', source, pilot)
    assert recipe['marking']['text'] == '0'


def test_0805_10_megohm_range_boundary_requires_further_review(source, pilot):
    source['part_number_manufacturer'] = '0805W8F1005T5E'
    source['manufacturers'][0]['part_number'] = '0805W8F1005T5E'
    with pytest.raises(ValueError, match='outside'):
        reviewed_recipe('electronic_resistor_0805_10000000_ohm', source, pilot)


@pytest.mark.parametrize('change', ['resistance', 'manufacturer', 'footprint', 'listed_part', 'decimal_code'])
def test_unverified_candidate_is_rejected(source, pilot, change):
    part = 'electronic_resistor_0805_1000_ohm'
    if change == 'resistance':
        part = 'electronic_resistor_0805_10000_ohm'
    elif change == 'manufacturer':
        source['manufacturer'] = 'Other'
    elif change == 'footprint':
        source['kicad']['machine_solder'] = 'R_0603'
    elif change == 'listed_part':
        source['manufacturers'] = []
    else:
        source['part_number_manufacturer'] = '0805W8F100JT5E'
    with pytest.raises(ValueError):
        reviewed_recipe(part, source, pilot)
