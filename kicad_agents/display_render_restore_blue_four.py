"""Stage compatible four-band blue axial images from a reviewed master."""
import argparse
import copy
import json
from pathlib import Path

from kicad_agents.display_render import RECIPES
from kicad_agents.display_render_axial_composite import recipe_for, render
from kicad_agents.display_render_restore_blue import STAGING, blue_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('master', type=Path)
    parser.add_argument('--index', default='selected_four.json')
    args = parser.parse_args()
    if Path(args.index).name != args.index or not args.index.endswith('.json'):
        raise ValueError('Index must be a JSON filename')
    index = STAGING / args.index
    if index.exists():
        raise FileExistsError(f'Existing batch index preserved: {index}')
    recipes = json.loads(RECIPES.read_text(encoding='utf8'))
    master = json.loads((args.master / 'manifest.json').read_text(encoding='utf8'))
    selected = []
    for part, recipe in recipes.items():
        if recipe.get('family') != 'axial_resistor' or len(recipe.get('marking', {}).get('bands', [])) != 4:
            continue
        try:
            recipe_for(part)
        except ValueError:
            continue
        if recipe['model'] != master['inputs']['model'] or (STAGING / part).exists():
            continue
        selected.append(part)
    for part in selected:
        recipe = copy.deepcopy(recipes[part])
        recipe['appearance_status'] = blue_status(recipe.get('appearance_status', '')) + ' Blue body shade is illustrative.'
        if 'appearance_status' in recipe['marking']:
            recipe['marking']['appearance_status'] = blue_status(recipe['marking']['appearance_status'])
        recipes[part] = recipe
    RECIPES.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part in selected:
        render(part, args.master, STAGING / part)
    index.write_text(json.dumps(selected, indent=2) + '\n', encoding='utf8')
    print('Staged', len(selected), 'four-band blue renders for review.')


if __name__ == '__main__':
    main()
