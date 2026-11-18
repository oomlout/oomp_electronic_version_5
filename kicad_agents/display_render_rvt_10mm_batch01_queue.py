"""Prepare individually verified 10 mm Honor RVT display illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_1000_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RVT_10MM_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_220_micro_farad_50_volt': ('RVT1H221M1010', 'C3358', '220 uF', '50 V', '220\n50V'),
    'electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_470_micro_farad_25_volt': ('RVT1E471M1010', 'C3351', '470 uF', '25 V', '470\n25V'),
    'electronic_capacitor_10_mm_diameter_10_2_mm_tall_electrolytic_470_micro_farad_35_volt': ('RVT1V471M1010', 'C3350', '470 uF', '35 V', '470\n35V'),
}

def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed component')
    mpn, supplier, value, voltage, text = PARTS[part]
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'Honor Elec' or record.get('part_number_manufacturer') != mpn
        or record.get('part_number_lcsc') != supplier or e.get('capacitance') != value
        or e.get('rated_voltage') != voltage or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 10.0, 'height': 10.2}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:CP_Elec_10x10'):
        raise ValueError('Identity, voltage, polarity or package changed')
    recipe = copy.deepcopy(recipes[PILOT])
    if (recipe.get('family') != 'aluminum_capacitor' or recipe['model'].get('metal_top_marking') is not True
        or recipe['model'].get('display_scale_xyz') != [1.0, 1.0, 1.02]):
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
