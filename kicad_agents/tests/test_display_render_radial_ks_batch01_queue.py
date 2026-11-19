import copy
import pytest
from kicad_agents.display_render_radial_ks_batch01_queue import PARTS, PILOT, reviewed_recipe


def test_each_part_has_distinct_marking_and_identity_guard():
    pilot = {'family': 'radial_aluminum_capacitor', 'represented_mpn': 'KS336M016C07RR0VH2FP0',
             'model': {'flat_top': {'radius': 1.4}, 'radial_stretch': {'extra_height': 3.0}},
             'marking': {}}
    recipes = {PILOT: pilot}
    original = copy.deepcopy(recipes)
    for part, (mpn, supplier, value, marking) in PARTS.items():
        record = {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': mpn,
                  'part_number_lcsc': supplier, 'electrical': {'capacitance': value,
                  'rated_voltage': '50 V', 'pin_spacing': '1.5 mm', 'polarized': True},
                  'dimensions_mm': {'length': 4., 'width': 4., 'height': 7.},
                  'kicad': {'machine_solder': 'Capacitor_THT:CP_Radial_D4.0mm_P1.50mm'}}
        result = reviewed_recipe(part, record, recipes, 'a' * 64)
        assert result['marking']['text'] == marking
        assert result['represented_mpn'] == mpn
        assert 'illustrative' in result['appearance_status'].lower()
        record['electrical']['rated_voltage'] = '16 V'
        with pytest.raises(ValueError, match='Identity'):
            reviewed_recipe(part, record, recipes, 'a' * 64)
    assert recipes == original
