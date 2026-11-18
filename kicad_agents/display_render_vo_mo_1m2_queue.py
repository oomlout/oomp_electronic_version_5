"""Prepare the individually reviewed VO 1.2 MΩ metal-oxide display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_1200000_ohm'
MPN = 'MO1/4W-1M2±5%-ST52'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VO_MO_1M2_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'VO' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'VO' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C601771' and all(t in str(x.get('product_name', '')) for t in ('1.2MΩ', '250mW', '5%', 'D2.7xL6.2mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Footprint changed')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_6800_ohm'])
    bands = bands_for(1200000)
    if r.get('family') != 'axial_resistor' or bands != ['brown', 'red', 'green', 'gold']:
        raise ValueError('Unexpected template or band code')
    r.update(represented_manufacturer='VO', represented_mpn=MPN)
    r['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'VO MO series and supplier listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Standard 5% four-band representation for 1.2 MΩ: brown, red, green, gold.'},
        appearance_status='Standard four-band representation; actual band count, spacing and shades are unverified.')
    r['appearance_status'] = ('Generic KiCad 6.3 × 2.5 mm axial body approximates the supplier-listed 6.2 × 2.7 mm body, with bent leads. '
        'Beige coating is illustrative; the VO specification describes gray coating.')
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
