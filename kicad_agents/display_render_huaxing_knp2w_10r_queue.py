"""Prepare the reviewed large Huaxing 2 W wirewound display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_10_ohm'
MPN = 'KNP2W-10Ω±5%T'
MANUFACTURER = 'Huaxing Mechanical-Elec.'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_HUAXING_KNP2W_10R_EVIDENCE.md')
MODEL = 'Resistor_THT.3dshapes/R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal.step'


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MANUFACTURER and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C714512' and all(t in str(x.get('product_name', '')) for t in ('10Ω', '2W', '5%', 'D5xL15.5mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_6800_ohm'])
    bands = bands_for(10)
    if r.get('family') != 'axial_resistor' or bands != ['brown', 'black', 'black', 'gold']:
        raise ValueError('Unexpected template or band code')
    r.update(package='din0516_horizontal_20_32mm', represented_manufacturer=MANUFACTURER, represented_mpn=MPN)
    r['model'].update(relative_path=MODEL, sha256='5d41e37d6dfee8d32447412d8ae01e8d1208a75fcda370392e1b311eb5a8f25b',
        expected_bounds_mm=[21.12, 5.0, 8.0], source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL)
    r['marking'].update(text=' / '.join(bands), bands=bands, body_span_mm=[2.41, 17.91], band_width_mm=.52,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Huaxing selected supplier listing and standard 5% representation reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Illustrative standard 5% four-band code for 10 Ω: brown, black, black, gold.'},
        appearance_status='Standard four-band code; the selected part’s exact band count, order and spacing are unverified.')
    r['appearance_status'] = ('Selected Huaxing wirewound part is rated 2 W, despite the legacy quarter-watt catalogue ID. '
        'The 15.5 × 5 mm KiCad body matches its listed dimensions; formed leads are 20.32 mm apart. '
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
