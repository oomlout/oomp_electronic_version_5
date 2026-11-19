"""Stage an explicitly disclosed AVX example for a conflicting generic item."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt'
REFERENCE = 'electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt_avx_taja475k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_A_GENERIC_4U7_EXAMPLE_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if (record.get('name_proper') != 'Capacitor 4.7 uF 16 V Tantalum 3216 AVX A'
        or record.get('manufacturer') != 'Xiangyee'
        or record.get('part_number_manufacturer') != 'CA45-B016K476T'
        or record.get('part_number_lcsc') != 'C6387914'
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or record.get('kicad', {}).get('machine_solder')
        or record.get('electrical')):
        raise ValueError('Generic identity or supplier conflict changed; review again')
    result = copy.deepcopy(recipes[REFERENCE])
    m = result.get('marking', {})
    if (result.get('family') != 'tantalum_capacitor' or result.get('package') != 'tantalum_3216_avx_a'
        or result.get('represented_mpn') != 'TAJA475K016RNJ'
        or m.get('capacitance_code') != '475' or m.get('rated_voltage_v') != '16'):
        raise ValueError('Reviewed AVX example changed')
    result['represented_manufacturer'] = 'KYOCERA AVX (illustrative example only)'
    result['represented_mpn'] = 'TAJA475K016RNJ (illustrative example only)'
    result['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'KYOCERA AVX TAJ specification and exact example listing',
        'source_record': f'parts_source/{PART}/working.yaml'}
    result['marking']['appearance_status'] = ('AVX example marking is illustrative; it does not depict the incompatible selected Xiangyee supplier part.')
    result['appearance_status'] = ('Illustrative AVX TAJA475K016RNJ 4.7 uF / 16 V A-case example. The currently linked Xiangyee CA45-B016K476T / C6387914 is listed as 47 uF, 16 V, 3528 B-case, conflicting with this item; do not treat it as interchangeable. The source procurement record is unresolved. Shape, marking, stripe and finish are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest())
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
