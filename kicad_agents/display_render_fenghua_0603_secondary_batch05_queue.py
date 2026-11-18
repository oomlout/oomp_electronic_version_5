"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch03_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_SECONDARY_BATCH05_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_300_pico_farad': ('0603B301K500NT','C1610','300 pF','X7R','10%'),
    'electronic_capacitor_0603_330_pico_farad_fenghua_adv_tech_0603b331k500nt': ('0603B331K500NT','C1612','330 pF','X7R','10%'),
    'electronic_capacitor_0603_390_pico_farad': ('0603B391K500NT','C1617','390 pF','X7R','10%'),
    'electronic_capacitor_0603_510_pico_farad': ('0603B511K500NT','C1626','510 pF','X7R','10%'),
    'electronic_capacitor_0603_2_nano_farad': ('0603B202K500NT','C1601','2 nF','X7R','10%'),
}
NO_ELECTRICAL = frozenset()


def reviewed_recipe(part, record, recipes, sha):
    r = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE, no_electrical=NO_ELECTRICAL)
    r['marking']['evidence']['document'] = 'Secondary supplier product data reviewed online'
    r['appearance_status'] += ' Dimensions and ratings were checked against a secondary supplier listing; the original drawing was not independently accessed.'
    return r


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
