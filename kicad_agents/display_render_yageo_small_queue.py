"""Discover exact YAGEO RC_L 0201/0402 unmarked resistor recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import PILOT, RECIPE_FILE, ROOT
from kicad_agents.display_render_small_resistor_queue import PACKAGES

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_(0201|0402)_([0-9]+(?:_[0-9]+)?)_ohm')


def resistance(code):
    match = re.fullmatch(r'([0-9]+)([RKM])([0-9]*)', code)
    if not match:
        raise ValueError('Unsupported YAGEO resistance notation')
    integer, unit, fraction = match.groups()
    value = Decimal(integer + ('.' + fraction if fraction else ''))
    return value * {'R': 1, 'K': 1000, 'M': 1000000}[unit]


def reviewed_recipe(part_id, record, pilot, evidence_sha256):
    identifier = PART.fullmatch(part_id)
    if not identifier:
        raise ValueError('Unsupported exact ID or variant')
    size, value = identifier.groups()
    package = PACKAGES[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(r'RC' + size + r'([FJ])R-07([0-9RKM]+)L', mpn)
    if not match or str(record.get('manufacturer', '')).upper() != 'YAGEO':
        raise ValueError('Manufacturer, series, tolerance or MPN needs review')
    tolerance, code = match.groups()
    ohms = Decimal(value.replace('_', '.'))
    if resistance(code) != ohms:
        raise ValueError('Part number and catalogue resistance disagree')
    upper = 22000000 if size == '0402' and tolerance == 'J' else 10000000
    if not Decimal(1) <= ohms <= Decimal(upper):
        raise ValueError('Value outside documented size and tolerance range')
    if record.get('kicad', {}).get('machine_solder') != package['footprint']:
        raise ValueError('Footprint does not match the reviewed package')
    if not any(isinstance(item, dict) and item.get('part_number') == mpn
               and str(item.get('manufacturer', '')).upper() == 'YAGEO'
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks matching manufacturer entry')
    if pilot.get('family') != 'chip_resistor' or pilot.get('marking', {}).get('policy') != 'uniroyal_0603_e96':
        raise ValueError('Unexpected pilot recipe')
    recipe = copy.deepcopy(pilot)
    recipe['package'] = f'{size}_imperial'
    recipe['represented_manufacturer'], recipe['represented_mpn'] = 'YAGEO', mpn
    recipe['disable_bump_for'] = ['coating', 'ceramic', 'termination']
    recipe['model'].update(relative_path=package['model'], sha256=package['sha256'],
                           expected_bounds_mm=package['bounds'], dimension_tolerance_mm=.015,
                           source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + package['model'])
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(),
        'sha256': evidence_sha256, 'document': 'YAGEO RC_L product specification V.12 (reviewed online)',
        'page': 3, 'rule': f'YAGEO RC{size} bodies are unmarked.',
        'source_record': f'parts_source/{part_id}/working.yaml'},
        'appearance_status': f'YAGEO documents RC{size} bodies as unmarked.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative ceramic, '
                                   'protective coating and plated terminations; represents one supplier choice.')
    return recipe


def discover(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    evidence_hash = hashlib.sha256((root / EVIDENCE).read_bytes()).hexdigest()
    eligible, skipped = {}, {}
    for size in PACKAGES:
        for directory in sorted((root / 'parts_source').glob(f'electronic_resistor_{size}_*')):
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
    args = parser.parse_args()
    eligible, skipped = discover()
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
        for key, recipe in eligible.items():
            if key in recipes:
                raise ValueError(f'Recipe appeared during discovery: {key}')
            recipes[key] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(eligible)} YAGEO RC_L candidates; {len(skipped)} other records need review')
    for part, recipe in eligible.items():
        print(part, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
