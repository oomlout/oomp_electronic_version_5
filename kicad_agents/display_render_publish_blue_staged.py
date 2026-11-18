"""Publish visually reviewed staged blue axial renders one part at a time."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from kicad_agents.display_render import ROOT, RECIPES
from kicad_agents.publish_display_render import publish

STAGING = ROOT / 'tmp/display_render/restore_blue_staged'
BACKUP = ROOT / 'tmp/display_render/restore_blue_previous'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--part', help='Publish one independently reviewed staged part')
    parser.add_argument('--four', action='store_true', help='Publish the reviewed four-band batch')
    parser.add_argument('--index', help='Publish a named, visually reviewed staging index')
    args = parser.parse_args()
    recipes = json.loads(RECIPES.read_text(encoding='utf8'))
    if sum(bool(x) for x in (args.part, args.four, args.index)) > 1:
        raise ValueError('Choose one publication mode')
    if args.index and (Path(args.index).name != args.index or not args.index.endswith('.json')):
        raise ValueError('Index must be a JSON filename')
    parts = [args.part] if args.part else json.loads((STAGING / (args.index or ('selected_four.json' if args.four else 'selected.json'))).read_text(encoding='utf8'))
    extra = 'electronic_resistor_quarter_watt_through_hole_6800000_ohm'
    if not args.part and not args.four and not args.index and (STAGING / extra / 'manifest.json').is_file():
        parts.append(extra)
    for part in parts:
        src = STAGING / part
        manifest = json.loads((src / 'manifest.json').read_text(encoding='utf8'))
        if manifest['part_id'] != part or manifest['recipe'] != recipes[part]:
            raise ValueError(f'Staged recipe differs: {part}')
        for name, meta in manifest['artifacts'].items():
            path = src / name
            if hashlib.sha256(path.read_bytes()).hexdigest() != meta['sha256']:
                raise ValueError(f'Staged image changed: {path}')
        paths = [ROOT / 'parts_source' / part / 'working.yaml']
        paths += [ROOT / 'parts' / part / name for name in ('working.yaml', 'README.md', 'web.yaml')]
        paths += [ROOT / 'parts' / part / 'data/display_render' / name for name in ('manifest.json', 'render.png', 'preview.webp')]
        for old in paths:
            if old.is_file():
                dest = BACKUP / old.relative_to(ROOT)
                if not dest.exists():
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(old, dest)
        target = ROOT / 'parts' / part / 'data/display_render'
        target.mkdir(parents=True, exist_ok=True)
        for name in ('manifest.json', 'render.png', 'preview.webp'):
            shutil.copy2(src / name, target / name)
        publish(part)
    print('Published', len(parts), 'reviewed blue renders.')


if __name__ == '__main__':
    main()
