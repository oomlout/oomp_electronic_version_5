"""Discover reviewed FOJAN FRC 1% chip resistor display recipes.

Only existing exact primary supplier records are used. Small packages are
documented as unmarked; 0603 E96 and >=100-ohm 0805/1206 use the manufacturer's
documented codes, including middle-character underlines for 0603 E24 exceptions.
Decimal codes, jumpers and ambiguous data remain for separate review.
"""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT, E24
from kicad_agents.display_render_small_resistor_queue import PACKAGES as SMALL
from kicad_agents.display_render_large_resistor_queue import PACKAGES as LARGE
from kicad_agents.package_markings import marking_text

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FOJAN_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_(0201|0402|0603|0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm')
MODEL_0603 = {'footprint': 'Resistor_SMD:R_0603_1608Metric'}


def reviewed_recipe(part_id, record, pilot, evidence_sha256):
    identifier = PART.fullmatch(part_id)
    if not identifier:
        raise ValueError('Unsupported ID or variant')
    size, value = identifier.groups()
    package = (SMALL | LARGE | {'0603': MODEL_0603})[size]
    mpn = str(record.get('part_number_manufacturer', '')).replace(' ', '')
    match = re.fullmatch(r'FRC' + size + r'F([0-9]{3})([0-9])TS', mpn)
    if not match or 'FOJAN' not in str(record.get('manufacturer', '')).upper():
        raise ValueError('Manufacturer, tolerance or exact MPN needs review')
    significant, exponent = match.groups()
    ohms = Decimal(value.replace('_', '.'))
    if ohms == 0 or Decimal(significant) * Decimal(10) ** int(exponent) != ohms:
        raise ValueError('Resistance mismatch or jumper needs review')
    minimum = Decimal(10) if size == '0201' else Decimal(1)
    if not minimum <= ohms <= Decimal(10000000):
        raise ValueError('Value is outside the documented FRC 1% range')
    if record.get('kicad', {}).get('machine_solder') != package['footprint']:
        raise ValueError('The reviewed KiCad footprint is not selected')
    if not any(isinstance(item, dict) and str(item.get('part_number', '')).replace(' ', '') == mpn
               and 'FOJAN' in str(item.get('manufacturer', '')).upper()
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks a matching manufacturer entry')
    if pilot.get('family') != 'chip_resistor' or pilot.get('marking', {}).get('policy') != 'uniroyal_0603_e96':
        raise ValueError('Unexpected pilot recipe')
    recipe = copy.deepcopy(pilot)
    recipe['package'] = f'{size}_imperial'
    recipe['represented_manufacturer'], recipe['represented_mpn'] = 'FOJAN', mpn
    if size != '0603':
        model = recipe['model']
        model.update(relative_path=package['model'], sha256=package['sha256'],
                     expected_bounds_mm=package['bounds'], dimension_tolerance_mm=.015,
                     source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + package['model'])
    evidence = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                'document': 'FOJAN FRC product specification FJ-JS-3001 V2.0 (reviewed online)',
                'source_record': f'parts_source/{part_id}/working.yaml'}
    if size in SMALL:
        recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
        evidence.update(page=8, rule=f'FOJAN FRC marking section: {size} bodies have no value code.')
        recipe['marking'] = {'policy': 'none', 'evidence': evidence,
                             'appearance_status': f'FOJAN documents {size} bodies as unmarked.'}
    elif size == '0603':
        try:
            code = marking_text({'policy': 'uniroyal_0603_e96', 'resistance_ohm': str(ohms),
                                 'evidence': {'document': 'FOJAN E96 table'}})
        except ValueError as exc:
            sig, exp = int(significant), int(exponent)
            if sig not in E24 or sig % 10 or exp + 1 > 9:
                raise ValueError('FOJAN E24 or other marking needs separate review') from exc
            code = f'{sig // 10:02d}{exp + 1}'
            evidence.update(page=59, document='FOJAN FRC catalogue marking table (reviewed online)',
                            rule=f'FOJAN FRC 0603 1% E24 exception: {ohms} ohm uses {code} with an underline under the middle character.')
            recipe['marking'] = {'policy': 'verified_literal', 'text': code, 'underline_character': 1,
                'evidence': evidence, 'maximum_width_mm': .76, 'maximum_height_mm': .32,
                'font_file': 'arialbd.ttf', 'appearance_status':
                'Documented FOJAN E24 exception code with middle-character underline; ink, typeface and placement are illustrative.'}
        else:
            if code[-1] not in 'YXABCDEF':
                raise ValueError('Multiplier outside the FOJAN documented table')
            evidence.update(page=8, rule=f'FOJAN FRC E96 table: {ohms} ohm uses {code}; 1% tolerance.')
            recipe['marking'] = {'policy': 'verified_literal', 'text': code, 'evidence': evidence,
                'maximum_width_mm': .76, 'maximum_height_mm': .32, 'font_file': 'arialbd.ttf',
                'appearance_status': 'Documented FOJAN E96 code; ink, typeface and placement are illustrative.'}
    else:
        if ohms < 100:
            raise ValueError('FOJAN below-100-ohm decimal marking needs separate review')
        code = significant + exponent
        evidence.update(page=8, rule=f'FOJAN FRC 1% marking: {code} represents {ohms} ohm.')
        recipe['marking'] = {'policy': 'verified_literal', 'text': code, 'evidence': evidence,
            'maximum_width_mm': package['marking_box'][0], 'maximum_height_mm': package['marking_box'][1],
            'font_file': 'arialbd.ttf', 'appearance_status':
            'Documented FOJAN value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative ceramic, '
                                   'protective coating and plated terminations; represents one supplier choice.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root/'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    evidence_hash = hashlib.sha256((root/EVIDENCE).read_bytes()).hexdigest()
    eligible, skipped = {}, {}
    for directory in sorted((root/'parts_source').glob('electronic_resistor_*')):
        source = directory/'working.yaml'
        if not source.is_file() or not (root/'parts'/directory.name/'working.yaml').is_file():
            continue
        if directory.name in recipes:
            continue
        try:
            record = yaml.safe_load(source.read_text(encoding='utf-8')) or {}
            recipe = reviewed_recipe(directory.name, record, recipes[PILOT], evidence_hash)
            eligible[directory.name] = recipe
        except (ValueError, TypeError, KeyError) as exc:
            skipped[directory.name] = str(exc)
    return eligible, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    eligible, skipped = discover()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps({'eligible': {key: {'mpn': value['represented_mpn'],
            'marking': value['marking'].get('text', '')} for key, value in eligible.items()},
            'requires_review': skipped}, indent=2) + '\n', encoding='utf-8')
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for part_id, recipe in eligible.items():
            if part_id in recipes:
                raise ValueError(f'Recipe appeared during discovery: {part_id}')
            recipes[part_id] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} FOJAN FRC candidates; {len(skipped)} records need separate review.')
    for part_id, recipe in eligible.items():
        print(part_id, recipe['represented_mpn'], recipe['marking'].get('text', '(unmarked)'))


if __name__ == '__main__':
    main()
