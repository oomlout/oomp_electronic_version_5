"""Prepare a height-adjusted Fenghua 1206 capacitor illustration."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

PART = 'electronic_capacitor_1206_470_nano_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_470NF_EVIDENCE.md')
PARTS = {PART: ('1206B474K500NT', 'C1871', '470 nF', 'X7R', '10%')}


def reviewed_recipe(record, recipes, sha):
    r = base_recipe(PART, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    r['model']['display_scale_xyz'] = [1.0, 1.0, .78125]
    r['appearance_status'] = ('Generic KiCad 1206 model scaled to the selected Fenghua part’s 1.25 mm nominal height; '
                              'shape details, ceramic colour and metallic terminations are illustrative.')
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
