"""Display-only miniSMDC package, based on the 020F drawing, in millimetres.

Mid-range overall dimensions and approximate concave end notches are used.
This simplified geometry is not a manufacturing model or footprint.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid miniSMDC display shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.02, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    # A 4.55 x 3.24 x 0.76 body, with nominal 0.60 wide tin-plated ends.
    add('coating', cq.Workplane('XY').box(3.35, 3.24, .76).translate((0, 0, .38)).val())
    for sign in (-1, 1):
        cap = cq.Workplane('XY').box(.60, 3.24, .76).translate((sign * 1.975, 0, .38))
        notch = cq.Workplane('XY').circle(.24).extrude(1.0).translate((sign * 2.275, 0, -.12))
        add('termination', cap.cut(notch).val())
    return dict(groups), np.array([-2.275, -1.62, 0.0]), np.array([2.275, 1.62, .76]), {'procedural': 1}
