"""Prepare the reviewed MaxLinear SP3243E SSOP-28 display pilot.

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

PART = 'electronic_ic_interface_rs_232_transceiver_ssop_28_208mil_maxlinear_sp3243eea_l_tr'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MAXLINEAR_SP3243E_SSOP28_RESEARCH.md')
MODEL = 'Package_SO.3dshapes/SSOP-28_5.3x10.2mm_P0.65mm.step'
MODEL_SHA256 = '7aa76979ae41da44bded1ed74115012868f2f3f5a757faf32bb9df4f92c1e313'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') != 'MaxLinear'
        or record.get('part_number_manufacturer') != 'SP3243EEA-L/TR'
        or (record.get('kicad') or {}).get('machine_solder') != ''
        or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'ssop_28_5_3mm'
    result['model'].update(
        relative_path=MODEL,
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
        expected_bounds_mm=[7.8, 10.2, 2.1],
        sha256=MODEL_SHA256,
        role_by_source_colour={'0.148,0.145,0.145':'coating','0.824,0.820,0.781':'termination','0.691,0.664,0.598':'pin_indicator'},
        required_roles=['coating','termination','pin_indicator'],
    )
    result['model']['display_scale_xyz'] = [1.0, 1.0, 0.9047619047619048]
    result['represented_manufacturer'] = 'MaxLinear'
    result['represented_mpn'] = 'SP3243EEA-L/TR'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'SP3243E',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 6.0, 'maximum_height_mm': 1.2,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'MaxLinear SP3243E SSOP-28 package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('SP3243E is an illustrative family identifier; exact physical top marking is unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('The KiCad SSOP-28 model has 7.8 x 10.2 x 2.1 mm source bounds; it is scaled vertically to 1.9 mm for display because MaxLinear specifies a 2.0 mm maximum. Source lists generic 10 x 5 mm without a dimension reference. Not a verified mechanical model or footprint.')
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
