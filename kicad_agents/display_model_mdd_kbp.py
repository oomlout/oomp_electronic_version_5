"""Procedural display-only MDD KBP bridge geometry from the reviewed outline.

The front is horizontal in XY for rendering: +X runs across the pin row,
+Y points toward the bevelled top, and +Z is the marked front face. The body
is 14.0 x 10.6 x 3.2 mm with four 0.8 x 0.4 mm leads at 3.81 mm pitch;
13.2 mm projects beyond the body. The front-left upper corner is bevelled.
Lead shoulders, finish, and the edge chamfer are illustrative.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.02, .08)
            group = groups[role]; offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in t) for t in triangles)

    outline = [(-7.0, -5.3), (7.0, -5.3), (7.0, 5.3), (-5.8, 5.3), (-7.0, 4.1)]
    body = cq.Workplane('XY').polyline(outline).close().extrude(3.2).val()
    add('coating', body)
    for x in (-5.715, -1.905, 1.905, 5.715):
        lead = cq.Workplane('XY').box(.8, 13.3, .4).translate((x, -11.85, .35)).val()
        add('termination', lead)
    return dict(groups), np.array([-7.0, -18.5, 0.0]), np.array([7.0, 5.3, 3.2]), {'procedural': 1}
