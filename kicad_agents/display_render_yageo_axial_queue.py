"""Discover exact 1% YAGEO MFR-25 axial resistors and five-band markings."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_AXIAL_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_quarter_watt_through_hole_([0-9]+(?:_[0-9]+)?)_ohm')
MODEL = 'Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.step'
MODEL_HASH = '46710ac36957e4073ef7e80153823ef7db1ea12932074cb71f43bc4b476a74dc'
COLOURS = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')


def resistance(code):
    match = re.fullmatch(r'([0-9]+)([RKM])([0-9]*)', code)
    if not match:
        raise ValueError('Unsupported YAGEO resistance notation')
    integer, unit, fraction = match.groups()
    return Decimal(integer + ('.' + fraction if fraction else '')) * {'R': 1, 'K': 1000, 'M': 1000000}[unit]


def bands_for(value):
    value = Decimal(value)
    for exponent in range(-2, 8):
        significant = value / (Decimal(10) ** exponent)
        if significant == significant.to_integral_value() and 100 <= significant <= 999:
            digits = [COLOURS[int(x)] for x in str(int(significant))]
            multiplier = {-2: 'silver', -1: 'gold'}.get(exponent, COLOURS[exponent] if exponent >= 0 else None)
            return digits + [multiplier, 'brown']
    raise ValueError('Resistance cannot be encoded exactly as five bands')


def reviewed_recipe(part_id, record, pilot, evidence_sha256):
    match = PART.fullmatch(part_id)
    if not match:
        raise ValueError('Unsupported exact axial ID')
    value = Decimal(match.group(1).replace('_', '.'))
    mpn = str(record.get('part_number_manufacturer', ''))
    code = re.fullmatch(r'MFR-25F[TRB][EF]52-([0-9RKM]+)', mpn)
    if not code or str(record.get('manufacturer', '')).upper() != 'YAGEO':
        raise ValueError('Manufacturer, size, tolerance or MPN needs review')
    if resistance(code.group(1)) != value or not Decimal(1) <= value <= Decimal(10000000):
        raise ValueError('Resistance or reviewed range disagrees')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and str(item.get('manufacturer', '')).upper() == 'YAGEO'
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks matching manufacturer entry')
    footprint = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'
    if record.get('kicad', {}).get('machine_solder') != footprint:
        raise ValueError('The reviewed bent-lead footprint is not selected')
    if pilot.get('family') != 'chip_resistor':
        raise ValueError('Unexpected source recipe')
    colours = bands_for(value)
    recipe = copy.deepcopy(pilot)
    recipe.update(family='axial_resistor', package='din0207_horizontal_7_62mm',
                  represented_manufacturer='YAGEO', represented_mpn=mpn)
    recipe['model'].update(relative_path=MODEL, sha256=MODEL_HASH,
        expected_bounds_mm=[8.22, 2.5, 5.5], dimension_tolerance_mm=.02,
        role_by_source_colour={'0.883,0.711,0.492': 'coating', '0.824,0.820,0.781': 'termination'},
        required_roles=['coating', 'termination'], copyright='2017 kicad StepUp',
        license='CC-BY-SA-4.0 with exception in source STEP header',
        license_url='https://creativecommons.org/licenses/by-sa/4.0/',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL)
    recipe['marking'] = {'policy': 'verified_literal', 'text': ' / '.join(colours), 'bands': colours,
        'body_span_mm': [.66, 6.96], 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
        'document': 'YAGEO MFR specification V.0 (reviewed online)', 'page': 14,
        'rule': f'1% five-band code for {value} ohm: ' + ', '.join(colours) + '.',
        'source_record': f'parts_source/{part_id}/working.yaml'},
        'appearance_status': 'The five-band value code is documented; traditional beige coating, stripe spacing and shades are illustrative.'}
    recipe['appearance_status'] = ('Generic KiCad axial package with bent leads at the selected 7.62 mm footprint pitch; '
                                   'body dimensions are within the manufacturer tolerance.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    evidence_hash = hashlib.sha256((root / EVIDENCE).read_bytes()).hexdigest()
    eligible, skipped = {}, {}
    for directory in sorted((root / 'parts_source').glob('electronic_resistor_quarter_watt_through_hole_*')):
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
    print(f'{len(eligible)} YAGEO axial candidates; {len(skipped)} other records need review')
    for part, recipe in eligible.items():
        print(part, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
