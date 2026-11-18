"""Prepare an evidenced and height-adjusted Fenghua 1206 illustration."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_120pf_queue import PART as PILOT, MAKER

PART = 'electronic_capacitor_1206_10_nano_farad'
MPN = '1206B103K500NT'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_10NF_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C1846' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6, 'height': .8}:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '10 nF'), ('rated_voltage', '50 V'), ('dielectric', 'X7R'), ('tolerance', '10%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric':
        raise ValueError('Unexpected source recipe')
    r.update(package='1206_imperial_3216_metric', represented_mpn=MPN)
    r['model'].update(relative_path='Capacitor_SMD.3dshapes/C_1206_3216Metric.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Capacitor_SMD.3dshapes/C_1206_3216Metric.step',
        expected_bounds_mm=[3.2, 1.6, 1.6], sha256='11e948c72c90e2b6322436b72745f40ff4e8ba0da64fb2a0df943dfa61e89c1a',
        display_scale_xyz=[1.0, 1.0, .5])
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Fenghua catalogue entry reviewed online',
                                'source_record': f'parts_source/{PART}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad 1206 model scaled to the selected Fenghua part’s 0.80 mm nominal height; '
                              'shape details, ceramic colour and metallic terminations are illustrative.')
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
