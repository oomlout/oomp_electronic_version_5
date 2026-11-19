"""Stage an individually researched Chengx KM 10 x 20 mm display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_radial_km_10x17_pilot_queue import PART as REFERENCE

PART = 'electronic_capacitor_10_mm_diameter_20_mm_tall_electrolytic_2200_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_2200UF_16V_10X20_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'KM228M016G20RR0VH2FP0'
        or record.get('part_number_lcsc') != 'C3328'
        or e.get('capacitance') != '2200 uF' or e.get('rated_voltage') != '16 V'
        or e.get('pin_spacing') != '5.0 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 10.0, 'height': 20.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result.get('represented_mpn') != 'KM477M035G17RR0VH2FP0'
        or result['model'].get('radial_stretch', {}).get('extra_height') != 7.0):
        raise ValueError('Reference model changed')
    result['package'] = 'radial_10x20_pitch5'
    result['model']['radial_stretch']['extra_height'] = 10.0
    result['represented_mpn'] = 'KM228M016G20RR0VH2FP0'
    result['marking'].update(text='2200uF\n16V\nKM 105C', maximum_width_mm=6.0,
        maximum_height_mm=6.0, evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Chengx KM series and LCSC C3328', 'source_record': f'parts_source/{PART}/working.yaml'})
    result['appearance_status'] = ('Illustrative KiCad radial model with the straight sleeve extended to 20 mm; leads and ends remain unchanged. Black sleeve, white print, stripe and finish may differ from the physical part. The supplier temperature rating conflicts with the source record.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest())
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
