"""Prepare HC14PW TSSOP-14 only after the HC00PW pilot is published."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_nexperia_tssop14_pilot_queue import (
    EVIDENCE, MODEL_SHA256, PART as PILOT, ROOT, RECIPE_FILE,
)

PART = 'electronic_ic_logic_hex_schmitt_trigger_inverter_tssop_14_nexperia_74hc14pw_118'


def candidate(record, pilot, evidence_bytes):
    if (record.get('manufacturer') != 'Nexperia'
        or record.get('part_number_manufacturer') != '74HC14PW,118'
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm'
        or record.get('dimensions_mm') != {'length': 5.0, 'width': 4.4, 'height': 1.1}):
        raise ValueError('Follow-on identity, footprint or dimensions changed')
    if (pilot.get('represented_mpn') != '74HC00PW,118' or pilot.get('marking', {}).get('text') != 'HC00'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TSSOP pilot recipe changed')
    if not any(PART in line and '74HC14PW,118' in line and '`HC14`' in line
               for line in evidence_bytes.decode('utf-8').splitlines()):
        raise ValueError('Exact follow-on marking evidence changed')
    if pilot['marking']['evidence']['sha256'] != hashlib.sha256(evidence_bytes).hexdigest():
        raise ValueError('Pilot evidence changed')
    result = copy.deepcopy(pilot)
    result['represented_mpn'] = '74HC14PW,118'
    result['marking']['text'] = 'HC14'
    result['marking']['evidence']['source_record'] = f'parts_source/{PART}/working.yaml'
    result['marking']['appearance_status'] = ('Nexperia lists HC14 as the package marking. '
        'Typeface, orientation, placement and variable lot/date details are illustrative.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf-8'))
    record = yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf-8'))
    recipe = candidate(record, recipes[PILOT], (ROOT/EVIDENCE).read_bytes())
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs; preserve it for review')
    if args.add:
        manifest_path = ROOT/'parts'/PILOT/'data/display_render/manifest.json'
        if not manifest_path.is_file():
            raise ValueError('Inspect and publish the independent TSSOP pilot first')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest.get('part_id') != PILOT or manifest.get('recipe') != recipes[PILOT]:
            raise ValueError('Published pilot differs from its current recipe')
        recipes.setdefault(PART, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original:
            raise RuntimeError('Recipes changed during validation; refusing to overwrite')
        if updated != original:
            temp = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                    temp = Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original:
                    raise RuntimeError('Recipes changed before replacement; refusing to overwrite')
                os.replace(temp, RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(PART, 'HC14 candidate only; final image review required')


if __name__ == '__main__':
    main()
