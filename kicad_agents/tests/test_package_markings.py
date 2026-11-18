from decimal import Decimal
import pytest

from kicad_agents.package_markings import E96, MULTIPLIERS, marking_text
from kicad_agents.display_render import locate_model


def recipe(value):
    return {'policy': 'uniroyal_0603_e96', 'resistance_ohm': value,
            'evidence': {'document': 'Reviewed manufacturer marking table'}}


@pytest.mark.parametrize('value,expected', [(10000,'01C'), (1960,'29B'), ('12.4','10X')])
def test_known_manufacturer_examples_and_pilot(value, expected):
    assert marking_text(recipe(value)) == expected


def test_all_e96_codes_round_trip_without_rounding():
    assert len(E96) == len(set(E96)) == 96
    for exponent, letter in MULTIPLIERS.items():
        for index, value in enumerate(E96, 1):
            ohms = Decimal(value) * Decimal(10) ** exponent
            assert marking_text(recipe(str(ohms))) == f'{index:02d}{letter}'


def test_unrepresentable_value_requires_a_different_reviewed_policy():
    with pytest.raises(ValueError, match='not exactly representable'):
        marking_text(recipe('12345'))


def test_unmarked_and_verified_literal_are_explicit():
    assert marking_text({'policy': 'none'}) == ''
    assert marking_text({'policy': 'verified_literal', 'text': 'ABC\n123', 'evidence': {'page': 2}}) == 'ABC\n123'
    with pytest.raises(ValueError, match='requires evidence'):
        marking_text({'policy': 'verified_literal', 'text': 'ABC'})


def test_illustrative_unmarked_appearance_requires_recorded_limitation():
    marking = {'policy': 'unmarked_illustration', 'evidence': {'file': 'review.md'},
               'appearance_status': 'No-marking policy not verified.'}
    assert marking_text(marking) == ''
    with pytest.raises(ValueError, match='explicit limitation'):
        marking_text({**marking, 'appearance_status': ''})
    with pytest.raises(ValueError, match='requires evidence'):
        marking_text({**marking, 'evidence': {}})


@pytest.mark.parametrize('voltage,letter', [('2.5', 'e'), ('4', 'G'), ('6.3', 'J'),
                                           ('10', 'A'), ('16', 'C'), ('20', 'D'),
                                           ('25', 'E'), ('35', 'V'), ('50', 'T')])
def test_avx_taj_voltage_codes(voltage, letter):
    marking = {'policy': 'avx_taj_illustrative', 'case': 'A', 'capacitance_code': '106',
               'rated_voltage_v': voltage, 'evidence': {'page': 1},
               'appearance_status': 'Logo and production code are illustrative or omitted.'}
    assert marking_text(marking) == f'106 {letter}'


def test_avx_taj_rejects_missing_evidence_or_unreviewed_values():
    marking = {'policy': 'avx_taj_illustrative', 'case': 'A', 'capacitance_code': '106',
               'rated_voltage_v': '10', 'evidence': {'page': 1},
               'appearance_status': 'Illustrative.'}
    for changes in ({'evidence': {}}, {'appearance_status': ''}, {'case': 'P'},
                    {'rated_voltage_v': '12'}, {'capacitance_code': '1.0'}):
        with pytest.raises(ValueError):
            marking_text({**marking, **changes})


def test_missing_model_does_not_fabricate_geometry(tmp_path):
    with pytest.raises(FileNotFoundError):
        locate_model('Resistor_SMD.3dshapes/missing.step', tmp_path)


def test_model_path_cannot_escape_configured_root(tmp_path):
    with pytest.raises(ValueError, match='remain within'):
        locate_model('../outside.step', tmp_path)
