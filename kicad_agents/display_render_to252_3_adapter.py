"""Assign reviewed material roles to KiCad's uncoloured TO-252-3 model.

The exact STEP file and all five solid signatures are checked before any
material is assigned.  Unlike TO-252-2, this version has three full leads.
"""
from collections import defaultdict

from kicad_agents import display_render as renderer

MODEL = 'Package_TO_SOT_SMD.3dshapes/TO-252-3_TabPin2.step'
MODEL_SHA = 'd3b527bc2ffb1900637eb60126d6a2059bde4028a65379615039436cd5d49a84'
SIGNATURES = [
    ('coating', 83.27705, (-3.11, 3.11, -3.25, 3.25, .02, 2.32)),
    ('termination', 11.70183, (-1.13, 4.11, -2.7, 2.7, 0., .5)),
    ('termination', 1.6019, (-5.79, -2.2377, -2.775, -1.785, 0., 1.4399)),
    ('termination', 1.6019, (-5.79, -2.2377, -.495, .495, 0., 1.4399)),
    ('termination', 1.6019, (-5.79, -2.2377, 1.785, 2.775, 0., 1.4399)),
]


def load(path, specification):
    import cadquery as cq
    import numpy as np

    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed TO-252-3 model')
    solids = cq.importers.importStep(str(path)).solids().vals()
    if len(solids) != len(SIGNATURES):
        raise ValueError('Unexpected TO-252-3 solid count')
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})
    for solid, (role, volume, expected) in zip(solids, SIGNATURES):
        box = solid.BoundingBox()
        actual = (box.xmin, box.xmax, box.ymin, box.ymax, box.zmin, box.zmax)
        if not solid.isValid() or abs(solid.Volume() - volume) > .005 or not np.allclose(actual, expected, atol=.003, rtol=0):
            raise ValueError('TO-252-3 solid differs from reviewed geometry')
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)
    if set(groups) != {'coating', 'termination'}:
        raise ValueError('Unexpected material regions')
    return dict(groups), np.array([-5.79, -3.25, 0.]), np.array([4.11, 3.25, 2.32]), {'reviewed_solids': len(solids)}
