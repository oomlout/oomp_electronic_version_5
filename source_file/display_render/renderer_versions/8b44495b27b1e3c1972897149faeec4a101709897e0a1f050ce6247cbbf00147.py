"""Procedural low-profile HC-49US crystal for display, dimensions in mm.

Based on the YXC family drawing; this is an illustration, not manufacturer CAD.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(solid, top_is_marked=False):
        if not solid.isValid():
            raise ValueError('Invalid crystal geometry')
        for face in solid.Faces():
            box = face.BoundingBox()
            top = (top_is_marked and face.geomType() == 'PLANE'
                   and abs(box.zmin - 9.6) < .001 and abs(box.zmax - 9.6) < .001)
            group = groups['coating' if top else 'termination']
            vertices, triangles = face.tessellate(.02, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)

    # Oval drawn can, seated on the thin wider flange; lead ends touch z=0.
    flange = cq.Workplane('XY').slot2D(11.4, 4.5).extrude(.25).translate((0, 0, 6.0))
    can = cq.Workplane('XY').slot2D(10.8, 4.0).extrude(3.35).translate((0, 0, 6.25))
    add(flange.val())
    add(can.val(), top_is_marked=True)
    for x in (-2.44, 2.44):
        add(cq.Workplane('XY').center(x, 0).circle(.225).extrude(6.0).val())
    return dict(groups), np.array([-5.7, -2.25, 0.0]), np.array([5.7, 2.25, 9.6]), {'procedural': 1}
