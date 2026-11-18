"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch03_queue import PILOT, reviewed_recipe as base_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_FRACTIONAL_C0G_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_0_5_pico_farad': ('0603CG0R5C500NT', 'C1633', '0.5 pF'),
    'electronic_capacitor_0603_2_5_pico_farad': ('0603CG2R5C500NT', 'C1652', '2.5 pF'),
    'electronic_capacitor_0603_3_3_pico_farad': ('0603CG3R3C500NT', 'C1660', '3.3 pF'),
    'electronic_capacitor_0603_3_9_pico_farad': ('0603CG3R9C500NT', 'C1662', '3.9 pF'),
    'electronic_capacitor_0603_4_pico_farad': ('0603CG4R0C500NT', 'C1668', '4 pF'),
    'electronic_capacitor_0603_5_pico_farad': ('0603CG5R0C500NT', 'C1673', '5 pF'),
    'electronic_capacitor_0603_6_2_pico_farad': ('0603CG6R2C500NT', 'C1678', '6.2 pF'),
    'electronic_capacitor_0603_7_pico_farad': ('0603CG7R0C500NT', 'C1682', '7 pF'),
}
NO_ELECTRICAL = frozenset()


def reviewed_recipe(part, record, recipes, sha):
    import copy
    if part not in PARTS: raise ValueError('Unreviewed part')
    mpn, lcsc, value = PARTS[part]
    if record.get('manufacturer') != 'FH (Guangdong Fenghua Advanced Tech)' or record.get('part_number_manufacturer') != mpn: raise ValueError('Identity changed')
    if not any(x.get('manufacturer') == record['manufacturer'] and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)): raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)): raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric': raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 1.6 or dims.get('width') != .8 or dims.get('height', .8) != .8: raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '50 V'), ('dielectric', 'C0G')):
        if token not in str(electrical.get(key, '')): raise ValueError(f'{key} changed')
    if electrical.get('tolerance') not in (None, ''): raise ValueError('Source tolerance changed; review required')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric': raise ValueError('Unexpected model')
    r.update(represented_manufacturer=record['manufacturer'], represented_mpn=mpn)
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'source_record': f'parts_source/{part}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad 0603 MLCC illustration; colour and terminations are illustrative. '
                              'The source record omits tolerance; manufacturer family code C indicates ±0.25 pF.')
    r['marking']['evidence']['document'] = 'Fenghua family specification and supplier product data reviewed online'
    r['appearance_status'] += ' Dimensions use the nominal Fenghua 0603 family specification; exact part thickness, finish and marking are not independently verified. Ratings were checked against supplier listings.'
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {p: reviewed_recipe(p, yaml.safe_load((ROOT / 'parts_source' / p / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for p in PARTS if p not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
