"""Prepare UNI-ROYAL references for unsourced 4×0402 arrays."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_ARRAY_0402_REFERENCES.md')
LOCAL_PDF = Path('parts_source/electronic_resistor_array_4_x_0402_convex_47000_ohm_8_pin/datasheet.pdf')
PDF_SHA256 = '6fc9dd06b3e4137a162b71b4057364f43615fd111871d3998918100a604aa0bc'
PARTS = {
    'electronic_resistor_array_4_x_0402_convex_1000000_ohm_8_pin': ('4D02WGJ0105TCE', '105'),
    'electronic_resistor_array_4_x_0402_convex_100000_ohm_8_pin': ('4D02WGJ0104TCE', '104'),
    'electronic_resistor_array_4_x_0402_convex_330_ohm_8_pin': ('4D02WGJ0331TCE', '331'),
    'electronic_resistor_array_4_x_0402_convex_510_ohm_8_pin': ('4D02WGJ0511TCE', '511'),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    ident = re.fullmatch(r'electronic_resistor_array_4_x_0402_convex_([0-9]+)_ohm_8_pin', part)
    if not ident or part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('manufacturers') or record.get('distributors'):
        raise ValueError('Supplier identity changed; review again')
    if (record.get('electrical') or {}).get('tolerance'):
        raise ValueError('Generic tolerance changed; review again')
    kicad = record.get('kicad') or {}
    if kicad.get('machine_solder') not in ('', None, 'Resistor_SMD:R_Array_Convex_4x0402'):
        raise ValueError('Footprint conflicts with reference')
    if record.get('dimensions_mm') != {'length': 2.0, 'width': 1.0}:
        raise ValueError('Source dimensions changed; review again')
    reference, mark = PARTS[part]
    if Decimal(mark[:2]) * Decimal(10) ** int(mark[2]) != Decimal(ident.group(1)):
        raise ValueError('Marking and nominal value disagree')
    if hashlib.sha256((ROOT / LOCAL_PDF).read_bytes()).hexdigest() != PDF_SHA256:
        raise ValueError('Manufacturer specification changed')
    recipe = copy.deepcopy(recipes['electronic_resistor_array_4_x_0402_convex_3300_ohm_8_pin'])
    if recipe.get('family') != 'chip_resistor_array' or recipe.get('package') != '4x0402_convex_8_pin':
        raise ValueError('Unexpected array template')
    recipe.update(represented_manufacturer='UNI-ROYAL', represented_mpn=reference)
    recipe['marking'].update(text=mark, evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'UNI-ROYAL JLC-01-015 array specification and exact reference listings',
        'source_record': f'parts_source/{part}/working.yaml',
        'rule': f'UNI-ROYAL 5% array marking {mark} represents {ident.group(1)} ohm per resistor.'},
        appearance_status='Documented value code; ink, typeface and placement are illustrative.')
    recipe['appearance_status'] = (f'Illustrates UNI-ROYAL {reference}, a 5% example; this generic entry has no selected manufacturer or tolerance. '
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
