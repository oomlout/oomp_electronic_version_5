"""Prepare the reviewed MicrOne ME6211 SOT-89 display candidate.

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

PART = 'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_89_3_microne_me6211a33pg_n'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MICRONE_ME6211_SOT89_RESEARCH.md')
MODEL = 'Package_TO_SOT_SMD.3dshapes/SOT-89-3.step'
MODEL_SHA256 = '844c0bb504d0c383535d9845c6376fe7a4053241a2ede8d8ef694df3fcfc37c8'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') not in ('', None)
        or record.get('part_number_manufacturer') != 'ME6211A33PG-N'
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 4.5, 'width': 2.5}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'sot_89_3'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[4.0, 4.5, 1.52],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination'],
    )
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'MicrOne (inferred from catalogue ID)'
    result['represented_mpn'] = 'ME6211A33PG-N'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': '6211A',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 2.5, 'maximum_height_mm': 0.45, 'offset_x_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'MicrOne ME6211 SOT-89 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('MicrOne identifies 6211A for the P package; voltage and production markings are omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad SOT-89 model has 4 x 4.5 x 1.52 mm overall bounds. The colourless source is assigned coating and metal roles by checked solid geometry; catalogue 4.5 x 2.5 mm dimensions do not specify their reference; manufacturer is inferred and the maker marking diagram was not visually confirmed; linked source datasheet is for ME6118, a different part. Not a verified mechanical model or footprint.')
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
