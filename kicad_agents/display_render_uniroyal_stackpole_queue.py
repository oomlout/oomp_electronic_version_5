"""Prepare two supplier-reviewed 2.7 MΩ and 8.2 MΩ displays."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for as bands_1
from kicad_agents.display_render_yageo_cfr_queue import bands_for as bands_5

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_UNIROYAL_STACKPOLE_EVIDENCE.md')
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_2700000_ohm': ('UNI-ROYAL', 'MF0W4FF2704A50', 'C2991790', ('2.7MΩ', '250mW', '1%', 'D2.2xL6.5mm')),
    'electronic_resistor_quarter_watt_through_hole_8200000_ohm': ('SEI(Stackpole Electronics Inc.)', 'RC12JB8M20', 'C19511659', ('8.2MΩ', '500mW', '5%', 'D3.6xL9.5mm')),
}
FOOTPRINT = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    manufacturer, mpn, lcsc, tokens = PARTS[part]
    if record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == manufacturer and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in tokens) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, rating, value or package changed')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Footprint changed')
    tolerance = '1%' if manufacturer == 'UNI-ROYAL' else '5%'
    for t in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t and str(t).replace('±', '').replace(' ', '') != tolerance:
            raise ValueError('Tolerance conflict')
    if tolerance == '1%':
        r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm'])
        bands = bands_1('2700000')
        status = ('The 6.3 × 2.5 mm KiCad body approximates the selected 6.5 × 2.2 mm body; '
                  'formed leads are 7.62 mm apart. Blue coating is illustrative.')
    else:
        r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_470_ohm'])
        bands = bands_5(Decimal('8200000'))
        status = ('The selected Stackpole part is rated 500 mW despite the quarter-watt catalogue ID. '
                  'The 9 × 3.2 mm KiCad body approximates the selected 9.5 × 3.6 mm body; '
                  'formed leads are 12.70 mm apart. The existing smaller footprint needs review. Blue coating is illustrative.')
    if r.get('family') != 'axial_resistor':
        raise ValueError('Unexpected template')
    r.update(represented_manufacturer=manufacturer, represented_mpn=mpn, appearance_status=status)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Supplier listings reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Standard {tolerance} value code: ' + ', '.join(bands) + '.'},
        appearance_status='Standard value code; exact manufacturer band count, placement and shades are unverified.')
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {p: reviewed_recipe(p, yaml.safe_load((ROOT / 'parts_source' / p / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for p in PARTS if p not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    for p, r in found.items():
        print(p, r['marking']['text'])
    print(len(found), 'reviewed parts')


if __name__ == '__main__':
    main()
