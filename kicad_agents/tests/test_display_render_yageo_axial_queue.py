from decimal import Decimal

import pytest
from PIL import Image

from kicad_agents.display_render import create_axial_band_texture
from kicad_agents.display_render_yageo_axial_queue import bands_for, resistance, reviewed_recipe


@pytest.mark.parametrize(('value', 'expected'), [
    ('1200', ['brown', 'red', 'black', 'brown', 'brown']),
    ('18', ['brown', 'grey', 'black', 'gold', 'brown']),
    ('4700000', ['yellow', 'violet', 'black', 'yellow', 'brown']),
])
def test_five_band_codes(value, expected):
    assert bands_for(Decimal(value)) == expected


def test_resistance_notation():
    assert resistance('1K2') == 1200
    assert resistance('18R') == 18
    with pytest.raises(ValueError):
        resistance('1K2L')


def test_axial_recipe_checks_identity_and_footprint():
    part = 'electronic_resistor_quarter_watt_through_hole_1200_ohm'
    mpn = 'MFR-25FTE52-1K2'
    record = {'manufacturer': 'YAGEO', 'part_number_manufacturer': mpn,
              'manufacturers': [{'manufacturer': 'YAGEO', 'part_number': mpn}],
              'kicad': {'machine_solder': 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'}}
    recipe = reviewed_recipe(part, record, {'family': 'chip_resistor', 'model': {}}, 'evidence-hash')
    assert recipe['marking']['bands'] == ['brown', 'red', 'black', 'brown', 'brown']
    assert recipe['model']['required_roles'] == ['coating', 'termination']
    for changed in ({**record, 'part_number_manufacturer': 'MFR-25FTE52-1K5'},
                    {**record, 'manufacturers': []}, {**record, 'kicad': {'machine_solder': 'wrong'}}):
        with pytest.raises(ValueError):
            reviewed_recipe(part, changed, {'family': 'chip_resistor', 'model': {}}, 'evidence-hash')


def test_texture_bands_span_the_whole_body_circumference(tmp_path):
    bands = ['brown', 'red', 'black', 'brown', 'brown']
    create_axial_band_texture({'bands': bands, 'body_span_mm': [.66, 6.96]},
                              [-.3, -1.25, -3], [7.92, 1.25, 2.5], tmp_path)
    image = Image.open(tmp_path / 'axial_bands.png').convert('RGB')
    assert all(image.getpixel((x, 0)) == image.getpixel((x, image.height-1)) for x in range(image.width))
    assert len(image.getcolors(maxcolors=2048 * 32)) >= 4
    assert image.getpixel((0, 0)) == (124, 166, 171)  # Original blue coating.
    with pytest.raises(ValueError):
        create_axial_band_texture({'bands': ['red'], 'body_span_mm': [.66, 6.96]},
                                  [-.3, -1.25, -3], [7.92, 1.25, 2.5], tmp_path)


def test_four_band_texture_has_gold_tolerance(tmp_path):
    bands = ['blue', 'grey', 'red', 'gold']
    create_axial_band_texture({'bands': bands, 'body_span_mm': [.66, 6.96]},
                              [-.3, -1.25, -3], [7.92, 1.25, 2.5], tmp_path)
    image = Image.open(tmp_path / 'axial_bands.png').convert('RGB')
    width = image.width
    def pixel_at(fraction):
        x = round((.66 + fraction * 6.3 + .3) * width / 8.22)
        return image.getpixel((x, 0))
    assert [pixel_at(f) for f in (.18, .33, .48, .78)] == [
        (40, 91, 166), (89, 97, 99), (195, 40, 39), (184, 149, 73)]
    assert pixel_at(.63) == (124, 166, 171)
