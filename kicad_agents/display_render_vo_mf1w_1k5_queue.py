"""Prepare the reviewed VO MF1W 1.5 kΩ axial display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

PART = 'electronic_resistor_quarter_watt_through_hole_1500_ohm'
MPN = 'MF1W-1K5±1%-TT63'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VO_MF1W_1K5_EVIDENCE.md')
MODEL = 'Resistor_THT.3dshapes/R_Axial_DIN0414_L11.9mm_D4.5mm_P15.24mm_Horizontal.step'


def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'VO' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == 'VO' and x.get('part_number') == MPN for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C2903196' and all(t in str(x.get('product_name', '')) for t in ('1.5kΩ', '1W', '1%', 'D4.5xL11mm')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or dimensions changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('1%', '±1%', '1 %', '±1 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_68000_ohm'])
    bands = bands_for(1500)
    if r.get('family') != 'axial_resistor' or bands != ['brown', 'green', 'black', 'brown', 'brown']:
        raise ValueError('Unexpected template or band code')
    r.update(package='din0414_horizontal_15_24mm', represented_manufacturer='VO', represented_mpn=MPN)
    r['model'].update(relative_path=MODEL, sha256='adda0647a71569528494b0c89336a4700aa00105603a72f3e617460fa4b7b776',
        expected_bounds_mm=[16.04, 4.5, 7.5], source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL)
    r['marking'].update(text=' / '.join(bands), bands=bands, body_span_mm=[1.67, 13.57], band_width_mm=.4,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'VO MF specification and selected supplier listing reviewed online',
                  'source_record': f'parts_source/{PART}/working.yaml', 'rule': 'Standard 1% five-band representation for 1.5 kΩ: brown, green, black, brown, brown.'},
        appearance_status='Standard 1% representation; the selected part’s exact band count and placement are unverified.')
    r['appearance_status'] = ('Selected VO MF1W is rated 1 W despite the legacy quarter-watt catalogue ID. '
        'The 11.9 × 4.5 mm KiCad body approximates the listed 11 × 4.5 mm body; formed leads are 15.24 mm apart. '
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
