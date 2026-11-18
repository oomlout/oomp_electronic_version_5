"""Prepare reviewed RALEC RTT01/02 unmarked display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_ralec_rtt_queue import marking_value

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RALEC_SMALL_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_(0201|0402)_([0-9]+(?:_[0-9]+)?)_ohm')
PACKAGES = {
    '0201': ('01', 'electronic_resistor_0201_0_ohm', 'Resistor_SMD:R_0201_0603Metric'),
    '0402': ('02', 'electronic_resistor_0402_1000_ohm', 'Resistor_SMD:R_0402_1005Metric'),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    ident = PART.fullmatch(part)
    if not ident:
        raise ValueError('Unsupported exact part ID')
    size, raw = ident.groups()
    prefix, pilot, footprint = PACKAGES[size]
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch('RTT' + prefix + r'([0-9R]{3,4})([FJ])TH', mpn)
    if record.get('manufacturer') != 'RALEC' or not match:
        raise ValueError('Unreviewed manufacturer or MPN')
    code, tolerance = match.groups()
    value = Decimal(raw.replace('_', '.'))
    if marking_value(code, tolerance) != value or not (Decimal(10) if size == '0201' else Decimal(1)) <= value <= Decimal(10000000):
        raise ValueError('Value or reviewed range mismatch')
    if record.get('kicad', {}).get('machine_solder') != footprint:
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == 'RALEC' and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    expected = Decimal(1 if tolerance == 'F' else 5)
    for t in ((record.get('electrical') or {}).get('tolerance'),
              ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance'),
              ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('tolerance')):
        if t is not None and str(t).strip():
            found = re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%', str(t))
            if not found or Decimal(found.group(1)) != expected:
                raise ValueError('Catalogue tolerance conflicts with MPN')
    recipe = copy.deepcopy(recipes[pilot])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != size + '_imperial' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Unexpected unmarked source template')
    recipe.update(represented_manufacturer='RALEC', represented_mpn=mpn)
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'RALEC RTT IE-SP-010, section 9.4 (reviewed online)', 'page': 14,
        'rule': f'RALEC RTT{prefix} bodies have no marking.', 'source_record': f'parts_source/{part}/working.yaml'},
        'appearance_status': f'RALEC documents RTT{prefix} bodies as unmarked.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative materials; '
                                   'represents one supplier choice.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for size in PACKAGES:
        for folder in sorted((ROOT / 'parts_source').glob(f'electronic_resistor_{size}_*')):
            source = folder / 'working.yaml'
            if folder.name in recipes or not source.is_file() or not (ROOT / 'parts' / folder.name / 'working.yaml').is_file():
                continue
            try:
                found[folder.name] = reviewed_recipe(folder.name, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, sha)
            except (ValueError, TypeError, KeyError):
                continue
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
        print(part, recipe['represented_mpn'], 'unmarked')
    print(len(found), 'reviewed candidates')


if __name__ == '__main__':
    main()
