"""Prepare individually reviewed 6.8 MΩ and 820 kΩ display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_UNIROYAL_CCO_HIGH_VALUE_EVIDENCE.md')
FOOTPRINT = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_6800000_ohm': ('UNI-ROYAL', 'MF02WFF6804A10', 'C51904866', ('6.8MΩ', '2W', '1%', 'D5xL15.5mm'), '6800000', '1%'),
    'electronic_resistor_quarter_watt_through_hole_820000_ohm': ('CCO(Chian Chia Elec)', 'RI40-1/4W-820KΩ ±2% T', 'C136537', ('820kΩ', '250mW', '2%', 'D2.3xL6.5mm'), '820000', '2%'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    maker, mpn, lcsc, tokens, value, tolerance = PARTS[part]
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in tokens) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, rating, value or package changed')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Footprint changed')
    for t in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t and str(t).replace('±', '').replace(' ', '') != tolerance:
            raise ValueError('Tolerance conflict')
    if tolerance == '1%':
        r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_12_ohm'])
        if r.get('package') != 'din0516_horizontal_20_32mm':
            raise ValueError('Unexpected model')
        status = ('Selected UNI-ROYAL part is rated 2 W despite the quarter-watt catalogue ID. '
                  'The KiCad 15.5 × 5 mm body matches the listed body size; formed leads are 20.32 mm apart. '
                  'The existing smaller footprint and dimensions need review. Blue coating is illustrative.')
    else:
        r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_1000_ohm'])
        if r.get('package') != 'din0207_horizontal_7_62mm':
            raise ValueError('Unexpected model')
        status = ('The 6.3 × 2.5 mm KiCad body approximates the selected 6.5 × 2.3 mm body; '
                  'formed leads are 7.62 mm apart. Blue coating is illustrative.')
    bands = bands_for(value)
    if tolerance == '2%':
        bands[-1] = 'red'
    r.update(represented_manufacturer=maker, represented_mpn=mpn, appearance_status=status)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Selected supplier listings reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Standard {tolerance} five-band value code: ' + ', '.join(bands) + '.'},
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
