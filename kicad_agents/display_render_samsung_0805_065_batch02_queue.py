"""Prepare individually evidenced Samsung 0.65 mm 0805 illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_065_100pf_queue import PART as PILOT
from kicad_agents.display_render_samsung_0805_batch01_queue import reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_065_BATCH02_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_22_pico_farad': ('CL21C220JBANNNC', 'C1804', '22 pF', '50 V', '5%', 'C0G'),
    'electronic_capacitor_0805_47_pico_farad': ('CL21C470JBANNNC', 'C14857', '47 pF', '50 V', '5%', 'C0G'),
    'electronic_capacitor_0805_2_2_nano_farad_samsung_electro_mechanics_cl21b222kbannnc': ('CL21B222KBANNNC', 'C1728', '2.2 nF', '50 V', '10%', 'X7R'),
}
NO_ELECTRICAL = frozenset(['electronic_capacitor_0805_47_pico_farad'])


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    dims = record.get('dimensions_mm') or {}
    expected_height = 1.25 if part == 'electronic_capacitor_0805_22_pico_farad' else None
    if dims.get('height') != expected_height:
        raise ValueError('Reviewed source height changed')
    r = base_recipe(part, record, recipes, sha, parts={p: data[:5] for p, data in PARTS.items()},
                    no_electrical=NO_ELECTRICAL, evidence=EVIDENCE, dielectric=PARTS[part][5])
    if recipes[PILOT]['model'].get('display_scale_xyz') != [1.0, 1.0, .52]:
        raise ValueError('Unexpected thin source model')
    r['model']['display_scale_xyz'] = [1.0, 1.0, .52]
    r['appearance_status'] = 'Generic KiCad 0805 model scaled to the Samsung part’s 0.65 mm nominal height. '
    if expected_height:
        r['appearance_status'] += 'The existing source lists 1.25 mm height and requires catalogue review. '
    else:
        r['appearance_status'] += 'The existing source does not specify a height. '
    r['appearance_status'] += 'Shape details, ceramic colour and metallic terminations are illustrative.'
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
