"""Stage the individually reviewed Chengx KS 4 x 7 mm display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_4_mm_diameter_7_mm_tall_electrolytic_33_micro_farad_16_volt'
REFERENCE = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KS_33UF_16V_EVIDENCE.md')
MODEL = 'Capacitor_THT.3dshapes/CP_Radial_D4.0mm_P1.50mm.step'
MODEL_SHA = '0b3df9c2ac243b2ec8cdfd919c97a826f512783901f259a9918ba28836e91262'


def reviewed_recipe(record, recipes, evidence_sha):
    electrical = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'KS336M016C07RR0VH2FP0'
        or record.get('part_number_lcsc') != 'C3314'
        or electrical.get('capacitance') != '33 uF' or electrical.get('rated_voltage') != '16 V'
        or electrical.get('pin_spacing') != '1.5 mm' or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 4.0, 'width': 4.0, 'height': 7.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D4.0mm_P1.50mm'):
        raise ValueError('KS pilot identity, dimensions, polarity or rating changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('Reference family changed')
    recipe['package'] = 'radial_4x7_pitch1_5'
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[4.0, 4.0, 6.0], sha256=MODEL_SHA,
        radial_stretch={'lower_z': 2.105151982969, 'upper_z': 3.8, 'extra_height': 3.0,
                        'center_xy': [.75, 0.0], 'radius': 2.0, 'tolerance': .05},
        flat_top={'center_xy': [.75, 0.0], 'radius': 1.4, 'cutoff_z': 3.5,
                  'disk_z': 3.9, 'segments': 128})
    recipe['represented_mpn'] = 'KS336M016C07RR0VH2FP0'
    recipe['marking'].update(text='33uF\n16V\nKS 105C', maximum_width_mm=2.6,
        maximum_height_mm=2.6,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                  'document': 'Chengx KS336 specification and LCSC C3314',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Value, voltage and series are illustrative; actual ink layout, logo and production code are unverified.')
    recipe['appearance_status'] = ('Illustrative 4 mm KiCad radial model with its straight sleeve extended to 7 mm and its vented metal top replaced by an unvented disk per the manufacturer outline. Black PVC and white ink follow the specification; stripe, top depth, shape and finish are illustrative.')
    return recipe


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
