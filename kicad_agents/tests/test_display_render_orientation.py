import unittest

import numpy as np

from kicad_agents.display_render_orientation import orient_to220_face_up


class To220OrientationTests(unittest.TestCase):
    def test_front_becomes_top_and_bounds_follow_pose(self):
        groups = {'coating': {'vertices': [[2, -1, 4], [7, -1, 12]],
                              'normals': [[0, -1, 0], [0, -1, 0]],
                              'triangles': []}}
        lower, upper = orient_to220_face_up(groups, [2, -1, -15], [7, 3, 13])
        np.testing.assert_allclose(lower, [-13, 2, -3])
        np.testing.assert_allclose(upper, [15, 7, 1])
        np.testing.assert_allclose(groups['coating']['vertices'], [[-4, 2, 1], [-12, 7, 1]])
        np.testing.assert_allclose(groups['coating']['normals'], [[0, 0, 1], [0, 0, 1]])

    def test_rejects_bad_bounds_or_nonfinite_geometry(self):
        with self.assertRaises(ValueError):
            orient_to220_face_up({}, [0, 0, 0], [1, 0, 1])
        with self.assertRaises(ValueError):
            orient_to220_face_up({'coating': {'vertices': [[float('nan'), 0, 0]],
                                               'normals': [[0, 0, 1]]}}, [0, 0, 0], [1, 1, 1])


if __name__ == '__main__':
    unittest.main()
