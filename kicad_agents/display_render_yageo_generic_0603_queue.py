"""Prepare documented Yageo visual references for generic 0603 entries."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.package_markings import marking_text

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0603_GENERIC_REFERENCES.md')
PARTS = {
    'electronic_resistor_0603_1600_ohm': ('RC0603JR-071K6L', '162', '5%'),
    'electronic_resistor_0603_30_ohm': ('RC0603JR-0730RL', '300', '5%'),
    'electronic_resistor_0603_53600_ohm': ('RC0603FR-0753K6L', '71C', '1%'),
    'electronic_resistor_0603_5_6_ohm': ('RC0603JR-075R6L', '5R6', '5%'),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('manufacturers') or record.get('distributors'):
        raise ValueError('Supplier identity changed; review again')
    if (record.get('electrical') or {}).get('tolerance'):
        raise ValueError('Generic tolerance changed; review again')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0603_1608Metric':
        raise ValueError('Footprint mismatch')
    reference, code, tolerance = PARTS[part]
    if tolerance == '1%' and marking_text({'policy': 'uniroyal_0603_e96',
            'resistance_ohm': '53600', 'evidence': {'document': 'Yageo EIA-96'}}) != code:
        raise ValueError('EIA-96 code does not match')
    recipe = copy.deepcopy(recipes['electronic_resistor_0603_59_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0603_imperial':
        raise ValueError('Unexpected 0603 template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'] = {'policy': 'verified_literal', 'text': code,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Yageo marking specification and exact reference listings (reviewed online)',
            'source_record': f'parts_source/{part}/working.yaml',
            'rule': f'Yageo {reference} uses value code {code}.'},
        'maximum_width_mm': .76, 'maximum_height_mm': .32, 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented Yageo value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = (f'Illustrates Yageo {reference}, a {tolerance} example; this generic entry has no selected manufacturer or tolerance. '
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
