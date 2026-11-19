"""Prepare the source-checked Fenghua 1206 22 µF / 10 V display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_1206_22_micro_farad_10_volt'
SOURCE = 'electronic_capacitor_1206_10_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_22UF_10V_EVIDENCE.md')
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != '1206X226K100NT'
        or record.get('part_number_lcsc') != 'C1859' or e.get('capacitance') != '22 uF'
        or e.get('rated_voltage') != '10 V' or e.get('dielectric') != 'X5R'
        or '10%' not in str(e.get('tolerance')) or e.get('polarized') is not False
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric'
        or not any(x.get('manufacturer') == MAKER and x.get('part_number') == '1206X226K100NT' for x in record.get('manufacturers', []) if isinstance(x, dict))):
        raise ValueError('Identity, rating, dielectric or package changed')
    result = copy.deepcopy(recipes[SOURCE])
    if (result.get('family') != 'chip_capacitor' or result.get('package') != '1206_imperial_3216_metric'
        or result['model'].get('expected_bounds_mm') != [3.2, 1.6, 1.6]
        or result['model'].get('display_scale_xyz') or result['marking'].get('policy') != 'unmarked_illustration'):
        raise ValueError('Reviewed source illustration changed')
    result['represented_manufacturer'] = MAKER
    result['represented_mpn'] = '1206X226K100NT'
    result['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Fenghua X5R series table and exact supplier listing', 'source_record': f'parts_source/{PART}/working.yaml'}
    result['appearance_status'] = ('Generic KiCad 1206 geometry is 1.6 mm high, matching the manufacturer series table, not an individual drawing. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(record, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
