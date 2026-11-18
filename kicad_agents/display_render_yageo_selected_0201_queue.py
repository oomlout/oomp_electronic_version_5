"""Prepare explicit Yageo visual references for selected 0201 records with unverified appearance."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0201_SELECTED_REFERENCES.md')
# Exact original selected identity, reference identity, and tolerance.
PARTS = {
    'electronic_resistor_0201_39_ohm': ('HWA CHN', 'HRC0201F39R0CNTO', 'C55098201', '39Ω', 'RC0201FR-0739RL', '1%'),
    'electronic_resistor_0201_270_ohm': ('HWA CHN', 'HRC0201J271 CNTO', 'C55098252', '270Ω', 'RC0201JR-07270RL', '5%'),
    'electronic_resistor_0201_390000_ohm': ('HWA CHN', 'HRC0201J394 CNTO', 'C55098269', '390kΩ', 'RC0201JR-07390KL', '5%'),
    'electronic_resistor_0201_680000_ohm': ('GiantOhm', 'GR0201J680KTAG00', 'C49655543', '680kΩ', 'RC0201JR-07680KL', '5%'),
}


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part not in PARTS:
        raise ValueError('No reviewed reference for this generic ID')
    manufacturer, selected, lcsc, value, reference, tolerance = PARTS[part]
    if record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != selected:
        raise ValueError('Selected supplier identity changed')
    if not any(x.get('manufacturer') == manufacturer and x.get('part_number') == selected
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Selected manufacturer entry missing')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0201_0603Metric':
        raise ValueError('Footprint mismatch')
    pattern = r'(?<![0-9.])' + tolerance[0] + r'(?:\.0+)?\s*%'
    if not any(x.get('key') == 'lcsc' and x.get('part_number') == lcsc and value in str(x.get('product_name', '')) and re.search(pattern, str(x.get('product_name', '')))
               for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Selected supplier tolerance needs review')
    for rating in ((record.get('electrical') or {}).get('tolerance'),
                   ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if rating and not re.search(pattern, str(rating)):
            raise ValueError('Catalogue tolerance conflicts with visual reference')
    recipe = copy.deepcopy(recipes['electronic_resistor_0201_2700_ohm'])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0201_imperial' or recipe.get('marking', {}).get('policy') != 'none':
        raise ValueError('Unexpected reference package')
    recipe.update(represented_manufacturer='YAGEO', represented_mpn=reference)
    recipe['marking'] = {'policy': 'none', 'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
        'document': 'Yageo RC_L 0201 marking specification and exact reference listings (reviewed online)',
        'source_record': f'parts_source/{part}/working.yaml',
        'rule': f'Yageo {reference} is an unmarked 0201 reference with the same nominal value and tolerance.'},
        'appearance_status': 'Yageo RC0201 bodies are unmarked.'}
    recipe['appearance_status'] = (f'Illustrates Yageo {reference}; the selected {manufacturer} {selected} appearance is unverified. '
        'Same nominal value and tolerance do not establish full interchangeability. '
        'Generic KiCad geometry and materials are illustrative.')
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
        print(part, recipe['represented_mpn'])
    print(len(found), 'reviewed visual references')


if __name__ == '__main__':
    main()
