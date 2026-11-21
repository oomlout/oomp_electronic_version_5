"""Render reviewed D2PAK geometry with an approximately clipped centre lead.

The KiCad STEP has three full leads. The source solid signatures are checked,
the centre solid is intersected with a short box, and no source CAD is changed.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from kicad_agents import display_render as renderer

PART = 'electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_55_volt_110_amp_infineon_technologies_irf3205strlpbf'
MODEL = 'Package_TO_SOT_SMD.3dshapes/TO-263-3_TabPin2.step'
MODEL_SHA = 'f8d7f00ad233d49496cf0b53aca1891fcbc2d8d007dfe42465186627fedd54d0'
SIGNATURES = [
    ('coating', 382.781, (-4.625, 4.625, -5., 5., .02, 4.42)),
    ('termination', 78.676, (-1.925, 5.625, -5., 5., 0., 1.27)),
    ('termination', 3.605, (-9.375, -4.425, -3.16, -1.92, 0., 2.95)),
    ('termination', 3.605, (-9.375, -4.425, -.62, .62, 0., 2.95)),
    ('termination', 3.605, (-9.375, -4.425, 1.92, 3.16, 0., 2.95)),
]


def load(path, specification):
    import cadquery as cq
    import numpy as np

    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed D2PAK model')
    solids = cq.importers.importStep(str(path)).solids().vals()
    if len(solids) != len(SIGNATURES):
        raise ValueError('Unexpected D2PAK solid count')
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})
    for index, (solid, (role, volume, expected)) in enumerate(zip(solids, SIGNATURES)):
        b = solid.BoundingBox()
        actual = (b.xmin, b.xmax, b.ymin, b.ymax, b.zmin, b.zmax)
        if not solid.isValid() or abs(solid.Volume() - volume) > .01 or not np.allclose(actual, expected, atol=.003, rtol=0):
            raise ValueError('D2PAK source geometry changed')
        if index == 3:
            # Body edge is x=-4.625; retain a short 0.5 mm external stub.
            clip = cq.Workplane('XY').box(1., 20., 10.).translate((-4.625, 0., 2.5)).val()
            solid = solid.intersect(clip)
            b = solid.BoundingBox()
            if not solid.isValid() or abs(b.xmin + 5.125) > .003 or abs(b.xmax + 4.425) > .003:
                raise ValueError('Centre lead trim failed geometry checks')
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)
    if set(groups) != {'coating', 'termination'}:
        raise ValueError('Unexpected D2PAK materials')
    return dict(groups), np.array([-9.375, -5., 0.]), np.array([5.625, 5., 4.42]), {
        'reviewed_solids': 5, 'centre_lead_external_stub_mm': .5}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    model = renderer.locate_model(MODEL)
    adapter_hash = renderer.digest(__file__)
    renderer.load_coloured_step = load
    renderer.generate(PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(model) != MODEL_SHA or renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Model or adapter changed during render')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
