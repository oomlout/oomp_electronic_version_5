"""Discover exact UNI-ROYAL 5% resistor variants with reviewed 3-character marks."""
import argparse
import copy
from decimal import Decimal
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import E24, RECIPE_FILE, ROOT

PART = re.compile(r'electronic_resistor_(0603|0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm_5_percent')
SPECS = {
    '0603': ('0603WAJ', 'electronic_resistor_0603_10000_ohm', 'Resistor_SMD:R_0603_1608Metric', (.76, .32)),
    '0805': ('0805W8J', 'electronic_resistor_0805_1000_ohm', 'Resistor_SMD:R_0805_2012Metric', (.95, .48)),
    '1206': ('1206W4J', 'electronic_resistor_1206_1000_ohm', 'Resistor_SMD:R_1206_3216Metric', (1.52, .64)),
}


def reviewed_recipe(part_id, record, recipes):
    match = PART.fullmatch(part_id)
    if not match:
        raise ValueError('Unsupported exact ID or tolerance variant')
    size, value = match.groups()
    prefix, pilot_id, footprint, box = SPECS[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    code = re.fullmatch(re.escape(prefix) + r'0([0-9]{2})([0-9JKL])T5E', mpn)
    if not code or 'UNI-ROYAL' not in str(record.get('manufacturer', '')).upper():
        raise ValueError('Manufacturer, tolerance or MPN needs review')
    digits, exponent_code = code.groups()
    exponent = {'J': -1, 'K': -2, 'L': -3}.get(exponent_code)
    if exponent is None:
        exponent = int(exponent_code)
    ohms = Decimal(value.replace('_', '.'))
    if Decimal(digits) * Decimal(10) ** exponent != ohms or int(digits) * 10 not in E24:
        raise ValueError('MPN resistance or E24 value disagrees')
    if not Decimal('0.1') <= ohms < Decimal(10000000):
        raise ValueError('Value outside reviewed 5% range')
    if record.get('kicad', {}).get('machine_solder') != footprint:
        raise ValueError('Footprint does not match reviewed package')
    if record.get('oomp_datasheet_common_with') != 'electronic_resistor_0402_0_ohm':
        raise ValueError('Shared manufacturer datasheet is not linked')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and 'UNI-ROYAL' in str(item.get('manufacturer', '')).upper()
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks matching manufacturer entry')
    if exponent >= 0:
        text = digits + str(exponent)
    elif exponent == -1:
        text = digits[0] + 'R' + digits[1]
    else:
        raise ValueError('Low-resistance marking needs separate review')
    recipe = copy.deepcopy(recipes[pilot_id])
    recipe['represented_manufacturer'], recipe['represented_mpn'] = 'UNI-ROYAL', mpn
    evidence = copy.deepcopy(recipes['electronic_resistor_0603_10000_ohm']['marking']['evidence'])
    evidence.update(page=3, rule=f'UNI-ROYAL 5% marking: {ohms} ohm is {text}; R denotes a decimal point.',
                    source_record=f'parts_source/{part_id}/working.yaml')
    recipe['marking'] = {'policy': 'verified_literal', 'text': text, 'evidence': evidence,
                         'maximum_width_mm': box[0], 'maximum_height_mm': box[1], 'font_file': 'arialbd.ttf',
                         'appearance_status': 'Documented 5% value code; ink, typeface and placement are illustrative.'}
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    eligible, skipped = {}, {}
    for directory in sorted((root / 'parts_source').glob('electronic_resistor_*_5_percent')):
        source = directory / 'working.yaml'
        if not source.is_file() or not (root / 'parts' / directory.name / 'working.yaml').is_file() or directory.name in recipes:
            continue
        try:
            eligible[directory.name] = reviewed_recipe(directory.name,
                yaml.safe_load(source.read_text(encoding='utf-8')) or {}, recipes)
        except (ValueError, TypeError, KeyError) as exc:
            skipped[directory.name] = str(exc)
    return eligible, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    eligible, skipped = discover()
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for key, recipe in eligible.items():
            if key in recipes:
                raise ValueError(f'Recipe appeared during discovery: {key}')
            recipes[key] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} UNI-ROYAL 5% candidates; {len(skipped)} other records need review')
    for part, recipe in eligible.items():
        print(part, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
