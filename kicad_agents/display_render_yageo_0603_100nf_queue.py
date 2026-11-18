"""Prepare an explicitly illustrative YAGEO 0603 100 nF display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0603_100_nano_farad'
PILOT = 'electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc'
MPN = 'CC0603KRX7R9BB104'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0603_100NF_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C14663' and all(t in str(x.get('product_name', '')) for t in ('100nF', '10%', '50V', 'X7R', '0603')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier value, rating or package changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 1.6, 'width': .8, 'height': .8}:
        raise ValueError('Dimensions changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric':
        raise ValueError('Unexpected model')
    r.update(represented_manufacturer='YAGEO', represented_mpn=MPN)
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'YAGEO selected part specification and source record',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = 'Generic KiCad nominal 0603 MLCC geometry with illustrative ceramic colour and metallic terminations; represents the selected YAGEO part.'
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes:
        raise ValueError('Existing recipe preserved')
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
    if args.add:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
