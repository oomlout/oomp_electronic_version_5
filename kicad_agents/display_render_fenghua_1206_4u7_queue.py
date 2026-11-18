"""Prepare a Fenghua 1206 illustration using inspected generic geometry."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_1206_10uf_queue import PART as PILOT

PART = 'electronic_capacitor_1206_4_7_micro_farad'
MAKER = 'FH (Guangdong Fenghua Advanced Tech)'
MPN = '1206B475K500NT'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_4U7_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C29823' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6}:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '4.7 uF'), ('rated_voltage', '50 V'), ('dielectric', 'X7R'), ('tolerance', '10%')):
        if electrical and token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '1206_imperial_3216_metric' or 'display_scale_xyz' in r['model']:
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=MAKER, represented_mpn=MPN)
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Fenghua product page reviewed online',
                                'source_record': f'parts_source/{PART}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad nominal 1206 MLCC geometry matches the selected Fenghua part dimensions; '
                              'ceramic colour and metallic terminations are illustrative.')
    if not electrical:
        r['appearance_status'] += ' The source record lacks electrical fields; ratings were checked against the manufacturer page.'
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes:
        raise ValueError('Existing recipe preserved')
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, sha)
    if args.add:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
