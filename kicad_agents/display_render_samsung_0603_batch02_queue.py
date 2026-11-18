"""Prepare individually evidenced Samsung 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0603_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0603_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_15_pico_farad': ('CL10C150JB8NNNC', 'C1644', '15 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_18_pico_farad': ('CL10C180JB8NNNC', 'C1647', '18 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_1_nano_farad': ('CL10B102KB8NNNC', 'C1588', '1 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_20_pico_farad': ('CL10C200JB8NNNC', 'C1648', '20 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_22_pico_farad': ('CL10C220JB8NNNC', 'C1653', '22 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_27_pico_farad': ('CL10C270JB8NNNC', 'C1656', '27 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_33_pico_farad': ('CL10C330JB8NNNC', 'C1663', '33 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_47_pico_farad': ('CL10C470JB8NNNC', 'C1671', '47 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_330_pico_farad': ('CL10C331JB8NNNC', 'C1664', '330 pF', '50 V', 'C0G', '5%'),
}


def reviewed_recipe(part, record, recipes, sha):
    return base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)


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
