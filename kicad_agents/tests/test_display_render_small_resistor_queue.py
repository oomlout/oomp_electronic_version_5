import json
from pathlib import Path

import pytest

from kicad_agents.display_render_small_resistor_queue import reviewed_recipe


@pytest.fixture
def pilot():
    return json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf-8'))[
        'electronic_resistor_0603_10000_ohm']


@pytest.fixture
def source():
    return {'manufacturer': 'UNI-ROYAL', 'part_number_manufacturer': '0402WGF1001TCE',
            'manufacturers': [{'manufacturer': 'UNI-ROYAL', 'part_number': '0402WGF1001TCE'}],
            'kicad': {'machine_solder': 'Resistor_SMD:R_0402_1005Metric'}}


def test_unmarked_0402_uses_its_own_verified_model(source, pilot):
    recipe = reviewed_recipe('electronic_resistor_0402_1000_ohm', source, pilot)
    assert recipe['represented_mpn'] == '0402WGF1001TCE'
    assert recipe['marking']['policy'] == 'none'
    assert recipe['marking']['evidence']['page'] == 3
    assert set(recipe['disable_bump_for']) == {'coating', 'ceramic', 'termination'}
    assert recipe['model']['expected_bounds_mm'] == [1., .5, .35]
    assert recipe['model']['relative_path'].endswith('R_0402_1005Metric.step')


@pytest.mark.parametrize('change', ['resistance', 'manufacturer', 'footprint', 'listed_part'])
def test_unverified_candidate_is_rejected(source, pilot, change):
    part = 'electronic_resistor_0402_1000_ohm'
    if change == 'resistance':
        part = 'electronic_resistor_0402_10000_ohm'
    elif change == 'manufacturer':
        source['manufacturer'] = 'Other'
    elif change == 'footprint':
        source['kicad']['machine_solder'] = 'R_0603'
    else:
        source['manufacturers'] = []
    with pytest.raises(ValueError):
        reviewed_recipe(part, source, pilot)


def test_0201_five_percent_uses_unmarked_e24_and_checks_tolerance(pilot):
    mpn='0201WMJ0182TEE'
    record={'manufacturer':'UNI-ROYAL','part_number_manufacturer':mpn,
            'manufacturers':[{'manufacturer':'UNI-ROYAL','part_number':mpn}],
            'kicad':{'machine_solder':'Resistor_SMD:R_0201_0603Metric'}}
    result=reviewed_recipe('electronic_resistor_0201_1800_ohm',record,pilot)
    assert result['marking']['policy']=='none'
    with pytest.raises(ValueError,match='tolerance'):
        reviewed_recipe('electronic_resistor_0201_1800_ohm',{**record,'electrical':{'tolerance':'±1%'}},pilot)
    with pytest.raises(ValueError):
        reviewed_recipe('electronic_resistor_0201_1900_ohm',record,pilot)


def test_manufacturer_variant_suffix_must_match_exact_mpn(source,pilot):
    part='electronic_resistor_0402_1000_ohm_uni_royal_uniroyal_elec_0402wgf1001tce'
    assert reviewed_recipe(part,source,pilot)['marking']['policy']=='none'
    with pytest.raises(ValueError,match='suffix'):
        reviewed_recipe(part.replace('0402wgf1001tce','other'),source,pilot)
