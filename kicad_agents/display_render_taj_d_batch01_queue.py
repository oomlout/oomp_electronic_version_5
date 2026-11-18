"""Prepare eight individually researched TAJ D-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_16_volt_avx_tajd107k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_D_BATCH01_EVIDENCE.md')
# Exact ID, MPN, distributor ID, source capacitance, voltage and package code.
PARTS = {
    'electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_10_volt_avx_tajd107k010rnej': ('TAJD107K010RNJ', 'C7222', '100 uF', '10', '107'),
    'electronic_capacitor_7343_avx_d_tantalum_100_micro_farad_20_volt_avx_tajd107k020rnej': ('TAJD107K020RNJ', 'C7224', '100 uF', '20', '107'),
    'electronic_capacitor_7343_avx_d_tantalum_10_micro_farad_35_volt_avx_tajd106k035rnej': ('TAJD106K035RNJ', 'C7221', '10 uF', '35', '106'),
    'electronic_capacitor_7343_avx_d_tantalum_22_micro_farad_35_volt_avx_tajd226k035rnej': ('TAJD226K035RNJ', 'C7225', '22 uF', '35', '226'),
    'electronic_capacitor_7343_avx_d_tantalum_330_micro_farad_10_volt_avx_tajd337k010rnej': ('TAJD337K010RNJ', 'C7226', '330 uF', '10', '337'),
    'electronic_capacitor_7343_avx_d_tantalum_470_micro_farad_6_3_volt_avx_tajd477k006rnej': ('TAJD477K006RNJ', 'C7229', '470 uF', '6.3', '477'),
    'electronic_capacitor_7343_avx_d_tantalum_47_micro_farad_16_volt_avx_tajd476k016rnej': ('TAJD476K016RNJ', 'C7227', '47 uF', '16', '476'),
    'electronic_capacitor_7343_avx_d_tantalum_47_micro_farad_25_volt_avx_tajd476k025rnej': ('TAJD476K025RNJ', 'C7228', '47 uF', '25', '476'),
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
        or electrical.get('case_size') != 'CASE-D-7343-31'
        or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 7.3, 'width': 4.3, 'height': 3.1}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-7343-31_Kemet-D'
        or mpn != f'TAJD{code}K{int(float(volts)):03d}RNJ'):
        raise ValueError('Selected part identity, ratings or package changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'tantalum_capacitor' or r['model'].get('display_scale_xyz') != [1.0, 1.0, 29/31]:
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
