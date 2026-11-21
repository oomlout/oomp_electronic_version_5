"""Prepare the reviewed JSCJ CJ78L05 SOT-89 display candidate.

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

PART = 'electronic_transistor_sot_89_3_bipolar_npn_30_volt_3_amp_jiangsu_changjing_electronics_technology_co_ltd_d882_range_160_320'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_D882_SOT89_RESEARCH.md')
MODEL = 'Package_TO_SOT_SMD.3dshapes/SOT-89-3.step'
MODEL_SHA256 = '844c0bb504d0c383535d9845c6376fe7a4053241a2ede8d8ef694df3fcfc37c8'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'Jiangsu Changjing Electronics Technology Co., Ltd.'
        or record.get('part_number_manufacturer') != 'D882(RANGE:160-320)'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:SOT-89-3'
        or record.get('dimensions_mm') != {'length': 4.5, 'width': 2.5, 'height': 1.5}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'sot_89_3'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[4.0, 4.5, 1.52],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination'],
    )
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'Jiangsu Changjing Electronics Technology Co., Ltd.'
    result['represented_mpn'] = 'D882(RANGE:160-320)'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'D882',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 2.0, 'maximum_height_mm': 0.6, 'offset_x_mm': 1.0,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'JSCJ D882 SOT-89 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('D882 is an illustrative identifier; the SOT-89 top marking, typeface, orientation, placement and production codes are unverified.'),
    }
    result['appearance_status'] = ('KiCad SOT-89 model has 4 x 4.5 x 1.52 mm overall bounds. The local PDF is from JCST, a different manufacturer; JSCJ package was independently reviewed online; its SOT-89 marking remains unverified. Finish and marking placement are approximate; not a verified mechanical model or footprint.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true', help='add the validated candidate recipe')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    assert hashlib.sha256((ROOT / 'parts_source' / PART / 'datasheet.pdf').read_bytes()).hexdigest() == '52bef9995ece4200a861c2b940a93862e72f076631151d985d45c7d19addd995'
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
