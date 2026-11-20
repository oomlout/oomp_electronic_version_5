"""Display-only SO-8 optocoupler mesh following Broadcom's nominal outline.

Body is 3.937 by 5.080 mm, overall height 3.175 mm and lead pitch 1.27 mm.
Lead profile, edge treatment and pin-one dot are illustrative, not a footprint.
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

    # Standoff and upper body add to 3.175 mm. Keep a broad flat marking face.
    body = cq.Workplane('XY').box(3.937, 5.08, 2.972).edges().chamfer(0.12).translate((0, 0, 1.689)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (1.88, 1.58), (2.25, 1.58), (2.61, 0.19), (2.997, 0.19),
            (2.997, 0.02), (2.48, 0.02), (2.10, 1.38), (1.88, 1.38),
        ]]
        for index in range(4):
            y = (index - 1.5) * 1.27
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.406).translate((0, y + 0.203, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.19).extrude(0.002).translate((-1.20, 1.80, 3.175)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-2.997, -2.54, 0.02]), np.array([2.997, 2.54, 3.177]), {'procedural': 1}
