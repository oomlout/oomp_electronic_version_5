"""Prepare the reviewed Huaxing 10 MΩ 1 W display recipe."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_10000000_ohm'
MPN = 'RI40-1W-10MΩ±2%T'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_HUAXING_RI40_10M_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    maker = 'Huaxing Mechanical-Elec.'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C714675' and all(t in str(x.get('product_name', '')) for t in ('10MΩ', '1W', '2%')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or tolerance changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Footprint changed; reassess discrepancy')
    for t in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t and str(t).replace('±', '').replace(' ', '') != '2%':
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1500_ohm'])
    bands = bands_for('10000000'); bands[-1] = 'red'
    if r.get('package') != 'din0414_horizontal_15_24mm' or bands != ['brown', 'black', 'black', 'green', 'red']:
        raise ValueError('Unexpected package or band code')
    r.update(represented_manufacturer=maker, represented_mpn=MPN)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Manufacturer approval sheet and supplier listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Standard 2% five-band code for 10 MΩ: brown, black, black, green, red.'},
        appearance_status='Standard value code; exact manufacturer band count, spacing and shades are unverified.')
    r['appearance_status'] = ('Selected Huaxing part is rated 1 W despite the quarter-watt catalogue ID. '
        'The 11.9 × 4.5 mm KiCad body approximates the specified 11.5 × 4.5 mm body; formed leads are 15.24 mm apart. '
        'The existing smaller footprint and dimensions need review. Blue coating is illustrative; the manufacturer specifies gray or pink.')
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
