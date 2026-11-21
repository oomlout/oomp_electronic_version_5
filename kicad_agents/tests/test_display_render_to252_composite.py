"""Guard the shared DPAK passes against incompatible package recipes."""
import copy
import json

import pytest

from kicad_agents import display_render_to252_composite as composite
from kicad_agents.display_render_infineon_irlr120n_dpak_queue import PART


@pytest.fixture
def recipes(tmp_path, monkeypatch):
    model = {'sha256': '3eb4c99603a4fe837c2fe9308bc174769ded87a785a0df48d2dc441432ee8b4c',
             'required_roles': ['coating', 'termination'], 'relative_path': 'reviewed.step'}
    recipe = {'package': 'to_252_2_dpak', 'family': 'transistor', 'model': model,
              'marking': {'rotation_degrees': 90, 'maximum_width_mm': 4.8, 'maximum_height_mm': .8},
              'output': {'pixels': 1400, 'samples': 256}}
    candidate = 'electronic_transistor_to_252_test_candidate'
    path = tmp_path / 'recipes.json'
    monkeypatch.setattr(composite.renderer, 'RECIPES', path)
    return path, candidate, recipe


def test_matching_dpak_recipe_accepted(recipes):
    path, candidate, recipe = recipes
    path.write_text(json.dumps({PART: recipe, candidate: copy.deepcopy(recipe)}), encoding='utf8')
    assert composite.read_recipe(candidate) == recipe


@pytest.mark.parametrize('change', ['model', 'family', 'marking', 'sampling'])
def test_incompatible_dpak_recipe_rejected(recipes, change):
    path, candidate, recipe = recipes
    other = copy.deepcopy(recipe)
    if change == 'model':
        other['model']['relative_path'] = 'different-model.step'
    elif change == 'family':
        other['family'] = 'integrated_circuit'
    elif change == 'marking':
        other['marking']['maximum_width_mm'] = 5.0
    else:
        other['output']['samples'] = 64
    path.write_text(json.dumps({PART: recipe, candidate: other}), encoding='utf8')
    with pytest.raises(ValueError):
        composite.read_recipe(candidate)
