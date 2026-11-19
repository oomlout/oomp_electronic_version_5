"""Prepare an exact manufacturer-evidenced 1206 1 nF display."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

PART = 'electronic_capacitor_1206_1_nano_farad_fenghua_adv_tech_1206cg102j500nt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_1NF_EVIDENCE.md')
PARTS = {PART: ('1206CG102J500NT', 'C1885', '1 nF', 'C0G', '5%')}


def reviewed_recipe(record, recipes, sha):
    result = base_recipe(PART, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Fenghua exact 1206CG102J500NT listing and series table'
    result['appearance_status'] = ('Generic KiCad 1206 geometry is scaled to the manufacturer-listed nominal 0.8 mm height. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    source = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(source, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
