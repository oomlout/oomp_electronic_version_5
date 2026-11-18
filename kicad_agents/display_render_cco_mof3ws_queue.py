"""Prepare reviewed large CCO MOF3WS metal-oxide display recipes."""
import argparse
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CCO_MOF3WS_EVIDENCE.md')
MANUFACTURER = 'CCO(Chian Chia Elec)'
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_47_ohm': ('MOF3WS-47Ω±5% T', 'C121800', '47'),
    'electronic_resistor_quarter_watt_through_hole_150000_ohm': ('MOF3WS-150KΩ±5% T', 'C121884', '150000'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value = PARTS[part]
    if record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MANUFACTURER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in ('3W', '5%', 'D5xL15.5mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, rating or package changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_10_ohm'])
    bands = bands_for(Decimal(value))
    if r.get('package') != 'din0516_horizontal_20_32mm' or bands[-1] != 'gold':
        raise ValueError('Unexpected model or tolerance')
    r.update(represented_manufacturer=MANUFACTURER, represented_mpn=mpn)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'CCO MOF specification and supplier listings reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Documented 5% four-band code for {value} ohm: ' + ', '.join(bands) + '.'},
        appearance_status='Documented four-band value code; stripe spacing and shades are illustrative.')
    r['appearance_status'] = ('Selected CCO MOF3WS is rated 3 W despite the legacy quarter-watt catalogue ID. '
        'The 15.5 × 5 mm KiCad body matches nominal dimensions; formed leads are 20.32 mm apart. '
        'The existing catalogue footprint and dimensions describe a much smaller part and need review. '
        'Blue coating is illustrative; CCO specifies gray or pink.')
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
