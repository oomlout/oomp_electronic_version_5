import copy
import pytest
from kicad_agents.display_render_taj_a_generic_4u7_queue import REFERENCE, reviewed_recipe


def sample():
    return {'name_proper': 'Capacitor 4.7 uF 16 V Tantalum 3216 AVX A', 'manufacturer': 'Xiangyee',
            'part_number_manufacturer': 'CA45-B016K476T', 'part_number_lcsc': 'C6387914',
            'dimensions_mm': {'length': 3.2, 'width': 1.6}, 'kicad': {'machine_solder': ''}}


def test_example_discloses_conflict_and_does_not_mutate_reference():
    recipes = {REFERENCE: {'family': 'tantalum_capacitor', 'package': 'tantalum_3216_avx_a',
               'represented_mpn': 'TAJA475K016RNJ', 'marking': {'capacitance_code': '475', 'rated_voltage_v': '16'}}}
    before = copy.deepcopy(recipes)
    r = reviewed_recipe(sample(), recipes, 'a'*64)
    assert '47 uF' in r['appearance_status'] and 'not' in r['appearance_status']
    assert 'example only' in r['represented_mpn']
    assert recipes == before


def test_supplier_change_requires_fresh_review():
    item = sample(); item['part_number_lcsc'] = 'different'
    with pytest.raises(ValueError, match='review again'):
        reviewed_recipe(item, {}, 'a'*64)
