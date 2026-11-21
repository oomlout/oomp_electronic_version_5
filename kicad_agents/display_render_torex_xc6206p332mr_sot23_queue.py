"""Prepare the reviewed Torex XC6206P332MR SOT-23 display pilot.

Run without --add to validate only. The recipe is a preview candidate, not a
substitute for checking pin-one orientation, text direction and the final image.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_23_torex_xc6206p332mr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TOREX_XC6206P332MR_RESEARCH.md')
MODEL = 'Package_TO_SOT_SMD.3dshapes/SOT-23.step'
MODEL_SHA256 = 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Torex'
        or record.get('part_number_manufacturer') != 'XC6206P332MR'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:SOT-23'
        or record.get('dimensions_mm') != {'length': 2.92, 'width': 2.8}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'sot_23_3'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[2.5, 3.0, 1.2],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['model']['display_scale_xyz'] = [1.0, 1.0, 0.9166666666666666]
    result['represented_manufacturer'] = 'Torex'
    result['represented_mpn'] = 'XC6206P332MR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': '662',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 1.5, 'maximum_height_mm': 0.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Torex XC6206 SOT-23 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('Torex specifies 662 as the fixed 3.3 V marking portion; the variable production-lot character is omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('The KiCad SOT-23 model has 2.5 x 3.0 x 1.2 mm source bounds; it is scaled vertically to 1.1 mm for display, within the Torex TO-236 maximum 1.15 mm height. Source drawing lists 2.8 mm overall width, conflicting with the Torex 2.4 mm nominal lead span. Not a verified mechanical model or footprint.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true', help='add the validated candidate recipe')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(record, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it and review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        updated = (json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8')
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print(PART, recipe['represented_mpn'], 'candidate only; preview review required')


if __name__ == '__main__':
    main()
