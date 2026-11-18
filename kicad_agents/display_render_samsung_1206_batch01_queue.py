"""Prepare individually evidenced unscaled Samsung 1206 illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_1206_10uf_queue import PART as PILOT, MAKER

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_1206_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_1206_100_micro_farad_6_3_volt_20_percent': ('CL31A107MQHNNNE', 'C15008', '100 uF', '6.3 V', 'X5R', '20%'),
    'electronic_capacitor_1206_10_micro_farad': ('CL31A106KBHNNNE', 'C13585', '10 uF', '50 V', 'X5R', '10%'),
    'electronic_capacitor_1206_1_micro_farad': ('CL31B105KBHNNNE', 'C1848', '1 uF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_1206_22_micro_farad': ('CL31A226KAHNNNE', 'C12891', '22 uF', '25 V', 'X5R', '10%'),
    'electronic_capacitor_1206_22_micro_farad_samsung_electro_mechanics_cl31a226kphnnne': ('CL31A226KPHNNNE', 'C5672', '22 uF', '10 V', 'X5R', '10%'),
    'electronic_capacitor_1206_2_2_micro_farad': ('CL31B225KBHNNNE', 'C50254', '2.2 uF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_1206_47_micro_farad': ('CL31A476MPHNNNE', 'C96123', '47 uF', '10 V', 'X5R', '20%'),
    'electronic_capacitor_1206_4_7_micro_farad_25_volt': ('CL31B475KAHNNNE', 'C1872', '4.7 uF', '25 V', 'X7R', '10%'),
    'electronic_capacitor_1206_4_7_micro_farad_samsung_electro_mechanics_cl31a475kohnnne': ('CL31A475KOHNNNE', 'C7237', '4.7 uF', '16 V', 'X5R', '10%'),
}
NO_ELECTRICAL = frozenset(p for p in PARTS if p not in {'electronic_capacitor_1206_1_micro_farad', 'electronic_capacitor_1206_4_7_micro_farad_25_volt'})


def reviewed_recipe(part, record, recipes, sha):
    if part not in PARTS:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, voltage, dielectric, tolerance = PARTS[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_1206_3216Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 3.2 or dims.get('width') != 1.6 or dims.get('height', 1.6) != 1.6:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', voltage), ('dielectric', dielectric), ('tolerance', tolerance)):
        if not electrical and part in NO_ELECTRICAL:
            continue
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '1206_imperial_3216_metric' or 'display_scale_xyz' in r['model']:
        raise ValueError('Unexpected source model')
    r['represented_mpn'] = mpn
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Individual Samsung product pages reviewed online',
                                 'source_record': f'parts_source/{part}/working.yaml'}
    if not electrical:
        r['appearance_status'] += ' The source record lacks electrical fields; ratings were checked against the manufacturer page.'
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
