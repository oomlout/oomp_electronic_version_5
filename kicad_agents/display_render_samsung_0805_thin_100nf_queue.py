"""Prepare a height-adapted Samsung 0805 display illustration."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

PART = 'electronic_capacitor_0805_100_nano_farad_samsung_electro_mechanics_cl21b104kbcnnnc'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_THIN_100NF_EVIDENCE.md')
PARTS = {PART: ('CL21B104KBCNNNC', 'C1711', '100 nF', '50 V', '10%')}


def reviewed_recipe(record, recipes, sha):
    r = base_recipe(PART, record, recipes, sha, parts=PARTS, no_electrical=frozenset(), evidence=EVIDENCE, dielectric='X7R')
    r = copy.deepcopy(r)
    r['model']['display_scale_xyz'] = [1.0, 1.0, 0.68]
    r['appearance_status'] = ('Generic KiCad 0805 geometry scaled vertically to the selected Samsung part’s nominal 0.85 mm height; '
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
