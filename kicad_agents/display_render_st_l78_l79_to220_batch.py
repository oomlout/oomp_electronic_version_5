"""Prepare individually reviewed ST TO-220 display variants from the pilot.

Run without --add to check the source identity. Each candidate still requires
visual review and a targeted publisher after its full-quality render.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_ic_power_management_linear_voltage_regulator_5_volt_to_220_stmicroelectronics_l7805cv_dg'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_ST_L78_L79_TO220_EVIDENCE.md')
PARTS = {
    'electronic_ic_power_management_linear_voltage_regulator_12_volt_to_220_stmicroelectronics_l7812cv_dg': 'L7812CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_15_volt_to_220_stmicroelectronics_l7815cv': 'L7815CV',
    'electronic_ic_power_management_linear_voltage_regulator_15_volt_to_220_stmicroelectronics_l7815cv_dg': 'L7815CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_24_volt_to_220_stmicroelectronics_l7824cv_dg': 'L7824CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_6_volt_to_220_stmicroelectronics_l7806cv_dg': 'L7806CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_8_volt_to_220_stmicroelectronics_l7808cv_dg': 'L7808CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_9_volt_to_220_stmicroelectronics_l7809cv_dg': 'L7809CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_negative_5_volt_to_220_stmicroelectronics_l7905cv_dg': 'L7905CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_negative_12_volt_to_220_stmicroelectronics_l7912cv_dg': 'L7912CV-DG',
    'electronic_ic_power_management_linear_voltage_regulator_negative_15_volt_to_220_stmicroelectronics_l7915cv_dg': 'L7915CV-DG',
}


def candidate(part, record, recipes):
    mpn = PARTS[part]
    if (record.get('manufacturer') != 'STMicroelectronics'
            or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != ''):
        raise ValueError(f'{part}: reviewed identity, dimensions or footprint changed')
    result = copy.deepcopy(recipes[REFERENCE])
    model, mark = result['model'], result['marking']
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    if (model.get('sha256') != '7cb065d935df5771f0ba6e48ddd180863a121af76483dad7f18e667a7b68204a'
            or model.get('display_orientation') != 'to220_face_up'
            or mark.get('offset_x_mm') != -3.52 or mark['evidence']['sha256'] != evidence_sha):
        raise ValueError('Pilot model, pose, marking position or evidence changed')
    family = mpn.removesuffix('-DG')
    gauge = 'dual-gauge' if mpn.endswith('-DG') else 'single-gauge'
    result['represented_mpn'] = mpn
    mark['text'] = family
    mark['evidence']['source_record'] = f'parts_source/{part}/working.yaml'
    mark['appearance_status'] = (f'{family} is an illustrative family identifier; the physical marking of {mpn} is unverified. '
                                 'Typeface, orientation, placement and variable lot/date details are illustrative.')
    result['appearance_status'] = (f'The generic KiCad TO-220-3 model is laid face-up for display. ST lists {mpn} as {gauge} TO-220; '
                                   'the model does not establish matching lead gauge. Overall bounds include straight leads. '
                                   'Not a verified mechanical model or footprint.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=sorted(PARTS))
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / args.part / 'working.yaml').read_text(encoding='utf8'))
    recipe = candidate(args.part, record, recipes)
    if args.part in recipes and recipes[args.part] != recipe:
        raise ValueError('Existing recipe differs; preserve and review it')
    if args.add and args.part not in recipes:
        recipes[args.part] = recipe
        updated = (json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write(updated)
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print(args.part, recipe['represented_mpn'], 'candidate only; preview review required')


if __name__ == '__main__':
    main()
