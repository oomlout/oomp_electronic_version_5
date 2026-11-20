"""Prepare seven individually evidenced TI TSSOP-14 display recipes.

Validation only unless --add is given. Inspect each output before publication.
"""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_nexperia_tssop14_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256
from kicad_agents.display_render_nexperia_tssop14_batch import FOOTPRINT

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_MAXIM_MAX31856_TSSOP14_EVIDENCE.md'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.analog\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != '74HC00PW,118'
        or pilot.get('marking', {}).get('text') != 'HC00'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TSSOP pilot recipe changed')
    raw = (ROOT / EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf-8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != 1:
        raise ValueError('onsemi evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf-8')) or {}
        if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 5.0, 'width': 4.4, 'height': 1.2}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = 'Maxim Integrated'
        recipe['represented_mpn'] = mpn
        recipe['appearance_status'] = ('Illustrative KiCad TSSOP-14 model measures 1.0 mm high; Catalogue lists 1.2 mm height and no footprint; manufacturer and exact MPN fields are absent, so MAX31856MUD+ is a represented example. Not a verified mechanical model.')
        mark = recipe['marking']; mark['text'] = text; mark['policy'] = 'illustrative_literal'
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'Maxim TSSOP-14 illustrative marking and package review',
            'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f"{text} is an illustrative partial family identifier; exact physical marking is not confirmed. Typeface, orientation, placement "
                                     'and variable lot/date details are illustrative.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'Existing recipe differs for {part}; preserve it')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true')
    args = parser.parse_args(); original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf-8'))
    additions = prepare(recipes)
    if args.add:
        manifest = json.loads((ROOT/'parts'/PART/'data/display_render/manifest.json').read_text(encoding='utf-8'))
        if manifest.get('part_id') != PART or manifest.get('recipe') != recipes[PART]:
            raise ValueError('Published independent pilot differs from recipe')
        for part, recipe in additions.items(): recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
        if updated != original:
            temp = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                    temp = Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed before replacement')
                os.replace(temp, RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(f'Validated {len(additions)} onsemi TSSOP identities; added={args.add}')


if __name__ == '__main__': main()
