"""Prepare additional individually evidenced Fenghua 0805 illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_3_9_nano_farad': ('0805B392K500NT', 'C1742', '3.9 nF', 'X7R', '10%'),
    'electronic_capacitor_0805_4_7_nano_farad': ('0805B472K500NT', 'C1744', '4.7 nF', 'X7R', '10%'),
    'electronic_capacitor_0805_6_8_nano_farad': ('0805B682K500NT', 'C1755', '6.8 nF', 'X7R', '10%'),
    'electronic_capacitor_0805_8_2_nano_farad': ('0805B822K500NT', 'C1758', '8.2 nF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha):
    dims = {'length': 2.0, 'width': 1.25}
    if part == 'electronic_capacitor_0805_4_7_nano_farad':
        dims['height'] = .8
    return base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE, expected_dims=dims)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {p: reviewed_recipe(p, yaml.safe_load((ROOT / 'parts_source' / p / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for p in PARTS if p not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
