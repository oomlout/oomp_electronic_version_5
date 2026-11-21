"""Procedural, display-only MDD W06/WOM outline from the family drawing.

The black moulded body is an 8.8 mm diameter by 5.5 mm cylinder. Four
0.75 mm diameter contacts use a 5.1 mm square pitch. The positive contact
extends 21 mm below the body; the other three extend 18 mm. Pin end shape,
surface finish and top-face markings are illustrative.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.02, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    body = cq.Workplane('XY').circle(4.4).extrude(5.5).translate((0, 0, 18)).val()
    add('coating', body)
    for x, y, bottom in [(-2.55, 2.55, -3.0), (2.55, 2.55, 0.0),
                          (-2.55, -2.55, 0.0), (2.55, -2.55, 0.0)]:
        lead = cq.Workplane('XY').circle(.375).extrude(18-bottom).translate((x, y, bottom)).val()
        add('termination', lead)
    return dict(groups), np.array([-4.4, -4.4, -3.0]), np.array([4.4, 4.4, 23.5]), {'procedural': 1}
