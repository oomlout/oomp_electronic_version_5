"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch03_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_BATCH05_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_1_5_nano_farad': ('0603B152K500NT', 'C1595', '1.5 nF', 'X7R', '10%'),
    'electronic_capacitor_0603_2_2_nano_farad': ('0603B222K500NT', 'C1604', '2.2 nF', 'X7R', '10%'),
    'electronic_capacitor_0603_4_7_nano_farad': ('0603B472K500NT', 'C53987', '4.7 nF', 'X7R', '10%'),
}
NO_ELECTRICAL = frozenset(['electronic_capacitor_0603_4_7_nano_farad'])


def reviewed_recipe(part, record, recipes, sha):
    return base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE, no_electrical=NO_ELECTRICAL)


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
