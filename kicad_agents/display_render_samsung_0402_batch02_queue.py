"""Prepare individually evidenced Samsung 0402 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0402_100pf_queue import PART as PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0402_BATCH02_EVIDENCE.md')
MAKER = 'Samsung Electro-Mechanics'
PARTS = {
 'electronic_capacitor_0402_100_nano_farad_50_volt': ('CL05B104KB54PNC','C307331','100 nF','50 V','X7R','10%'),
 'electronic_capacitor_0402_1_micro_farad': ('CL05A105KA5NQNC','C52923','1 uF','25 V','X5R','10%'),
 'electronic_capacitor_0402_220_nano_farad': ('CL05B224KO5NNNC','C16772','220 nF','16 V','X7R','10%'),
 'electronic_capacitor_0402_2_2_micro_farad': ('CL05A225MQ5NSNC','C12530','2.2 uF','6.3 V','X5R','20%'),
 'electronic_capacitor_0402_4_7_micro_farad': ('CL05A475KP5NRNC','C368809','4.7 uF','10 V','X5R','10%'),
 'electronic_capacitor_0402_4_7_micro_farad_10_volt_20_percent': ('CL05A475MP5NRNC','C23733','4.7 uF','10 V','X5R','20%'),
}
WITH_HEIGHT = 'electronic_capacitor_0402_4_7_micro_farad_10_volt_20_percent'
NO_ELECTRICAL = frozenset(p for p in PARTS if p not in (WITH_HEIGHT,'electronic_capacitor_0402_100_nano_farad_50_volt'))


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
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0402_1005Metric':
        raise ValueError('Footprint changed')
    dims = {'length': 1.0, 'width': .5}
    if part == WITH_HEIGHT:
        dims['height'] = .5
    if record.get('dimensions_mm') != dims:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    if part == WITH_HEIGHT and electrical.get('temperature_range') != '-55 to +85 C':
        raise ValueError('Temperature range changed')
    for key, token in (('capacitance', value), ('rated_voltage', voltage), ('dielectric', dielectric), ('tolerance', tolerance)):
        if not electrical and part in NO_ELECTRICAL:
            continue
        if token not in str(electrical.get(key, '')).replace('μ', 'u').replace('µ', 'u'):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0402_imperial_1005_metric':
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=MAKER, represented_mpn=mpn)
    r['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': sha, 'document': 'Individual Samsung product pages reviewed online',
                                'source_record': f'parts_source/{part}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad nominal 0402 MLCC geometry matches the selected Samsung part dimensions; '
                              'ceramic colour and metallic terminations are illustrative.')
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
