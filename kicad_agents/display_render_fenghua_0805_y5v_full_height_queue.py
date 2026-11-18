"""Prepare individually evidenced Fenghua 0805 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_batch01_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_Y5V_FULL_HEIGHT_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_12_nano_farad_fenghua_adv_tech_0805f123m500nt': ('0805F123M500NT', 'C1763', '12 nF', 'Y5V', '20%'),
    'electronic_capacitor_0805_220_nano_farad_fenghua_adv_tech_0805f224m500nt': ('0805F224M500NT', 'C1770', '220 nF', 'Y5V', '20%'),
    'electronic_capacitor_0805_39_nano_farad': ('0805F393M500NT', 'C1776', '39 nF', 'Y5V', '20%'),
    'electronic_capacitor_0805_470_nano_farad_fenghua_adv_tech_0805f474m500nt': ('0805F474M500NT', 'C1778', '470 nF', 'Y5V', '20%'),
    'electronic_capacitor_0805_68_nano_farad_fenghua_adv_tech_0805f683m500nt': ('0805F683M500NT', 'C1781', '68 nF', 'Y5V', '20%'),
    'electronic_capacitor_0805_82_nano_farad': ('0805F823M500NT', 'C1782', '82 nF', 'Y5V', '20%'),
}


def reviewed_recipe(part, record, recipes, sha):
    import copy
    r = base_recipe(part, record, recipes, sha, parts=PARTS, evidence=EVIDENCE)
    source = recipes['electronic_capacitor_0805_10_micro_farad_16_volt']
    if source['model'].get('expected_bounds_mm') != [2.0, 1.25, 1.25] or source['model'].get('display_scale_xyz'):
        raise ValueError('Unexpected full-height source model')
    r['model'] = copy.deepcopy(source['model'])
    r['marking']['evidence']['document'] = 'Secondary supplier product data reviewed online'
    height = '1.25 mm'
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
