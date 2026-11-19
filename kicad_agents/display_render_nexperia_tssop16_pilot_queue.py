"""Prepare the reviewed Nexperia HC595 SOIC-16 display pilot.

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

PART = 'electronic_ic_logic_serial_in_parallel_out_shift_register_tssop_16_nexperia_74hc595pw_118'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_TSSOP16_PILOT_EVIDENCE.md')
MODEL = 'Package_SO.3dshapes/TSSOP-16_4.4x5mm_P0.65mm.step'
MODEL_SHA256 = '6ad5e98224d02a427d9a6b929a28dbc158b9925fba5adec12db05079f1016948'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != '74HC595PW,118'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm'
        or record.get('dimensions_mm') != {'length': 5.0, 'width': 4.4, 'height': 1.1}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'tssop_16_4.4x5mm_p0.65mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.4, 5.0, 1.1],
        sha256=MODEL_SHA256,
    )
    result['represented_manufacturer'] = 'Nexperia'
    result['represented_mpn'] = '74HC595PW,118'
    result['marking'] = {
        'policy': 'verified_literal', 'text': 'HC595',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 3.5, 'maximum_height_mm': 0.8,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Nexperia TSSOP16 marking and package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('Nexperia lists HC595 as the package marking. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative KiCad TSSOP-16 model with nominal moulded body and plated leads; '
                                   'catalogue height is 1.1 mm; the KiCad model is 1.1 mm high and matches the catalogue; Nexperia permits up to 1.2 mm. '
                                   'Inspect the pin-one indicator and marking orientation against the source before publication.')
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
