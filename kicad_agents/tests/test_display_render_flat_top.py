import numpy as np
import pytest

from kicad_agents.display_render_radial import replace_grooved_top


def sample_group():
    return {'vertices': [[0, 0, -2], [.2, 0, -2], [0, .2, 0],
                         [0, 0, 3.7], [1, 0, 3.9], [0, 1, 3.9]],
            'normals': [[0, 0, 1]] * 6,
            'triangles': [[0, 1, 2], [3, 4, 5]]}


def test_preserves_lead_and_replaces_top_with_upward_fan():
    result = replace_grooved_top(sample_group(), center_xy=[0, 0], radius=1,
                                 cutoff_z=3.5, disk_z=3.9, segments=32)
    assert result['triangles'][0] == [0, 1, 2]
    assert len(result['triangles']) == 33
    v = np.asarray(result['vertices'])
    for triangle in result['triangles'][1:]:
        points = v[triangle]
        assert np.allclose(points[:, 2], 3.9)
        assert np.cross(points[1]-points[0], points[2]-points[0])[2] > 0


def test_refuses_intersecting_or_unexpected_geometry():
    group = sample_group()
    group['triangles'].append([0, 4, 5])
    with pytest.raises(ValueError, match='crosses'):
        replace_grooved_top(group, center_xy=[0, 0], radius=1, cutoff_z=3.5, disk_z=3.9)
    group = sample_group()
    group['vertices'][4][0] = 2
    with pytest.raises(ValueError, match='radius'):
        replace_grooved_top(group, center_xy=[0, 0], radius=1, cutoff_z=3.5, disk_z=3.9)
