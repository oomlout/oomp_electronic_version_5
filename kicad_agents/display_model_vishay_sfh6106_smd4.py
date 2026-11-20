"""Illustrative four-lead Vishay SFH6106 surface-mount optocoupler mesh.

Nominal body 6.645 x 4.69 mm, body height 3.555 mm, lead span 9.78 mm and
2.54 mm pitch follow Vishay's SMD outline. Lead form and details
are approximations for display; this is not a mechanical model or footprint.
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

    body = cq.Workplane('XY').box(6.645, 4.69, 3.555).edges().chamfer(0.13).translate((0, 0, 1.9775)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (3.24, 1.95), (3.7, 1.95), (4.17, 0.23), (4.89, 0.23),
            (4.89, 0.02), (4.04, 0.02), (3.50, 1.75), (3.24, 1.75),
        ]]
        for index in range(2):
            y = (index - 0.5) * 2.54
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(1.27).translate((0, y + 0.635, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.22).extrude(0.002).translate((-2.5, 1.4, 3.755)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-4.89, -2.345, 0.02]), np.array([4.89, 2.345, 3.757]), {'procedural': 1}
