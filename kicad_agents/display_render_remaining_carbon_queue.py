"""Prepare two carbon-film value illustrations with incomplete source MPNs."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_REMAINING_CARBON_EVIDENCE.md')
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_39_ohm': ('TyoHM', 'T/B', 'C5200377', '39', ('39Ω', '250mW', '5%', 'D2.4xL6.5mm'), 'electronic_resistor_quarter_watt_through_hole_6800_ohm'),
    'electronic_resistor_quarter_watt_through_hole_39000_ohm': ('VO', 'STB5', 'C337041', '39000', ('39kΩ', '125mW', '5%', 'D2.3xL3.7mm'), 'electronic_resistor_quarter_watt_through_hole_2400_ohm'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    maker, fragment, lcsc, value, tokens, template = PARTS[part]
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != fragment:
        raise ValueError('Selected source identity changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in tokens) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or package changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Footprint changed')
    for t in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t and str(t).replace('±', '').replace(' ', '') != '5%':
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes[template])
    bands = bands_for(Decimal(value))
    r.update(represented_manufacturer=maker, represented_mpn='Incomplete in source record')
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Stored supplier selection and standard colour code; exact MPN unverified',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Standard 5% four-band code for {value} Ω: ' + ', '.join(bands) + '.'},
        appearance_status='Standard value code; exact manufacturer band count, placement and shades are unverified.')
    size = ('The 6.3 × 2.5 mm model approximates the listed 6.5 × 2.4 mm body.' if value == '39' else
            'The 3.6 × 1.6 mm model approximates the listed 3.7 × 2.3 mm length but is thinner. The selected 125 mW rating and smaller body conflict with the quarter-watt ID and existing footprint.')
    r['appearance_status'] = (f'Illustrates the saved {maker} {lcsc} selection; the manufacturer part number is truncated and the supplier page was unavailable during review. '
        f'{size} Model leads are 7.62 mm apart. Blue coating is illustrative.')
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {p: reviewed_recipe(p, yaml.safe_load((ROOT / 'parts_source' / p / 'working.yaml').read_text(encoding='utf8')), recipes, sha) for p in PARTS if p not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for p, recipe in found.items():
        print(p, recipe['marking']['text'])


if __name__ == '__main__':
    main()
