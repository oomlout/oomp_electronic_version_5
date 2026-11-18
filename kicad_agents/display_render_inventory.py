"""Inventory catalogue render state without generating or modifying parts.

The report distinguishes valid manifest metadata, queued recipes, older model
images and parts that still require research. It does not determine whether a
model or marking can be sourced merely from a part's name.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

from working_oomp_populate_display_render import ROOT, apply_extras


def inventory(root=ROOT):
    recipes = json.loads((root / 'source_file/display_render/recipes.json').read_text(encoding='utf-8'))
    # The metadata validator uses the actual repository root and verifies recipe,
    # evidence, studio, renderer and output hashes, including archived renderers.
    if root.resolve() != ROOT.resolve():
        raise ValueError('Inventory must use the active repository root')
    extras = {part_id: {} for part_id in recipes}
    apply_extras(extras)
    result = []
    for directory in sorted((root / 'parts_source').glob('electronic_*')):
        if not directory.is_dir() or not (directory / 'working.yaml').is_file():
            continue
        part_id = directory.name
        fields = part_id.split('_')
        category = fields[1] if len(fields) > 1 else 'unknown'
        part = root / 'parts' / part_id
        manifest = part / 'data/display_render/manifest.json'
        legacy = part / 'data/model_3d_render.png'
        if extras.get(part_id, {}).get('display_render'):
            state = 'render_valid'
        elif part_id in recipes and manifest.is_file():
            state = 'render_needs_validation'
        elif part_id in recipes:
            state = 'recipe_prepared'
        elif legacy.is_file():
            state = 'legacy_render_needs_review'
        else:
            state = 'needs_research'
        result.append({'id': part_id, 'category': category, 'state': state,
                       'generated_record_exists': (part / 'working.yaml').is_file()})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rows = inventory()
    summary = defaultdict(Counter)
    for row in rows:
        summary[row['category']][row['state']] += 1
    payload = {'summary': {category: dict(counts) for category, counts in sorted(summary.items())},
               'parts': rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(f'Inventoried {len(rows)} electronic component records: {args.output}')
    for category, counts in sorted(summary.items()):
        print(category, dict(counts))


if __name__ == '__main__':
    main()
