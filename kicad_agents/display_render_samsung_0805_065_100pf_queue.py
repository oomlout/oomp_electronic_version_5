"""Prepare a selected thin Samsung 0805 display with source-height disclosure."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_batch01_queue import reviewed_recipe as base_recipe

PART = 'electronic_capacitor_0805_100_pico_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_065_RESEARCH.md')
PARTS = {PART: ('CL21C101JBANNNC', 'C1790', '100 pF', '50 V', '5%')}


def reviewed_recipe(record, recipes, sha):
    if (record.get('dimensions_mm') or {}).get('height') != 1.25:
        raise ValueError('Reviewed source-height discrepancy changed')
    r = base_recipe(PART, record, recipes, sha, parts=PARTS, no_electrical=frozenset(), evidence=EVIDENCE, dielectric='C0G')
    r['model']['display_scale_xyz'] = [1.0, 1.0, 0.52]
    r['appearance_status'] = ('Generic KiCad 0805 model scaled to the Samsung part’s 0.65 mm nominal height. '
                              'The existing source lists 1.25 mm height and requires catalogue review. '
                              'Shape details, ceramic colour and metallic terminations are illustrative.')
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes:
        raise ValueError('Existing recipe preserved')
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, sha)
    if args.add:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
