"""Prepare five individually researched TAJ B-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_3528_avx_b_tantalum_10_micro_farad_16_volt_avx_tajb106k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_A_BATCH_B03_EVIDENCE.md')
# Exact ID, MPN, distributor ID, source capacitance, voltage and package code.
PARTS = {
    'electronic_capacitor_3528_avx_b_tantalum_33_micro_farad_10_volt_avx_tajb336k010rnej': ('TAJB336K010RNJ', 'C7202', '33 uF', '10', '336'),
    'electronic_capacitor_3528_avx_b_tantalum_33_micro_farad_16_volt_avx_tajb336k016rnej': ('TAJB336K016RNJ', 'C7203', '33 uF', '16', '336'),
    'electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_16_volt_avx_tajb475k016rnej': ('TAJB475K016RNJ', 'C7204', '4.7 uF', '16', '475'),
    'electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_25_volt_avx_tajb475k025rnej': ('TAJB475K025RNJ', 'C7205', '4.7 uF', '25', '475'),
    'electronic_capacitor_3528_avx_b_tantalum_4_7_micro_farad_35_volt_avx_tajb475k035rnej': ('TAJB475K035RNJ', 'C7206', '4.7 uF', '35', '475'),
}


def reviewed_recipe(part, record, recipes, evidence_sha):
    if part not in PARTS:
        raise ValueError('Unreviewed TAJ part')
    mpn, supplier, capacitance, volts, code = PARTS[part]
    electrical = record.get('electrical') or {}
    if (record.get('part_number_manufacturer') != mpn
        or record.get('part_number_lcsc') != supplier
        or electrical.get('capacitance') != capacitance
        or electrical.get('rated_voltage') != volts + ' V'
        or electrical.get('case_size') != 'CASE-B-3528-21'
        or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 3.5, 'width': 2.8, 'height': 2.1}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-3528-21_Kemet-B'
        or mpn != f'TAJB{code}K{int(volts):03d}RNJ'):
        raise ValueError('Selected part identity, ratings or package changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'tantalum_capacitor' or r['model'].get('display_scale_xyz') != [1.0, 1.0, 19/21]:
        raise ValueError('TAJ pilot changed')
    r['represented_mpn'] = mpn
    r['marking'].update(capacitance_code=code, rated_voltage_v=volts,
                        evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                                  'document': 'KYOCERA AVX TAJ datasheet and individual supplier listing',
                                  'source_record': f'parts_source/{part}/working.yaml'})
    r['appearance_status'] += ' Marking is composited from shared material passes; indirect reflections are approximate.'
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    found = {part: reviewed_recipe(part, yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8')), recipes, sha)
             for part in PARTS if part not in recipes}
    if args.add:
        recipes.update(found)
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part, recipe in found.items():
        print(part, recipe['represented_mpn'])


if __name__ == '__main__':
    main()
