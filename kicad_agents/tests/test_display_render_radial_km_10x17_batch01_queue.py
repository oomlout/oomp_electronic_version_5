import copy
import pytest
from kicad_agents.display_render_radial_km_10x17_batch01_queue import PARTS, PILOT, reviewed_recipe


def test_reviewed_parts_keep_identity_and_reject_wrong_voltage():
    recipes = {PILOT: {'family': 'radial_aluminum_capacitor', 'represented_mpn': 'KM477M035G17RR0VH2FP0',
                       'model': {'radial_stretch': {'extra_height': 7.0}}, 'marking': {}}}
    original = copy.deepcopy(recipes)
    for part, (mpn, supplier, value, voltage, text) in PARTS.items():
        record = {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': mpn,
                  'part_number_lcsc': supplier, 'electrical': {'capacitance': value, 'rated_voltage': voltage,
                  'pin_spacing': '5.0 mm', 'polarized': True}, 'dimensions_mm': {'length': 10., 'width': 10., 'height': 17.},
                  'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'}}
        result = reviewed_recipe(part, record, recipes, 'a' * 64)
        assert result['represented_mpn'] == mpn
        assert result['marking']['text'] == text
        record['electrical']['rated_voltage'] = '6.3 V'
        with pytest.raises(ValueError, match='Identity'):
            reviewed_recipe(part, record, recipes, 'a' * 64)
    assert recipes == original
