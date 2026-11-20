"""Build an illustrative TI NS-14 display mesh, without exporting CAD files.

Body dimensions and 1.27 mm pin pitch follow TI's nominal package index. The
lead cross-section and pin-one dot are visual approximations, not a footprint.
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

    # Preserve a flat top for the package marking while softening molded edges.
    body = cq.Workplane('XY').box(5.3, 10.3, 1.75).edges().chamfer(0.12).translate((0, 0, 1.075)).val()
    add('coating', body)
    for side in (-1, 1):
        profile = [(side*x, z) for x, z in [
            (2.55, 1.25), (3.07, 1.25), (3.32, 0.18), (3.9, 0.18),
            (3.9, 0.02), (3.18, 0.02), (2.94, 1.05), (2.55, 1.05),
        ]]
        for index in range(7):
            y = (index - 3) * 1.27
            lead = cq.Workplane('XZ').polyline(profile).close().extrude(0.42).translate((0, y + 0.21, 0)).val()
            add('termination', lead)
    marker = cq.Workplane('XY').circle(0.22).extrude(0.002).translate((-1.65, 4.15, 1.95)).val()
    add('pin_indicator', marker)
    return dict(groups), np.array([-3.9, -5.15, 0.02]), np.array([3.9, 5.15, 1.952]), {'procedural': 1}
