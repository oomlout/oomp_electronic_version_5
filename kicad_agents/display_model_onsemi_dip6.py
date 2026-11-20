"""Illustrative onsemi 646BX DIP-6 mesh; no CAD files are exported.

The 8.51 x 6.35 mm body and 2.54 mm pitch follow onsemi's package index.
Pin length, lead shape, body chamfers and the pin-one dot are approximations.
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

    body = cq.Workplane('XY').box(6.35, 8.51, 3.5).edges().chamfer(0.16).translate((0, 0, 5.05)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (3.05, 4.55), (3.82, 4.55), (4.05, 4.20), (4.05, 0.0),
            (3.75, 0.0), (3.75, 4.10), (3.05, 4.25),
        ]]
        for index in range(3):
            y = (index - 1) * 2.54
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.48).translate((0, y + 0.24, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.25).extrude(0.002).translate((-2.05, 3.0, 6.8)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-4.05, -4.255, 0.0]), np.array([4.05, 4.255, 6.802]), {'procedural': 1}
