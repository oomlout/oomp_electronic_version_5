"""Prepare the reviewed onsemi FOD817 SMD-4 display pilot.

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

PART = 'electronic_ic_memory_spi_nand_flash_1_gbit_updfn_8_micron_mt29f1g01abafdwb'
REFERENCE = 'electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MICRON_MT29F1G01_UDFN8_RESEARCH.md')
MODEL = 'kicad_agents/display_model_micron_mt29f1g01_udfn8.py'
MODEL_SHA256 = 'd5763d5662010ade13aae69ec858bfa2568d2da42ef5e02046317beec0e8dd8b'


def reviewed_recipe(record, recipes, evidence_sha256):
    """Reject changed source identity or an unreviewed reference model."""
    if (record.get('manufacturer') not in ('', None)
        or record.get('part_number_manufacturer') != 'MT29F1G01ABAFDWB'
        or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
        or record.get('dimensions_mm') != {'length': 6.0, 'width': 5.0}):
        raise ValueError('Pilot identity, footprint or dimensions changed; review again')
    reference = recipes[REFERENCE]
    if (reference.get('family') != 'integrated_circuit'
        or reference.get('model', {}).get('required_roles') != ['coating', 'termination', 'pin_indicator']):
        raise ValueError('Reviewed SOIC material reference changed')
    result = copy.deepcopy(reference)
    result['package'] = 'micron_mt29f1g01_udfn8'
    result['disable_bump_for'] = ['coating', 'termination', 'pin_indicator']
    result['model'].update(
        relative_path=MODEL,
        source_url='https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        expected_bounds_mm=[8.0, 6.0, 0.652],
        sha256=MODEL_SHA256,
    )
    result['model']['copyright'] = 'Procedural model generated in this repository'
    result['model']['license'] = 'Project source; procedural display geometry'
    result['model'].pop('license_url', None)
    result['model'].pop('role_by_source_colour', None)
    result['represented_manufacturer'] = 'Micron (inferred from family and datasheet)'
    result['represented_mpn'] = 'MT29F1G01ABAFDWB'
    result['marking'] = {
        'policy': 'illustrative_literal', 'text': 'MT29F1G01',
        'font_file': 'arialbd.ttf', 'rotation_degrees': 90,
        'maximum_width_mm': 4.0, 'maximum_height_mm': 0.7,
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha256,
                     'document': 'Micron MT29F1G01 U-PDFN package review',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': ('MT29F1G01 is an illustrative partial family identifier; exact physical marking and complete orderable are unverified. '
                              'Typeface, orientation, placement and variable lot/date details are illustrative.'),
    }
    result['appearance_status'] = ('Procedural eight-terminal model has 8 x 6 x 0.65 mm body and 1.27 mm pitch, based on the reviewed Micron WB drawing. Catalogue 6 x 5 mm dimensions conflict; manufacturer Micron is inferred, complete orderable and footprint are missing. Terminal form, marking and pin-one indicator appearance are approximate; not a verified mechanical model or footprint.')
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
