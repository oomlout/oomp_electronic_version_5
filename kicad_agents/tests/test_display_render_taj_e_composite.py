import copy
import json
import pytest
from kicad_agents import display_render_taj_e_composite as compositor
from kicad_agents.display_render_taj_e_batch01_queue import PARTS, PILOT
from kicad_agents.display_render_resistor_queue import RECIPE_FILE


def test_e_compositor_rejects_unreviewed_geometry_and_layout(tmp_path, monkeypatch):
    all_recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    part = next(iter(PARTS))
    recipes = {PILOT: all_recipes[PILOT], part: all_recipes[part]}
    registry = tmp_path / 'recipes.json'
    monkeypatch.setattr(compositor.renderer, 'RECIPES', registry)
    def write(): registry.write_text(json.dumps(recipes), encoding='utf8')
    write()
    assert compositor.read_recipe(part)['represented_mpn'] == PARTS[part][0]
    for field in ('model', 'offset', 'policy'):
        old = copy.deepcopy(recipes[part])
        if field == 'model': recipes[part]['model']['sha256'] = 'incorrect'
        if field == 'offset': recipes[part]['marking']['offset_x_mm'] = 100
        if field == 'policy': recipes[part]['marking']['policy'] = 'none'
        write()
        with pytest.raises(ValueError): compositor.read_recipe(part)
        recipes[part] = old
