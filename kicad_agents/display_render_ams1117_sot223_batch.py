"""Prepare exact AMS1117 SOT-223 candidates; inspect every rendered variant."""
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

REFERENCE = 'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_223_3_maxlinear_spx1117m3_l_3_3_tr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_AMS1117_SOT223_EVIDENCE.md')
PARTS = {
    'electronic_ic_power_management_linear_voltage_regulator_1_8_volt_sot_223_3_advanced_monolithic_systems_ams1117_1_8': ('AMS1117-1.8', '1.8', {'length': 10.0, 'width': 5.0}),
    'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_223_3_advanced_monolithic_systems_ams1117_3_3': ('AMS1117-3.3', '3.3', {'length': 6.5, 'width': 7.0}),
    'electronic_ic_power_management_linear_voltage_regulator_5_volt_sot_223_3_advanced_monolithic_systems_ams1117_5': ('AMS1117-5.0', '5.0', {'length': 6.5, 'width': 7.0}),
    'electronic_ic_power_management_linear_voltage_regulator_adjustable_sot_223_3_advanced_monolithic_systems_ams1117_adj': ('AMS1117-ADJ', 'ADJ', {'length': 10.0, 'width': 5.0}),
}


def candidate(part, record, recipes):
    mpn, code, dimensions = PARTS[part]
    if (record.get('manufacturer') != 'Advanced Monolithic Systems' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != dimensions
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:SOT-223-3_TabPin2'):
        raise ValueError('Source identity, dimensions or footprint changed; review again')
    result = copy.deepcopy(recipes[REFERENCE])
    if (result.get('family') != 'integrated_circuit' or result.get('package') != 'sot_223_3'
            or result['model'].get('sha256') != '77ad6dbacc493cb619c728f26d2ddcf461eb0feb6b977b47d01d51e67016f654'):
        raise ValueError('SOT-223 reference geometry changed')
    result['represented_manufacturer'] = 'Advanced Monolithic Systems'
    result['represented_mpn'] = mpn
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'AMS1117\n' + code,
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 3.5, 'maximum_height_mm': 2.2,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
                     'document': 'Advanced Monolithic Systems AMS1117 SOT-223 package review',
                     'source_record': f'parts_source/{part}/working.yaml'},
        'appearance_status': 'Family and voltage text are illustrative; the physical marking, typeface, placement and variable production details are unverified.',
    }
    discrepancy = ('Source lists 10 x 5 mm without a defined reference, differing from the model. '
                   if dimensions == {'length': 10.0, 'width': 5.0} else '')
    spelling = ('The source uses AMS1117-ADJ; the manufacturer data sheet lists the adjustable SOT-223 as AMS1117. '
                if code == 'ADJ' else '')
    result['appearance_status'] = ('KiCad SOT-223 model has 7.0 x 6.5 x 1.7 mm overall bounds. '
                                   + discrepancy + spelling + 'Pin marker and appearance are illustrative; not a verified mechanical model or footprint.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=sorted(PARTS))
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT/'parts_source'/args.part/'working.yaml').read_text(encoding='utf8'))
    recipe = candidate(args.part, record, recipes)
    if args.part in recipes and recipes[args.part] != recipe:
        raise ValueError('Existing recipe differs; preserve and review it')
    if args.add and args.part not in recipes:
        recipes[args.part] = recipe
        data = (json.dumps(recipes, ensure_ascii=False, indent=2)+'\n').encode('utf8')
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write(data)
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
