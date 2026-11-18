"""Prepare evidenced Yageo illustrations for unsourced generic 0201 parts."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0201_GENERIC_REFERENCES.md')
PARTS = {
    'electronic_resistor_0201_1600_ohm': 'RC0201FR-071K6L',
    'electronic_resistor_0201_200000_ohm': 'RC0201FR-07200KL',
    'electronic_resistor_0201_20000_ohm': 'RC0201FR-0720KL',
    'electronic_resistor_0201_300_ohm': 'RC0201FR-07300RL',
    'electronic_resistor_0201_53600_ohm': 'RC0201FR-0753K6L',
    'electronic_resistor_0201_8200000_ohm': 'RC0201FR-078M2L',
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('manufacturers') or record.get('distributors'):
        raise ValueError('Supplier identity has changed; review again')
    if (record.get('electrical') or {}).get('tolerance'):
        raise ValueError('Generic tolerance has changed; review again')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0201_0603Metric':
        raise ValueError('Footprint mismatch')
    recipe = copy.deepcopy(recipes['electronic_resistor_0201_2700_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0201_imperial' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Unexpected unmarked template')
    reference = PARTS[part]
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Yageo RC_L 0201 specification and exact reference listings (reviewed online)',
        'source_record': f'parts_source/{part}/working.yaml',
        'rule': f'Yageo {reference} is an unmarked 0201 part of the catalogue nominal value.'},
        'appearance_status': 'Yageo RC0201 bodies are unmarked.'}
    recipe['appearance_status'] = (f'Illustrates Yageo {reference}, a 1% example; this generic entry has no selected manufacturer or tolerance. '
                                   'KiCad geometry and materials are illustrative.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for part in PARTS:
        source = ROOT / 'parts_source' / part / 'working.yaml'
        if part not in recipes and source.is_file() and (ROOT / 'parts' / part / 'working.yaml').is_file():
            found[part] = reviewed_recipe(part, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, sha)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    found = discover()
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(part in recipes for part in found):
            raise ValueError('Existing recipe preserved')
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'])
    print(len(found), 'reviewed visual references')


if __name__ == '__main__':
    main()
