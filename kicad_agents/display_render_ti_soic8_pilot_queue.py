"""Validate or stage the individually sourced TI NE5532DR SOIC-8 pilot.

Read-only by default. Check the model, pin-one, marking and final independently
before using a shared-pass approach for other SOIC-8 components.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json

import yaml

from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_amplifier_operational_amplifier_dual_low_noise_soic_8_texas_instruments_ne5532dr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
MODEL_SHA256 = '07f46cff378d30e6c27dfd5a03092c795323f86d91c71fc7e743f4f418dc553a'
EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_TI_SOIC8_PREPARATION.md'


def candidate(record, reference, evidence_sha256):
    if (record.get('manufacturer') != 'Texas Instruments'
        or record.get('part_number_manufacturer') != 'NE5532DR'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm'
        or record.get('dimensions_mm') != {'length': 4.9, 'width': 3.9, 'height': 1.75}):
        raise ValueError('TI pilot identity, footprint or dimensions changed')
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('represented_mpn') != 'NE555DR'
        or reference.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('SOIC-8 reference changed')
    recipe = copy.deepcopy(reference)
    recipe['represented_mpn'] = 'NE5532DR'
    recipe['marking'] = {
        'policy': 'verified_literal', 'text': 'N5532', 'font_file': 'arialbd.ttf',
        'maximum_width_mm': 2.6, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE, 'sha256': evidence_sha256,
                     'document': 'Texas Instruments SOIC-8 manufacturer marking and package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TI lists N5532 as the device marking. Typeface, placement, '
                              'logos and variable lot/date details are illustrative.'),
    }
    recipe['appearance_status'] = ('Illustrative KiCad SOIC-8 model; TI D0008A drawing '
                                   'specifies 1.75 mm maximum height. Inspect pin-one and text orientation.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf-8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf-8'))
    sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    recipe = candidate(record, recipes[REFERENCE], sha)
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it for manual review')
    if args.add and PART not in recipes:
        recipes[PART] = recipe
        RECIPE_FILE.write_text(json.dumps(recipes, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(PART, 'N5532 candidate only; model and preview review required')


if __name__ == '__main__':
    main()
