import numpy as np
import json
import pytest
from PIL import Image
from kicad_agents.display_render_radial import prepare_radial, create_radial_textures, write_meshes


def test_standard_renderer_rejects_radial_recipe_before_model_loading(tmp_path, monkeypatch):
    from kicad_agents import display_render
    recipes = tmp_path / 'recipes.json'
    recipes.write_text(json.dumps({'example': {'family': 'radial_aluminum_capacitor'}}), encoding='utf-8')
    monkeypatch.setattr(display_render, 'RECIPES', recipes)
    with pytest.raises(ValueError, match='display_render_radial'):
        display_render.generate('example', check=True)


def test_radial_adapter_keeps_top_unprinted_and_preserves_leads(tmp_path):
    vertices = [[1, 0, .5], [0, 1, 1], [-1, 0, 1.5], [0, 0, 2], [1, 0, 2], [0, 1, 2]]
    normals = [[1, 0, 0]] * 6
    groups = {'coating': {'vertices': vertices, 'normals': normals, 'triangles': [[0, 1, 2], [3, 4, 5]]},
              'termination': {'vertices': [[0, 0, -2], [1, 0, -1], [0, 1, 0]],
                              'normals': [[1, 0, 0]] * 3, 'triangles': [[0, 1, 2]]}}
    params = {'center_xy': [0, 0], 'radius': 1, 'lower_z': .5, 'upper_z': 1.5,
              'extra_height': 1, 'tolerance': .05}
    groups, lower, upper = prepare_radial(groups, np.array([-1, -1, -2]), np.array([1, 1, 2]),
        {'model': {'radial_stretch': params}}, {'camera_direction': [1, -1, 1]})
    assert len(groups['coating']['triangles']) == 1
    assert len(groups['sleeve_background']['triangles']) == 1
    assert groups['termination']['vertices'][0][2] == -2
    assert upper[2] == 3
    write_meshes(groups, lower, upper, tmp_path)
    assert (tmp_path / 'coating.obj').read_text(encoding='ascii').count('\nvt ') == 3


def test_radial_texture_contains_text_and_preserves_background(tmp_path):
    marking = {'font_file': 'arialbd.ttf', 'maximum_width_mm': 2, 'maximum_height_mm': 1}
    params = {'radius': 2, 'lower_z': 1, 'upper_z': 4, 'extra_height': 2}
    result = create_radial_textures(marking, '100uF\n50V', params, tmp_path)
    image = np.asarray(Image.open(tmp_path / 'marking.png'))
    assert result['sha256'] and image.max() == 255 and image[0, 0] == 0
    assert np.count_nonzero(image) > 100
