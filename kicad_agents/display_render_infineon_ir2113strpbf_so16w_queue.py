"""Prepare the reviewed Nexperia CD4067BM SOIC-16 display pilot.

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

PART = 'electronic_ic_driver_half_bridge_gate_driver_soic_16_infineon_ir2113strpbf'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IR2112_IR2113_SO16W_EVIDENCE.md')
MODEL = 'Package_SO.3dshapes/SOIC-16W_7.5x10.3mm_P1.27mm.step'
MODEL_SHA256 = '159663ceb2b4996b1b89d3111e4a355fc27de3e24d3570f50e5ed9086e0d73af'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Infineon Technologies'
        or record.get('part_number_manufacturer') != 'IR2113STRPBF'
        or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
        or record.get('dimensions_mm') != {'length': 9.9, 'width': 3.9}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'soic_16w_7.5x10.3mm_p1.27mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[10.3, 10.3, 2.75],
        sha256=MODEL_SHA256,
        display_scale_xyz=[1.0, 1.0, 2.5/2.75],
    )
    result['represented_manufacturer'] = 'Infineon Technologies'
    result['represented_mpn'] = 'IR2113STRPBF'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'IR2113',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 6.5, 'maximum_height_mm': 1.3,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Infineon IR2113 SOIC16W package and illustrative marking review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('IR2113 is an illustrative partial identifier; exact physical marking is not confirmed. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative KiCad SOIC-16W model scaled vertically from 2.75 mm to 2.5 mm, within Infineon 2.35–2.65 mm range. Catalogue 9.9 x 3.9 mm conflicts with manufacturer wide body 10.1–10.5 x 7.4–7.6 mm; catalogue height and footprint are missing. Not a verified mechanical model or footprint.')
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
