"""Stage two individually researched Chengx GR 10 x 20 mm illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_km_10x20_pilot_queue import PART as REFERENCE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_GR_10X20_BATCH_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_1500_micro_farad_16_volt':
        ('GR158M016G20RR0VL4FP0', 'C3311', '1500 uF', '16 V', '1500uF\n16V\nGR 105C'),
    'electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_470_micro_farad_50_volt':
        ('GR477V050G20RR0VH4FP0', 'C3312', '470 uF', '50 V', '470uF\n50V\nGR 105C'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed GR part')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('pin_spacing') != '5.0 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 10., 'width': 10., 'height': 20.}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result.get('represented_mpn') != 'KM228M016G20RR0VH2FP0'
        or result['model'].get('radial_stretch', {}).get('extra_height') != 10.):
        raise ValueError('Reviewed 10 x 20 model changed')
    result['represented_mpn'] = mpn
    result['radial_palette'] = 'green_gold' if supplier == 'C3311' else 'black_gold'
    result['marking'].update(text=text, evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Chengx GR series and individual supplier listing',
        'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Value, voltage and GR series marking are illustrative; actual printing, logo and production code are unverified.')
    result['appearance_status'] = ('Illustrative KiCad radial model with its straight sleeve extended to 20 mm; ends and leads remain unchanged. Sleeve and ink colours follow the manufacturer part-number key; shades, negative stripe, proportions and finish are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    if args.add:
        from kicad_agents.display_render_radial import radial_palette
        radial_palette('green_gold')
        radial_palette('black_gold')
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
