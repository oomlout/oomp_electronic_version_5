"""Illustrative four-lead onsemi FOD817 surface-mount optocoupler mesh.

Nominal body 6.5 x 4.6 mm, overall height 3.85 mm, lead span 10.16 mm and
2.54 mm pitch follow onsemi CASE 709AH outline. Lead form and details
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

    body = cq.Workplane('XY').box(6.5, 4.6, 3.5).edges().chamfer(0.13).translate((0, 0, 2.1)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (3.18, 1.95), (3.7, 1.95), (4.3, 0.23), (5.08, 0.23),
            (5.08, 0.02), (4.17, 0.02), (3.50, 1.75), (3.18, 1.75),
        ]]
        for index in range(2):
            y = (index - 0.5) * 2.54
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(1.27).translate((0, y + 0.635, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.22).extrude(0.002).translate((-2.4, 1.4, 3.85)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-5.08, -2.3, 0.02]), np.array([5.08, 2.3, 3.852]), {'procedural': 1}
