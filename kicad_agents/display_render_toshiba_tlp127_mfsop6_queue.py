"""Prepare the reviewed Toshiba TLP127 four-lead MFSOP6 display pilot.

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

PART = 'electronic_ic_optocoupler_photodarlington_output_optocoupler_sop_4_toshiba_tlp127_tpl_u_f'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TOSHIBA_TLP127_MFSOP6_EVIDENCE.md')
MODEL = 'kicad_agents/display_model_toshiba_mfsop6_4pin.py'
MODEL_SHA256 = '07b1875eea7bf09d83d7a3f6fdc5177ffe12f11247aa50f394bb1b7f511f24ee'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'TOSHIBA'
        or record.get('part_number_manufacturer') != 'TLP127(TPL,U,F)'
        or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'toshiba_mfsop6_4pin'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        expected_bounds_mm=[7.0, 3.6, 2.482],
        sha256=MODEL_SHA256,
    )
    result['model']['copyright'] = 'Procedural model generated in this repository'
    result['model']['license'] = 'Project source; procedural display geometry'
    result['model'].pop('license_url', None)
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'TOSHIBA'
    result['represented_mpn'] = 'TLP127(TPL,U,F)'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'TLP127',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 2.0, 'maximum_height_mm': 0.7,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Toshiba TLP127 MFSOP6 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TLP127 is an illustrative family identifier; exact physical marking is unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative procedural four-lead MFSOP6 model uses nominal 4.4 x 3.6 mm body, 2.5 mm height and 2.54 mm pitch from Toshiba 11-4C1. Catalogue lists 10 x 5 mm without height or footprint. Lead shape, placement and pin-one indicator are approximate; not a verified mechanical model or footprint.')
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
