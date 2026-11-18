"""Prepare the exact RALEC RTA03-4D303JTP array from its local datasheet."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import RECIPE_FILE, ROOT

PART = 'electronic_resistor_array_4_x_0603_convex_30000_ohm_8_pin'
SOURCE = Path('parts_source') / PART
PILOT = 'electronic_resistor_array_4_x_0603_convex_10000_ohm_8_pin'


def reviewed_recipe(record, pilot, evidence_sha256):
    mpn = 'RTA03-4D303JTP'
    if record.get('manufacturer') != 'RALEC' or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Exact manufacturer or MPN changed')
    if not any(isinstance(item, dict) and item.get('manufacturer') == 'RALEC' and item.get('part_number') == mpn
               for item in record.get('manufacturers') or []):
        raise ValueError('Primary MPN lacks matching manufacturer entry')
    kicad = record.get('kicad', {})
    if (kicad.get('machine_solder') != 'Resistor_SMD:R_Array_Convex_4x0603'
        or kicad.get('symbol') not in ('Device:R_Pack04', 'Device:R_Pack04_Split')):
        raise ValueError('Footprint or four-resistor symbol does not match')
    if pilot.get('package') != '4x0603_convex_8_pin' or pilot.get('family') != 'chip_resistor_array':
        raise ValueError('Unexpected array model')
    recipe = copy.deepcopy(pilot)
    recipe.update(represented_manufacturer='RALEC', represented_mpn=mpn)
    recipe['marking'].update(text='303', evidence={'file': (SOURCE / 'datasheet.pdf').as_posix(),
        'sha256': evidence_sha256, 'page': 14, 'document': 'RALEC RTA chip resistor array specification IE-SP-011',
        'rule': 'RTA03-4D 5% marking 303 represents 30,000 ohm per resistor.',
        'source_record': (SOURCE / 'working.yaml').as_posix()})
    recipe['appearance_status'] = ('Generic KiCad four-resistor array with illustrative ceramic, coating and metal '
                                   'terminations; model size matches manufacturer nominal dimensions.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
    evidence = ROOT / SOURCE / 'datasheet.pdf'
    recipe = reviewed_recipe(yaml.safe_load((ROOT / SOURCE / 'working.yaml').read_text(encoding='utf-8')) or {},
                             recipes[PILOT], hashlib.sha256(evidence.read_bytes()).hexdigest())
    if args.add:
        if PART in recipes:
            raise ValueError('Existing recipe preserved')
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(PART, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
