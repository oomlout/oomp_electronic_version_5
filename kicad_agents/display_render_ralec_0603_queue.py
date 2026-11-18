"""Prepare the reviewed RALEC RTT03 59-ohm EIAJ-96 display recipe."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.package_markings import marking_text

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RALEC_0603_EVIDENCE.md')
PART = 'electronic_resistor_0603_59_ohm'
MPN = 'RTT0359R0FTP'
TEMPLATE = 'electronic_resistor_0603_102000_ohm'


def reviewed_recipe(part, record, recipes, evidence_hash):
    if part != PART or record.get('manufacturer') != 'RALEC' or record.get('part_number_manufacturer') != MPN:
        raise ValueError('Unreviewed primary identity')
    if record.get('kicad', {}).get('machine_solder') != 'Resistor_SMD:R_0603_1608Metric':
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == 'RALEC' and x.get('part_number') == MPN
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    ratings = (record.get('jlcpcb_selection') or {}).get('ratings') or {}
    if ratings.get('MFR.Part #') != MPN or ratings.get('JLCPCB Part #') != 'C4257' or ratings.get('Resistance') != '59Ω' or '1%' not in str(ratings.get('Tolerance', '')):
        raise ValueError('Supplier value or tolerance missing')
    electrical = record.get('electrical') or {}
    if electrical.get('tolerance') and '1%' not in str(electrical['tolerance']):
        raise ValueError('Tolerance conflict')
    code = marking_text({'policy': 'uniroyal_0603_e96', 'resistance_ohm': '59', 'evidence': {'document': 'RALEC EIAJ-96 table'}})
    if code != '75X':
        raise ValueError('Unexpected EIAJ-96 code')
    recipe = copy.deepcopy(recipes[TEMPLATE])
    if recipe.get('family') != 'chip_resistor' or recipe.get('package') != '0603_imperial':
        raise ValueError('Unexpected package template')
    recipe.update(represented_manufacturer='RALEC', represented_mpn=MPN)
    recipe['marking'] = {'policy': 'verified_literal', 'text': code,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
            'document': 'RALEC RTT IE-SP-010 EIAJ-96 marking table (reviewed online)',
            'rule': 'Code 75 means 590 and X means 0.1: 59 ohm.',
            'source_record': f'parts_source/{part}/working.yaml'},
        'maximum_width_mm': .76, 'maximum_height_mm': .32, 'font_file': 'arialbd.ttf',
        'appearance_status': 'Documented value code; typeface, ink and placement are illustrative.'}
    recipe['appearance_status'] = 'Generic KiCad nominal package with illustrative materials; represents one supplier choice.'
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes:
        print('Already present:', PART)
        return
    source = ROOT / 'parts_source' / PART / 'working.yaml'
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(PART, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, sha)
    if args.add:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'], recipe['marking']['text'])


if __name__ == '__main__':
    main()
