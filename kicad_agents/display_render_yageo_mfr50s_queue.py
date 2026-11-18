"""Prepare reviewed miniature half-watt Yageo axial display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for, resistance

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_MFR50S_EVIDENCE.md')
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_3900_ohm': ('MFR50SFTE52-3K9', 'C1375312', '3900'),
    'electronic_resistor_quarter_watt_through_hole_820_ohm': ('MFR50SFTE52-820R', 'C1374618', '820'),
    'electronic_resistor_quarter_watt_through_hole_3300000_ohm': ('MFR50SFTE52-3M3', 'C914831', '3300000'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value = PARTS[part]
    if record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected manufacturer or MPN changed')
    if resistance(mpn.removeprefix('MFR50SFTE52-')) != Decimal(value):
        raise ValueError('Resistance mismatch')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in ('500mW', '1%', 'D2.4xL6.3mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, rating or package changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Footprint changed')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('1%', '±1%', '1 %', '±1 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm'])
    bands = bands_for(value)
    if r.get('family') != 'axial_resistor' or bands[-1] != 'brown':
        raise ValueError('Unexpected template or tolerance')
    r.update(represented_manufacturer='YAGEO', represented_mpn=mpn)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'YAGEO MFR specification and individual supplier listings reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'1% five-band code for {value} ohm: ' + ', '.join(bands) + '.'},
        appearance_status='Documented 1% five-band code; band spacing and shades are illustrative.')
    r['appearance_status'] = ('The selected YAGEO MFR50S is rated 500 mW (half watt), despite the legacy quarter-watt catalogue ID. '
        'Generic KiCad 6.3 × 2.5 mm body approximates the specified 6.3 × 2.4 mm body, with bent leads at 7.62 mm pitch. Blue finish is illustrative.')
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {part: reviewed_recipe(part, yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for part in PARTS if part not in recipes and (ROOT / 'parts' / part / 'working.yaml').is_file()}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'], recipe['marking']['text'])
    print(len(found), 'reviewed parts')


if __name__ == '__main__':
    main()
