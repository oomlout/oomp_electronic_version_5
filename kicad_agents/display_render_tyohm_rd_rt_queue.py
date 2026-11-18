"""Prepare two supplier-reviewed TyoHM quarter-watt axial displays."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TYOHM_RD_RT_EVIDENCE.md')
FOOTPRINT = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_5600000_ohm': ('RD 1/4W 5M6 J T/B A1', 'C433702', '5600000', '5.6MΩ', 'D2.4xL6.5mm', '6.5 × 2.4 mm', 'Its manufacturer coating colour has not been confirmed.'),
    'electronic_resistor_quarter_watt_through_hole_2200000_ohm': ('RT 1/4W 2M2 J T/B', 'C5200510', '2200000', '2.2MΩ', 'D2.4xL6.4mm', '6.4 × 2.4 mm', 'The manufacturer specifies light green coating.'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, value_text, dimensions, body, colour = PARTS[part]
    if record.get('manufacturer') != 'TyoHM' or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'TyoHM' and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in (value_text, '250mW', '5%', dimensions)) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Existing footprint changed')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_6800_ohm'])
    bands = bands_for(Decimal(value))
    if r.get('family') != 'axial_resistor' or bands[-1] != 'gold':
        raise ValueError('Unexpected template or tolerance')
    r.update(represented_manufacturer='TyoHM', represented_mpn=mpn)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Supplier listings and TyoHM RT specification reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Standard 5% four-band code for {value} ohm: ' + ', '.join(bands) + '.'},
        appearance_status='Standard 5% four-band code; exact manufacturer band count, placement and shades are unverified.')
    r['appearance_status'] = (f'The 6.3 × 2.5 mm KiCad body approximates the selected {body} body; formed leads are 7.62 mm apart. '
        f'Blue coating is illustrative. {colour}')
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {part: reviewed_recipe(part, yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for part in PARTS if part not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'], recipe['marking']['text'])
    print(len(found), 'reviewed parts')


if __name__ == '__main__':
    main()
