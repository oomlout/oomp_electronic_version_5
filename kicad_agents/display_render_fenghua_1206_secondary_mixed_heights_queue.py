"""Prepare individually evidenced Fenghua 1206 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_1206_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_1206_SECONDARY_MIXED_HEIGHTS_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_3_3_nano_farad': ('1206B332K500NT', 'C1863', '3.3 nF', 'X7R', '10%'),
    'electronic_capacitor_1206_62_pico_farad': ('1206CG620J500NT', 'C1921', '62 pF', 'C0G', '5%'),
    'electronic_capacitor_1206_82_pico_farad': ('1206CG820J500NT', 'C1924', '82 pF', 'C0G', '5%'),
}
MISSING_TOLERANCE = None


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
    height, source_part, expected_scale = {
        'electronic_capacitor_1206_3_3_nano_farad': (1.25, 'electronic_capacitor_1206_470_nano_farad', [1.0, 1.0, .78125]),
        'electronic_capacitor_1206_62_pico_farad': (1.6, 'electronic_capacitor_1206_10_micro_farad_16_volt', None),
        'electronic_capacitor_1206_82_pico_farad': (.8, 'electronic_capacitor_1206_10_nano_farad', [1.0, 1.0, .5]),
    }[part]
    source = recipes[source_part]
    if source['model'].get('expected_bounds_mm') != [3.2, 1.6, 1.6] or source['model'].get('display_scale_xyz') != expected_scale:
        raise ValueError('Unexpected source model')
    r['model'] = copy.deepcopy(source['model'])
    r['marking']['evidence']['document'] = 'Secondary supplier product data reviewed online'
    r['appearance_status'] = (f'Generic KiCad 1206 geometry is {height} mm high, matching the secondary supplier listing. Ceramic colour, terminations and unmarked appearance are illustrative; the manufacturer drawing was not independently accessed.')
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
