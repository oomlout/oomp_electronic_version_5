"""Prepare the reviewed small CCO 2.4 kΩ carbon-film display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_2400_ohm'
MPN = 'CF1/6W-2.4KΩ±5% T'
MANUFACTURER = 'CCO(Chian Chia Elec)'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CCO_CF1_6W_2K4_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MANUFACTURER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C119879' and all(t in str(x.get('product_name', '')) for t in ('2.4kΩ', '167mW', '5%', 'D1.8xL3.2mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_68000_ohm'])
    bands = bands_for(2400)
    if r.get('package') != 'din0204_horizontal_7_62mm' or bands != ['red', 'yellow', 'red', 'gold']:
        raise ValueError('Unexpected template or band code')
    r.update(represented_manufacturer=MANUFACTURER, represented_mpn=MPN)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'CCO carbon-film specification and selected supplier listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Documented 5% four-band code for 2.4 kΩ: red, yellow, red, gold.'},
        appearance_status='Documented four-band code; stripe spacing and shades are illustrative.')
    r['appearance_status'] = ('Selected CCO CF1/6W is rated 167 mW despite the legacy quarter-watt catalogue ID. '
        'The 3.6 × 1.6 mm KiCad body approximates the selected 3.2 × 1.8 mm part; the existing catalogue footprint and dimensions depict a larger body. '
        'Bent leads at 7.62 mm pitch and blue coating are illustrative.')
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
