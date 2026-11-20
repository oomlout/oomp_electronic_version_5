"""Display-only Toshiba 11-10C401S SMD optocoupler package.

Nominal body 9.66 x 6.4 mm, 4.0 mm overall height and 2.54 mm lead
pitch follow Toshiba's package drawing; lead profile and dot are illustrative.
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

    body = cq.Workplane('XY').box(6.4, 9.66, 3.65).edges().chamfer(0.15).translate((0, 0, 2.175)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (3.1, 1.95), (3.65, 1.95), (4.1, 0.2), (4.7, 0.2),
            (4.7, 0.025), (3.98, 0.025), (3.48, 1.75), (3.1, 1.75),
        ]]
        for index in range(4):
            y = (index - 1.5) * 2.54
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.5).translate((0, y + 0.25, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.24).extrude(0.002).translate((-2.25, 3.8, 4.0)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-4.7, -4.83, 0.025]), np.array([4.7, 4.83, 4.002]), {'procedural': 1}
