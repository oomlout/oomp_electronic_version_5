import copy
import json
from pathlib import Path

import pytest

from kicad_agents.display_render_resistor_queue import reviewed_recipe


@pytest.fixture
def pilot():
    recipes = json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    return recipes['electronic_resistor_0603_10000_ohm']


@pytest.fixture
def source():
    return {'manufacturer': 'UNI-ROYAL', 'part_number_manufacturer': '0603WAF1001T5E',
            'manufacturers': [{'manufacturer': 'UNI-ROYAL', 'part_number': '0603WAF1001T5E'}],
            'kicad': {'machine_solder': 'Resistor_SMD:R_0603_1608Metric'},
            'oomp_datasheet_common_with': 'electronic_resistor_0402_0_ohm'}


def test_reviewed_existing_part_produces_its_documented_1k_marking(source, pilot):
    original = copy.deepcopy(pilot)
    recipe, text = reviewed_recipe('electronic_resistor_0603_1000_ohm', source, pilot)
    assert text == '01B'
    assert recipe['represented_mpn'] == '0603WAF1001T5E'
    assert recipe['marking']['resistance_ohm'] == 1000
    assert pilot == original


def test_e24_outside_e96_is_explicitly_underlined(source, pilot):
    source['part_number_manufacturer'] = '0603WAF1201T5E'
    source['manufacturers'][0]['part_number'] = '0603WAF1201T5E'
    recipe, text = reviewed_recipe('electronic_resistor_0603_1200_ohm', source, pilot)
    assert text == '122'
    assert recipe['marking']['policy'] == 'verified_literal'
    assert recipe['marking']['underline'] is True
    assert recipe['marking']['evidence']['page'] == 4


def test_decimal_exponent_in_manufacturer_part_number(source, pilot):
    source['part_number_manufacturer'] = '0603WAF100JT5E'
    source['manufacturers'][0]['part_number'] = '0603WAF100JT5E'
    recipe, text = reviewed_recipe('electronic_resistor_0603_10_ohm', source, pilot)
    assert text == '01X'
    assert recipe['marking']['resistance_ohm'] == 10


def test_reviewed_shared_document_reference_does_not_require_duplicate_pointer(source, pilot):
    source.pop('oomp_datasheet_common_with')
    source['jlcpcb_selection'] = {'datasheet_pages': {'document':
        'UNI-ROYAL Thick Film Chip Resistors data sheet, Feb.12 2019 V.3 (shared family copy)'}}
    recipe, text = reviewed_recipe('electronic_resistor_0603_1000_ohm', source, pilot)
    assert text == '01B'


@pytest.mark.parametrize('alteration', ['wrong_value', 'wrong_supplier', 'wrong_footprint', 'missing_evidence', 'unlisted_mpn', 'non_e96'])
def test_queue_rejects_unverified_or_unsupported_records(source, pilot, alteration):
    part = 'electronic_resistor_0603_1000_ohm'
    if alteration == 'wrong_value':
        part = 'electronic_resistor_0603_10000_ohm'
    elif alteration == 'wrong_supplier':
        source['manufacturer'] = 'Other'
    elif alteration == 'wrong_footprint':
        source['kicad']['machine_solder'] = 'R_0402'
    elif alteration == 'missing_evidence':
        source.pop('oomp_datasheet_common_with')
    elif alteration == 'unlisted_mpn':
        source['manufacturers'] = []
    else:
        part = 'electronic_resistor_0603_1230_ohm'
        source['part_number_manufacturer'] = '0603WAF1231T5E'
        source['manufacturers'][0]['part_number'] = '0603WAF1231T5E'
    with pytest.raises(ValueError):
        reviewed_recipe(part, source, pilot)
