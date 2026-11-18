"""Prepare a manufacturer-matched generic Fenghua 0402 illustration."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_120pf_queue import PART as PILOT, MAKER

PART = 'electronic_capacitor_0402_100_pico_farad'
MPN = '0402CG101J500NT'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0402_100PF_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C1546' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0402_1005Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 1.0, 'width': .5, 'height': .5}:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '100 pF'), ('rated_voltage', '50 V'), ('dielectric', 'C0G'), ('tolerance', '5%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric':
        raise ValueError('Unexpected source recipe')
    r.update(package='0402_imperial_1005_metric', represented_mpn=MPN)
    r['model'].update(relative_path='Capacitor_SMD.3dshapes/C_0402_1005Metric.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Capacitor_SMD.3dshapes/C_0402_1005Metric.step',
        expected_bounds_mm=[1.0, .5, .5], sha256='03e44c4b2b727b8d4b6b1fd598cbd12dd5e614f1dfeefa96a92a07e3a3b312a2')
    r['model'].pop('display_scale_xyz')
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Fenghua product page reviewed online',
                                'source_record': f'parts_source/{PART}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad nominal 0402 MLCC geometry matches the selected Fenghua part dimensions; '
                              'ceramic colour and metallic terminations are illustrative.')
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
