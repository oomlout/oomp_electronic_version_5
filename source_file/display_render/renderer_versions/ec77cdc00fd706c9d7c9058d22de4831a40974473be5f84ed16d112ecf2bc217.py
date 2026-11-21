"""PICO II axial fuse display geometry with shortened leads, in millimetres."""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid PICO fuse display shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.025, .06)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    body = cq.Workplane('YZ').center(0, 1.4).circle(1.4).extrude(7.11).translate((-3.555, 0, 0))
    add('coating', body.val())
    for start in (-11.555, 3.555):
        lead = cq.Workplane('YZ').center(0, 1.4).circle(.32).extrude(8.0).translate((start, 0, 0))
        add('termination', lead.val())
    return dict(groups), np.array([-11.555, -1.4, 0.]), np.array([11.555, 1.4, 2.8]), {'procedural': 1}
