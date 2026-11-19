"""Prepare an evidenced TI TLC555CD SOIC-8 example."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_ti_soic8_pilot_queue import MODEL_SHA256, PART, ROOT, RECIPE_FILE
from kicad_agents.display_render_ti_soic8_batch import FOOTPRINT

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_TI_TLC555CD_EXAMPLE_EVIDENCE.md'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.ti\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != 'NE5532DR' or pilot.get('marking', {}).get('text') != 'N5532'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256): raise ValueError('Reviewed SOIC-8 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != 1: raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') not in (None, '') or record.get('part_number_manufacturer') not in (None, '') or mpn != 'TLC555CD' or 'tlc555cd' not in record.get('lcsc_search', '').lower()
            or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
            or record.get('dimensions_mm') != {'length': 4.9, 'width': 3.9, 'height': 1.75}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_manufacturer'] = 'Texas Instruments'; recipe['represented_mpn'] = mpn
        recipe['appearance_status'] = ('Illustrative TI TLC555CD example with KiCad SOIC-8 model; catalogue source does not specify manufacturer or manufacturer part number. TI D0008A specifies 1.75 mm maximum height. TLC555CD is listed obsolete by TI.')
        mark = recipe['marking']; mark['text'] = text
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'TI TLC555CD example marking and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'TI lists {text} as TLC555CD marking. Typeface, placement, logo and variable date/traceability details are illustrative.')
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
    print(f'Validated {len(additions)} TI TLC555CD examples; added={args.add}')


if __name__ == '__main__': main()
