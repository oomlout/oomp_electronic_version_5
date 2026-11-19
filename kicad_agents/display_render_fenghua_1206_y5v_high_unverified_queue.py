"""Prepare exact high-value 1206 Y5V examples with unverified heights."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

SOURCE = 'electronic_capacitor_1206_10_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_Y5V_HIGH_UNVERIFIED_EVIDENCE.md')
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'
PARTS = {
    'electronic_capacitor_1206_1_micro_farad_fenghua_adv_tech_1206f105m500nt': ('1206F105M500NT', 'C1926', '1 uF', '50 V'),
    'electronic_capacitor_1206_4_7_micro_farad_fenghua_adv_tech_1206f475m250nt': ('1206F475M250NT', 'C1939', '4.7 uF', '25 V'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, supplier, value, voltage = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn
        or record.get('part_number_lcsc') != supplier or e.get('capacitance') != value
        or e.get('rated_voltage') != voltage or e.get('dielectric') != 'Y5V'
        or '20%' not in str(e.get('tolerance')) or e.get('polarized') is not False
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric'
        or not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict))):
        raise ValueError('Identity, rating, dielectric or package changed')
    result = copy.deepcopy(recipes[SOURCE])
    if (result.get('family') != 'chip_capacitor' or result.get('package') != '1206_imperial_3216_metric'
        or result['model'].get('expected_bounds_mm') != [3.2, 1.6, 1.6]
        or result['model'].get('display_scale_xyz') or result['marking'].get('policy') != 'unmarked_illustration'):
        raise ValueError('Reviewed source illustration changed')
    result['represented_manufacturer'] = MAKER
    result['represented_mpn'] = mpn
    result['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Exact LCSC identity; thickness unverified', 'source_record': f'parts_source/{part}/working.yaml'}
    result['appearance_status'] = ('Generic KiCad 1206 geometry is shown at 1.6 mm height as an illustration; the available manufacturer table does not cover these Y5V parts, so actual thickness is unverified. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
