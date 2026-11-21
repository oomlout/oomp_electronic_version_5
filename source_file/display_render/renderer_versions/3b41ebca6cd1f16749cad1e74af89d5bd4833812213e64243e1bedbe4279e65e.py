"""5 x 20 mm glass fuse display geometry, with hollow tube and visible wire.

Cap length, glass wall and wire diameter are approximate. Units are millimetres;
the model is for display only and is not a fuse or footprint specification.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        if not solid.isValid():
            raise ValueError('Invalid glass fuse shape')
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.025, .06)
            group = groups[role]
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)

    # Tube extends a little beneath each cap. Its ring section creates real air
    # inside the glass instead of hiding the element inside opaque geometry.
    tube = cq.Workplane('YZ').center(0, 2.6).circle(2.45).circle(2.10).extrude(12.8).translate((-6.4, 0, 0))
    add('coating', tube.val())
    wire = cq.Workplane('YZ').center(0, 2.6).circle(.10).extrude(13.0).translate((-6.5, 0, 0))
    add('ceramic', wire.val())
    for start in (-10.0, 6.2):
        cap = cq.Workplane('YZ').center(0, 2.6).circle(2.6).extrude(3.8).translate((start, 0, 0))
        add('termination', cap.val())
    return dict(groups), np.array([-10., -2.6, 0.]), np.array([10., 2.6, 5.2]), {'procedural': 1}
