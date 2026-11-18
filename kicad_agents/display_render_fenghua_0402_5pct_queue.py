"""Find verified unmarked Fenghua RC-02 5% display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0402_5PCT_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_0402_([0-9]+)_ohm(?:_5_percent)?')
MAKERS = {'FH', 'FH (GUANGDONG FENGHUA ADVANCED TECH)'}


def reviewed_recipe(part, record, recipes, evidence_hash):
    ident = PART.fullmatch(part)
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(r'RC-02K([0-9]{3})JT', mpn)
    if not ident or not match or str(record.get('manufacturer', '')).upper() not in MAKERS:
        raise ValueError('Unreviewed identifier, manufacturer or series')
    code = match.group(1)
    value = Decimal(ident.group(1))
    if value != Decimal(code[:2]) * (Decimal(10) ** int(code[2])) or not Decimal(1) <= value <= Decimal(10000000):
        raise ValueError('Value or reviewed range mismatch')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0402_1005Metric':
        raise ValueError('Footprint mismatch')
    if not any(str(x.get('manufacturer', '')).upper() in MAKERS and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    found_rating = False
    ratings = (record.get('jlcpcb_selection') or {}).get('ratings') or {}
    for rating in ((record.get('electrical') or {}).get('tolerance'), ratings.get('Tolerance'), ratings.get('tolerance')):
        if rating is not None and str(rating).strip():
            found = re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%', str(rating))
            if not found or Decimal(found.group(1)) != 5:
                raise ValueError('Catalogue tolerance conflicts with MPN')
            found_rating = True
    if not found_rating:
        raise ValueError('Explicit tolerance needed')
    recipe = copy.deepcopy(recipes['electronic_resistor_0402_1000_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0402_imperial' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Unexpected unmarked source template')
    recipe.update(represented_manufacturer='FH', represented_mpn=mpn)
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Fenghua RC/RS approval sheet R-6.1 (reviewed online)',
        'rule': 'Fenghua RC-02 0402 bodies are unmarked.', 'source_record': f'parts_source/{part}/working.yaml'},
        'appearance_status': 'Fenghua documents RC-02 0402 bodies as unmarked.'}
    recipe['appearance_status'] = ('Generic KiCad nominal package geometry with illustrative materials; '
                                   'represents one supplier choice.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for folder in sorted((ROOT / 'parts_source').glob('electronic_resistor_0402_*')):
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
        print(part, recipe['represented_mpn'])
    print(len(found), 'reviewed candidates')


if __name__ == '__main__':
    main()
