"""Prepare reviewed RALEC RTT05/06 display recipes, without rendering."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RALEC_RTT_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_(0805|1206)_([0-9]+(?:_[0-9]+)?)_ohm(.*)')
PACKAGES = {'0805': ('05', 'electronic_resistor_0805_1000_ohm', 'Resistor_SMD:R_0805_2012Metric'),
            '1206': ('06', 'electronic_resistor_1206_1000_ohm', 'Resistor_SMD:R_1206_3216Metric')}


def marking_value(code, tolerance):
    if len(code) != (4 if tolerance == 'F' else 3):
        raise ValueError('Code length does not match tolerance')
    if re.fullmatch(r'[0-9]+R[0-9]+', code):
        return Decimal(code.replace('R', '.'))
    if not code.isdigit():
        raise ValueError('Unsupported value code')
    return Decimal(code[:-1]) * Decimal(10) ** int(code[-1])


def reviewed_recipe(part_id, record, pilot, evidence_hash):
    ident = PART.fullmatch(part_id)
    if not ident:
        raise ValueError('Unsupported part ID')
    size, number, suffix = ident.groups()
    prefix, _, footprint = PACKAGES[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch('RTT' + prefix + r'([0-9R]{3,4})([FJ])TP', mpn)
    if record.get('manufacturer') != 'RALEC' or not match:
        raise ValueError('Unreviewed primary manufacturer or MPN')
    code, tolerance = match.groups()
    allowed_suffixes = ('', '_ralec_' + mpn.lower()) + (('_5_percent',) if tolerance == 'J' else ())
    if suffix not in allowed_suffixes:
        raise ValueError('Variant ID has a conflicting identity or tolerance')
    value = Decimal(number.replace('_', '.'))
    if not Decimal(1) <= value <= Decimal(27000000) or marking_value(code, tolerance) != value:
        raise ValueError('Value or supported range disagrees with MPN')
    if ('R' in code) != (value < (Decimal(100) if tolerance == 'F' else Decimal(10))):
        raise ValueError('Code is not in the documented decimal or exponent form')
    if record.get('kicad', {}).get('machine_solder') != footprint:
        raise ValueError('Footprint mismatch')
    if not any(isinstance(x, dict) and x.get('manufacturer') == 'RALEC' and x.get('part_number') == mpn
               for x in record.get('manufacturers') or []):
        raise ValueError('Primary manufacturer entry missing')
    if pilot.get('family') != 'chip_resistor' or pilot.get('package') != size + '_imperial':
        raise ValueError('Unexpected package pilot')
    recipe = copy.deepcopy(pilot)
    recipe.update(represented_manufacturer='RALEC', represented_mpn=mpn)
    recipe['marking'].update(policy='verified_literal', text=code,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
                  'document': 'RALEC RTT IE-SP-010 2011 and 2024 (reviewed online)', 'page': 13,
                  'rule': f'RTT{prefix} {"1%" if tolerance == "F" else "5%"} marking {code} represents {value} ohm.',
                  'source_record': f'parts_source/{part_id}/working.yaml'})
    dimension_note = ('KiCad 1206 model is 3.20 mm long, 0.05 mm longer than the manufacturer maximum.'
                      if size == '1206' else 'KiCad 0805 model uses nominal geometry within the listed body tolerances.')
    recipe['appearance_status'] = ('Generic KiCad display geometry with illustrative coating and terminations; '
                                   + dimension_note + ' Represents one supplier choice.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found, skipped = {}, {}
    for size, (_, pilot_id, _) in PACKAGES.items():
        for directory in sorted((ROOT / 'parts_source').glob(f'electronic_resistor_{size}_*')):
            source = directory / 'working.yaml'
            if directory.name in recipes or not source.is_file() or not (ROOT/'parts'/directory.name/'working.yaml').is_file():
                continue
            try:
                found[directory.name] = reviewed_recipe(directory.name, yaml.safe_load(source.read_text(encoding='utf8')) or {},
                                                         recipes[pilot_id], evidence_hash)
            except (ValueError, KeyError, TypeError) as exc:
                skipped[directory.name] = str(exc)
    return found, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    found, skipped = discover()
    if args.add:
        recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
        if any(key in recipes for key in found):
            raise ValueError('Recipe appeared after discovery')
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    print(f'{len(found)} RALEC candidates; {len(skipped)} need other review')
    for key, value in found.items():
        print(key, value['represented_mpn'], value['marking']['text'])

if __name__ == '__main__':
    main()
