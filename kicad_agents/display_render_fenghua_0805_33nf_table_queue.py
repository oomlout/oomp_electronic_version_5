"""Prepare the individually identified Fenghua 0805 33 nF display."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import reviewed_recipe as base_recipe

PART = 'electronic_capacitor_0805_33_nano_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_33NF_TABLE_EVIDENCE.md')
PARTS = {PART: ('0805B333K500NT', 'C1739', '33 nF', 'X7R', '10%')}


def reviewed_recipe(record, recipes, sha):
    result = base_recipe(PART, record, recipes, sha, parts=PARTS, evidence=EVIDENCE,
                         expected_dims={'length': 2.0, 'width': 1.25, 'height': .8})
    result['marking']['evidence']['document'] = 'Fenghua X7R series table and exact supplier listing'
    result['appearance_status'] = ('Generic KiCad 0805 geometry is scaled to 0.8 mm nominal height from the manufacturer series table, not a part-specific drawing. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


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
