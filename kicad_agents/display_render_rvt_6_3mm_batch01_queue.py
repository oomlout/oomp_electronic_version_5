"""Prepare individually verified 6.3 mm Honor RVT display illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_100_micro_farad_25_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RVT_6_3MM_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_100_micro_farad_35_volt': ('RVT1V101M0607', 'C3339', '100 uF', '35 V', '100\n35V'),
    'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_16_volt': ('RVT1C221M0607', 'C3342', '220 uF', '16 V', '220\n16V'),
    'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_470_micro_farad_6_3_volt': ('RVT0J471M0607', 'C3354', '470 uF', '6.3 V', '470\n6.3V'),
    'electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_47_micro_farad_50_volt': ('RVT1H470M0607', 'C3349', '47 uF', '50 V', '47\n50V'),
}

def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed component')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'Honor Elec' or record.get('part_number_manufacturer') != mpn
        or record.get('part_number_lcsc') != supplier or e.get('capacitance') != value
        or e.get('rated_voltage') != voltage or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 6.3, 'width': 6.3, 'height': 7.7}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:CP_Elec_6.3x7.7'):
        raise ValueError('Identity, voltage, polarity or package changed')
    recipe = copy.deepcopy(recipes[PILOT])
    if (recipe.get('family') != 'aluminum_capacitor' or recipe['model'].get('metal_top_marking') is not True
        or recipe['model'].get('display_scale_xyz') != [1.0, 1.0, 1.0]):
        raise ValueError('Pilot model changed')
    recipe['represented_mpn'] = mpn
    recipe['marking']['text'] = text
    recipe['appearance_status'] += ' Marking is composited from shared material passes; indirect reflections are approximate.'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Honor RVT series specification and individual supplier listing',
        'source_record': f'parts_source/{part}/working.yaml'}
    return recipe

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
        print(p, recipe['represented_mpn'])

if __name__ == '__main__':
    main()
