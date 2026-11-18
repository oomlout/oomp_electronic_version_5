"""Prepare a dimension-checked Samsung 0805 MLCC display illustration."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0805_12_nano_farad'
PILOT = 'electronic_capacitor_0805_10_micro_farad_16_volt'
MPN = '0805B123K500NT'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_12NF_SECONDARY_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    maker = 'FH (Guangdong Fenghua Advanced Tech)'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C1715' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 2.0 or dims.get('width') != 1.25 or dims.get('height', 1.25) != 1.25:
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '12 nF'), ('rated_voltage', '50 V'), ('dielectric', 'X7R'), ('tolerance', '10%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric' or r['model'].get('expected_bounds_mm') != [2.0,1.25,1.25]:
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=maker, represented_mpn=MPN)
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Secondary supplier product data reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad nominal 0805 MLCC geometry matches the dimensions reported by secondary suppliers; '
                              'ceramic colour and metallic terminations are illustrative. The original manufacturer drawing was not independently accessed.')
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
