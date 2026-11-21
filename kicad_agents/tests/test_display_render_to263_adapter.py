"""Geometry checks for the reviewed D2PAK display adapter."""
import unittest

import numpy as np

from kicad_agents.display_render import locate_model
from kicad_agents.display_render_infineon_irf3205s_to263 import MODEL, MODEL_SHA, load


class D2PakAdapterTests(unittest.TestCase):
    def test_two_full_leads_and_short_centre(self):
        groups, lower, upper, details = load(locate_model(MODEL), {'sha256': MODEL_SHA})
        self.assertEqual(details['centre_lead_external_stub_mm'], .5)
        np.testing.assert_allclose(upper - lower, [15., 10., 4.42], atol=.003)
        vertices = np.asarray(groups['termination']['vertices'])
        full_tips = vertices[vertices[:, 0] < -9.3]
        self.assertTrue(np.any(full_tips[:, 1] < -1.9))
        self.assertTrue(np.any(full_tips[:, 1] > 1.9))
        self.assertFalse(np.any(np.abs(full_tips[:, 1]) < .7))
        centre = vertices[(np.abs(vertices[:, 1]) < .63) & (vertices[:, 0] < -4.625)]
        self.assertTrue(len(centre))
        self.assertAlmostEqual(float(centre[:, 0].min()), -5.125, places=2)

    def test_rejects_unreviewed_model_hash(self):
        with self.assertRaises(ValueError):
            load(locate_model(MODEL), {'sha256': '0' * 64})


if __name__ == '__main__':
    unittest.main()
