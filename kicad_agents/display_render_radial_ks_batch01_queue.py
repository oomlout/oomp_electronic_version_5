"""Stage two individually checked KS 4 x 7 mm radial illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_ks_pilot_queue import PART as PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KS_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_1_micro_farad_50_volt':
        ('KS105M050C07RR0VH2FP0', 'C2760', '1 uF', '1uF\n50V\nKS 105C'),
    'electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_2_2_micro_farad_50_volt':
        ('KS225M050C07RR0VH2FP0', 'C2065', '2.2 uF', '2.2uF\n50V\nKS 105C'),
}


def reviewed_recipe(part, record, recipes, evidence_sha):
    if part not in PARTS:
        raise ValueError('Unreviewed KS part')
    mpn, supplier, value, text = PARTS[part]
    electrical = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != mpn or record.get('part_number_lcsc') != supplier
        or electrical.get('capacitance') != value or electrical.get('rated_voltage') != '50 V'
        or electrical.get('pin_spacing') != '1.5 mm' or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 4.0, 'width': 4.0, 'height': 7.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D4.0mm_P1.50mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[PILOT])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result.get('represented_mpn') != 'KS336M016C07RR0VH2FP0'
        or result['model'].get('flat_top', {}).get('radius') != 1.4
        or result['model'].get('radial_stretch', {}).get('extra_height') != 3.0):
        raise ValueError('Reviewed KS pilot changed')
    result['represented_mpn'] = mpn
    result['marking'].update(text=text, evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
        'document': 'Individual JLCPCB listing and related Chengx KS specification',
        'source_record': f'parts_source/{part}/working.yaml'})
    result['appearance_status'] = ('Illustrative 4 mm KiCad radial model with sleeve extended to 7 mm and unvented top based on a related KS drawing. Black and white appearance, negative stripe, top depth, shape and finish are illustrative; this sibling part’s exact artwork was not verified.')
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
