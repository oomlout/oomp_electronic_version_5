"""Prepare reviewed YAGEO RC_L 1% 0805/1206 display recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_small_queue import resistance

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_RC_L_LARGE_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_(0805|1206)_([0-9]+)_ohm')
PACKAGES = {
    '0805': ('electronic_resistor_0805_1000_ohm', 'Resistor_SMD:R_0805_2012Metric', (.95, .48)),
    '1206': ('electronic_resistor_1206_1000_ohm', 'Resistor_SMD:R_1206_3216Metric', (1.52, .64)),
}


def marking(value):
    for exponent in range(8):
        significant = value / (Decimal(10) ** exponent)
        if significant == significant.to_integral_value() and 100 <= significant <= 999:
            return f'{int(significant):03d}{exponent}'
    raise ValueError('Value cannot be encoded as four digits')


def reviewed_recipe(part, record, recipes, evidence_hash):
    match = PART.fullmatch(part)
    if not match:
        raise ValueError('Unsupported ID')
    size, raw = match.groups()
    value = Decimal(raw)
    mpn = str(record.get('part_number_manufacturer', ''))
    code = re.fullmatch('RC' + size + r'FR-07([0-9RKM]+)L', mpn)
    if str(record.get('manufacturer', '')).upper() != 'YAGEO' or not code or resistance(code.group(1)) != value:
        raise ValueError('Manufacturer, MPN, or value mismatch')
    if not Decimal(10) <= value <= Decimal(10000000):
        raise ValueError('Outside reviewed value range')
    pilot, footprint, box = PACKAGES[size]
    if record.get('kicad', {}).get('machine_solder') != footprint:
        raise ValueError('Footprint mismatch')
    if not any(str(x.get('manufacturer', '')).upper() == 'YAGEO' and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Primary manufacturer entry missing')
    if not any('1%' in str(x.get('product_name', '')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier 1% rating missing')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'),
                      ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance is not None and str(tolerance).strip():
            found = re.search(r'(?<![0-9.])([0-9]+(?:\.[0-9]+)?)\s*%', str(tolerance))
            if not found or Decimal(found.group(1)) != 1:
                raise ValueError('Catalogue tolerance conflicts with MPN')
    recipe = copy.deepcopy(recipes[pilot])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != size + '_imperial':
        raise ValueError('Unexpected package template')
    digits = marking(value)
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=mpn)
    recipe['marking'] = {'policy': 'verified_literal', 'text': digits,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'YAGEO RC_L product specification V.10 (reviewed online)', 'page': 3,
            'rule': f'1% four-digit marking {digits} represents {value} ohm.',
            'source_record': f'parts_source/{part}/working.yaml'},
        'maximum_width_mm': box[0], 'maximum_height_mm': box[1], 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = 'Generic KiCad nominal package with illustrative materials; represents one supplier choice.'
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for size in PACKAGES:
        for folder in sorted((ROOT / 'parts_source').glob(f'electronic_resistor_{size}_*')):
            source = folder / 'working.yaml'
            if folder.name in recipes or not source.is_file() or not (ROOT / 'parts' / folder.name / 'working.yaml').is_file():
                continue
            try:
                found[folder.name] = reviewed_recipe(folder.name, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, evidence_hash)
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
