"""Prepare five individually researched TAJ A-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_3216_avx_a_tantalum_10_micro_farad_10_volt_avx_taja106k010rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_A_BATCH03_EVIDENCE.md')
# Exact ID, MPN, distributor ID, source capacitance, voltage and package code.
PARTS = {
    'electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_6_3_volt_avx_taja226k006rnej': ('TAJA226K006RNJ', 'C7182', '22 uF', '6.3', '226'),
    'electronic_capacitor_3216_avx_a_tantalum_33_micro_farad_10_volt_avx_taja336k010rnej': ('TAJA336K010RNJ', 'C7186', '33 uF', '10', '336'),
    'electronic_capacitor_3216_avx_a_tantalum_33_micro_farad_6_3_volt_avx_taja336k006rnej': ('TAJA336K006RNJ', 'C7185', '33 uF', '6.3', '336'),
    'electronic_capacitor_3216_avx_a_tantalum_47_micro_farad_6_3_volt_avx_taja476k006rnej': ('TAJA476K006RNJ', 'C7190', '47 uF', '6.3', '476'),
    'electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_20_volt_avx_taja475k020rnej': ('TAJA475K020RNJ', 'C7188', '4.7 uF', '20', '475'),
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
        or mpn != f"TAJA{code}K{ {'6.3': '006', '10': '010', '20': '020'}[volts] }RNJ"):
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
