"""Prepare reviewed UNI-ROYAL 0603 render recipes from existing records.

This does not render, publish, infer a supplier or change component records.
Only exact catalogue IDs with a matching primary MPN, model footprint and
manufacturer are selected. Unsupported markings are left for separate review.
"""
from __future__ import annotations

import argparse
import copy
from decimal import Decimal
import json
from pathlib import Path
import re

import yaml

from kicad_agents.package_markings import marking_text

ROOT = Path(__file__).resolve().parents[1]
PILOT = 'electronic_resistor_0603_10000_ohm'
RECIPE_FILE = ROOT / 'source_file/display_render/recipes.json'
PART_ID = re.compile(r'electronic_resistor_0603_([1-9][0-9]*)_ohm')
MPN = re.compile(r'0603WAF([0-9]{3})([0-9JKL])T5E')
E24 = {100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300,
       330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910}


def reviewed_recipe(part_id, record, pilot):
    """Return a recipe only if source identity and the reviewed marking rule agree."""
    identifier = PART_ID.fullmatch(part_id)
    manufacturer = str(record.get('manufacturer', '')).upper()
    mpn = str(record.get('part_number_manufacturer', ''))
    manufacturer_part = MPN.fullmatch(mpn)
    if not identifier or not manufacturer_part or 'UNI-ROYAL' not in manufacturer:
        raise ValueError('Needs separately reviewed identity or marking policy')
    ohms = int(identifier.group(1))
    significant_text, exponent_code = manufacturer_part.groups()
    significant = int(significant_text)
    exponent = {'J': -1, 'K': -2, 'L': -3}.get(exponent_code)
    if exponent is None:
        exponent = int(exponent_code)
    if Decimal(significant) * Decimal(10) ** exponent != ohms:
        raise ValueError('Part number and catalogue resistance disagree')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0603_1608Metric':
        raise ValueError('The reviewed KiCad footprint is not selected')
    reference = record.get('oomp_datasheet_common_with')
    source_pages = (record.get('jlcpcb_selection') or {}).get('datasheet_pages') or {}
    reviewed_document = str(source_pages.get('document', '')) if isinstance(source_pages, dict) else ''
    if (reference != 'electronic_resistor_0402_0_ohm'
        and 'UNI-ROYAL Thick Film Chip Resistors data sheet, Feb.12 2019 V.3' not in reviewed_document):
        raise ValueError('The shared manufacturer datasheet has not been linked')
    listed = record.get('manufacturers') or []
    if not any(item.get('part_number') == mpn and 'UNI-ROYAL' in str(item.get('manufacturer', '')).upper()
               for item in listed if isinstance(item, dict)):
        raise ValueError('Primary MPN lacks a matching manufacturer entry')
    recipe = copy.deepcopy(pilot)
    if recipe['family'] != 'chip_resistor' or recipe['marking']['policy'] != 'uniroyal_0603_e96':
        raise ValueError('Unexpected pilot recipe; review before reusing')
    recipe['represented_mpn'] = mpn
    recipe['represented_manufacturer'] = 'UNI-ROYAL'
    marking = recipe['marking']
    marking['resistance_ohm'] = ohms
    marking['tolerance_percent'] = 1
    try:
        code = marking_text(marking)  # Exact E96 values only; do not round.
        marking['evidence']['rule'] = (
            f'Section 4(6): {significant} x 10^{exponent} ohm = {ohms} ohm; '
            f'the E96 code is {code}. Section 2 identifies F as 1% tolerance.')
    except ValueError:
        if significant not in E24 or significant % 10 or not -1 <= exponent < 9:
            raise ValueError('Value is neither exactly E96 nor a supported E24 value')
        code = f'{significant // 10:02d}{exponent + 1}'
        marking.update(policy='verified_literal', text=code, underline=True)
        marking['evidence']['page'] = 4
        marking['evidence']['rule'] = (
            f'Section 4(7): {ohms} ohm is an E24 value outside E96; '
            f'the 5% style code {code} is underlined for 1% tolerance. '
            'Section 2 identifies F as 1% tolerance.')
        marking['appearance_status'] = (
            'Documented underlined code; approximate ink, typeface and placement, '
            'not a photograph or exact production-lot reproduction.')
    marking['evidence']['source_record'] = f'parts_source/{part_id}/working.yaml'
    return recipe, code


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    pilot = recipes[PILOT]
    eligible, skipped = {}, {}
    for directory in sorted((root / 'parts_source').glob('electronic_resistor_0603_*')):
        source = directory / 'working.yaml'
        if not source.is_file() or not (root / 'parts' / directory.name / 'working.yaml').is_file():
            continue
        if directory.name in recipes:
            continue
        try:
            record = yaml.safe_load(source.read_text(encoding='utf-8')) or {}
            recipe, code = reviewed_recipe(directory.name, record, pilot)
            eligible[directory.name] = {'mpn': recipe['represented_mpn'], 'code': code, 'recipe': recipe}
        except (ValueError, TypeError, KeyError) as exc:
            skipped[directory.name] = str(exc)
    return eligible, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true', help='Add eligible recipes; never overwrite existing recipes')
    parser.add_argument('--report', type=Path, help='Write a discovery report outside the recipe registry')
    args = parser.parse_args()
    eligible, skipped = discover()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        report = {'eligible': {key: {'mpn': value['mpn'], 'marking': value['code']}
                               for key, value in eligible.items()}, 'requires_review': skipped}
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for part_id, item in eligible.items():
            if part_id in recipes:
                raise ValueError(f'Recipe appeared during discovery: {part_id}')
            recipes[part_id] = item['recipe']
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} additional verified marking candidates; {len(skipped)} require separate review.')
    for part_id, item in eligible.items():
        suffix = ' (underlined)' if item['recipe']['marking'].get('underline') else ''
        print(part_id, item['mpn'], item['code'] + suffix)


if __name__ == '__main__':
    main()
