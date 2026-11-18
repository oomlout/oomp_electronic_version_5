"""Prepare Huaxing MF 1/4W 1% axial display recipes with five bands."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_yageo_axial_queue import bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_HUAXING_MF_EVIDENCE.md')
PART = re.compile(r'electronic_resistor_quarter_watt_through_hole_([0-9]+)_ohm')
TEMPLATE = 'electronic_resistor_quarter_watt_through_hole_1200_ohm'
FOOTPRINT = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'


def reviewed_recipe(part, record, recipes, evidence_hash):
    identifier = PART.fullmatch(part)
    mpn = str(record.get('part_number_manufacturer', ''))
    match = re.fullmatch(r'MF1/4W-([0-9]+(?:\.[0-9]+)?)([KM]?)Ω±1%T52', mpn)
    if not identifier or not match or record.get('manufacturer') != 'Huaxing Mechanical-Elec.':
        raise ValueError('Unsupported exact part or manufacturer')
    value = Decimal(identifier.group(1))
    stated = Decimal(match.group(1)) * {'': 1, 'K': 1000, 'M': 1000000}[match.group(2)]
    if value != stated or not Decimal(1) <= value <= Decimal(10000000):
        raise ValueError('Resistance or reviewed range mismatch')
    if record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Footprint mismatch')
    if not any(x.get('manufacturer') == 'Huaxing Mechanical-Elec.' and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    if not any('1%' in str(x.get('product_name', '')) and '250mW' in str(x.get('product_name', ''))
               for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier 1% quarter-watt rating missing')
    for t in ((record.get('electrical') or {}).get('tolerance'),
              ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t is not None and str(t).strip() and not re.search(r'(?<![0-9.])1\s*%', str(t)):
            raise ValueError('Tolerance conflict')
    recipe = copy.deepcopy(recipes[TEMPLATE])
    if recipe.get('family') != 'axial_resistor' or recipe.get('package') != 'din0207_horizontal_7_62mm':
        raise ValueError('Unexpected axial template')
    bands = bands_for(value)
    recipe.update(represented_manufacturer='Huaxing Mechanical-Elec.', represented_mpn=mpn)
    recipe['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
                  'document': 'Huaxing MF/RJ specification, sections 4 and 5 (reviewed online)',
                  'rule': f'1% five-band code for {value} ohm: ' + ', '.join(bands) + '.',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Documented five-band code; stripe spacing and shades are illustrative.')
    recipe['appearance_status'] = ('Generic KiCad axial geometry with bent leads at 7.62 mm pitch. '
        'Blue coating is the requested illustrative finish; the Huaxing specification states blue.')
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
