"""Prepare individually evidenced Samsung 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0603_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0402_0603_NEXT_EVIDENCE.md')
PARTS = {
 'electronic_capacitor_0603_10_micro_farad_25_volt_20_percent': ('CL10A106MA8NRNC','C96446','10 uF','25 V','X5R','20%'),
 'electronic_capacitor_0603_22_micro_farad': ('CL10A226MQ8NRNC','C59461','22 uF','6.3 V','X5R','20%'),
 'electronic_capacitor_0603_4_7_micro_farad': ('CL10A475KA8NQNC','C69335','4.7 uF','25 V','X5R','10%'),
 'electronic_capacitor_0603_220_nano_farad_samsung_electro_mechanics_cl10f224zb8nnnc': ('CL10F224ZB8NNNC','C1698','220 nF','50 V','Y5V','-20%~+80%'),
}
NO_ELECTRICAL = frozenset(['electronic_capacitor_0603_22_micro_farad','electronic_capacitor_0603_4_7_micro_farad'])


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
