"""Prepare two 1206 C0G illustrations with unverified exact height."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_LOW_UNLISTED_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_2_pico_farad': ('1206CG2R0C500NT', 'C1901', '2 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_1206_3_pico_farad': ('1206CG3R0C500NT', 'C1911', '3 pF', 'C0G', '0.25 pF'),
}


def reviewed_recipe(part, record, recipes, sha):
    checked = copy.deepcopy(record)
    e = checked.get('electrical') or {}
    missing = not e.get('tolerance')
    if missing:
        e['tolerance'] = '0.25 pF'
    checked['electrical'] = e
    result = base_recipe(part, checked, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    result['marking']['evidence']['document'] = 'Exact supplier identity; Fenghua series table for adjacent values only'
    result['appearance_status'] = ('Generic KiCad 1206 geometry is shown at 0.8 mm height as an illustration; the manufacturer table does not list this exact value, so actual thickness is unverified. Ceramic colour, terminations and unmarked appearance are illustrative.')
    if missing:
        result['appearance_status'] += ' The source record omits tolerance; the supplier lists ±0.25 pF.'
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
