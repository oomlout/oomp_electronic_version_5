"""Prepare individually evidenced Fenghua 0603 capacitor illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0603_batch01_queue import PILOT, MAKER

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0603_25V_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0603_220_nano_farad_fenghua_adv_tech_0603b224k250nt': ('0603B224K250NT','C1606','220 nF','X7R','10%'),
    'electronic_capacitor_0603_330_nano_farad': ('0603B334K250NT','C1615','330 nF','X7R','10%'),
}
NO_ELECTRICAL = frozenset()


def reviewed_recipe(part, record, recipes, sha, *, parts=PARTS, evidence=EVIDENCE, no_electrical=NO_ELECTRICAL):
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, dielectric, tolerance = parts[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0603_1608Metric':
        raise ValueError('Footprint changed')
    dims = record.get('dimensions_mm') or {}
    if dims.get('length') != 1.6 or dims.get('width') != .8 or dims.get('height', .8) != .8:
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '25 V'), ('dielectric', dielectric), ('tolerance', tolerance)):
        if not electrical and part in no_electrical:
            continue
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0603_imperial_1608_metric':
        raise ValueError('Unexpected source model')
    r.update(represented_manufacturer=MAKER, represented_mpn=mpn)
    r['marking']['evidence'] = {'file': evidence.as_posix(), 'sha256': sha, 'document': 'Part-specific evidence reviewed online',
                                'source_record': f'parts_source/{part}/working.yaml'}
    r['appearance_status'] = ('Generic KiCad nominal 0603 MLCC geometry with illustrative ceramic colour and metallic terminations; '
                              'represents the selected Fenghua part.')
    if not electrical:
        r['appearance_status'] += ' The source record lacks electrical fields; ratings were checked against the manufacturer page.'
    if part.endswith('0603b224k250nt'):
        r['appearance_status'] += ' Dimensions and ratings were checked against secondary distributor listings; the original manufacturer drawing was not independently accessed.'
    else:
        r['appearance_status'] += ' Dimensions and ratings were checked against the manufacturer catalogue.'
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
