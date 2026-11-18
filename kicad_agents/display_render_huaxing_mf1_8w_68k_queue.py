"""Prepare the reviewed Huaxing 1/8 W 68 kΩ small axial display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_68000_ohm'
MPN = 'MF1/8W-68KΩ±1%T52'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_HUAXING_MF1_8W_68K_EVIDENCE.md')
MODEL = 'Resistor_THT.3dshapes/R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal.step'


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'Huaxing Mechanical-Elec.' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'Huaxing Mechanical-Elec.' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C713932' and all(t in str(x.get('product_name', '')) for t in ('68kΩ', '125mW', '1%', 'D1.8xL3.2mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm'])
    bands = bands_for(68000)
    if r.get('family') != 'axial_resistor' or bands != ['blue', 'grey', 'black', 'red', 'brown']:
        raise ValueError('Unexpected template or band code')
    r.update(package='din0204_horizontal_7_62mm', represented_manufacturer='Huaxing Mechanical-Elec.', represented_mpn=MPN)
    r['model'].update(relative_path=MODEL, sha256='a68bc07f83e555444e1844fd40d0eadcb2b2fec94e4bc54969d2940836b12f5c',
        expected_bounds_mm=[8.12, 1.6, 4.6], source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL)
    r['marking'].update(text=' / '.join(bands), bands=bands, body_span_mm=[2.01, 5.61],
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Huaxing MF specification and selected source record reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Standard 1% five-band code for 68 kΩ: blue, grey, black, red, brown.'},
        appearance_status='Standard five-band code; exact stripe spacing and shades are illustrative.')
    r['appearance_status'] = ('Selected Huaxing part is rated 125 mW, despite the legacy quarter-watt catalogue ID. '
        'The 3.6 × 1.6 mm KiCad body approximates the selected 3.2 × 1.8 mm part; the existing catalogue footprint and dimensions depict a larger body. '
        'Bent leads at 7.62 mm pitch and beige coating are illustrative; the manufacturer describes blue coating.')
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
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    print(PART, recipe['marking']['text'])


if __name__ == '__main__':
    main()
