"""Prepare individually evidenced Fenghua 1206 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_10_pico_farad': ('1206CG100J500NT', 'C1883', '10 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_220_pico_farad_fenghua_adv_tech_1206cg221j500nt': ('1206CG221J500NT', 'C1897', '220 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_270_pico_farad': ('1206CG271J500NT', 'C1900', '270 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_330_pico_farad_fenghua_adv_tech_1206cg331j500nt': ('1206CG331J500NT', 'C1907', '330 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_56_pico_farad': ('1206CG560J500NT', 'C1919', '56 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_68_pico_farad': ('1206CG680J500NT', 'C1922', '68 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_2_7_nano_farad': ('1206B272K500NT', 'C1860', '2.7 nF', 'X7R', '10%'),
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
