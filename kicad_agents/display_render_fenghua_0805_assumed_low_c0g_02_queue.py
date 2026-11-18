"""Prepare low-value Fenghua 0805 illustrations with tolerance disclosure."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_ASSUMED_LOW_C0G_02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_3_pico_farad': ('0805CG3R0C500NT', 'C1810', '3 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0805_3_3_pico_farad': ('0805CG3R3C500NT', 'C1811', '3.3 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0805_3_6_pico_farad': ('0805CG3R6C500NT', 'C1812', '3.6 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0805_4_pico_farad': ('0805CG4R0C500NT', 'C1819', '4 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0805_5_pico_farad': ('0805CG5R0C500NT', 'C1824', '5 pF', 'C0G', '0.25 pF'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    checked = copy.deepcopy(record)
    electrical = checked.get('electrical') or {}
    if not electrical:
        raise ValueError('Selected electrical data missing')
    missing_tolerance = not electrical.get('tolerance')
    if missing_tolerance:
        electrical['tolerance'] = '0.25 pF'
    checked['electrical'] = electrical
    r = base_recipe(part, checked, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    r['marking']['evidence']['document'] = 'Fenghua family specification and supplier listings reviewed online'
    r['appearance_status'] = ('Illustrative KiCad 0805 model at 0.8 mm thickness, one of several thicknesses in the Fenghua family specification. Exact part thickness, ceramic colour, termination finish and marking are not verified.')
    if missing_tolerance:
        r['appearance_status'] += ' The source record omits tolerance; manufacturer family code C indicates ±0.25 pF.'
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
