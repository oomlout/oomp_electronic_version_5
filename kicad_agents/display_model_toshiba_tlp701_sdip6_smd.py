"""Illustrative six-lead Toshiba TLP701 surface-mount optocoupler mesh.

Nominal body 6.8 x 4.58 mm, height 4.0 mm, lead span 9.7 mm and
1.27 mm pitch follow Toshiba's 11-5J1S outline. Lead form and details
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

    body = cq.Workplane('XY').box(6.8, 4.58, 3.8).edges().chamfer(0.13).translate((0, 0, 2.1)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (3.30, 1.95), (3.65, 1.95), (4.15, 0.19), (4.85, 0.19),
            (4.85, 0.02), (4.03, 0.02), (3.48, 1.75), (3.30, 1.75),
        ]]
        for index in range(3):
            y = (index - 1) * 1.27
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.4).translate((0, y + 0.2, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.22).extrude(0.002).translate((-2.5, 1.4, 4.0)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-4.85, -2.29, 0.02]), np.array([4.85, 2.29, 4.002]), {'procedural': 1}
