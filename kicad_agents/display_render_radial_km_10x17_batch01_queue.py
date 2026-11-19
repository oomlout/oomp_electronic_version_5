"""Stage two individually checked KM 10 x 17 mm radial illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_km_10x17_pilot_queue import PART as PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_10X17_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_100_micro_farad_100_volt':
        ('KM107M100G17RR0VH2FP0', 'C3336', '100 uF', '100 V', '100uF\n100V\nKM 105C'),
    'electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_15_micro_farad_400_volt':
        ('KM156M400G17RR0VH2FP0', 'C5300', '15 uF', '400 V', '15uF\n400V\nKM 105C'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed KM part')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or e.get('capacitance') != value or e.get('rated_voltage') != voltage
        or e.get('pin_spacing') != '5.0 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 10.0, 'height': 17.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[PILOT])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result.get('represented_mpn') != 'KM477M035G17RR0VH2FP0'
        or result['model'].get('radial_stretch', {}).get('extra_height') != 7.0):
        raise ValueError('Reviewed KM pilot changed')
    result['represented_mpn'] = mpn
    result['marking'].update(text=text, evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Individual LCSC listing and Chengx KM specification',
        'source_record': f'parts_source/{part}/working.yaml'})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
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
