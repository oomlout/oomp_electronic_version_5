"""Approximate display-only Micron WB 8 x 6 mm U-PDFN package.

Eight contacts, 1.27 mm pitch and the body outline follow the reviewed
manufacturer drawing. Contact shape and top marking appearance are illustrative.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)

    body = cq.Workplane('XY').box(8.0, 6.0, .615).edges().chamfer(.04).translate((0, 0, .3425)).val()
    add('coating', body)
    for x in (-3.8, 3.8):
        for y in (-1.905, -.635, .635, 1.905):
            add('termination', cq.Workplane('XY').box(.4, .4, .08).translate((x, y, .04)).val())
    marker = cq.Workplane('XY').circle(.18).extrude(.002).translate((-3.2, 2.2, .65)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-4., -3., 0.]), np.array([4., 3., .652]), {'procedural': 1}
