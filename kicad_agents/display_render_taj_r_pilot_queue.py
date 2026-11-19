"""Prepare the individually researched TAJ R 10 µF / 6.3 V display."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_2012_avx_r_tantalum_10_micro_farad_6_3_volt_avx_tajr106m006rnej'
REFERENCE = 'electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_16_volt_avx_tajd107k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_R_10UF_6V3_EVIDENCE.md')
MODEL = 'Capacitor_Tantalum_SMD.3dshapes/CP_EIA-2012-12_Kemet-R.step'
MODEL_SHA = '275d7287aed10aea764beeb4af0b66fa1eb49eeaf05dcd7341232a91dcab8957'


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('part_number_manufacturer') != 'TAJR106M006RNJ'
        or record.get('part_number_lcsc') != 'C7235'
        or e.get('capacitance') != '10 uF' or e.get('rated_voltage') != '6.3 V'
        or e.get('case_size') != 'CASE-R-2012-12' or e.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 2.0, 'width': 1.25, 'height': 1.2}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-2012-12_Kemet-R'):
        raise ValueError('Identity, rating, polarity or R-case package changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe.get('family') != 'tantalum_capacitor':
        raise ValueError('Reference family changed')
    recipe['package'] = 'tantalum_2012_avx_r'
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[2.0, 1.2, 1.2], sha256=MODEL_SHA,
        display_scale_xyz=[2.05/2.0, 1.3/1.2, 1.0])
    recipe['represented_mpn'] = 'TAJR106M006RNJ'
    recipe['marking'] = {'policy': 'illustrative_literal', 'text': 'J\n106', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': .75, 'maximum_height_mm': .65, 'offset_x_mm': .15,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': sha,
            'document': 'KYOCERA AVX TAJ specification and exact supplier listing',
            'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Voltage and capacitance marking layout are illustrative; ink, logo, lot code and any higher-rated substitute may differ.'}
    recipe['appearance_status'] = ('Generic KiCad Kemet R-case model scaled in X and Y to the TAJ nominal envelope; body colour, stripe, shape and metal finish are illustrative. Stripe indicates the positive anode.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(record, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
