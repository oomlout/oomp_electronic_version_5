"""Prepare the reviewed Nexperia 74HC00D SOIC-14 display pilot.

Run without --add to validate only. The recipe is a preview candidate, not a
substitute for checking pin-one orientation, text direction and the final image.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_logic_quad_2_input_nand_gate_soic_14_nexperia_74hc00d_653'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_SO14_PREPARATION.md')
MODEL = 'Package_SO.3dshapes/SOIC-14_3.9x8.7mm_P1.27mm.step'
MODEL_SHA256 = '3b9a775da256c8afcc28dcddfbc2eb3f266107fe61ce8446d96f2c52b6f44a70'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != '74HC00D,653'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm'
        or record.get('dimensions_mm') != {'length': 8.7, 'width': 3.9, 'height': 1.75}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'soic_14_3.9x8.7mm_p1.27mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.0, 8.7, 1.75],
        sha256=MODEL_SHA256,
    )
    result['represented_manufacturer'] = 'Nexperia'
    result['represented_mpn'] = '74HC00D,653'
    result['marking'] = {
        'policy': 'verified_literal', 'text': '74HC00D',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 5.5, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Nexperia SO14 marking and package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('Nexperia lists 74HC00D as the package marking. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Illustrative KiCad SOIC-14 model with nominal moulded body and plated leads. '
                                   'Inspect the pin-one indicator and marking orientation against the source before publication.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true', help='add the validated candidate recipe')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = reviewed_recipe(record, recipes, sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it and review manually')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(PART, recipe['represented_mpn'], 'candidate only; preview review required')


if __name__ == '__main__':
    main()
