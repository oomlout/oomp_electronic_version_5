"""Prepare the individually researched TAJ E 220 µF 16 V display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_7343_avx_e_tantalum_220_micro_farad_16_volt_avx_taje227k016rnej'
REFERENCE = 'electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_16_volt_avx_tajd107k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_E_220UF_16V_EVIDENCE.md')
MODEL = 'Capacitor_Tantalum_SMD.3dshapes/CP_EIA-7343-43_Kemet-X.step'
MODEL_SHA = '6df0b66df244026544264f9a5fd03c989c2dc4c86a42c5fef64c730425f0fd9a'


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('part_number_manufacturer') != 'TAJE227K016RNJ'
        or record.get('part_number_lcsc') != 'C7231'
        or e.get('capacitance') != '220 uF' or e.get('rated_voltage') != '16 V'
        or e.get('case_size') != 'CASE-E-7343-43' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 7.3, 'width': 4.3, 'height': 4.3}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-7343-43_Kemet-X'):
        raise ValueError('Selected identity, rating, polarity or package changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe.get('family') != 'tantalum_capacitor':
        raise ValueError('Reference family changed')
    recipe['package'] = 'tantalum_7343_avx_e'
    model = recipe['model']
    model.update(relative_path=MODEL,
                 source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
                 expected_bounds_mm=[7.6, 4.6, 4.3], sha256=MODEL_SHA,
                 display_scale_xyz=[73/76, 43/46, 41/43])
    recipe['represented_mpn'] = 'TAJE227K016RNJ'
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': '227 C', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.7, 'maximum_height_mm': 1.3, 'offset_x_mm': .45,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': sha,
            'document': 'KYOCERA AVX TAJ series specification and supplier listing',
            'source_record': f'parts_source/{PILOT}/working.yaml'},
        'appearance_status': 'Capacitance and voltage marking are illustrative; actual ink, manufacturer logo, lot code and any higher-rated substitute may differ.'}
    recipe['appearance_status'] = ('Generic KiCad Kemet X-case model scaled in all three dimensions to the TAJ E nominal envelope; yellow body, stripe, shape and metal finish are illustrative. Stripe indicates the positive anode.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PILOT / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(record, recipes, sha)
    if PILOT in recipes and recipes[PILOT] != recipe:
        raise ValueError('Existing pilot differs; review manually')
    if args.add and PILOT not in recipes:
        recipes[PILOT] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PILOT, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
