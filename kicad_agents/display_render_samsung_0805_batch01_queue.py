"""Prepare evidenced Samsung 0805 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_10uf_queue import PART as PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_SAMSUNG_0805_BATCH01_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_22_micro_farad': ('CL21A226MAQNNNE', 'C45783', '22 uF', '25 V', '20%'),
    'electronic_capacitor_0805_22_micro_farad_samsung_electro_mechanics_cl21a226mqqnnne': ('CL21A226MQQNNNE', 'C5674', '22 uF', '6.3 V', '20%'),
    'electronic_capacitor_0805_2_2_micro_farad': ('CL21A225KBQNNNE', 'C377773', '2.2 uF', '50 V', '10%'),
    'electronic_capacitor_0805_4_7_micro_farad': ('CL21A475KAQNNNE', 'C1779', '4.7 uF', '25 V', '10%'),
}
NO_ELECTRICAL = frozenset(list(PARTS)[:3])


def reviewed_recipe(part, record, recipes, sha, *, parts=PARTS, no_electrical=NO_ELECTRICAL, evidence=EVIDENCE, dielectric='X5R'):
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, voltage, tolerance = parts[part]
    maker = 'Samsung Electro-Mechanics'
    if record.get('manufacturer') != maker or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == maker and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 2.0 or dims.get('width') != 1.25 or dims.get('height', 1.25) != 1.25:
        raise ValueError('Dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', voltage), ('dielectric', dielectric), ('tolerance', tolerance)):
        if not electrical and part in no_electrical:
            continue
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric':
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=maker, represented_mpn=mpn)
    r['marking'].update(policy='unmarked_illustration',
        evidence={'file': evidence.as_posix(), 'sha256': sha, 'document': 'Individual Samsung product page reviewed online',
                  'source_record': f'parts_source/{part}/working.yaml'},
        appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad nominal 0805 MLCC geometry matches the selected Samsung part dimensions; '
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
