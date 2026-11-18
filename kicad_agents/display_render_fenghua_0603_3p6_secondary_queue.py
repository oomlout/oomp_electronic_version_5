"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch03_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_0805_NEXT_EVIDENCE.md')
PARTS = {'electronic_capacitor_0603_3_6_pico_farad': ('0603CG3R6C500NT','C1661','3.6 pF','C0G','0.25 pF')}
NO_ELECTRICAL = frozenset()


def reviewed_recipe(part, record, recipes, sha):
    if not record.get('electrical') or record['electrical'].get('tolerance'):
        raise ValueError('Expected missing tolerance changed')
    checked = copy.deepcopy(record)
    checked['electrical']['tolerance'] = '±0.25 pF'
    r = base_recipe(part, checked, recipes, sha, parts=PARTS, evidence=EVIDENCE, no_electrical=NO_ELECTRICAL)
    r['appearance_status'] += ' The source record omits tolerance; the secondary listing specifies ±0.25 pF.'
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
