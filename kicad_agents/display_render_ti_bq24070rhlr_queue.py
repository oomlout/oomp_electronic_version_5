"""Prepare the reviewed TI BQ24070RHLR RHL20 display pilot.

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

PART = 'electronic_ic_power_management_battery_charger_ic_qfn_20_ep_texas_instruments_bq24070rhlr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TI_BQ24070RHLR_RESEARCH.md')
MODEL = 'kicad_agents/display_model_ti_rhl0020a.py'
MODEL_SHA256 = '107d3cffb53bb3b25e94367d661ba80ce8c8eb5f48d270e647d8a1b3b232251e'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Texas Instruments'
        or record.get('part_number_manufacturer') != 'BQ24070RHLR'
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'ti_rhl0020a_vqfn20'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        expected_bounds_mm=[3.58, 4.58, 0.902],
        sha256=MODEL_SHA256,
    )
    result['model']['copyright'] = 'Procedural model generated in this repository'
    result['model']['license'] = 'Project source; procedural display geometry'
    result['model'].pop('license_url', None)
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'Texas Instruments'
    result['represented_mpn'] = 'BQ24070RHLR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'BRQ',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 1.8, 'maximum_height_mm': 0.8,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'TI BQ24070RHLR RHL20 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TI specifies BRQ as the fixed device marking; logo and variable production characters are omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative procedural RHL20 model uses a 3.5 x 4.5 x 0.9 mm body and 20 signal contacts at 0.5 mm pitch plus exposed pad. Source lists 10 x 5 mm without a defined reference. Contacts extend 0.04 mm beyond each body edge for visibility; contact shape, exposed pad and pin-one indicator are approximate. Not a verified mechanical model or footprint.')
    result['disable_bump_for'] = ['coating', 'termination', 'pin_indicator']
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
