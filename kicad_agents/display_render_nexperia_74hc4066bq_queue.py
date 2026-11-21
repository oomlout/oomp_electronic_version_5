"""Prepare the reviewed Nexperia 74HC4066BQ DHVQFN14 display pilot.

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

PART = 'electronic_ic_logic_analog_switch_qfn_14_nexperia_74hc4066bq'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_74HC4066BQ_EVIDENCE.md')
MODEL = 'kicad_agents/display_model_nexperia_sot762_1.py'
MODEL_SHA256 = 'aea2ad86a0ec5591a1225982fcdcbe73a32e8045de30a31a054daf0370af6726'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') not in ('', None)
        or record.get('part_number_manufacturer') not in ('', None)
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_DFN_QFN:QFN-14-1EP_3x3mm_P0.5mm_EP1.65x1.65mm'
        or record.get('dimensions_mm') != {'height': 0.9, 'length': 3.0, 'width': 3.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'nexperia_sot762_1_dhvqfn14'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        expected_bounds_mm=[2.524, 3.024, 0.852],
        sha256=MODEL_SHA256,
    )
    result['model']['copyright'] = 'Procedural model generated in this repository'
    result['model']['license'] = 'Project source; procedural display geometry'
    result['model'].pop('license_url', None)
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'Nexperia (inferred from catalogue ID)'
    result['represented_mpn'] = '74HC4066BQ'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'HC4066',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 1.7, 'maximum_height_mm': 0.6,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Nexperia 74HC4066BQ SOT762-1 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('HC4066 is an illustrative family identifier; exact physical marking is unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative procedural SOT762-1 model uses a 2.5 x 3.0 x 0.85 mm body and 14 contacts at 0.5 mm pitch. Nexperia and 74HC4066BQ are inferred from the catalogue ID. Source lists 3 x 3 x 0.9 mm and a different footprint; contacts extend 0.012 mm beyond each body edge for visibility; contact shape, exposed pad and pin-one indicator are approximate. Not a verified mechanical model or footprint.')
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
