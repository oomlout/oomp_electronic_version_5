"""Prepare manufacturer-evidenced Fenghua 0805 illustrations."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_fenghua_0805_120pf_queue import PART as PILOT, MAKER

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_FENGHUA_0805_ASSUMED_X7R_03_EVIDENCE.md')
PARTS = {
    'electronic_capacitor_0805_300_pico_farad': ('0805B301K500NT', 'C1735', '300 pF', 'X7R', '10%'),
    'electronic_capacitor_0805_330_pico_farad': ('0805B331K500NT', 'C1737', '330 pF', 'X7R', '10%'),
    'electronic_capacitor_0805_390_pico_farad': ('0805B391K500NT', 'C1741', '390 pF', 'X7R', '10%'),
    'electronic_capacitor_0805_510_pico_farad': ('0805B511K500NT', 'C1749', '510 pF', 'X7R', '10%'),
    'electronic_capacitor_0805_560_pico_farad': ('0805B561K500NT', 'C1751', '560 pF', 'X7R', '10%'),
}


def reviewed_recipe(part, record, recipes, sha, *, parts=PARTS, evidence=EVIDENCE, expected_dims=None):
    if part not in parts:
        raise ValueError('Unreviewed part')
    mpn, lcsc, value, dielectric, tolerance = parts[part]
    if record.get('manufacturer') != MAKER or record.get('part_number_manufacturer') != mpn:
        raise ValueError('Selected identity changed')
    if not any(x.get('manufacturer') == MAKER and x.get('part_number') == mpn for x in record.get('manufacturers', []) if isinstance(x, dict)):
        raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == lcsc for x in record.get('distributors', []) if isinstance(x, dict)):
        raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric':
        raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != (expected_dims if expected_dims is not None else {'length': 2.0, 'width': 1.25}):
        raise ValueError('Source dimensions changed')
    electrical = record.get('electrical') or {}
    for key, token in (('capacitance', value), ('rated_voltage', '50 V'), ('dielectric', dielectric), ('tolerance', tolerance)):
        if token not in str(electrical.get(key, '')):
            raise ValueError(f'{key} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r['model'].get('display_scale_xyz') != [1.0, 1.0, .64]:
        raise ValueError('Unexpected source model')
    r['represented_mpn'] = mpn
    r['marking']['evidence'] = {'file': evidence.as_posix(), 'sha256': sha, 'document': 'Individual Fenghua catalogue entries reviewed online',
                                 'source_record': f'parts_source/{part}/working.yaml'}
    r['marking']['evidence']['document'] = 'Fenghua family specification and individual supplier listings reviewed online'
    r['appearance_status'] = ('Illustrative KiCad 0805 model at 0.8 mm thickness, one of several thicknesses in the Fenghua family specification. Exact part thickness, ceramic colour, termination finish and marking are not verified.')
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
