import numpy as np
import pytest
from kicad_agents.radial_display_geometry import straight_sleeve_triangles, stretch_sleeve, sleeve_triangle_uv


def test_stretch_preserves_leads_and_moves_cap():
    vertices = [[0, 0, -2], [1, 0, -1], [0, 1, 0],
                [1, 0, 2], [0, 1, 4], [-1, 0, 6],
                [1, 0, 8], [0, 1, 9], [-1, 0, 10]]
    normals = [[1, 0, 0]] * len(vertices)
    out, transformed = stretch_sleeve(vertices, normals, [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 2, 6, 4)
    assert np.allclose(out[:3], vertices[:3])
    assert np.allclose(out[3:6, 2], [2, 6, 10])
    assert np.allclose(out[6:, 2], [12, 13, 14])
    assert np.allclose(np.linalg.norm(transformed, axis=1), 1)


def test_stretch_refuses_triangles_crossing_deformation_boundary():
    with pytest.raises(ValueError, match='crosses'):
        stretch_sleeve([[1, 0, 1], [0, 1, 3], [-1, 0, 4]], [[1, 0, 0]] * 3, [[0, 1, 2]], 2, 6, 4)


def test_stretch_transforms_boundary_normals_and_rejects_ambiguous_sharing():
    vertices = [[1, 0, 2], [0, 1, 3], [-1, 0, 4]]
    normals = [[1, 0, 1]] * 3
    _, transformed = stretch_sleeve(vertices, normals, [[0, 1, 2]], 2, 6, 4)
    assert np.allclose(transformed[0], np.array([1, 0, .5]) / np.sqrt(1.25))
    vertices += [[1, 1, 1], [0, 0, 1]]
    normals += [[1, 0, 1]] * 2
    with pytest.raises(ValueError, match='shared sloped normals'):
        stretch_sleeve(vertices, normals, [[0, 1, 2], [0, 3, 4]], 2, 6, 4)


def test_cylindrical_mapping_unwraps_seam_without_distorting_triangle():
    angles = np.deg2rad([359, 1, 5])
    vertices = [[np.cos(a), np.sin(a), z] for a, z in zip(angles, [0, .5, 1])]
    uv = sleeve_triangle_uv(vertices, [[0, 1, 2]], [0, 0], 0, 1)
    assert uv.shape == (1, 3, 2)
    assert np.ptp(uv[0, :, 0]) < .02
    assert np.allclose(uv[0, :, 1], [0, .5, 1])


def test_cylindrical_mapping_rejects_axis_and_out_of_height():
    with pytest.raises(ValueError, match='axis'):
        sleeve_triangle_uv([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 1, 2]], [0, 0], 0, 1)
    with pytest.raises(ValueError, match='height'):
        sleeve_triangle_uv([[1, 0, 0], [1, 1, .5], [0, 1, 2]], [[0, 1, 2]], [0, 0], 0, 1)


def test_sleeve_selection_excludes_top_and_non_cylindrical_faces():
    vertices = [[1, 0, 0], [0, 1, .5], [-1, 0, 1],
                [0, 0, 1], [1, 0, 1], [0, 1, 1],
                [1, 0, 2], [0, 1, 2], [-1, 0, 2]]
    mask = straight_sleeve_triangles(vertices, [[0, 1, 2], [3, 4, 5], [6, 7, 8]], [0, 0], 1, 0, 1)
    assert mask.tolist() == [True, False, False]
