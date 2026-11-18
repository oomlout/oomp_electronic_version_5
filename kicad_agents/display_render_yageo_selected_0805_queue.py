"""Prepare explicitly illustrative Yageo RC 0805 recipes for incomplete FOJAN identities."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0805_SELECTED_REFERENCES.md')
PARTS = {
    'electronic_resistor_0805_330000_ohm': ('RC0805JR-07330KL', '334', 'C2907320', '330kΩ'),
    'electronic_resistor_0805_510000_ohm': ('RC0805JR-07510KL', '514', 'C2907332', '510kΩ'),
    'electronic_resistor_0805_820_ohm': ('RC0805JR-07820RL', '821', 'C2933571', '820Ω'),
}
TEMPLATES = {'0805': ('electronic_resistor_0805_1000_ohm', (.95, .48)),
             '1206': ('electronic_resistor_1206_1000_ohm', (1.52, .64))}


def reviewed_recipe(part, record, recipes, evidence_hash):
    match = re.fullmatch(r'electronic_resistor_(0805|1206)_([0-9]+)_ohm', part)
    if not match or part not in PARTS:
        raise ValueError('No reviewed reference for this exact ID')
    size, value = match.groups()
    reference, mark, lcsc, nominal = PARTS[part]
    if Decimal(mark[:2]) * Decimal(10) ** int(mark[2]) != Decimal(value):
        raise ValueError('Marking and nominal value disagree')
    if record.get('manufacturer') != 'FOJAN' or record.get('part_number_manufacturer') != 'TS':
        raise ValueError('Selected identity has changed; review again')
    if not any(x.get('manufacturer') == 'FOJAN' and x.get('part_number') == 'TS' for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Selected manufacturer entry changed')
    if not any(x.get('key') == 'lcsc' and x.get('part_number') == lcsc and nominal in str(x.get('product_name', '')) and '5%' in str(x.get('product_name', '')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Selected supplier value or tolerance changed')
    for tolerance in ((record.get('electrical') or {}).get('tolerance'), ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if tolerance and not re.search(r'(?<![0-9.])5(?:\.0+)?\s*%', str(tolerance)):
            raise ValueError('Explicit tolerance conflicts with reference')
    metric = {'0805': '2012', '1206': '3216'}[size]
    if record.get('kicad', {}).get('machine_solder') != f'Resistor_SMD:R_{size}_{metric}Metric':
        raise ValueError('Footprint mismatch')
    template, box = TEMPLATES[size]
    recipe = copy.deepcopy(recipes[template])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != size + '_imperial':
        raise ValueError('Unexpected package template')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'] = {'policy': 'verified_literal', 'text': mark,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'Yageo RC_L specification and exact reference listings (reviewed online)',
            'source_record': f'parts_source/{part}/working.yaml',
            'rule': f'Yageo 5% RC {size} marking {mark} represents {value} ohm.'},
        'maximum_width_mm': box[0], 'maximum_height_mm': box[1], 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented value code; ink, typeface and placement are illustrative.'}
    recipe['appearance_status'] = (f'Illustrates Yageo {reference}, a 5% example; the selected FOJAN identity is truncated and its appearance unverified. Same nominal value and tolerance do not establish full interchangeability. '
                                   'KiCad geometry and materials are illustrative.')
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {}
    for part in PARTS:
        source = ROOT / 'parts_source' / part / 'working.yaml'
        if part not in recipes and source.is_file() and (ROOT / 'parts' / part / 'working.yaml').is_file():
            found[part] = reviewed_recipe(part, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, sha)
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
    print(len(found), 'reviewed visual references')


if __name__ == '__main__':
    main()
