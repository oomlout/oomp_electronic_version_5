"""Prepare exact 1206 Y5V illustrations with unverified heights."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_Y5V_UNVERIFIED_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_15_nano_farad': ('1206F153M500NT', 'C1928', '15 nF', 'Y5V', '20%'),
    'electronic_capacitor_1206_22_nano_farad_fenghua_adv_tech_1206f223m500nt': ('1206F223M500NT', 'C1931', '22 nF', 'Y5V', '20%'),
    'electronic_capacitor_1206_33_nano_farad_fenghua_adv_tech_1206f333m500nt': ('1206F333M500NT', 'C1935', '33 nF', 'Y5V', '20%'),
    'electronic_capacitor_1206_150_nano_farad': ('1206F154M500NT', 'C1929', '150 nF', 'Y5V', '20%'),
}


def reviewed_recipe(part, record, recipes, sha):
    result = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Exact supplier identity; exact thickness unverified'
    result['appearance_status'] = ('Generic KiCad 1206 geometry is shown at 0.8 mm height as an illustration; the available manufacturer table does not cover these Y5V parts, so actual thickness is unverified. Ceramic colour, terminations and unmarked appearance are illustrative.')
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
