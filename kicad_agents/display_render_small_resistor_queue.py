"""Prepare source-backed unmarked UNI-ROYAL 0201/0402 resistor recipes.

The manufacturer datasheet says these sizes are not marked (section 4(1)).
No component records, renders or pages are changed by discovery.
"""
from __future__ import annotations

import argparse
import copy
from decimal import Decimal
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT, E24

PACKAGES = {
    '0201': {'footprint': 'Resistor_SMD:R_0201_0603Metric',
             'model': 'Resistor_SMD.3dshapes/R_0201_0603Metric.step',
             'sha256': '33893da67f0e1d523ba6096fc78c9fb67e7770efb072fcf51f480f9365706a1d',
             'bounds': [.6, .3, .23], 'mpn_prefix': '0201WMF'},
    '0402': {'footprint': 'Resistor_SMD:R_0402_1005Metric',
             'model': 'Resistor_SMD.3dshapes/R_0402_1005Metric.step',
             'sha256': '91507e5af4251cb4ef38e04889c9b98da29904432bd83786bba13ae9b605eacb',
             'bounds': [1., .5, .35], 'mpn_prefix': '0402WGF'},
}
PART = re.compile(r'electronic_resistor_(0201|0402)_([0-9]+(?:_[0-9]+)?)_ohm(.*)')


def reviewed_recipe(part_id, record, pilot):
    if pilot.get('family') != 'chip_resistor' or pilot.get('marking', {}).get('policy') != 'uniroyal_0603_e96':
        raise ValueError('Unexpected pilot recipe; review before reusing')
    identifier = PART.fullmatch(part_id)
    if not identifier:
        raise ValueError('Unsupported ID or variant needs separate review')
    size, value, suffix = identifier.groups()
    package = PACKAGES[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(re.escape(package['mpn_prefix']) + r'([0-9]{3})([0-9JKL])T[0-9A-Z]E', mpn)
    five_percent = False
    if not match and size == '0201':
        match = re.fullmatch(r'0201WMJ0([0-9]{2})([0-9JKL])T[0-9A-Z]E', mpn)
        five_percent = bool(match)
    if not match or 'UNI-ROYAL' not in str(record.get('manufacturer', '')).upper():
        raise ValueError('Manufacturer or exact part number needs separate review')
    if suffix not in ('', '_uni_royal_uniroyal_elec_' + mpn.lower()):
        raise ValueError('Variant suffix does not match the selected manufacturer and MPN')
    significant, exponent_code = match.groups()
    if five_percent and int(significant) * 10 not in E24:
        raise ValueError('5% value code is not in the reviewed E24 series')
    expected_tolerance = Decimal(5 if five_percent else 1)
    electrical = record.get('electrical') or {}
    ratings = (record.get('jlcpcb_selection') or {}).get('ratings') or {}
    for tolerance in (electrical.get('tolerance'), ratings.get('Tolerance')):
        if tolerance is not None and str(tolerance).strip():
            parsed = re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%', str(tolerance))
            if not parsed or Decimal(parsed.group(1)) != expected_tolerance:
                raise ValueError('Catalogue tolerance conflicts with the MPN')
    exponent = {'J': -1, 'K': -2, 'L': -3}.get(exponent_code)
    if exponent is None:
        exponent = int(exponent_code)
    ohms = Decimal(value.replace('_', '.'))
    if Decimal(significant) * Decimal(10) ** exponent != ohms:
        raise ValueError('Part number and catalogue resistance disagree')
    if ohms != 0 and not Decimal(1) <= ohms <= Decimal(10000000):
        raise ValueError('Value is outside this datasheet size/tolerance range')
    if record.get('kicad', {}).get('machine_solder') != package['footprint']:
        raise ValueError('The reviewed KiCad footprint is not selected')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and 'UNI-ROYAL' in str(item.get('manufacturer', '')).upper()
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks a matching manufacturer entry')
    recipe = copy.deepcopy(pilot)
    recipe['package'] = f'{size}_imperial'
    recipe['represented_manufacturer'] = 'UNI-ROYAL'
    recipe['represented_mpn'] = mpn
    # The fine bump texture can generate non-finite path samples at tiny scale.
    # The reviewed smooth materials retain the same colours and reflectance.
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    model = recipe['model']
    model.update(relative_path=package['model'], sha256=package['sha256'],
                 expected_bounds_mm=package['bounds'], dimension_tolerance_mm=.015,
                 source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + package['model'])
    evidence = copy.deepcopy(recipe['marking']['evidence'])
    evidence.update(page=3, rule=f'Section 4(1): UNI-ROYAL {size} bodies have no marking.',
                    source_record=f'parts_source/{part_id}/working.yaml')
    recipe['marking'] = {'policy': 'none', 'evidence': evidence,
                         'appearance_status': f'Manufacturer documents {size} bodies as unmarked.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative ceramic, '
                                   'protective coating and plated terminations; represents one supplier choice.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    pilot = recipes[PILOT]
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
                    yaml.safe_load(source.read_text(encoding='utf-8')) or {}, pilot)
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
        args.report.write_text(json.dumps({'eligible': {key: value['represented_mpn'] for key, value in eligible.items()},
                                           'requires_review': skipped}, indent=2) + '\n', encoding='utf-8')
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for part_id, recipe in eligible.items():
            if part_id in recipes:
                raise ValueError(f'Recipe appeared during discovery: {part_id}')
            recipes[part_id] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} manufacturer-documented unmarked candidates; {len(skipped)} require review.')
    for part_id, recipe in eligible.items():
        print(part_id, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
