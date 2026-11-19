"""Prepare the exact green-and-gold Chengx GR radial display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_1000_micro_farad_10_volt'
REFERENCE = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_GR_1000UF_10V_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'GR108M010F12RR0VL4FP0'
        or record.get('part_number_lcsc') != 'C3299'
        or e.get('capacitance') != '1000 uF' or e.get('rated_voltage') != '10 V'
        or e.get('pin_spacing') != '3.5 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 8., 'width': 8., 'height': 12.}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D8.0mm_P3.50mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'radial_aluminum_capacitor'
        or result['model'].get('radial_stretch', {}).get('extra_height') != 4.):
        raise ValueError('Reviewed 8 x 12 model changed')
    result['represented_mpn'] = 'GR108M010F12RR0VL4FP0'
    result['radial_palette'] = 'green_gold'
    result['marking'].update(text='1000uF\n10V\nGR 105C', maximum_width_mm=5.2,
        maximum_height_mm=3.8, evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Exact Chengx GR specification and LCSC C3299', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Value, voltage and GR marking layout are illustrative; exact typography and production artwork are unverified.')
    result['appearance_status'] = ('Illustrative KiCad radial model with straight sleeve extended to 12 mm. Green sleeve and gold lettering follow the exact manufacturer specification; shades, stripe, proportions and finish are illustrative.')
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
        from kicad_agents.display_render_radial import radial_palette
        radial_palette('green_gold')
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
