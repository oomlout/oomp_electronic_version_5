"""Prepare the reviewed Winbond AT25DF321A-SH-T SOIC-8 display pilot.

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

PART = 'electronic_ic_memory_spi_nor_flash_32_mbit_soic_8_208mil_renesas_at25df321a_sh_t'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_RENESAS_AT25DF321A_SOIC8_RESEARCH.md')
MODEL = 'Package_SO.3dshapes/SOIC-8_5.3x5.3mm_P1.27mm.step'
MODEL_SHA256 = '121aee742692bb7bc9ef49972786ecb89d1b2d62ab089ed278651a884c800331'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'RENESAS'
        or record.get('part_number_manufacturer') != 'AT25DF321A-SH-T'
        or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'soic_8_5_3x5_3mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.8, 5.3, 2.16],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['represented_manufacturer'] = 'Renesas'
    result['represented_mpn'] = 'AT25DF321A-SH-T'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'AT25DF321A',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 3.6, 'maximum_height_mm': 0.75,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Renesas AT25DF321A SOIC package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('AT25DF321A is an illustrative partial identifier; exact package marking is unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('KiCad SOIC-8 model has 5.3 x 5.3 mm body, 7.8 mm lead span and 2.16 mm overall height, within manufacturer limits. Catalogue gives generic 10 x 5 mm, conflicting with package dimensions, and omits height and footprint. Package details remain illustrative; not a verified mechanical model or PCB footprint.')
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
