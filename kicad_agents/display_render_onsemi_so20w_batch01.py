"""Prepare individually evidenced Nexperia SO20W follow-ons after pilot review."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_nexperia_so20w_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_SO20W_BATCH01_EVIDENCE.md'
FOOTPRINT = 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.onsemi\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != '74HC244D,653' or pilot.get('marking', {}).get('text') != '74HC244D'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256
        or pilot.get('model', {}).get('display_scale_xyz') != [1.0, 1.0, 2.65/2.75]
        or 'scaled vertically' not in pilot.get('appearance_status', '')):
        raise ValueError('SO20W pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 3 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
            or record.get('dimensions_mm') != {'length': 12.8, 'width': 7.5, 'height': 2.65}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn; recipe['represented_manufacturer'] = 'onsemi'
        recipe['appearance_status'] = ('Illustrative KiCad SOIC-20W model scaled vertically from 2.75 mm to catalogue 2.65 mm; onsemi case 751BJ specifies 2.64 mm maximum. Display approximation, not a verified mechanical model.')
        mark = recipe['marking']; mark['text'] = text
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'onsemi SO20W marking and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'onsemi lists {text} as the package marking. Typeface, orientation, '
                                     'placement and variable lot/date details are illustrative.')
        if mpn == 'MM74HC244WMX':
            mark['policy'] = 'illustrative_literal'
            mark['appearance_status'] = 'HC244A is an illustrative example shown in the SOIC diagram; the legend says HC240A and the order table does not explicitly map a mark to this orderable. Typeface, placement and variable codes are illustrative.'
        if part in recipes and recipes[part] != recipe: raise ValueError(f'Conflicting recipe for {part}')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true')
    args = parser.parse_args(); original = RECIPE_FILE.read_bytes(); recipes = json.loads(original.decode('utf8'))
    additions = prepare(recipes)
    if args.add:
        m = json.loads((ROOT/'parts'/PART/'data/display_render/manifest.json').read_text(encoding='utf8'))
        if m.get('part_id') != PART or m.get('recipe') != recipes[PART]: raise ValueError('Published pilot changed')
        for part, recipe in additions.items(): recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf8')
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
    print(f'Validated {len(additions)} onsemi SO20W identities; added={args.add}')


if __name__ == '__main__': main()
