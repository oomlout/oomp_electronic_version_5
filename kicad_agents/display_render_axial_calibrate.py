"""Render an isolated synthetic axial band pass for a reviewed recipe."""
import argparse
import json
from pathlib import Path

from kicad_agents import display_render as renderer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    parser.add_argument('colour', choices=('black', 'white'))
    parser.add_argument('folder', type=Path)
    args = parser.parse_args()
    recipes = json.loads(renderer.RECIPES.read_text(encoding='utf8'))
    recipe = recipes[args.part_id]
    if recipe.get('family') != 'axial_resistor' or len(recipe['marking']['bands']) not in (4, 5):
        raise ValueError('Expected a reviewed four- or five-band axial recipe')
    bands = [args.colour] * len(recipe['marking']['bands'])
    recipe['marking'].update(bands=bands, text=' / '.join(bands))
    args.folder.mkdir(parents=True, exist_ok=True)
    isolated = args.folder / f'{args.colour}_recipes.json'
    if isolated.exists():
        raise FileExistsError(isolated)
    isolated.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    renderer.RECIPES = isolated
    renderer.generate(part_id=args.part_id, output=args.folder / args.colour)


if __name__ == '__main__':
    main()
