"""Prepare explicitly illustrative Yageo RC 0805/1206 generic recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_LARGE_GENERIC_REFERENCES.md')
PARTS = {
    'electronic_resistor_0805_1600_ohm': ('RC0805FR-071K6L', '1601'),
    'electronic_resistor_0805_53600_ohm': ('RC0805FR-0753K6L', '5362'),
    'electronic_resistor_1206_1600_ohm': ('RC1206FR-071K6L', '1601'),
    'electronic_resistor_1206_200000_ohm': ('RC1206FR-07200KL', '2003'),
    'electronic_resistor_1206_20000_ohm': ('RC1206FR-0720KL', '2002'),
    'electronic_resistor_1206_53600_ohm': ('RC1206FR-0753K6L', '5362'),
}
TEMPLATES = {'0805': ('electronic_resistor_0805_1000_ohm', (.95, .48)),
             '1206': ('electronic_resistor_1206_1000_ohm', (1.52, .64))}


def reviewed_recipe(part, record, recipes, evidence_hash):
    match = re.fullmatch(r'electronic_resistor_(0805|1206)_([0-9]+)_ohm', part)
    if not match or part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    size, value = match.groups()
    reference, mark = PARTS[part]
    if Decimal(mark[:3]) * Decimal(10) ** int(mark[3]) != Decimal(value):
        raise ValueError('Marking and nominal value disagree')
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('manufacturers') or record.get('distributors'):
        raise ValueError('Supplier identity changed; review again')
    if (record.get('electrical') or {}).get('tolerance'):
        raise ValueError('Generic tolerance changed; review again')
    metric = {'0805': '2012', '1206': '3216'}[size]
    if record.get('kicad', {}).get('machine_solder') != f'Resistor_SMD:R_{size}_{metric}Metric':
        raise ValueError('Footprint mismatch')
    template, box = TEMPLATES[size]
    recipe = copy.deepcopy(recipes[template])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != size + '_imperial':
        raise ValueError('Unexpected package template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'] = {'policy': 'verified_literal', 'text': mark,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Yageo RC_L specification and exact reference listings (reviewed online)',
            'source_record': f'parts_source/{part}/working.yaml',
            'rule': f'Yageo 1% RC {size} marking {mark} represents {value} ohm.'},
        'maximum_width_mm': box[0], 'maximum_height_mm': box[1], 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented value code; ink, typeface and placement are illustrative.'}
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
        print(part, recipe['represented_mpn'], recipe['marking']['text'])
    print(len(found), 'reviewed visual references')


if __name__ == '__main__':
    main()
