"""Prepare individually evidenced 0.85 mm Samsung 0805 illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_thin_100nf_queue import PART as PILOT
from kicad_agents.display_render_samsung_0805_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_THIN_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_1_nano_farad': ('CL21B102KBCNNNC', 'C46653', '1 nF', '50 V', '10%'),
    'electronic_capacitor_0805_47_nano_farad': ('CL21B473KBCNNNC', 'C53134', '47 nF', '50 V', '10%'),
}


def reviewed_recipe(part, record, recipes, sha):
    r = base_recipe(part, record, recipes, sha, parts=PARTS, no_electrical=frozenset(PARTS), evidence=EVIDENCE, dielectric='X7R')
    if recipes[PILOT]['model'].get('display_scale_xyz') != [1.0, 1.0, .68]:
        raise ValueError('Unexpected thin source model')
    r['model']['display_scale_xyz'] = [1.0, 1.0, .68]
    r['appearance_status'] = ('Generic KiCad 0805 geometry scaled vertically to the selected Samsung part’s nominal 0.85 mm height; '
                              'shape details, ceramic colour and metallic terminations are illustrative.')
    if not record.get('electrical'):
        r['appearance_status'] += ' The source record lacks electrical fields; ratings were checked against the manufacturer page.'
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
