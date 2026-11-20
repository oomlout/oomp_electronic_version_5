"""Prepare the individually evidenced onsemi 6N137M DIP-8 display."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_ti_dip8_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256

EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_6N137M_DIP8_EVIDENCE.md'
FOOTPRINT = 'Package_DIP:DIP-8_W7.62mm'
ROW = re.compile(r'^\| `([^`]+)` \| ([^|]+?) \| `([^`]+)` \| \[[^]]+\]\((https://www\.onsemi\.com/[^)]+)\) \|$')


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != 'TL072CP' or pilot.get('marking', {}).get('text') != 'TL072CP'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256
        or pilot.get('model', {}).get('required_roles') != ['coating', 'termination']
        or 'projecting pins' not in pilot.get('appearance_status', '')):
        raise ValueError('DIP-8 pilot changed')
    raw = (ROOT/EVIDENCE).read_bytes()
    rows = [m.groups() for line in raw.decode('utf8').splitlines() if (m := ROW.match(line))]
    if len(rows) != 1 or len({r[0] for r in rows}) != len(rows): raise ValueError('Evidence table changed')
    result = {}
    for part, mpn, text, _ in rows:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') not in ('', None)
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        recipe = copy.deepcopy(pilot); recipe['represented_mpn'] = mpn; recipe['represented_manufacturer'] = 'onsemi'
        recipe['appearance_status'] = 'Illustrative generic KiCad DIP-8 model. Source lists 10 x 5 mm without width reference, height or footprint; onsemi case 646CQ nominal body is 9.655 x 6.6 mm. Model overall bounds 7.874 x 9.270 x 6.980 mm include projecting pins. Molded notch is an illustrative pin-one indicator and is not confirmed for this part. Not a verified mechanical model or footprint.'
        mark = recipe['marking']; mark['text'] = text
        mark['evidence'] = {'file': EVIDENCE, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'onsemi PDIP marking and package review', 'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'onsemi depicts {text} as the package marking. Typeface, '
                                     'placement and orientation are illustrative; manufacturer logo and variable lot/date details are omitted.')
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
    print(f'Validated {len(additions)} onsemi DIP-8 identities; added={args.add}')


if __name__ == '__main__': main()
