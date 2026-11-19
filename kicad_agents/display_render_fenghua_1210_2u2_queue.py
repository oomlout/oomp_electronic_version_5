"""Prepare the manufacturer-evidenced Fenghua 1210 2.2 µF display pilot."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_1210_2_2_micro_farad'
REFERENCE = 'electronic_capacitor_1206_10_nano_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1210_2U2_EVIDENCE.md')
MODEL = 'Capacitor_SMD.3dshapes/C_1210_3225Metric.step'
MODEL_SHA = 'f8510481c5044113cf49b0fa6dd54ddab9224508bd6808e1afab8ef0cefdefc9'


def reviewed_recipe(record, recipes, sha):
    e = record.get('electrical') or {}
    if (record.get('manufacturer') != 'FH (Guangdong Fenghua Advanced Tech)'
        or record.get('part_number_manufacturer') != '1210B225K500NT'
        or record.get('part_number_lcsc') != 'C1950'
        or e.get('capacitance') != '2.2 uF' or e.get('rated_voltage') != '50 V'
        or 'X7R' not in str(e.get('dielectric')) or '10%' not in str(e.get('tolerance'))
        or e.get('polarized') is not False
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 2.5, 'height': 1.6}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1210_3225Metric'):
        raise ValueError('Selected identity, ratings or 1210 dimensions changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if recipe.get('family') != 'chip_capacitor':
        raise ValueError('Reference family changed')
    recipe['package'] = '1210_imperial_3225_metric'
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[3.2, 2.5, 2.5], sha256=MODEL_SHA,
        display_scale_xyz=[1.0, 1.0, .64])
    recipe['represented_mpn'] = '1210B225K500NT'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Fenghua exact 1210B225K500NT catalogue entry and series table',
        'source_record': f'parts_source/{PART}/working.yaml'}
    recipe['appearance_status'] = ('Generic KiCad 1210 geometry is scaled to the manufacturer-listed nominal 1.6 mm height. Ceramic colour, terminations and unmarked appearance are illustrative.')
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
