"""Prepare strictly reviewed Fenghua RS-06 5% E24 1206 display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, E24

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_RS_1206_EVIDENCE.md')


def reviewed_recipe(part, record, recipes, evidence_hash):
    identity = re.fullmatch(r'electronic_resistor_1206_([0-9]+)_ohm', part)
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(r'RS-06K([0-9]{3})JT', mpn)
    if not identity or not match or record.get('manufacturer') != 'FH (Guangdong Fenghua Advanced Tech)':
        raise ValueError('Unreviewed part identity')
    code = match.group(1)
    value = Decimal(identity.group(1))
    if int(code[:2]) * 10 not in E24 or Decimal(code[:2]) * Decimal(10) ** int(code[2]) != value:
        raise ValueError('Resistance or E24 mismatch')
    if not Decimal(100) <= value <= Decimal(1000000):
        raise ValueError('Value outside reviewed K coefficient range')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_1206_3216Metric':
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == record['manufacturer'] and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    ratings = (record.get('jlcpcb_selection') or {}).get('ratings') or {}
    for rating in ((record.get('electrical') or {}).get('tolerance'), ratings.get('Tolerance')):
        if not rating or not re.search(r'(?<![0-9.])5\s*%', str(rating)):
            raise ValueError('Both selected supplier and catalogue must confirm 5%')
    if not record.get('part_number_lcsc'):
        raise ValueError('Selected supplier code missing')
    recipe = copy.deepcopy(recipes['electronic_resistor_1206_1200000_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '1206_imperial':
        raise ValueError('Unexpected 1206 template')
    recipe.update(represented_manufacturer='FH', represented_mpn=mpn)
    recipe['marking'] = {'policy': 'verified_literal', 'text': code,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Fenghua RC/RS approval sheet R-6.1, pages 4 and 7 (reviewed online)',
            'source_record': f'parts_source/{part}/working.yaml',
            'rule': f'Fenghua 5% E24 marking {code} represents {value} ohm.'},
        'maximum_width_mm': 1.52, 'maximum_height_mm': .64, 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented Fenghua value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative materials; '
                                   'represents one supplier choice.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for folder in sorted((ROOT / 'parts_source').glob('electronic_resistor_1206_*')):
        if folder.name in recipes or not (folder / 'working.yaml').is_file() or not (ROOT / 'parts' / folder.name / 'working.yaml').is_file():
            continue
        try:
            found[folder.name] = reviewed_recipe(folder.name, yaml.safe_load((folder / 'working.yaml').read_text(encoding='utf8')) or {}, recipes, evidence_hash)
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
        print(part, recipe['represented_mpn'], recipe['marking']['text'])
    print(len(found), 'reviewed candidates')


if __name__ == '__main__':
    main()
