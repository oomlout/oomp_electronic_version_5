"""Review UNI-ROYAL generic and exact-variant IDs omitted by older queues."""
import argparse
import copy
import json
import re
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE, PILOT
from kicad_agents.display_render_uniroyal_five_percent_queue import reviewed_recipe as five_percent
from kicad_agents.display_render_large_resistor_queue import reviewed_recipe as one_percent

CASES = {
    'electronic_resistor_0805_3600_ohm': ('5', '0805W8J0362T5E'),
    'electronic_resistor_1206_12000_ohm': ('5', '1206W4J0123T5E'),
    'electronic_resistor_1206_15000_ohm': ('5', '1206W4J0153T5E'),
    'electronic_resistor_1206_6_8_ohm': ('5', '1206W4J068JT5E'),
    'electronic_resistor_1206_510_ohm': ('5', '1206W4J0511T5E'),
    'electronic_resistor_1206_270_ohm_uni_royal_uniroyal_elec_1206w4f2700t5e': ('1', '1206W4F2700T5E'),
    'electronic_resistor_1206_470_ohm_uni_royal_uniroyal_elec_1206w4f4700t5e': ('1', '1206W4F4700T5E'),
}


def reviewed_recipe(part, record, recipes):
    if part not in CASES:
        raise ValueError('Unreviewed exact ID')
    tolerance, mpn = CASES[part]
    if record.get('part_number_manufacturer') != mpn:
        raise ValueError('Primary MPN differs from reviewed identity')
    if record.get('oomp_datasheet_common_with') != 'electronic_resistor_0402_0_ohm':
        raise ValueError('Manufacturer family datasheet is not linked')
    observed = [(record.get('electrical') or {}).get('tolerance'),
                ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')]
    if not any(x is not None and str(x).strip() for x in observed):
        observed = [x.get('product_name') for x in record.get('distributors', [])
                    if isinstance(x, dict) and x.get('product_name')]
    observed = [str(x) for x in observed if x is not None and str(x).strip()]
    if not observed or any(not re.search(r'(?<![0-9.])' + tolerance + r'\s*%', x) for x in observed):
        raise ValueError('Missing or conflicting catalogue tolerance')
    if tolerance == '5':
        recipe = five_percent(part + '_5_percent', record, recipes)
    else:
        canonical = part.split('_ohm_', 1)[0] + '_ohm'
        recipe = one_percent(canonical, record, recipes[PILOT])
    recipe = copy.deepcopy(recipe)
    recipe['marking']['evidence']['source_record'] = f'parts_source/{part}/working.yaml'
    return recipe


def discover():
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    found = {}
    for part in CASES:
        if part in recipes:
            continue
        source = ROOT / 'parts_source' / part / 'working.yaml'
        if not source.is_file() or not (ROOT / 'parts' / part / 'working.yaml').is_file():
            raise ValueError('Missing reviewed record: ' + part)
        found[part] = reviewed_recipe(part, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes)
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
