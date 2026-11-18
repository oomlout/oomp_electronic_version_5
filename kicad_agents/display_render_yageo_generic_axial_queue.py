"""Prepare documented Yageo references for unsourced generic axial entries."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for as five_bands, resistance
from kicad_agents.display_render_yageo_cfr_queue import bands_for as four_bands
from kicad_agents.display_render_huaxing_axial_queue import FOOTPRINT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_AXIAL_GENERIC_REFERENCES.md')
PARTS = {
    'electronic_resistor_quarter_watt_through_hole_1600_ohm': ('CFR-25JB-52-1K6', '1K6', '5%'),
    'electronic_resistor_quarter_watt_through_hole_200000_ohm': ('CFR-25JB-52-200K', '200K', '5%'),
    'electronic_resistor_quarter_watt_through_hole_20000_ohm': ('CFR-25JB-52-20K', '20K', '5%'),
    'electronic_resistor_quarter_watt_through_hole_300_ohm': ('CFR-25JB-52-300R', '300R', '5%'),
    'electronic_resistor_quarter_watt_through_hole_53600_ohm': ('MFR-25FBF52-53K6', '53K6', '1%'),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    ident = re.fullmatch(r'electronic_resistor_quarter_watt_through_hole_([0-9]+)_ohm', part)
    if not ident or part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('manufacturers') or record.get('distributors'):
        raise ValueError('Supplier identity changed; review again')
    if (record.get('electrical') or {}).get('tolerance'):
        raise ValueError('Generic tolerance changed; review again')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Footprint mismatch')
    reference, value_code, tolerance = PARTS[part]
    value = Decimal(ident.group(1))
    if resistance(value_code) != value:
        raise ValueError('Reference value mismatch')
    bands = four_bands(value) if tolerance == '5%' else five_bands(value)
    template = ('electronic_resistor_quarter_watt_through_hole_6800_ohm' if tolerance == '5%'
                else 'electronic_resistor_quarter_watt_through_hole_1000_ohm')
    recipe = copy.deepcopy(recipes[template])
    if recipe.get('family') != 'axial_resistor' or len(recipe.get('marking', {}).get('bands', [])) != len(bands):
        raise ValueError('Unexpected axial template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Yageo CFR/MFR specification and exact reference listings (reviewed online)',
            'source_record': f'parts_source/{part}/working.yaml',
            'rule': f'Yageo {tolerance} code for {value} ohm: ' + ', '.join(bands) + '.'},
        appearance_status='Documented value bands; beige coating, band spacing and shades are illustrative.')
    recipe['appearance_status'] = (f'Illustrates Yageo {reference}, a {tolerance} example; this generic entry has no selected manufacturer or tolerance. '
                                   'Beige KiCad body and bent-lead presentation are illustrative.')
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
