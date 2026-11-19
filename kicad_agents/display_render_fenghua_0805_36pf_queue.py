"""Prepare an 0805 36 pF illustration with unverified exact height."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import reviewed_recipe as base_recipe

PART = 'electronic_capacitor_0805_36_pico_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_36PF_EVIDENCE.md')
PARTS = {PART: ('0805CG360J500NT', 'C1816', '36 pF', 'C0G', '5%')}


def reviewed_recipe(record, recipes, sha):
    result = base_recipe(PART, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Exact LCSC identity; exact thickness unverified'
    result['appearance_status'] = ('Generic KiCad 0805 geometry is shown at 0.8 mm height as an illustration; the available manufacturer table does not list this exact value, so actual thickness is unverified. Ceramic colour, terminations and unmarked appearance are illustrative.')
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
