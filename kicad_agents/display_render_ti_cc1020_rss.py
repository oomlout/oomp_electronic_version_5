"""Display-only CC1020 model with its isolated KiCad thermal pad corrected.

The 4.70 mm source pad is scaled to TI's 4.28 mm nominal size. The original
small chamfer is proportionally scaled and is not an exact TI 0.3 mm chamfer.
The underlying coating is closed; perimeter contacts are not moved.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from kicad_agents import display_render as renderer

PART = 'electronic_ic_rf_sub_ghz_rf_transceiver_qfn_32_ep_texas_instruments_cc1020rssr'
MODEL = 'Package_DFN_QFN.3dshapes/QFN-32-1EP_7x7mm_P0.65mm_EP5.46x5.46mm.step'
MODEL_SHA = 'f8cb3647a783167910c468bc09d5de74223779876388b796a66718dc82b11a1a'
original_loader = renderer.load_coloured_step


def load(path, specification):
    if renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA:
        raise ValueError('Unreviewed CC1020 source model')
    groups, lower, upper, counts = original_loader(path, specification)
    mesh = groups['termination']
    vertices = np.asarray(mesh['vertices'], dtype=float)
    normals = np.asarray(mesh['normals'], dtype=float)
    triangles = np.asarray(mesh['triangles'], dtype=int)
    points = vertices[triangles]
    selected = (np.all(np.abs(points[:, :, 0]) <= 2.351, axis=1)
                & np.all(np.abs(points[:, :, 1]) <= 2.351, axis=1)
                & np.all(points[:, :, 2] >= -.001, axis=1)
                & np.all(points[:, :, 2] <= .021, axis=1))
    if int(selected.sum()) != 13:
        raise ValueError('Unexpected thermal-pad triangles')
    chosen = np.unique(triangles[selected])
    others = np.unique(triangles[~selected])
    if np.intersect1d(chosen, others).size:
        raise ValueError('Thermal pad shares vertices with contacts')
    if not (np.allclose(points[selected].min(axis=(0, 1)), [-2.35, -2.35, 0], atol=.002)
            and np.allclose(points[selected].max(axis=(0, 1)), [2.35, 2.35, .02], atol=.002)):
        raise ValueError('Thermal pad bounds changed')
    scale = np.array([4.28 / 4.70, 4.28 / 4.70, 1.0])
    vertices[chosen] *= scale
    normals[chosen] /= scale
    lengths = np.linalg.norm(normals[chosen], axis=1)
    if np.any(~np.isfinite(lengths)) or np.any(lengths <= 0):
        raise ValueError('Invalid thermal-pad normals')
    normals[chosen] /= lengths[:, None]
    mesh['vertices'], mesh['normals'] = vertices.tolist(), normals.tolist()
    coating = groups['coating']
    start = len(coating['vertices'])
    coating['vertices'].extend([[-2.35, -2.35, .02], [-2.35, 2.35, .02],
                                [2.35, 2.35, .02], [2.35, -2.35, .02]])
    coating['normals'].extend([[0., 0., -1.]] * 4)
    coating['triangles'].extend([(start, start+1, start+2), (start, start+2, start+3)])
    counts['display_pad_correction'] = '4.70 to 4.28 mm; scaled chamfer; underside closed'
    return groups, lower, upper, counts


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
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['input_fingerprint'] = hashlib.sha256((manifest['input_fingerprint'] + adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
