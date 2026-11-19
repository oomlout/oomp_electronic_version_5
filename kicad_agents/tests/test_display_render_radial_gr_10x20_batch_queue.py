import copy
import pytest
from kicad_agents.display_render_radial_gr_10x20_batch_queue import PARTS, REFERENCE, reviewed_recipe


def test_part_codes_select_reviewed_colours_and_reject_wrong_polarity():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'represented_mpn': 'KM228M016G20RR0VH2FP0',
               'model': {'radial_stretch': {'extra_height': 10.}}, 'marking': {}}}
    original = copy.deepcopy(recipes)
    for part, (mpn, supplier, value, voltage, text) in PARTS.items():
        record = {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': mpn,
                  'part_number_lcsc': supplier, 'electrical': {'capacitance': value, 'rated_voltage': voltage,
                  'pin_spacing': '5.0 mm', 'polarized': True}, 'dimensions_mm': {'length': 10., 'width': 10., 'height': 20.},
                  'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'}}
        result = reviewed_recipe(part, record, recipes, 'a'*64)
        assert result['marking']['text'] == text
        assert result['radial_palette'] == ('green_gold' if supplier == 'C3311' else 'black_gold')
        record['electrical']['polarized'] = False
        with pytest.raises(ValueError, match='Identity'):
            reviewed_recipe(part, record, recipes, 'a'*64)
    assert recipes == original
