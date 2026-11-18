"""Prepare individually reviewed half-watt carbon-film displays."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_cfr_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_HALF_WATT_CARBON_EVIDENCE.md')
MODEL = 'Resistor_THT.3dshapes/R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal.step'
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_470_ohm': ('VO', 'CR1/2W-470Ω±5%-XT52', 'C2894503', '470', '470Ω', 'D3.5xL9mm', '9 × 3.5 mm'),
    'electronic_resistor_quarter_watt_through_hole_270000_ohm': ('SEI(Stackpole Electronics Inc.)', 'CF12JT270K', 'C2586012', '270000', '270kΩ', 'D2.7xL8.5mm', '8.5 × 2.7 mm'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    manufacturer, mpn, lcsc, value, value_text, dims, body = PARTS[part]
    if record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == manufacturer and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc and all(t in str(x.get('product_name', '')) for t in (value_text, '500mW', '5%', dims)) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier, value, rating or package changed')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal':
        raise ValueError('Existing footprint changed; reassess mismatch')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and str(tolerance).strip() not in ('5%', '±5%', '5 %', '±5 %'):
            raise ValueError('Tolerance conflict')
    r = copy.deepcopy(recipes['electronic_resistor_quarter_watt_through_hole_10_ohm'])
    bands = bands_for(Decimal(value))
    if r.get('family') != 'axial_resistor' or bands[-1] != 'gold':
        raise ValueError('Unexpected template or tolerance')
    r.update(package='din0309_horizontal_12_70mm', represented_manufacturer=manufacturer, represented_mpn=mpn)
    r['model'].update(relative_path=MODEL, sha256='ccfacca9fc7ae291c5d1d457d716f8bf1a41d9f9d558fab89ca042784fe0ad70',
        expected_bounds_mm=[13.4, 3.2, 6.2], source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL)
    r['marking'].update(text=' / '.join(bands), bands=bands, body_span_mm=[1.85, 10.85], band_width_mm=.3,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Manufacturer specifications and selected supplier listings reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml', 'rule': f'Standard 5% four-band code for {value} ohm: ' + ', '.join(bands) + '.'},
        appearance_status='Standard 5% four-band code; band placement and shades are illustrative.')
    r['appearance_status'] = (f'Selected part is rated 500 mW despite the legacy quarter-watt catalogue ID. '
        f'The 9 × 3.2 mm KiCad body approximates the selected {body} body; formed leads are 12.70 mm apart. '
        'The existing catalogue footprint and dimensions describe a smaller part and need review. Blue coating is illustrative.')
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
