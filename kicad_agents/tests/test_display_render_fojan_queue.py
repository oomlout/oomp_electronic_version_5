import json
from pathlib import Path

import pytest

from kicad_agents.display_render_fojan_queue import reviewed_recipe


@pytest.fixture
def pilot():
    return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))[
        'electronic_resistor_0603_10000_ohm']


@pytest.fixture
def source():
    return {'manufacturer': 'FOJAN', 'part_number_manufacturer': 'FRC0603F1023TS',
            'manufacturers': [{'manufacturer': 'FOJAN', 'part_number': 'FRC0603F1023TS'}],
            'kicad': {'machine_solder': 'Resistor_SMD:R_0603_1608Metric'}}


def test_fojan_e96_uses_fojan_evidence_and_exact_code(source, pilot):
    recipe = reviewed_recipe('electronic_resistor_0603_102000_ohm', source, pilot, 'test-sha')
    assert recipe['represented_manufacturer'] == 'FOJAN'
    assert recipe['marking']['policy'] == 'verified_literal'
    assert recipe['marking']['text'] == '02D'
    assert recipe['marking']['evidence']['file'].endswith('DISPLAY_RENDER_FOJAN_EVIDENCE.md')


def test_fojan_small_package_is_unmarked(source, pilot):
    source['part_number_manufacturer'] = 'FRC0402F1001TS'
    source['manufacturers'][0]['part_number'] = 'FRC0402F1001TS'
    source['kicad']['machine_solder'] = 'Resistor_SMD:R_0402_1005Metric'
    recipe = reviewed_recipe('electronic_resistor_0402_1000_ohm', source, pilot, 'test-sha')
    assert recipe['marking']['policy'] == 'none'
    assert set(recipe['disable_bump_for']) == {'coating', 'ceramic', 'termination'}


def test_0201_outside_fojan_datasheet_range_is_rejected(source, pilot):
    source['part_number_manufacturer'] = 'FRC0201F2005TS'
    source['manufacturers'][0]['part_number'] = 'FRC0201F2005TS'
    source['kicad']['machine_solder'] = 'Resistor_SMD:R_0201_0603Metric'
    with pytest.raises(ValueError, match='outside'):
        reviewed_recipe('electronic_resistor_0201_20000000_ohm', source, pilot, 'test-sha')


def test_fojan_e24_underline_is_only_the_middle_character(source, pilot):
    source['part_number_manufacturer'] = 'FRC0603F1201TS'
    source['manufacturers'][0]['part_number'] = 'FRC0603F1201TS'
    recipe = reviewed_recipe('electronic_resistor_0603_1200_ohm', source, pilot, 'test-sha')
    assert recipe['marking']['text'] == '122'
    assert recipe['marking']['underline_character'] == 1
    assert not recipe['marking'].get('underline')


@pytest.mark.parametrize('change', ['value', 'manufacturer', 'footprint', 'listing', 'jumper'])
def test_unreviewed_or_mismatched_fojan_parts_are_rejected(source, pilot, change):
    part = 'electronic_resistor_0603_102000_ohm'
    if change == 'value':
        part = 'electronic_resistor_0603_1000_ohm'
    elif change == 'manufacturer':
        source['manufacturer'] = 'Other'
    elif change == 'footprint':
        source['kicad']['machine_solder'] = 'R_0402'
    elif change == 'listing':
        source['manufacturers'] = []
    else:
        part = 'electronic_resistor_0603_0_ohm'
        source['part_number_manufacturer'] = 'FRC0603F0000TS'
        source['manufacturers'][0]['part_number'] = 'FRC0603F0000TS'
    with pytest.raises(ValueError):
        reviewed_recipe(part, source, pilot, 'test-sha')
