"""Render reviewed TO-3P variants with display-only lead-length adjustment."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from kicad_agents import display_render as renderer
from kicad_agents.display_render_onsemi_to3p_queue import PARTS, MODEL_SHA

ORIGINAL_LOAD = renderer.load_coloured_step


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=PARTS)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    target_length = PARTS[args.part][3]
    target_bottom = 2.7 - target_length
    factor = target_bottom / -18.0
    adapter_sha = renderer.digest(__file__)

    def load(path, specification):
        if (renderer.digest(path) != MODEL_SHA or specification.get('sha256') != MODEL_SHA
            or specification.get('display_lead_length_mm') != target_length):
            raise ValueError('Unreviewed TO-3P model or lead length')
        groups, lower, upper, colours = ORIGINAL_LOAD(path, specification)
        if (not np.allclose(lower, [-2.305, -1.4, -18.0], atol=.005)
            or not np.allclose(upper, [13.205, 3.11, 22.7], atol=.005)):
            raise ValueError('Unexpected TO-3P envelope')
        body = np.asarray(groups['coating']['vertices'])
        if abs(body[:, 2].min() - 2.7) > .005:
            raise ValueError('Unexpected TO-3P body base')
        metal = groups['termination']
        vertices = np.asarray(metal['vertices'], dtype=float)
        normals = np.asarray(metal['normals'], dtype=float)
        mask = vertices[:, 2] < 0
        if int(mask.sum()) != 72 or abs(vertices[:, 2].min() + 18.0) > .005:
            raise ValueError('Unexpected TO-3P lead mesh')
        vertices[mask, 2] *= factor
        normals[mask, 2] /= factor
        lengths = np.linalg.norm(normals, axis=1)
        if np.any(~np.isfinite(lengths)) or np.any(lengths <= 0):
            raise ValueError('Invalid TO-3P mesh normals')
        normals /= lengths[:, None]
        metal['vertices'], metal['normals'] = vertices.tolist(), normals.tolist()
        lower = lower.copy()
        lower[2] = target_bottom
        return groups, lower, upper, dict(colours, corrected_lead_vertices=int(mask.sum()))

    renderer.load_coloured_step = load
    renderer.generate(args.part, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(__file__) != adapter_sha:
        raise RuntimeError('TO-3P adapter changed during rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_sha
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + adapter_sha).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
