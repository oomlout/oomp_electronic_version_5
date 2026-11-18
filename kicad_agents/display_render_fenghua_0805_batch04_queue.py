"""Prepare individually evidenced Fenghua 0805 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_BATCH04_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_220_pico_farad_fenghua_adv_tech_0805cg221j500nt': ('0805CG221J500NT', 'C1805', '220 pF', 'C0G', '5%'),
    'electronic_capacitor_0805_330_pico_farad_fenghua_adv_tech_0805cg331j500nt': ('0805CG331J500NT', 'C1815', '330 pF', 'C0G', '5%'),
    'electronic_capacitor_0805_330_nano_farad': ('0805B334K500NT', 'C1740', '330 nF', 'X7R', '10%'),
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
