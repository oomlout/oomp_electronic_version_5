"""Prepare the reviewed Raspberry Pi RP2040 QFN-56 display pilot.

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

PART = 'electronic_ic_microcontroller_dual_core_arm_cortex_m0_plus_qfn_56_7_mm_x_7_mm_raspberry_pi_rp2040'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RASPBERRY_PI_RP2040_QFN56_RESEARCH.md')
MODEL = 'Package_DFN_QFN.3dshapes/QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm.step'
MODEL_SHA256 = '010e8039ec6f28fb1c5f5c6d170757af464c82c200ecc655c8150398117e2283'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Raspberry Pi'
        or record.get('part_number_manufacturer') != 'RP2040'
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 7.0, 'width': 7.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'qfn_56_7x7mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.0, 7.0, 0.9],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['represented_manufacturer'] = 'Raspberry Pi'
    result['represented_mpn'] = 'RP2040'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'RP2040',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 4.0, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Raspberry Pi RP2040 QFN-56 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('RP2040 is an illustrative identifier; actual package markings include a logo and production-specific details. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad QFN-56 model has 7 x 7 x 0.9 mm overall bounds and 0.4 mm pitch. Raspberry Pi specifies a 7 x 7 mm reduced-pad QFN-56 with 0.9 mm maximum height and 3.0 to 3.2 mm exposed pad. Source does not select a footprint or specify height. Not a verified mechanical model or footprint.')
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
