"""Prepare the reviewed generic ST LD1117 3.3 V SOT-223 display pilot.

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

PART = 'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_223_4_st_ld1117_3_3'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_BL_ST_LD1117_RESEARCH.md')
MODEL = 'Package_TO_SOT_SMD.3dshapes/SOT-223.step'
MODEL_SHA256 = '77ad6dbacc493cb619c728f26d2ddcf461eb0feb6b977b47d01d51e67016f654'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') not in ('', None)
        or record.get('part_number_manufacturer') not in ('', None)
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 6.5, 'width': 7.0, 'height': 1.8}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'sot_223_3'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.0, 6.5, 1.7],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['represented_manufacturer'] = 'ST (inferred from catalogue ID)'
    result['represented_mpn'] = 'LD1117 3.3 V family (exact orderable unspecified)'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'LD1117\n3.3',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 3.5, 'maximum_height_mm': 2.2,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'ST LD1117 SOT-223 family package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('LD1117 and 3.3 are illustrative family and voltage identifiers; exact physical marking and production characters are unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad SOT-223 model has 7.0 x 6.5 x 1.7 mm overall bounds. Manufacturer ST is inferred from the ID; exact orderable is unspecified. The source package drawing incorrectly shows two small leads on each side, unlike the ST drawing with three leads and a tab. Pin marker and appearance are illustrative. Not a verified mechanical model or footprint.')
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
