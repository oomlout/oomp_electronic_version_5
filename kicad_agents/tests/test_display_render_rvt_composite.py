import copy
import json

import pytest
from kicad_agents import display_render_rvt_composite as compositor
from kicad_agents.display_render_resistor_queue import RECIPE_FILE
from kicad_agents.display_render_rvt_8mm_batch01_queue import PILOT, PARTS


def test_compositor_rejects_changed_geometry_and_marking_position(tmp_path, monkeypatch):
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    target = next(iter(PARTS))
    reduced = {PILOT: recipes[PILOT], target: recipes[target]}
    registry = tmp_path / 'recipes.json'
    def write():
        registry.write_text(json.dumps(reduced), encoding='utf8')
    write()
    monkeypatch.setattr(compositor.renderer, 'RECIPES', registry)
    assert compositor.read_recipe(target)['represented_mpn'] == PARTS[target][0]
    for mutate in ('offset', 'model', 'package'):
        original = copy.deepcopy(reduced[target])
        if mutate == 'offset': reduced[target]['marking']['offset_x_mm'] = 100
        if mutate == 'model': reduced[target]['model']['sha256'] = 'wrong'
        if mutate == 'package': reduced[target]['package'] = 'unreviewed'
        write()
        with pytest.raises(ValueError): compositor.read_recipe(target)
        reduced[target] = original
