import copy
import pytest
from kicad_agents.display_render_radial_km_large_queue import MODELS, PARTS, REFERENCE, reviewed_recipe


def test_each_large_part_has_own_dimensions_marking_and_guard():
    recipes = {REFERENCE: {'family': 'radial_aluminum_capacitor', 'model': {}, 'marking': {}}}
    before = copy.deepcopy(recipes)
    for part, (mpn, supplier, value, voltage, diameter, height, text) in PARTS.items():
        record = {'manufacturer': 'CX(Dongguan Chengxing Elec)', 'part_number_manufacturer': mpn,
                  'part_number_lcsc': supplier, 'electrical': {'capacitance': value, 'rated_voltage': voltage,
                  'pin_spacing': '7.5 mm', 'polarized': True}, 'dimensions_mm': {'length': diameter, 'width': diameter, 'height': height},
                  'kicad': {'machine_solder': f'Capacitor_THT:CP_Radial_D{diameter:.1f}mm_P7.50mm'}}
        result = reviewed_recipe(part, record, recipes, 'a'*64)
        assert result['marking']['text'] == text
        assert result['model']['sha256'] == MODELS[diameter][1]
        assert diameter + result['model']['radial_stretch']['extra_height'] == height
        record['electrical']['rated_voltage'] = '6.3 V'
        with pytest.raises(ValueError, match='Identity'):
            reviewed_recipe(part, record, recipes, 'a'*64)
    assert recipes == before
