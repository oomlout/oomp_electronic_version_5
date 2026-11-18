"""Prepare the reviewed TyoHM RN1WS 1.8 kΩ axial display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_1800_ohm'
MPN = 'RN1WS1.8KΩFT/BA1'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TYOHM_RN1WS_1K8_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'TyoHM' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'TyoHM' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C385265' and all(t in str(x.get('product_name', '')) for t in ('1.8kΩ', '1W', '1%', 'D3.3xL9.2mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('1%', '±1%', '1 %', '±1 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_470_ohm'])
    bands = bands_for(1800)
    if r.get('package') != 'din0309_horizontal_12_70mm' or bands != ['brown', 'grey', 'black', 'brown', 'brown']:
        raise ValueError('Unexpected template or band code')
    r.update(represented_manufacturer='TyoHM', represented_mpn=MPN)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'TyoHM RN specification and selected source listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': '1% five-band code for 1.8 kΩ: brown, grey, black, brown, brown.'},
        appearance_status='Documented five-band value code; stripe spacing and shades are illustrative.')
    r['appearance_status'] = ('Selected TyoHM RN1WS is rated 1 W despite the legacy quarter-watt catalogue ID. '
        'The 9 × 3.2 mm KiCad body approximates the listed 9.2 × 3.3 mm body; formed leads are 12.70 mm apart. '
        'The existing catalogue footprint and dimensions describe a smaller part and need review. Blue coating is illustrative.')
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
