"""Approximate RXEF010 radial fuse resting face-up for display only, in mm."""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid radial fuse shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.03, .08)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    # The family drawing specifies maxima, so these dimensions are illustrative.
    body = cq.Workplane('XY').ellipse(3.3, 3.5).extrude(2.4).translate((3.3, 0, 0))
    add('coating', body.val())
    for y in (-2.54, 2.54):
        lead = cq.Workplane('YZ').center(y, 1.2).circle(.255).extrude(-10.5).translate((1.5, 0, 0))
        add('termination', lead.val())
    return dict(groups), np.array([-9.0, -3.5, 0.0]), np.array([6.6, 3.5, 2.4]), {'procedural': 1}
