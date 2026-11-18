"""Prepare five individually researched TAJ A-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_3216_avx_a_tantalum_10_micro_farad_10_volt_avx_taja106k010rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_A_BATCH02_EVIDENCE.md')
# Exact ID, MPN, distributor ID, source capacitance, voltage and package code.
PARTS = {
    'electronic_capacitor_3216_avx_a_tantalum_1_micro_farad_35_volt_avx_taja105k035rnej': ('TAJA105K035RNJ', 'C7176', '1 uF', '35', '105'),
    'electronic_capacitor_3216_avx_a_tantalum_2_2_micro_farad_25_volt_avx_taja225k025rnej': ('TAJA225K025RNJ', 'C7181', '2.2 uF', '25', '225'),
    'electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt_avx_taja475k016rnej': ('TAJA475K016RNJ', 'C7187', '4.7 uF', '16', '475'),
    'electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_25_volt_avx_taja475k025rnej': ('TAJA475K025RNJ', 'C7189', '4.7 uF', '25', '475'),
    'electronic_capacitor_3216_avx_a_tantalum_6_8_micro_farad_16_volt_avx_taja685k016rnej': ('TAJA685K016RNJ', 'C7191', '6.8 uF', '16', '685'),
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
        or electrical.get('case_size') != 'CASE-A-3216-18'
        or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 3.2, 'width': 1.6, 'height': 1.8}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A'
        or mpn != f'TAJA{code}K{int(volts):03d}RNJ'):
        raise ValueError('Selected part identity, ratings or package changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'tantalum_capacitor' or r['model'].get('display_scale_xyz') != [1.0, 1.0, 8/9]:
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
