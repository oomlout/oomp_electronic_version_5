"""Discover UNI-ROYAL 4D02/4D03 5% four-resistor array recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT

EVIDENCE = Path('parts_source/electronic_resistor_array_4_x_0402_convex_47000_ohm_8_pin/datasheet.pdf')
REFERENCE = 'electronic_resistor_array_4_x_0402_convex_47000_ohm_8_pin'
PART = re.compile(r'electronic_resistor_array_4_x_(0402|0603)_convex_([0-9]+(?:_[0-9]+)?)_ohm_8_pin')
MODELS = {
    '0402': ('02', 'C', 'Resistor_SMD.3dshapes/R_Array_Convex_4x0402.step',
             '36ded1f7b7c9e9dcddde3eb3200acdf1c0e0b60046893660e6f043afc2ec7fad', [1., 2., .35], (1.1, .32)),
    '0603': ('03', '5', 'Resistor_SMD.3dshapes/R_Array_Convex_4x0603.step',
             'bec072c4d44e4c5ff693e18ede4078c7e66e7a670d53b00a20edd2c0aecdf3c2', [1.6, 3.2, .5], (1.75, .5)),
}


def reviewed_recipe(part_id, record, pilot, evidence_sha256):
    identifier = PART.fullmatch(part_id)
    if not identifier:
        raise ValueError('Unsupported exact array ID')
    size, value_string = identifier.groups()
    model_size, packing, model, model_hash, bounds, box = MODELS[size]
    value = Decimal(value_string.replace('_', '.'))
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch('4D' + model_size + r'WGJ0([0-9]{2})([0-9])T' + packing + 'E', mpn)
    if not match or 'UNI-ROYAL' not in str(record.get('manufacturer', '')).upper():
        raise ValueError('Manufacturer, series or tolerance needs review')
    digits, exponent = match.groups()
    expected = Decimal(digits) * (Decimal(10) ** int(exponent))
    minimum = Decimal(10) if size == '0402' else Decimal(1)
    if value != expected or (value != 0 and not minimum <= value <= Decimal(1000000)):
        raise ValueError('Resistance or reviewed datasheet range disagrees')
    if value == 0 and (size != '0603' or digits != '00' or exponent != '0'):
        raise ValueError('Jumper variant needs separate review')
    kicad = record.get('kicad', {})
    if (kicad.get('machine_solder') != 'Resistor_SMD:R_Array_Convex_4x' + size
        or kicad.get('symbol') not in ('Device:R_Pack04', 'Device:R_Pack04_Split')):
        raise ValueError('Footprint or four-resistor symbol does not match')
    if part_id != REFERENCE and record.get('oomp_datasheet_common_with') != REFERENCE:
        raise ValueError('Shared manufacturer datasheet is not linked')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and 'UNI-ROYAL' in str(item.get('manufacturer', '')).upper()
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks matching manufacturer entry')
    if pilot.get('family') != 'chip_resistor':
        raise ValueError('Unexpected source appearance')
    recipe = copy.deepcopy(pilot)
    recipe.update(family='chip_resistor_array', package=f'4x{size}_convex_8_pin',
                  represented_manufacturer='UNI-ROYAL', represented_mpn=mpn)
    recipe['model'].update(relative_path=model, sha256=model_hash, expected_bounds_mm=bounds,
                           dimension_tolerance_mm=.015, copyright='2017 kicad StepUp',
                           license='GPL-3.0-or-later with exception in source STEP header',
                           license_url='https://www.gnu.org/licenses/gpl-3.0.html',
                           source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model)
    text = '0' if value == 0 else digits + exponent
    recipe['marking'] = {'policy': 'verified_literal', 'text': text, 'rotation_degrees': 90,
                         'maximum_width_mm': box[0], 'maximum_height_mm': box[1], 'font_file': 'arialbd.ttf',
                         'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256, 'page': 8,
                                      'document': 'UNI-ROYAL chip resistor array specification JLC-01-015',
                                      'rule': (f'4D{model_size} jumper marking {text} denotes zero ohms.' if value == 0
                                               else f'4D{model_size} 5% array marking {text} represents {value} ohm per resistor.'),
                                      'source_record': f'parts_source/{part_id}/working.yaml'},
                         'appearance_status': 'Manufacturer documents the value code; font, ink and placement are illustrative.'}
    recipe['appearance_status'] = ('Generic KiCad four-resistor array with illustrative ceramic, coating and metal '
                                   'terminations; model size is within the manufacturer dimensional tolerance.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    evidence_hash = hashlib.sha256((root / EVIDENCE).read_bytes()).hexdigest()
    eligible, skipped = {}, {}
    for directory in sorted((root / 'parts_source').glob('electronic_resistor_array_4_x_*_convex_*')):
        source = directory / 'working.yaml'
        if not source.is_file() or not (root / 'parts' / directory.name / 'working.yaml').is_file() or directory.name in recipes:
            continue
        try:
            eligible[directory.name] = reviewed_recipe(directory.name,
                yaml.safe_load(source.read_text(encoding='utf-8')) or {}, recipes[PILOT], evidence_hash)
        except (ValueError, TypeError, KeyError) as exc:
            skipped[directory.name] = str(exc)
    return eligible, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--part')
    args = parser.parse_args()
    eligible, skipped = discover()
    if args.part:
        if args.part not in eligible:
            raise ValueError(f'Part is not an eligible new candidate: {args.part}')
        eligible = {args.part: eligible[args.part]}
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for key, recipe in eligible.items():
            if key in recipes:
                raise ValueError(f'Recipe appeared during discovery: {key}')
            recipes[key] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} UNI-ROYAL array candidates; {len(skipped)} other records need review')
    for part, recipe in eligible.items():
        print(part, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
