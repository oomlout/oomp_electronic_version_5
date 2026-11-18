"""Prepare individually evidenced Samsung 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0603_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0603_BATCH03_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_220_pico_farad': ('CL10B221KB8NNNC', 'C1603', '220 pF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_3_3_nano_farad': ('CL10B332KB8NNNC', 'C1613', '3.3 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_470_nano_farad': ('CL10B474KA8NNNC', 'C1623', '470 nF', '25 V', 'X7R', '10%'),
    'electronic_capacitor_0603_47_nano_farad': ('CL10B473KB8NNNC', 'C1622', '47 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_270_pico_farad_samsung_electro_mechanics_cl10c271jb8nnnc': ('CL10C271JB8NNNC', 'C1657', '270 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_4_7_nano_farad_samsung_electro_mechanics_cl10b472kb8nnnc': ('CL10B472KB8NNNC', 'C1621', '4.7 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_2_2_micro_farad_10_volt': ('CL10A225KP8NNNC', 'C1607', '2.2 uF', '10 V', 'X5R', '10%'),
    'electronic_capacitor_0603_4_7_micro_farad_10_volt': ('CL10A475KP8NNNC', 'C1705', '4.7 uF', '10 V', 'X5R', '10%'),
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
