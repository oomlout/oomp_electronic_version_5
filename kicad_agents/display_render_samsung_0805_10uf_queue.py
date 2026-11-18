"""Prepare a dimension-checked Samsung 0805 MLCC display illustration."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0805_10_micro_farad_16_volt'
PILOT = 'electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc'
MPN = 'CL21A106KOQNNNE'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_10UF_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    maker = 'Samsung Electro-Mechanics'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C1713' for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 2.0 or dims.get('width') != 1.25 or dims.get('height', 1.25) != 1.25:
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', '10 uF'), ('rated_voltage', '16 V'), ('dielectric', 'X5R'), ('tolerance', '10%')):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric':
        raise ValueError('Unexpected source model')
    r.update(package='0805_imperial_2012_metric', represented_manufacturer=maker, represented_mpn=MPN)
    model = r['model']
    model.update(relative_path='Capacitor_SMD.3dshapes/C_0805_2012Metric.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Capacitor_SMD.3dshapes/C_0805_2012Metric.step',
        expected_bounds_mm=[2.0, 1.25, 1.25],
        sha256='9a669c1a2f1ea25b88b401acef6efeaa80a067bd7da9db6993de719a7fbe155c')
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Samsung product page reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad nominal 0805 MLCC geometry matches the selected Samsung part dimensions; '
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
    recipe = reviewed_recipe(yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
    if args.add:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
