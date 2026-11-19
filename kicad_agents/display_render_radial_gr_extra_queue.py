"""Prepare three individually researched Chengx GR radial illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_km_6x11_pilot_queue import PART as REF_6

REF_8 = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_GR_EXTRA_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_470_micro_farad_10_volt':
        ('GR477M010F12RR0VL4FP0', 'C2033', '470 uF', '10 V', 8., 12., '3.5 mm', REF_8, 4., 'green_gold', '470uF\n10V\nGR 105C'),
    'electronic_capacitor_8_mm_diameter_14_mm_tall_electrolytic_470_micro_farad_25_volt':
        ('GR477M025F14RR0VL4FP0', 'C5154', '470 uF', '25 V', 8., 14., '3.5 mm', REF_8, 6., 'green_gold', '470uF\n25V\nGR 105C'),
    'electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_220_micro_farad_10_volt':
        ('GR227M010E11RR0VH4FP0', 'C2036', '220 uF', '10 V', 6.3, 11., '2.5 mm', REF_6, 4.7, 'black_gold', '220uF\n10V\nGR 105C'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed GR part')
    mpn, supplier, value, voltage, diameter, height, pitch, reference, extension, palette, text = PARTS[part]
    e = record.get('electrical') or {}
    footprint = 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm' if diameter == 8 else 'Capacitor_THT:CP_Radial_D6.3mm_P2.50mm'
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('pin_spacing') != pitch or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': diameter, 'width': diameter, 'height': height}
        or record.get('kicad', {}).get('machine_solder') != footprint):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[reference])
    if result.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('Reference family changed')
    result['package'] = f'radial_{str(diameter).replace(".", "_")}x{int(height)}'
    result['model']['radial_stretch']['extra_height'] = extension
    result['represented_mpn'] = mpn
    result['radial_palette'] = palette
    result['marking'].update(text=text, evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Individual LCSC listing and Chengx part-number key', 'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Value, voltage and GR marking layout are illustrative; actual typography and production artwork are unverified.')
    result['appearance_status'] = (f'Illustrative KiCad radial model with straight sleeve extended to {height:g} mm, preserving ends and leads. Sleeve and ink colours follow the Chengx code; shades, stripe, shape and finish are illustrative.')
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
