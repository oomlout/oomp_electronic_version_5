"""Prepare documented YAGEO CFR-25 5% axial four-band recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import COLOURS, resistance
from kicad_agents.display_render_huaxing_axial_queue import FOOTPRINT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_CFR_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_quarter_watt_through_hole_([0-9]+)_ohm')
TEMPLATE = 'electronic_resistor_quarter_watt_through_hole_6800_ohm'


def bands_for(value):
    for exponent in range(8):
        significant = value / (Decimal(10) ** exponent)
        if significant == significant.to_integral_value() and 10 <= significant <= 99:
            return [COLOURS[int(x)] for x in str(int(significant))] + [COLOURS[exponent], 'gold']
    raise ValueError('Value cannot be represented by reviewed four-band code')


def reviewed_recipe(part, record, recipes, evidence_hash):
    identifier = PART.fullmatch(part)
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(r'CFR-25J[BT]-52-([0-9RKM]+)', mpn)
    if not identifier or not match or record.get('manufacturer') != 'YAGEO':
        raise ValueError('Unsupported exact part or manufacturer')
    value = Decimal(identifier.group(1))
    if resistance(match.group(1)) != value or not Decimal(10) <= value <= Decimal(10000000):
        raise ValueError('Resistance or reviewed range mismatch')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    if not any('5%' in str(x.get('product_name', '')) and '250mW' in str(x.get('product_name', ''))
               for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier 5% quarter-watt rating missing')
    for t in ((record.get('electrical') or {}).get('tolerance'),
              ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t is not None and str(t).strip() and not re.search(r'(?<![0-9.])5\s*%', str(t)):
            raise ValueError('Tolerance conflict')
    recipe = copy.deepcopy(recipes[TEMPLATE])
    if recipe.get('family') != 'axial_resistor' or len(recipe.get('marking', {}).get('bands', [])) != 4:
        raise ValueError('Unexpected four-band template')
    bands = bands_for(value)
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=mpn)
    recipe['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
                  'document': 'YAGEO CFR specification V.0 (reviewed online)', 'page': 14,
                  'rule': f'5% four-band code for {value} ohm: ' + ', '.join(bands) + '.',
                  'source_record': f'parts_source/{part}/working.yaml'})
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for folder in sorted((ROOT / 'parts_source').glob('electronic_resistor_quarter_watt_through_hole_*')):
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
        print(part, recipe['represented_mpn'], recipe['marking']['text'])
    print(len(found), 'reviewed candidates')


if __name__ == '__main__':
    main()
