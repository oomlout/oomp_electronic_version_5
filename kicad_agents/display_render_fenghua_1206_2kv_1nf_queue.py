"""Prepare the exact Fenghua 2 kV display without adding electrical fields."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_1206_1_nano_farad_2000_volt'
SOURCE = 'electronic_capacitor_1206_470_nano_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_2KV_1NF_EVIDENCE.md')
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'


def reviewed_recipe(record, recipes, sha):
    if (record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != '1206B102K202NT'
        or record.get('part_number_lcsc') != 'C9196' or record.get('electrical')
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric'
        or not any(x.get('manufacturer') == MAKER and x.get('part_number') == '1206B102K202NT' for x in record.get('manufacturers', []) if isinstance(x, dict))):
        raise ValueError('Identity, electrical state or package changed')
    result = copy.deepcopy(recipes[SOURCE])
    if (result.get('family') != 'chip_capacitor' or result.get('package') != '1206_imperial_3216_metric'
        or result['model'].get('display_scale_xyz') != [1.0, 1.0, .78125]
        or result['marking'].get('policy') != 'unmarked_illustration'):
        raise ValueError('Reviewed source illustration changed')
    result['represented_manufacturer'] = MAKER
    result['represented_mpn'] = '1206B102K202NT'
    result['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Fenghua exact high-voltage product entry', 'source_record': f'parts_source/{PART}/working.yaml'}
    result['appearance_status'] = ('Generic KiCad 1206 geometry is scaled to the manufacturer-listed 1.25 mm nominal height. The manufacturer lists 1 nF / 2 kV X7R; this source record omits electrical fields. Ceramic colour, terminations and unmarked appearance are illustrative.')
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
