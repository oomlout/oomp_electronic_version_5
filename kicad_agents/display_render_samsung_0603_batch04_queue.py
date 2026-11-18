"""Prepare individually evidenced Samsung 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0603_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0603_BATCH04_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_100_pico_farad': ('CL10C101JB8NNNC', 'C14858', '100 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_12_pico_farad': ('CL10C120JB8NNNC', 'C38523', '12 pF', '50 V', 'C0G', '5%'),
    'electronic_capacitor_0603_22_nano_farad': ('CL10B223KB8NNNC', 'C21122', '22 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_33_nano_farad': ('CL10B333KB8NNNC', 'C21117', '33 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_220_nano_farad': ('CL10B224KA8NNNC', 'C21120', '220 nF', '25 V', 'X7R', '10%'),
    'electronic_capacitor_0603_10_micro_farad': ('CL10A106KP8NNNC', 'C19702', '10 uF', '10 V', 'X5R', '10%'),
    'electronic_capacitor_0603_1_micro_farad_16_volt': ('CL10A105KO8NNNC', 'C1592', '1 uF', '16 V', 'X5R', '10%'),
    'electronic_capacitor_0603_10_micro_farad_6_3_volt_20_percent': ('CL10A106MQ8NNNC', 'C1691', '10 uF', '6.3 V', 'X5R', '20%'),
}
NO_ELECTRICAL = frozenset(list(PARTS)[:6])


def reviewed_recipe(part, record, recipes, sha):
    return base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE,
                       allow_missing_electrical=part in NO_ELECTRICAL)


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
