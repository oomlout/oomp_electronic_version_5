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


def test_missing_model_does_not_fabricate_geometry(tmp_path):
    with pytest.raises(FileNotFoundError):
        locate_model('Resistor_SMD.3dshapes/missing.step', tmp_path)


def test_model_path_cannot_escape_configured_root(tmp_path):
    with pytest.raises(ValueError, match='remain within'):
        locate_model('../outside.step', tmp_path)
