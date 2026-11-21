"""Approximate TI RHL0020A VQFN20 geometry for display only.

Body dimensions, 20 perimeter contacts and exposed-pad size follow TI's
package outline and the KiCad RHL footprint. Terminal reveals, corners,
pin-one mark and underside details are illustrative, not a PCB footprint.
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

    body = cq.Workplane('XY').box(3.5, 4.5, .85).edges().chamfer(.025).translate((0, 0, .475)).val()
    add('coating', body)
    # Eight 0.5 mm-pitch contacts on each long edge. A small reveal makes the
    # metal visible at the molded edge and is an explicit display approximation.
    for x in (-1.59, 1.59):
        for y in (-1.75, -1.25, -.75, -.25, .25, .75, 1.25, 1.75):
            add('termination', cq.Workplane('XY').box(.4, .24, .12).translate((x, y, .06)).val())
    # Two signal contacts at each short edge, per the RHL drawing.
    for y in (-2.09, 2.09):
        for x in (-.75, .75):
            add('termination', cq.Workplane('XY').box(.24, .4, .12).translate((x, y, .06)).val())
    # Thermal pad and its four extensions, approximated from the TI drawing.
    add('termination', cq.Workplane('XY').box(2.05, 3.05, .07).translate((0, 0, .035)).val())
    for y in (-1.74, 1.74):
        add('termination', cq.Workplane('XY').box(.75, .43, .07).translate((0, y, .035)).val())
        for x in (-.275, .275):
            add('termination', cq.Workplane('XY').box(.20, .40, .12).translate((x, -2.09 if y < 0 else 2.09, .06)).val())
    marker = cq.Workplane('XY').circle(.095).extrude(.002).translate((-.95, -1.65, .9)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-1.79, -2.29, 0.0]), np.array([1.79, 2.29, .902]), {'procedural': 1}
