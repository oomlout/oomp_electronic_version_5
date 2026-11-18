"""Prepare individually evidenced Fenghua 1206 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_BATCH03_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_1_nano_farad': ('1206B102K500NT', 'C1845', '1 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_22_nano_farad': ('1206B223K500NT', 'C1856', '22 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_220_nano_farad': ('1206B224K500NT', 'C1857', '220 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_1_pico_farad': ('1206CG1R0C500NT', 'C1891', '1 pF', 'C0G', '0.25 pF'),
}
MISSING_TOLERANCE = 'electronic_capacitor_1206_1_pico_farad'


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    checked = copy.deepcopy(record)
    electrical = checked.get('electrical') or {}
    if not electrical:
        raise ValueError('Selected electrical data missing')
    missing = part == MISSING_TOLERANCE and not electrical.get('tolerance')
    if missing:
        electrical['tolerance'] = '0.25 pF'
    checked['electrical'] = electrical
    r = base_recipe(part, checked, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    if missing:
        r['appearance_status'] += ' The source record omits tolerance; manufacturer specifies ±0.25 pF.'
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
