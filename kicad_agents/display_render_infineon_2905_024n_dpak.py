"""Render reviewed 2905 and 024N DPAK candidates with checked short-centre-lead model."""
import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_st_l78m05_dpak as adapter
from kicad_agents.display_render_infineon_2905_024n_dpak_queue import PARTS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=PARTS)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    model_file = renderer.locate_model(adapter.MODEL)
    adapter_hash = renderer.digest(adapter.__file__)
    runner_hash = renderer.digest(__file__)
    renderer.load_coloured_step = adapter.load
    renderer.generate(args.part, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if (renderer.digest(model_file) != adapter.MODEL_SHA or renderer.digest(adapter.__file__) != adapter_hash
        or renderer.digest(__file__) != runner_hash):
        raise RuntimeError('Model or adapter changed while rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['model']['runner_sha256'] = runner_hash
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + adapter_hash + runner_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
