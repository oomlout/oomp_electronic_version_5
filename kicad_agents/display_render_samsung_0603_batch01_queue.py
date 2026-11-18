"""Prepare individually evidenced Samsung 0603 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0603_BATCH01_EVIDENCE.md')
PILOT = 'electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc'
PARTS = {
    'electronic_capacitor_0603_100_nano_farad_25_volt': ('CL10B104KA8NNNC', 'C1590', '100 nF', '25 V', 'X7R', '10%'),
    'electronic_capacitor_0603_10_nano_farad_samsung_electro_mechanics_cl10b103kb8nnnc': ('CL10B103KB8NNNC', 'C1589', '10 nF', '50 V', 'X7R', '10%'),
    'electronic_capacitor_0603_10_pico_farad': ('CL10C100JB8NNNC', 'C1634', '10 pF', '50 V', 'C0G', '5%'),
}


def reviewed_recipe(part, record, recipes, sha, *, parts=None, evidence=None, allow_missing_electrical=False):
    parts = PARTS if parts is None else parts
    evidence = EVIDENCE if evidence is None else evidence
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, voltage, dielectric, tolerance = parts[part]
    maker = 'Samsung Electro-Mechanics'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 1.6 or dims.get('width') != .8 or dims.get('height', .8) != .8:
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', voltage), ('dielectric', dielectric), ('tolerance', tolerance)):
        if allow_missing_electrical and not electrical:
            continue
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric':
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=maker, represented_mpn=mpn)
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': evidence.as_posix(), 'sha256': sha, 'document': 'Individual Samsung reference specification reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad nominal 0603 MLCC geometry with illustrative ceramic colour and metallic terminations; '
                              'represents the selected Samsung part.')
    if allow_missing_electrical and not electrical:
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
