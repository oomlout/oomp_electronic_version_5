import copy
import json
import numpy as np
import pytest
import yaml

from kicad_agents.display_render import scale_display_geometry
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_samsung_0805_thin_100nf_queue import PART, reviewed_recipe


def test_nonuniform_scaling_transforms_positions_and_normals():
    groups = {'ceramic': {'vertices': [(2, 1, 1)], 'normals': [(1, 0, 1)], 'triangles': []}}
    low, high = scale_display_geometry(groups, np.array([0, 0, 0]), np.array([2, 1.25, 1.25]), [1, 1, .68])
    assert np.allclose(low, [0, 0, 0])
    assert np.allclose(high, [2, 1.25, .85])
    assert np.allclose(groups['ceramic']['vertices'][0], [2, 1, .68])
    normal = np.array([1, 0, 1/.68]); normal /= np.linalg.norm(normal)
    assert np.allclose(groups['ceramic']['normals'][0], normal)


@pytest.mark.parametrize('scale', [[1, 1, 0], [1, 1, -1], [1, 1, float('nan')], [1, 1]])
def test_invalid_scale_is_rejected(scale):
    with pytest.raises(ValueError):
        scale_display_geometry({}, [0, 0, 0], [1, 1, 1], scale)


def test_selected_part_guard():
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8'))
    recipes = json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    recipe = reviewed_recipe(record, recipes, 'test')
    assert recipe['model']['display_scale_xyz'] == [1.0, 1.0, .68]
    assert 'illustrative' in recipe['appearance_status']
    record = copy.deepcopy(record); record['electrical']['rated_voltage'] = '25 V'
    with pytest.raises(ValueError):
        reviewed_recipe(record, recipes, 'test')
