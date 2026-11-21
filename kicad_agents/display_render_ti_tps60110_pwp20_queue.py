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

PART = 'electronic_ic_power_management_charge_pump_regulated_converter_htssop_20_ep_texas_instruments_tps60110pwpr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TI_TPS60110_PWP20_EVIDENCE.md')
MODEL = 'Package_SO.3dshapes/HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm.step'
MODEL_SHA256 = 'fa00bb36905740c1f79dc3a9305094118bcb85b4f26bcc1a923ae18bca943e06'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Texas Instruments'
        or record.get('part_number_manufacturer') != 'TPS60110PWPR'
        or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'htssop_20_ep'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[6.4, 6.6, 1.2],
        sha256=MODEL_SHA256,
    )
    result['represented_manufacturer'] = 'Texas Instruments'
    result['represented_mpn'] = 'TPS60110PWPR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'TPS60110',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 4.5, 'maximum_height_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'TI TPS60110 PWP package and marking review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('TI specifies TPS60110 for TPS60110PWPR; variable production characters are omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad HTSSOP-20 model has 6.4 x 6.6 x 1.2 mm overall bounds. Its 3.4 x 6.6 mm thermal pad is display-corrected to 2.0 x 2.7 mm and the underside is filled; the pad remains approximate. Catalogue 10 x 5 mm dimensions are generic and footprint is missing. A catalogue note says 3.3 V, while manufacturer and source ratings indicate 5 V. Not a verified mechanical model or footprint.')
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
