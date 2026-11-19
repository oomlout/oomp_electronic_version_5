"""Prepare an example render without choosing a generic part's supplier."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0603_2200_pico_farad'
REFERENCE = 'electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_0603_2200PF_EVIDENCE.md')


def reviewed_recipe(record, recipes, sha):
    if (record.get('name_proper') != 'Capacitor 2200 pF 0603'
        or record.get('dimensions_mm') != {'length': 1.6, 'width': .8}
        or record.get('manufacturers') != [] or record.get('distributors') != []
        or record.get('manufacturer') or record.get('part_number_manufacturer')
        or record.get('electrical')
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric'):
        raise ValueError('Generic identity, package or procurement state changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if (recipe.get('family') != 'chip_capacitor' or recipe.get('package') != '0603_imperial_1608_metric'
        or recipe['model'].get('expected_bounds_mm') != [1.6, .8, .8]
        or recipe['model'].get('display_scale_xyz')):
        raise ValueError('Reference model changed')
    recipe['represented_manufacturer'] = 'FH (Guangdong Fenghua Advanced Tech)'
    recipe['represented_mpn'] = '0603B222K500NT'
    recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha,
        'document': 'Fenghua exact example and JLCPCB listing',
        'source_record': f'parts_source/{PART}/working.yaml'}
    recipe['appearance_status'] = ('Illustrative Fenghua 2.2 nF example for a generic record without a selected supplier or voltage; this does not select procurement or electrical ratings. KiCad shape, ceramic colour, finish and unmarked appearance are illustrative.')
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
