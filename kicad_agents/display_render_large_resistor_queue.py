"""Prepare UNI-ROYAL 0805/1206 1% resistor recipes with four-digit markings.

The KiCad package and the exact existing supplier identity must agree with the
manufacturer datasheet. Ambiguous, decimal-exponent and non-primary supplier
records are left for independent research. No rendering is performed here.
"""
from __future__ import annotations

import argparse
import copy
from decimal import Decimal
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT

PACKAGES = {
    '0805': {'footprint': 'Resistor_SMD:R_0805_2012Metric',
             'model': 'Resistor_SMD.3dshapes/R_0805_2012Metric.step',
             'sha256': 'ded342cdb394fb45395227beaaa75cc390613cf2581b29cd6d22c12abd6103b2',
             'bounds': [2., 1.2, .45], 'mpn_prefix': '0805W8F',
             'marking_box': [.95, .48]},
    '1206': {'footprint': 'Resistor_SMD:R_1206_3216Metric',
             'model': 'Resistor_SMD.3dshapes/R_1206_3216Metric.step',
             'sha256': 'f5d1ea5c47935091292bd1c6c698e0df88d3d4bbf92bf66b4c97e49df5be9ebc',
             'bounds': [3.2, 1.6, .55], 'mpn_prefix': '1206W4F',
             'marking_box': [1.52, .64]},
}
PART = re.compile(r'electronic_resistor_(0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm')


def reviewed_recipe(part_id, record, pilot):
    if pilot.get('family') != 'chip_resistor' or pilot.get('marking', {}).get('policy') != 'uniroyal_0603_e96':
        raise ValueError('Unexpected pilot recipe; review before reusing')
    identifier = PART.fullmatch(part_id)
    if not identifier:
        raise ValueError('Unsupported ID or variant needs separate review')
    size, value = identifier.groups()
    package = PACKAGES[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(re.escape(package['mpn_prefix']) + r'([0-9]{3})([0-9])T[0-9A-Z]E', mpn)
    if not match or 'UNI-ROYAL' not in str(record.get('manufacturer', '')).upper():
        raise ValueError('Manufacturer or exact part number needs separate review')
    significant, exponent = match.groups()
    ohms = Decimal(value.replace('_', '.'))
    if Decimal(significant) * Decimal(10) ** int(exponent) != ohms:
        raise ValueError('Part number and catalogue resistance disagree')
    if ohms != 0 and not Decimal('0.1') <= ohms < Decimal(10000000):
        raise ValueError('Value is outside this datasheet size/tolerance range')
    if record.get('kicad', {}).get('machine_solder') != package['footprint']:
        raise ValueError('The reviewed KiCad footprint is not selected')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and 'UNI-ROYAL' in str(item.get('manufacturer', '')).upper()
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks a matching manufacturer entry')
    code = '0' if ohms == 0 else significant + exponent
    recipe = copy.deepcopy(pilot)
    recipe['package'] = f'{size}_imperial'
    recipe['represented_manufacturer'] = 'UNI-ROYAL'
    recipe['represented_mpn'] = mpn
    model = recipe['model']
    model.update(relative_path=package['model'], sha256=package['sha256'],
                 expected_bounds_mm=package['bounds'], dimension_tolerance_mm=.015,
                 source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + package['model'])
    evidence = copy.deepcopy(recipe['marking']['evidence'])
    rule = ('Section 4(2): a zero-ohm resistor normally carries 0.' if ohms == 0 else
            f'Section 4(4): 1% resistor, first three digits significant, last is the exponent: {code}.')
    evidence.update(page=3, rule=rule, source_record=f'parts_source/{part_id}/working.yaml')
    recipe['marking'] = {'policy': 'verified_literal', 'text': code, 'evidence': evidence,
        'maximum_width_mm': package['marking_box'][0], 'maximum_height_mm': package['marking_box'][1],
        'font_file': 'arialbd.ttf', 'appearance_status':
        'Documented value code; approximate ink, typeface and placement, not a photograph of a production lot.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative ceramic, '
                                   'protective coating and plated terminations; represents one supplier choice.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    eligible, skipped = {}, {}
    for size in PACKAGES:
        for directory in sorted((root / 'parts_source').glob(f'electronic_resistor_{size}_*')):
            source = directory / 'working.yaml'
            if not source.is_file() or not (root / 'parts' / directory.name / 'working.yaml').is_file():
                continue
            if directory.name in recipes:
                continue
            try:
                eligible[directory.name] = reviewed_recipe(directory.name,
                    yaml.safe_load(source.read_text(encoding='utf-8')) or {}, recipes[PILOT])
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
            'marking': value['marking']['text']} for key, value in eligible.items()},
            'requires_review': skipped}, indent=2) + '\n', encoding='utf-8')
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for part_id, recipe in eligible.items():
            if part_id in recipes:
                raise ValueError(f'Recipe appeared during discovery: {part_id}')
            recipes[part_id] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} manufacturer-documented marking candidates; {len(skipped)} require review.')
    for part_id, recipe in eligible.items():
        print(part_id, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
