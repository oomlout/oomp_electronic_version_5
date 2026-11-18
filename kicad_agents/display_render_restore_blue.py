"""Restore the reviewed original blue finish on compatible axial displays.

Stage shared-pass images for visual review. Existing outputs and pages are not
overwritten by this command. Publish only after reviewing the staged images.
"""
import copy
import json
from pathlib import Path

from kicad_agents.display_render import RECIPES, ROOT
from kicad_agents.display_render_axial_composite import recipe_for, render

MASTER = ROOT / 'source_file/display_render/masters/24db4ef9524c55fec4537df7a798e65e02f02279125426a553107b4a9cc5dbb9'
STAGING = ROOT / 'tmp/display_render/restore_blue_staged'


def blue_status(text):
    return (text.replace('Traditional beige', 'Blue').replace('traditional beige', 'blue')
            .replace('Beige', 'Blue').replace('beige', 'blue'))


def main():
    recipes = json.loads(RECIPES.read_text(encoding='utf8'))
    master = json.loads((MASTER / 'manifest.json').read_text(encoding='utf8'))
    selected = []
    for part, recipe in recipes.items():
        if recipe.get('family') != 'axial_resistor':
            continue
        try:
            recipe_for(part)
        except ValueError:
            continue
        if recipe['model'] != master['inputs']['model']:
            continue
        selected.append(part)
    STAGING.mkdir(parents=True, exist_ok=True)
    backup = STAGING / 'original_recipes.json'
    if backup.exists():
        raise FileExistsError(f'Prior staging exists: {backup}')
    backup.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part in selected:
        recipe = copy.deepcopy(recipes[part])
        recipe['appearance_status'] = blue_status(recipe.get('appearance_status', ''))
        recipe['appearance_status'] += ' Blue body shade is illustrative.'
        if 'appearance_status' in recipe['marking']:
            recipe['marking']['appearance_status'] = blue_status(recipe['marking']['appearance_status'])
        recipes[part] = recipe
    RECIPES.write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for part in selected:
        render(part, MASTER, STAGING / part)
    (STAGING / 'selected.json').write_text(json.dumps(selected, indent=2) + '\n', encoding='utf8')
    print('Staged', len(selected), 'blue axial renders for review.')


if __name__ == '__main__':
    main()
