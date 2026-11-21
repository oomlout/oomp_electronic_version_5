"""Prepare the reviewed TI W25Q16JV UX USON-10 display pilot.

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

PART = 'electronic_ic_memory_spi_nor_flash_uson_8_winbond_w25q16jvuxiq'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_WINBOND_W25Q16JVUXIQ_RESEARCH.md')
MODEL = 'Package_DFN_QFN.3dshapes/DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm.step'
MODEL_SHA256 = 'd1a0c43ea32a8b2ce1b2e57208cef09b38462bda190e1253857c35649bfc56f7'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') not in (None, '')
        or record.get('part_number_manufacturer') not in (None, '')
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_DFN_QFN:USON-8-1EP_2x2mm_P0.5mm_EP0.8x1.6mm'
        or record.get('dimensions_mm') != {'height': 0.55, 'length': 3.0, 'width': 2.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'uson_8_2x3mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[2.0, 2.98, 0.77],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['model']['display_scale_xyz'] = [1.0, 1.0, 0.7142857142857143]
    result['represented_manufacturer'] = 'Winbond (inferred from catalogue ID)'
    result['represented_mpn'] = 'W25Q16JVUXIQ'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': '1P',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 1.0, 'maximum_height_mm': 0.5,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'TI W25Q16JV UX USON package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('Winbond specifies 1P as the fixed prefix for W25Q16JVUXIQ; variable production characters are omitted. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Inferred Winbond identity; KiCad 2 x 2.98 x 0.77 mm model is vertically scaled to 0.55 mm. Its 0.61 x 2.2 mm exposed pad is illustrative and not established in the extracted maker UX drawing. Source selects a 2 x 2 mm footprint and draws terminals on four sides, conflicting with the maker 3 x 2 mm two-row package. Not a verified mechanical model or footprint.')
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
