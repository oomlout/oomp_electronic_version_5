"""Prepare the reviewed CX KM 4.7 µF, 250 V radial display recipe."""
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
PART = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_4_7_micro_farad_250_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_4_7UF_250V_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    electrical = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'KM475M250F12RR0VH2FP0'
        or record.get('part_number_lcsc') != 'C2775'
        or electrical.get('capacitance') != '4.7 uF'
        or electrical.get('rated_voltage') != '250 V'
        or electrical.get('pin_spacing') != '3.5 mm'
        or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'height': 12.0, 'length': 8.0, 'width': 8.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm'
        or record.get('kicad', {}).get('symbol') != 'Device:C_Polarized'):
        raise ValueError('Review changed identity, value, polarity or dimensions')
    recipe = copy.deepcopy(recipes[PILOT])
    if (recipe.get('family') != 'radial_aluminum_capacitor'
        or recipe.get('represented_mpn') != 'KM107M050F12RR0VH2FP0'
        or recipe['model'].get('radial_stretch', {}).get('extra_height') != 4.0):
        raise ValueError('Pilot recipe changed')
    recipe['represented_mpn'] = 'KM475M250F12RR0VH2FP0'
    recipe['marking']['text'] = '4.7uF\n250V\nKM 105C'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'CX KM series and LCSC C2775 listing',
        'source_record': f'parts_source/{PART}/working.yaml'}
    return recipe


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    source = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(source, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it and review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
