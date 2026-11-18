"""Prepare seven individually researched TAJ C-case display recipes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_16_volt_avx_tajc106k016rnej'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TAJ_C_BATCH01_EVIDENCE.md')
# Exact ID, MPN, distributor ID, source capacitance, voltage and package code.
PARTS = {
    'electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_25_volt_avx_tajc106k025rnej': ('TAJC106K025RNJ', 'C7210', '10 uF', '25', '106'),
    'electronic_capacitor_6032_avx_c_tantalum_10_micro_farad_35_volt_avx_tajc106k035rnej': ('TAJC106K035RNJ', 'C7211', '10 uF', '35', '106'),
    'electronic_capacitor_6032_avx_c_tantalum_220_micro_farad_6_3_volt_avx_tajc227k006rnej': ('TAJC227K006RNJ', 'C7216', '220 uF', '6.3', '227'),
    'electronic_capacitor_6032_avx_c_tantalum_22_micro_farad_25_volt_avx_tajc226k025rnej': ('TAJC226K025RNJ', 'C7214', '22 uF', '25', '226'),
    'electronic_capacitor_6032_avx_c_tantalum_33_micro_farad_16_volt_avx_tajc336k016rnej': ('TAJC336K016RNJ', 'C7217', '33 uF', '16', '336'),
    'electronic_capacitor_6032_avx_c_tantalum_47_micro_farad_16_volt_avx_tajc476k016rnej': ('TAJC476K016RNJ', 'C7219', '47 uF', '16', '476'),
    'electronic_capacitor_6032_avx_c_tantalum_68_micro_farad_16_volt_avx_tajc686k016rnej': ('TAJC686K016RNJ', 'C7220', '68 uF', '16', '686'),
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
        or electrical.get('case_size') != 'CASE-C-6032-28'
        or electrical.get('polarized') is not True
        or record.get('dimensions_mm') != {'length': 6.0, 'width': 3.2, 'height': 2.8}
        or record.get('kicad', {}).get('machine_solder') != 'Capacitor_Tantalum_SMD:CP_EIA-6032-28_Kemet-C'
        or mpn != f'TAJC{code}K{int(float(volts)):03d}RNJ'):
        raise ValueError('Selected part identity, ratings or package changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'tantalum_capacitor' or r['model'].get('display_scale_xyz') != [1.0, 1.0, 13/14]:
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
