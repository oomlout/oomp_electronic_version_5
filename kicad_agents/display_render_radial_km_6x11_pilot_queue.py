"""Stage the individually reviewed Chengx KM 6.3 x 11 mm display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_6_3_mm_diameter_11_mm_tall_electrolytic_10_micro_farad_100_volt'
REFERENCE = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_10UF_100V_6X11_EVIDENCE.md')
MODEL = 'Capacitor_THT.3dshapes/CP_Radial_D6.3mm_P2.50mm.step'
MODEL_SHA = '39dc7bf95fed00917ab20af81ff9e25a70f8d003bc07cffea11840489a11933e'


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'KM106M100E11RR0VH2FP0'
        or record.get('part_number_lcsc') != 'C2029'
        or e.get('capacitance') != '10 uF' or e.get('rated_voltage') != '100 V'
        or e.get('pin_spacing') != '2.5 mm' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 6.3, 'width': 6.3, 'height': 11.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D6.3mm_P2.50mm'):
        raise ValueError('Identity, rating, dimensions or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if result.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('Reference family changed')
    result['package'] = 'radial_6_3x11_pitch2_5'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.3, 6.3, 8.3], sha256=MODEL_SHA,
        radial_stretch={'lower_z': 2.13502085691, 'upper_z': 6.1, 'extra_height': 4.7,
                        'center_xy': [1.25, 0.], 'radius': 3.15, 'tolerance': .05})
    result['represented_mpn'] = 'KM106M100E11RR0VH2FP0'
    result['marking'].update(text='10uF\n100V\nKM 105C', maximum_width_mm=4.1, maximum_height_mm=3.4,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
                  'document': 'Chengx KM series and LCSC C2029', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Value, voltage and series are illustrative; exact printing, logo and production code are unverified.')
    result['appearance_status'] = ('Illustrative KiCad radial model with straight sleeve extended to 11 mm, leaving ends and leads unchanged. Sleeve, stripe, shape and finish may differ. The supplier temperature rating conflicts with the source record.')
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
