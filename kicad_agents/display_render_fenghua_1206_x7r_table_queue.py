"""Prepare exact 1206 X7R parts supported by the Fenghua series table."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_X7R_TABLE_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_330_pico_farad': ('1206B331K500NT', 'C1862', '330 pF', 'X7R', '10%'),
    'electronic_capacitor_1206_33_nano_farad': ('1206B333K500NT', 'C1864', '33 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_3_9_nano_farad': ('1206B392K500NT', 'C1867', '3.9 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_4_7_nano_farad': ('1206B472K500NT', 'C1869', '4.7 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_560_pico_farad': ('1206B561K500NT', 'C1875', '560 pF', 'X7R', '10%'),
    'electronic_capacitor_1206_56_nano_farad': ('1206B563K500NT', 'C1877', '56 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_5_6_nano_farad': ('1206B562K500NT', 'C1876', '5.6 nF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha):
    result = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Fenghua X7R series table and exact supplier listing'
    result['appearance_status'] = ('Generic KiCad 1206 geometry is scaled to 0.8 mm nominal height from the manufacturer series table, not a part-specific drawing. Ceramic colour, terminations and unmarked appearance are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part in PARTS:
        source = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        recipe = reviewed_recipe(part, source, recipes, sha)
        if part in recipes and recipes[part] != recipe:
            raise ValueError('Existing recipe differs; review manually')
        if args.add:
            recipes[part] = recipe
        print(part, recipe['represented_mpn'])
    if args.add:
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
