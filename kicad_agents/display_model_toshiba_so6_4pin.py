"""Illustrative Toshiba four-lead SO6 package for display only.

Nominal body 4.55 x 3.7 mm, height 2.1 mm, span 7.0 mm and 2.54 mm
pin pitch follow Toshiba's SO6 drawing. Lead shape and marker are approximate.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(0.003, 0.08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)

    body = cq.Workplane('XY').box(4.55, 3.7, 2.0).edges().chamfer(0.1).translate((0, 0, 1.1)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (2.12, 1.3), (2.48, 1.3), (2.85, 0.19), (3.5, 0.19),
            (3.5, 0.02), (2.72, 0.02), (2.34, 1.1), (2.12, 1.1),
        ]]
        for index in range(2):
            y = (index - 0.5) * 2.54
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.4).translate((0, y + 0.2, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.16).extrude(0.002).translate((-1.45, 1.08, 2.1)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-3.5, -1.85, 0.02]), np.array([3.5, 1.85, 2.102]), {'procedural': 1}
