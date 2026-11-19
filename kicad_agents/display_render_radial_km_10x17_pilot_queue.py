"""Stage the reviewed Chengx KM 10 x 17 mm radial display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_10_mm_diameter_17_mm_tall_electrolytic_470_micro_farad_35_volt'
REFERENCE = 'electronic_capacitor_8_mm_diameter_12_mm_tall_electrolytic_100_micro_farad_50_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RADIAL_KM_470UF_35V_10X17_EVIDENCE.md')
MODEL = 'Capacitor_THT.3dshapes/CP_Radial_D10.0mm_P5.00mm.step'
MODEL_SHA = '7367f35dd5439e325ba3912de65e9200831fdc6698080ffd056cd268649ba41d'


def reviewed_recipe(record, recipes, sha):
    electrical = record.get('electrical') or {}
    if (record.get('manufacturer') != 'CX(Dongguan Chengxing Elec)'
        or record.get('part_number_manufacturer') != 'KM477M035G17RR0VH2FP0'
        or record.get('part_number_lcsc') != 'C2064'
        or electrical.get('capacitance') != '470 uF' or electrical.get('rated_voltage') != '35 V'
        or electrical.get('pin_spacing') != '5.0 mm' or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 10.0, 'height': 17.0}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_THT:CP_Radial_D10.0mm_P5.00mm'):
        raise ValueError('Pilot identity, dimensions, rating or polarity changed')
    result = copy.deepcopy(recipes[REFERENCE])
    if result.get('family') != 'radial_aluminum_capacitor':
        raise ValueError('Reference family changed')
    result['package'] = 'radial_10x17_pitch5'
    result['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[10., 10., 12.], sha256=MODEL_SHA,
        radial_stretch={'lower_z': 2.13502085691, 'upper_z': 9.8, 'extra_height': 7.,
                        'center_xy': [2.5, 0.], 'radius': 5., 'tolerance': .05})
    result['represented_mpn'] = 'KM477M035G17RR0VH2FP0'
    result['marking'].update(text='470uF\n35V\nKM 105C', maximum_width_mm=6.0,
        maximum_height_mm=5.5,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': sha,
                  'document': 'Chengx KM series and JLCPCB C2064',
                  'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Value, voltage and series are illustrative; exact printing, logo and production code are unverified.')
    result['appearance_status'] = ('Illustrative KiCad radial model with the straight sleeve extended to 17 mm; leads and ends remain unchanged. Black sleeve, white print, negative stripe, body proportions and finish may differ from the physical part. The supplier temperature rating conflicts with the source record.')
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
