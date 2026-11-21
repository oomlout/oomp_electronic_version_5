"""Render the reviewed D882 TO-126 model with adapted leads and material regions.

The source is one uncoloured solid. Face classification and the lead extension
are restricted to the pinned, measured KiCad geometry; the source is untouched.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from kicad_agents import display_render as renderer

PART = 'electronic_transistor_to_126_bipolar_npn_30_volt_3_amp_jiangsu_changjing_electronics_technology_co_ltd_d882_range_160_320'
MODEL = 'Package_TO_SOT_THT.3dshapes/TO-126-3_Vertical.step'
MODEL_SHA = '6cb4ab2049af821a4bd7162ee7b11b91bdea76f43915d9c1fbb0cb1cdeeaa9c6'
LEAD_EXTENSION_MM = 2.75


def load(path, specification):
    import cadquery as cq
    import numpy as np

    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed TO-126 STEP')
    solids = cq.importers.importStep(str(path)).solids().vals()
    if len(solids) != 1 or not solids[0].isValid() or len(solids[0].Faces()) != 66:
        raise ValueError('TO-126 solid topology changed')
    box = solids[0].BoundingBox()
    bounds = [box.xmin, box.xmax, box.ymin, box.ymax, box.zmin, box.zmax]
    if not np.allclose(bounds, [-1.72, 6.28, -1.25, 2., -9.75, 14.], atol=.003, rtol=0):
        raise ValueError('TO-126 source bounds changed')
    groups = defaultdict(lambda: {'vertices': [], 'normals': [], 'triangles': []})
    counts = defaultdict(int)
    for face in solids[0].Faces():
        b = face.BoundingBox()
        # The three leads occupy the narrow central Y slab and terminate at
        # the body base. The rear thermal pad is the recessed y=2 panel.
        lead = b.zmin < 3.001 and b.zmax <= 3.001 and b.ymin >= -.264 and b.ymax <= .264
        rear_pad = (b.ymin >= 1.975 and b.xmin >= -.721 and b.xmax <= 5.281
                    and b.zmin >= 4.999 and b.zmax <= 13.001)
        role = 'termination' if lead or rear_pad else 'coating'
        counts['lead_faces' if lead else 'rear_pad_faces' if rear_pad else 'body_faces'] += 1
        vertices, triangles = face.tessellate(.003, .08)
        offset = len(groups[role]['vertices'])
        for v in vertices:
            x, y, z = v.toTuple()
            if lead and z < -0.001:
                z -= LEAD_EXTENSION_MM
            groups[role]['vertices'].append((x, y, z))
            groups[role]['normals'].append(face.normalAt(v).toTuple())
        groups[role]['triangles'].extend(tuple(offset + i for i in tri) for tri in triangles)
    if set(groups) != {'coating', 'termination'} or counts['lead_faces'] < 25 or counts['rear_pad_faces'] < 5:
        raise ValueError(f'Unexpected TO-126 material classification: {dict(counts)}')
    counts['lead_extension_mm'] = LEAD_EXTENSION_MM
    return dict(groups), np.array([-1.72, -1.25, -12.5]), np.array([6.28, 2., 14.]), dict(counts)


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
        raise RuntimeError('Model or adapter changed while rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapted_bounds_mm'] = manifest['model']['source_bounds_mm']
    manifest['model']['source_bounds_mm'] = [8.0, 3.25, 23.75]
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
