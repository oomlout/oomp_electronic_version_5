import pytest
from kicad_agents.display_render_radial import radial_palette


def test_default_appearance_is_preserved_and_copy_is_independent():
    first = radial_palette('black_white')
    assert first['body'] == [.016, .018, .022]
    assert first['ink'] == [.78, .79, .76]
    first['body'][0] = 1
    assert radial_palette('black_white')['body'][0] == .016


def test_green_gold_palette_and_reject_unknown():
    p = radial_palette('green_gold')
    assert p['body'][1] > p['body'][0] and p['body'][1] > p['body'][2]
    assert p['ink'][0] > p['ink'][1] > p['ink'][2]
    assert radial_palette('black_gold')['ink'] == p['ink']
    assert radial_palette('black_gold')['body'] == radial_palette('black_white')['body']
    with pytest.raises(ValueError, match='Unreviewed'):
        radial_palette('unreviewed')
