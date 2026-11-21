"""Drawing-based display-only Kangnex WJ127 two-position terminal block.

Body: 10.00 x 8.12 x 10.14 mm. Contacts: 5.00 mm pitch, 0.95 x 0.50 mm,
4.20 mm projection. Two top screws and front openings are included with
illustrative head, recess, cage and mould details; see the evidence record.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid terminal-block display shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.03, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    # Approximate the sloping upper sides shown in the manufacturer side view.
    profile = [(-4.06, 0), (4.06, 0), (4.06, 6.0), (2.7, 10.14),
               (-2.9, 10.14), (-4.06, 5.5)]
    body = cq.Workplane('YZ').polyline(profile).close().extrude(10.0).translate((-5.0, 0, 0))
    for x in (-2.5, 2.5):
        screw_hole = cq.Workplane('XY').circle(1.70).extrude(3.0).translate((x, 0, 7.2))
        front_opening = cq.Workplane('XY').box(3.35, 3.1, 3.7).translate((x, -3.0, 3.15))
        body = body.cut(screw_hole).cut(front_opening)
    add('coating', body.val())
    for x in (-2.5, 2.5):
        screw = cq.Workplane('XY').circle(1.45).extrude(.65).translate((x, 0, 8.50))
        slot = cq.Workplane('XY').box(2.5, .45, .35).translate((x, 0, 9.06))
        screw = screw.cut(slot)
        add('termination', screw.val())
        cage = cq.Workplane('XY').box(3.0, .35, 3.1).translate((x, -1.65, 3.15)).val()
        add('termination', cage)
        pin = cq.Workplane('XY').box(.95, .50, 4.2, centered=(True, True, False)).translate((x, -.14, -4.2)).val()
        add('termination', pin)
    return dict(groups), np.array([-5.0, -4.06, -4.2]), np.array([5.0, 4.06, 10.14]), {'procedural': 1}
