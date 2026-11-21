"""Procedural HC-49SMD crystal display illustration, dimensions in mm."""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(solid, top_is_marked=False):
        if not solid.isValid():
            raise ValueError('Invalid SMD crystal geometry')
        for face in solid.Faces():
            box = face.BoundingBox()
            top = (top_is_marked and face.geomType() == 'PLANE'
                   and abs(box.zmin - 3.8) < .001 and abs(box.zmax - 3.8) < .001)
            group = groups['coating' if top else 'termination']
            vertices, triangles = face.tessellate(.02, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)

    # Family drawing: 11.4 mm carrier, 10 mm can and two underside terminals.
    carrier = cq.Workplane('XY').slot2D(11.4, 4.8).extrude(.25).translate((0, 0, .05))
    can = cq.Workplane('XY').slot2D(10.0, 3.8).extrude(3.5).translate((0, 0, .3))
    add(carrier.val())
    add(can.val(), top_is_marked=True)
    for x in (-3.0, 3.0):
        add(cq.Workplane('XY').center(x, 0).box(4.0, .8, .05, centered=(True, True, False)).val())
    return dict(groups), np.array([-5.7, -2.4, 0.0]), np.array([5.7, 2.4, 3.8]), {'procedural': 1}
