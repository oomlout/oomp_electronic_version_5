"""Prepare the reviewed TI TPS5430 SOIC PowerPAD-10 display pilot.

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

PART = 'electronic_ic_power_management_buck_converter_soic_8_ep_texas_instruments_tps5430ddar'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TI_TPS5430_SOIC8_EP_RESEARCH.md')
MODEL = 'Package_SO.3dshapes/SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm.step'
MODEL_SHA256 = '2d6f7e774e8143e3320cbd59eb5be9f3b7864614644e3b072006e1eb05fb7fa6'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Texas Instruments'
        or record.get('part_number_manufacturer') != 'TPS5430DDAR'
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'soic_8_3_9x4_9mm_ep2_29x3mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.0, 4.9, 1.55],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['represented_manufacturer'] = 'Texas Instruments'
    result['represented_mpn'] = 'TPS5430DDAR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': '5430',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 1.8, 'maximum_height_mm': 0.6,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'TI TPS5430 SOIC PowerPAD package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TI specifies 5430 for TPS5430DDAR; variable production characters are omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad SOIC-8 PowerPAD display has 3.9 x 4.9 mm body, 6.0 mm lead span, 1.55 mm overall height, 1.27 mm pitch and an approximate 2.29 x 3 mm exposed pad. Source lists generic 10 x 5 mm dimensions without a documented reference. Not a verified mechanical model or footprint.')
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
