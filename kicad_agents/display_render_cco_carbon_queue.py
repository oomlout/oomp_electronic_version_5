"""Prepare supplier-verified CCO CF quarter-watt 5% axial recipes."""
import argparse
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_huaxing_axial_queue import PART, FOOTPRINT
from kicad_agents.display_render_yageo_cfr_queue import TEMPLATE, bands_for

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_CCO_CF_IDENTITIES_01.json')
MANUFACTURER = 'CCO(Chian Chia Elec)'


def reviewed_recipe(part, record, recipes, evidence_hash, identities, evidence_path=EVIDENCE):
    identifier = PART.fullmatch(part)
    identity = identities.get(part)
    if not identifier or not identity:
        raise ValueError('No individually reviewed identity')
    mpn = identity['mpn']
    match = re.fullmatch(r'CF1/4W-([0-9]+(?:\.[0-9]+)?)([KM]?)Ω±5% T', mpn)
    if not match or record.get('manufacturer') != MANUFACTURER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Manufacturer or MPN mismatch')
    value = Decimal(identifier.group(1))
    if value != Decimal(match.group(1)) * {'': 1, 'K': 1000, 'M': 1000000}[match.group(2)]:
        raise ValueError('Resistance mismatch')
    if not Decimal(10) <= value <= Decimal(10000000) or record.get('kicad', {}).get('machine_solder') != FOOTPRINT:
        raise ValueError('Unsupported value or footprint')
    if not any(x.get('manufacturer') == MANUFACTURER and x.get('part_number') == mpn
               for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry missing')
    if not any(x.get('part_number') == identity['lcsc'] and '5%' in str(x.get('product_name', ''))
               and '250mW' in str(x.get('product_name', '')) for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier identity or 5% quarter-watt rating missing')
    for t in ((record.get('electrical') or {}).get('tolerance'),
              ((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get('Tolerance')):
        if t is not None and str(t).strip() and not re.search(r'(?<![0-9.])5\s*%', str(t)):
            raise ValueError('Tolerance conflict')
    recipe = copy.deepcopy(recipes[TEMPLATE])
    if recipe.get('family') != 'axial_resistor' or len(recipe.get('marking', {}).get('bands', [])) != 4:
        raise ValueError('Unexpected four-band template')
    bands = bands_for(value)
    recipe.update(represented_manufacturer=MANUFACTURER, represented_mpn=mpn)
    recipe['marking'].update(text=' / '.join(bands), bands=bands,
        evidence={'file': evidence_path.as_posix(), 'sha256': evidence_hash,
                  'document': 'CCO CF manufacturer specification and individual supplier listing (reviewed online)',
                  'supplier_url': identity['url'],
                  'rule': f'5% four-band code for {value} ohm: ' + ', '.join(bands) + '.',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Documented four-band code; stripe spacing and shades are illustrative.')
    recipe['appearance_status'] = ('Generic KiCad axial geometry with bent leads at 7.62 mm pitch. '
        'Traditional beige coating and materials are illustrative.')
    return recipe


def discover(evidence_path=EVIDENCE):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    evidence = ROOT / evidence_path
    identities = {x['part_id']: x for x in json.loads(evidence.read_text(encoding='utf8'))['records']}
    sha = hashlib.sha256(evidence.read_bytes()).hexdigest()
    found = {}
    for part in identities:
        if part in recipes:
            continue
        source = ROOT / 'parts_source' / part / 'working.yaml'
        if not source.is_file() or not (ROOT / 'parts' / part / 'working.yaml').is_file():
            raise ValueError('Missing reviewed record: ' + part)
        found[part] = reviewed_recipe(part, yaml.safe_load(source.read_text(encoding='utf8')) or {}, recipes, sha, identities, evidence_path)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--evidence', type=Path, default=EVIDENCE)
    args = parser.parse_args()
    found = discover(args.evidence)
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
