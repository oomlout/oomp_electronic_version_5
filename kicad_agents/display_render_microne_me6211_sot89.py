"""Render the inspected, uncoloured KiCad SOT-89 for MicrOne ME6211A33 using explicit solid roles.

The model's five solids are checked against measured bounding boxes and volumes;
the large moulding is black and the tab plus three leads are metal. This adapter
does not infer a pin-one marking on an otherwise unmarked package.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from kicad_agents import display_render as renderer

PART = 'electronic_ic_power_management_linear_voltage_regulator_3_3_volt_sot_89_3_microne_me6211a33pg_n'
MODEL = 'Package_TO_SOT_SMD.3dshapes/SOT-89-3.step'
MODEL_SHA = '844c0bb504d0c383535d9845c6376fe7a4053241a2ede8d8ef694df3fcfc37c8'
SIGNATURES = [
    ('coating', 16.0812, (-1.25, 1.25, -2.25, 2.25, .02, 1.52)),
    ('termination', 1.3296, (-.75, 1.75, -.8, .8, 0., .4)),
    ('termination', .24, (-2.25, -.75, -1.7, -1.3, 0., .4)),
    ('termination', .24, (-2.25, -.75, -.2, .2, 0., .4)),
    ('termination', .24, (-2.25, -.75, 1.3, 1.7, 0., .4)),
]


def load(path, specification):
    import cadquery as cq
    import numpy as np

    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed SOT-89 model')
    solids = cq.importers.importStep(str(path)).solids().vals()
    if len(solids) != len(SIGNATURES):
        raise ValueError('Unexpected SOT-89 solid count')
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})
    for solid, (role, volume, expected) in zip(solids, SIGNATURES):
        box = solid.BoundingBox()
        actual = (box.xmin, box.xmax, box.ymin, box.ymax, box.zmin, box.zmax)
        if not solid.isValid() or abs(solid.Volume() - volume) > .005 or not np.allclose(actual, expected, atol=.003, rtol=0):
            raise ValueError('SOT-89 solid differs from reviewed geometry')
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)
    if set(groups) != {'coating', 'termination'}:
        raise ValueError('Unexpected material regions')
    return dict(groups), np.array([-2.25, -2.25, 0.]), np.array([1.75, 2.25, 1.52]), {'reviewed_solids': len(solids)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    model_file = renderer.locate_model(MODEL)
    adapter_hash = renderer.digest(__file__)
    renderer.load_coloured_step = load
    renderer.generate(PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(model_file) != MODEL_SHA or renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Model or adapter changed while rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
