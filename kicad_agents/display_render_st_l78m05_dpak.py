"""Render the inspected, uncoloured KiCad TO-252-2 using explicit solid roles.

The model's five solids are checked against measured bounding boxes and volumes;
the large moulding is black and the tab, two leads and short centre stub are metal. This adapter
does not infer a pin-one marking on an otherwise unmarked package.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from kicad_agents import display_render as renderer

PART = 'electronic_ic_power_management_linear_voltage_regulator_5_volt_to_252_2_dpak_stmicroelectronics_l78m05abdt_tr'
MODEL = 'Package_TO_SOT_SMD.3dshapes/TO-252-2.step'
MODEL_SHA = '3eb4c99603a4fe837c2fe9308bc174769ded87a785a0df48d2dc441432ee8b4c'
SIGNATURES = [
    ('coating', 83.27705, (-3.11, 3.11, -3.25, 3.25, .02, 2.32)),
    ('termination', 11.70183, (-1.13, 4.11, -2.7, 2.7, 0., .5)),
    ('termination', 1.6019, (-5.79, -2.2377, -2.775, -1.785, 0., 1.4399)),
    ('termination', .67751, (-3.91, -2.2377, -.495, .495, .9399, 1.4399)),
    ('termination', 1.6019, (-5.79, -2.2377, 1.785, 2.775, 0., 1.4399)),
]


def load(path, specification):
    import cadquery as cq
    import numpy as np

    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed TO-252-2 model')
    solids = cq.importers.importStep(str(path)).solids().vals()
    if len(solids) != len(SIGNATURES):
        raise ValueError('Unexpected TO-252-2 solid count')
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})
    for solid, (role, volume, expected) in zip(solids, SIGNATURES):
        box = solid.BoundingBox()
        actual = (box.xmin, box.xmax, box.ymin, box.ymax, box.zmin, box.zmax)
        if not solid.isValid() or abs(solid.Volume() - volume) > .005 or not np.allclose(actual, expected, atol=.003, rtol=0):
            raise ValueError('TO-252-2 solid differs from reviewed geometry')
        group = groups[role]
        for face in solid.Faces():
            vertices, triangles = face.tessellate(.003, .08)
            offset = len(group['vertices'])
            group['vertices'].extend(v.toTuple() for v in vertices)
            group['normals'].extend(face.normalAt(v).toTuple() for v in vertices)
            group['triangles'].extend(tuple(offset + i for i in triangle) for triangle in triangles)
    if set(groups) != {'coating', 'termination'}:
        raise ValueError('Unexpected material regions')
    return dict(groups), np.array([-5.79, -3.25, 0.]), np.array([4.11, 3.25, 2.32]), {'reviewed_solids': len(solids)}


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
