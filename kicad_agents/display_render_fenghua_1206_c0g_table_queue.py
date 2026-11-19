"""Prepare 1206 C0G illustrations supported by the local Fenghua table."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_C0G_TABLE_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_100_pico_farad': ('1206CG101J500NT', 'C1884', '100 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_470_pico_farad_fenghua_adv_tech_1206cg471j500nt': ('1206CG471J500NT', 'C1917', '470 pF', 'C0G', '5%'),
}


def reviewed_recipe(part, record, recipes, sha):
    result = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Fenghua C0G series table and exact part listing'
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
