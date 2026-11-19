"""Prepare 1206 displays while disclosing unverified exact height."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_UNLISTED_VALUES_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_25_pico_farad': ('1206CG250J500NT', 'C1898', '25 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_36_pico_farad': ('1206CG360J500NT', 'C1908', '36 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_390_pico_farad': ('1206B391K500NT', 'C1866', '390 pF', 'X7R', '10%'),
    'electronic_capacitor_1206_500_pico_farad': ('1206B501K500NT', 'C1873', '500 pF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha):
    result = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Exact supplier identity; manufacturer series table for adjacent values only'
    result['appearance_status'] = ('Generic KiCad 1206 geometry is shown at 0.8 mm height as an illustration; the manufacturer table does not list this exact value, so actual thickness is unverified. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, record, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
