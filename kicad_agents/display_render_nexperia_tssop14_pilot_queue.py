"""Validate or stage the individually sourced Nexperia 74HC00PW TSSOP pilot.

The default is read-only. Review its preview, pin-one indicator, dimensions and
the independent full render before considering other TSSOP parts.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json

import yaml

from kicad_agents.display_render_nexperia_so14_pilot_queue import PART as REFERENCE
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_ic_logic_quad_2_input_nand_gate_tssop_14_nexperia_74hc00pw_118'
MODEL = 'Package_SO.3dshapes/TSSOP-14_4.4x5mm_P0.65mm.step'
MODEL_SHA256 = '3ee5786aae56190997aa793ba3cfc003fd616782770e29719b4562f012982245'
EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_TSSOP14_PREPARATION.md'


def candidate(record, reference, evidence_sha256):
    if (record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != '74HC00PW,118'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm'
        or record.get('dimensions_mm') != {'length': 5.0, 'width': 4.4, 'height': 1.1}):
        raise ValueError('TSSOP pilot identity, footprint or dimensions changed')
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('represented_mpn') != '74HC00D,653'
        or reference.get('marking', {}).get('text') != '74HC00D'):
        raise ValueError('SO14 material reference changed')
    recipe = copy.deepcopy(reference)
    recipe['package'] = 'tssop_14_4.4x5mm_p0.65mm'
    recipe['model'].update(relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.4, 5.0, 1.0], sha256=MODEL_SHA256)
    recipe['represented_mpn'] = '74HC00PW,118'
    recipe['marking'] = {
        'policy': 'verified_literal', 'text': 'HC00', 'font_file': 'arialbd.ttf',
        'rotation_degrees': 90, 'maximum_width_mm': 3.0, 'maximum_height_mm': 0.8,
        'evidence': {'file': EVIDENCE, 'sha256': evidence_sha256,
                     'document': 'Nexperia TSSOP14 marking and package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('Nexperia lists HC00 as the package marking. Typeface, orientation, '
                              'placement and variable lot/date details are illustrative.'),
    }
    recipe['appearance_status'] = (
        'Illustrative KiCad TSSOP-14 model: nominal model height 1.0 mm versus the '
        'catalogue 1.1 mm; manufacturer outline specifies a 1.2 mm maximum. '
        'Inspect pin-one and lettering orientation before publication.'
    )
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
    print(PART, 'HC00 candidate only; model and preview review required')


if __name__ == '__main__':
    main()
