"""Prepare the reviewed CCO cement resistor display approximation."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_resistor_quarter_watt_through_hole_100_ohm'
MPN = 'CR-L5W100Ω 5% P'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CCO_CEMENT_100R_EVIDENCE.md')
MODEL = 'Resistor_THT.3dshapes/R_Axial_Power_L25.0mm_W9.0mm_P27.94mm.step'


def reviewed_recipe(record, recipes, sha):
    maker = 'CCO(Chian Chia Elec)'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C216402' and all(t in str(x.get('product_name', '')) for t in ('100Ω', '5W', '5%', 'D9.5xL22mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed')
    for t in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t and str(t).replace('±', '').replace(' ', '') != '5%':
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_0603_10000_ohm'])
    r.update(family='cement_power_resistor', package='axial_cement_25x9_27_94mm', represented_manufacturer=maker, represented_mpn=MPN)
    r['model'] = {'relative_path': MODEL, 'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        'copyright': '2017 kicad StepUp', 'license': 'CC-BY-SA-4.0 with KiCad library exception',
        'license_url': 'https://www.kicad.org/libraries/license/', 'expected_bounds_mm': [28.74, 9.0, 12.0],
        'dimension_tolerance_mm': .03, 'sha256': '96e46332a3cd87eadfe6f9cabedf1325433fef297cf7302f8f65420a4e39c3ad',
        'role_by_source_colour': {'0.895,0.891,0.813': 'coating', '0.824,0.820,0.781': 'termination'},
        'required_roles': ['coating', 'termination']}
    r['marking'] = {'policy': 'illustrative_literal', 'text': '100Ω 5W', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 15, 'maximum_height_mm': 3,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Selected supplier listing reviewed online',
                     'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Illustrative text uses the listed resistance and rated power; exact factory print not verified.'},
        'appearance_status': 'Illustrative value and power text; the exact factory marking, font and placement are unverified.'}
    r['appearance_status'] = ('Selected CCO part is 5 W despite the legacy quarter-watt ID. The generic 25 × 9 mm KiCad body is longer and narrower than the listed 22 × 9.5 mm body; '
        'its formed leads are 27.94 mm apart. The existing smaller footprint and dimensions need review. Body finish is illustrative.')
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
    print(PART, recipe['marking']['text'])


if __name__ == '__main__':
    main()
