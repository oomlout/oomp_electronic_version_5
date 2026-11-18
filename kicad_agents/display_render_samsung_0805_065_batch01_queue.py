"""Prepare reviewed Samsung 0.65 mm 0805 illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_065_100pf_queue import PART as PILOT
from kicad_agents.display_render_samsung_0805_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_065_RESEARCH.md')
PARTS = {
    'electronic_capacitor_0805_10_nano_farad': ('CL21B103KBANNNC', 'C1710', '10 nF', '50 V', '10%', 'X7R'),
    'electronic_capacitor_0805_20_pico_farad': ('CL21C200JBANNNC', 'C1798', '20 pF', '50 V', '5%', 'C0G'),
    'electronic_capacitor_0805_22_nano_farad': ('CL21B223KBANNNC', 'C1729', '22 nF', '50 V', '10%', 'X7R'),
}


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    if (record.get('dimensions_mm') or {}).get('height') != 1.25:
        raise ValueError('Reviewed source-height discrepancy changed')
    r = base_recipe(part, record, recipes, sha, parts={p: data[:5] for p, data in PARTS.items()},
                    no_electrical=frozenset(), evidence=EVIDENCE, dielectric=PARTS[part][5])
    if recipes[PILOT]['model'].get('display_scale_xyz') != [1.0, 1.0, .52]:
        raise ValueError('Unexpected thin source model')
    r['model']['display_scale_xyz'] = [1.0, 1.0, .52]
    r['appearance_status'] = ('Generic KiCad 0805 model scaled to the Samsung part’s 0.65 mm nominal height. '
                              'The existing source lists 1.25 mm height and requires catalogue review. '
                              'Shape details, ceramic colour and metallic terminations are illustrative.')
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
