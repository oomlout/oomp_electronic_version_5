"""Illustrative Nexperia SOT762-1 DHVQFN14 geometry for display only.

Nominal 2.5 x 3.0 x 0.85 mm body, 0.5 mm pitch and the 14-contact layout
follow the manufacturer outline and reviewed KiCad footprint. Contacts, central
pad, corners and pin-one indicator are approximations, not a PCB footprint.
"""
from collections import defaultdict


def build():
    import cadquery as cq
    import numpy as np

    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})

    def add(role, solid):
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)

    body = cq.Workplane('XY').box(2.5, 3.0, .80).edges().chamfer(.025).translate((0, 0, .45)).val()
    add('coating', body)
    # Contacts 2-6 and 9-13 run along the two long edges.
    # A 0.012 mm edge reveal keeps the metallic sides visible in the render.
    for x in (-1.062, 1.062):
        for y in (-1.0, -.5, 0., .5, 1.0):
            add('termination', cq.Workplane('XY').box(.4, .25, .12).translate((x, y, .06)).val())
    # Contacts 1, 14 and 7, 8 are on the two short edges.
    for y in (-1.312, 1.312):
        for x in (-.25, .25):
            add('termination', cq.Workplane('XY').box(.25, .4, .12).translate((x, y, .06)).val())
    add('termination', cq.Workplane('XY').box(1.0, 1.5, .07).translate((0, 0, .035)).val())
    marker = cq.Workplane('XY').circle(.085).extrude(.002).translate((-.82, -1.1, .85)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-1.262, -1.512, 0.0]), np.array([1.262, 1.512, .852]), {'procedural': 1}
