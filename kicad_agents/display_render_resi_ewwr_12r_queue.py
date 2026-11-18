"""Prepare the reviewed RESI EWWR 12 Ω large axial display."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_12_ohm'
MPN = 'EWWR0003J12R0T9'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RESI_EWWR_12R_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'RESI' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'RESI' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C348852' and all(t in str(x.get('product_name', '')) for t in ('12Ω', '3W', '5%', 'D5.5xL15mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_10_ohm'])
    bands = bands_for(Decimal(12))
    if r.get('package') != 'din0516_horizontal_20_32mm' or bands != ['brown', 'red', 'black', 'gold']:
        raise ValueError('Unexpected template or band code')
    r.update(represented_manufacturer='RESI', represented_mpn=MPN)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'RESI EWWR specification and selected supplier listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Standard 5% four-band representation for 12 Ω: brown, red, black, gold.'},
        appearance_status='Standard 5% representation; the selected part’s exact band count and placement are unverified.')
    r['appearance_status'] = ('Selected RESI EWWR0003 is rated 3 W despite the legacy quarter-watt catalogue ID. '
        'The 15.5 × 5 mm KiCad body is within the specified 15 × 5.5 mm tolerance; formed leads are 20.32 mm apart. '
        'The existing catalogue footprint and dimensions describe a much smaller part and need review. Blue coating is illustrative.')
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
