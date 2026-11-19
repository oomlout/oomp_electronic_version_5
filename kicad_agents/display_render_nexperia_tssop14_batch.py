"""Prepare individually sourced Nexperia TSSOP-14 candidates after the pilot.

Read-only by default. Every resulting render still needs individual review.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_nexperia_tssop14_pilot_queue import (
    EVIDENCE as PILOT_EVIDENCE, MODEL_SHA256, PART as PILOT, ROOT, RECIPE_FILE,
)

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_NEXPERIA_TSSOP14_BATCH_EVIDENCE.md'
FOLLOWUP = 'electronic_ic_logic_hex_schmitt_trigger_inverter_tssop_14_nexperia_74hc14pw_118'
FOOTPRINT = 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.nexperia\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != '74HC00PW,118' or pilot.get('marking', {}).get('text') != 'HC00'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TSSOP pilot recipe changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf-8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 12 or len({row[0] for row in rows}) != 12:
        raise ValueError('TSSOP evidence table changed')
    rows.append((FOLLOWUP, '74HC14PW,118', 'HC14', ''))
    result = {}
    for part, mpn, text, _url in rows:
        file = PILOT_EVIDENCE if part == FOLLOWUP else EVIDENCE
        data = (ROOT/file).read_bytes()
        if not any(part in line and mpn in line and f'`{text}`' in line for line in data.decode('utf-8').splitlines()):
            raise ValueError(f'Individual marking evidence changed for {part}')
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf-8')) or {}
        if (record.get('manufacturer') != 'Nexperia' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
            or record.get('dimensions_mm') != {'length':5.0, 'width':4.4, 'height':1.1}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn
        mark = recipe['marking']; mark['text'] = text
        mark['evidence'] = {'file':file, 'sha256':hashlib.sha256(data).hexdigest(),
            'document':'Nexperia TSSOP-14 marking and package review',
            'source_record':f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'Nexperia lists {text} as the package marking. Typeface, '
                                     'orientation, placement and variable lot/date details are illustrative.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'Existing recipe differs for {part}; preserve it')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true')
    args = parser.parse_args(); original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf-8'))
    additions = prepare(recipes)
    if args.add:
        manifest_path = ROOT/'parts'/PILOT/'data/display_render/manifest.json'
        if not manifest_path.is_file(): raise ValueError('Inspect and publish the independent TSSOP pilot first')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest.get('part_id') != PILOT or manifest.get('recipe') != recipes[PILOT]:
            raise ValueError('Published TSSOP pilot differs from current recipe')
        for part, recipe in additions.items(): recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
        if updated != original:
            temp = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                    temp=Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed before replacement')
                os.replace(temp, RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(f'Validated {len(additions)} TSSOP identities and markings; added={args.add}')


if __name__ == '__main__':
    main()
