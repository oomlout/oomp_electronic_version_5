"""Stage one blue axial render that cannot use the shared five-band passes."""
import argparse
import json

from kicad_agents.display_render import ROOT, RECIPES, generate
from kicad_agents.display_render_axial_composite import recipe_for
from kicad_agents.display_render_restore_blue import STAGING, blue_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    args = parser.parse_args()
    part = args.part_id
    recipes = json.loads(RECIPES.read_text(encoding='utf8'))
    recipe = recipes[part]
    if recipe.get('family') != 'axial_resistor':
        raise ValueError('Not an axial resistor')
    try:
        recipe_for(part)
    except ValueError:
        pass
    else:
        raise ValueError('Use the reviewed shared-pass batch for this part')
    dest = STAGING / part
    if dest.exists():
        raise FileExistsError(f'Existing staging preserved: {dest}')
    recipe['appearance_status'] = blue_status(recipe.get('appearance_status', ''))
    recipe['appearance_status'] += ' Blue body shade is illustrative.'
    if 'appearance_status' in recipe['marking']:
        recipe['marking']['appearance_status'] = blue_status(recipe['marking']['appearance_status'])
    recipes[part] = recipe
    RECIPES.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    generate(part_id=part, output=dest)


if __name__ == '__main__':
    main()
