"""Nominal 451-series ceramic fuse, procedural display geometry in millimetres.

The simplified square ceramic centre and caps follow the manufacturer family
drawing. Small edge rounding and appearance are illustrative, not production CAD.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid fuse display shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.02, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    # A nominal 6.10 mm overall length includes two 1.45 mm end caps.
    add('coating', cq.Workplane('XY').box(3.20, 2.69, 2.69).translate((0, 0, 1.345)).val())
    for x in (-2.325, 2.325):
        cap = cq.Workplane('XY').box(1.45, 2.69, 2.69).edges().fillet(.06)
        add('termination', cap.translate((x, 0, 1.345)).val())
    return dict(groups), np.array([-3.05, -1.345, 0.0]), np.array([3.05, 1.345, 2.69]), {'procedural': 1}
