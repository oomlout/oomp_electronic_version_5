"""Prepare individually evidenced Fenghua 0402 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0402_100pf_queue import PART as PILOT, MAKER

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0402_LAST_MIXED_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0402_3_pico_farad': ('0402CG3R0C500NT', 'C1564', '3 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0402_4_pico_farad': ('0402CG4R0C500NT', 'C1568', '4 pF', 'C0G', '0.25 pF'),
    'electronic_capacitor_0402_100_nano_farad_fenghua_adv_tech_0402f104m500nt': ('0402F104M500NT', 'C1581', '100 nF', 'Y5V', '20%'),
    'electronic_capacitor_0402_15_nano_farad': ('0402F153M500NT', 'C1583', '15 nF', 'Y5V', '20%'),
}
NO_ELECTRICAL = frozenset(['electronic_capacitor_0402_3_pico_farad', 'electronic_capacitor_0402_4_pico_farad'])
NO_TOLERANCE = NO_ELECTRICAL
NO_HEIGHT = frozenset(PARTS)


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, dielectric, tolerance = PARTS[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0402_1005Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != ({'length': 1.0, 'width': .5} if part in NO_HEIGHT else {'height': .5, 'length': 1.0, 'width': .5}):
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '50 V'), ('dielectric', dielectric), ('tolerance', tolerance)):
        if not electrical and part in NO_ELECTRICAL:
            continue
        if key == 'tolerance' and part in NO_TOLERANCE and not electrical.get(key):
            continue
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0402_imperial_1005_metric' or 'display_scale_xyz' in r['model']:
        raise ValueError('Unexpected source model')
    r['represented_mpn'] = mpn
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Fenghua family specification and supplier listings reviewed online',
                                'source_record': f'parts_source/{part}/working.yaml'}
    if not electrical:
        r['appearance_status'] += ' The source record lacks electrical fields; ratings were checked against the supplier listing.'
    if part in NO_TOLERANCE:
        r['appearance_status'] += ' The source record omits tolerance; the manufacturer specifies ±0.25 pF.'
    r['appearance_status'] += ' Dimensions use Fenghua 0402 family specifications; exact thickness, colour and marking remain unverified.'
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
