"""Procedural SOT-523 visual geometry, based on the reviewed CBI outline.

Nominal body 1.6 x 0.8 mm, overall lead span 1.6 mm, height 0.7 mm,
and same-side lead spacing 1.0 mm. Bends and edge bevels are illustrative.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    body = cq.Workplane('XY').box(.8, 1.6, .6).edges().chamfer(.035).translate((0, 0, .4)).val()
    add('coating', body)
    # Three nominal gullwing terminals: two on the left, one on the right.
    # The polygon describes a single lead in X/Z, then it is extruded along Y.
    for side, center in [(-1, -.5), (-1, .5), (1, 0.0)]:
        profile = [(side * x, z) for x, z in [(.36, .22), (.51, .22), (.62, .09), (.8, .09),
                                              (.8, 0.0), (.57, 0.0), (.46, .13), (.36, .13)]]
        lead = cq.Workplane('XZ').polyline(profile).close().extrude(.30).translate((0, center + .15, 0)).val()
        add('termination', lead)
    return dict(groups), np.array([-.8, -.8, 0.0]), np.array([.8, .8, .7]), {'procedural': 1}
