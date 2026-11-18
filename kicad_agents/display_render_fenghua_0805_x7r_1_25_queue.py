"""Prepare individually evidenced Fenghua 0805 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_X7R_1_25_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_5_1_nano_farad': ('0805B512K500NT', 'C1750', '5.1 nF', 'X7R', '10%'),
    'electronic_capacitor_0805_3_3_nano_farad': ('0805B332K500NT', 'C1738', '3.3 nF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha):
    import copy
    r = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    source = recipes['electronic_capacitor_0805_10_micro_farad_16_volt']
    if source['model'].get('expected_bounds_mm') != [2.0, 1.25, 1.25] or source['model'].get('display_scale_xyz'):
        raise ValueError('Unexpected full-height source model')
    r['model'] = copy.deepcopy(source['model'])
    r['marking']['evidence']['document'] = 'Secondary supplier product data reviewed online'
    height = '1.25 mm' if part.endswith('5_1_nano_farad') else '1.20 mm'
    r['appearance_status'] = (f'Generic KiCad 0805 geometry is 1.25 mm high; the secondary supplier lists {height} for the selected part. '
                              'Ceramic colour, terminations and unmarked appearance are illustrative; the manufacturer drawing was not independently accessed.')
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
