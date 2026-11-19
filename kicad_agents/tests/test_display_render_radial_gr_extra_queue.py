import copy
import pytest
from kicad_agents.display_render_radial_gr_extra_queue import PARTS, REF_6, REF_8, reviewed_recipe


def test_each_series_colour_dimensions_and_guard():
    recipes = {p: {'family': 'radial_aluminum_capacitor', 'model': {'radial_stretch': {'extra_height': 4.}}, 'marking': {}}
               for p in [REF_6, REF_8]}
    before = copy.deepcopy(recipes)
    for part, (mpn, supplier, value, voltage, diameter, height, pitch, _, extension, palette, text) in PARTS.items():
        footprint = 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm' if diameter == 8 else 'Capacitor_THT:CP_Radial_D6.3mm_P2.50mm'
        r = {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': mpn,
             'part_number_lcsc': supplier, 'electrical': {'capacitance': value, 'rated_voltage': voltage,
             'pin_spacing': pitch, 'polarized': True}, 'dimensions_mm': {'length': diameter, 'width': diameter, 'height': height},
             'kicad': {'machine_solder': footprint}}
        out = reviewed_recipe(part, r, recipes, 'a'*64)
        assert out['radial_palette'] == palette and out['marking']['text'] == text
        assert out['model']['radial_stretch']['extra_height'] == extension
        r['electrical']['rated_voltage'] = '999 V'
        with pytest.raises(ValueError, match='Identity'):
            reviewed_recipe(part, r, recipes, 'a'*64)
    assert recipes == before
