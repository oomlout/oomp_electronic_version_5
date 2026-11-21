"""Render the reviewed procedural Nexperia SOT762-1 display model using the shared studio."""
import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_model_nexperia_sot762_1 as model
from kicad_agents import display_render as renderer

PART = 'electronic_ic_logic_analog_switch_qfn_14_nexperia_74hc4066bq'
MODEL = 'kicad_agents/display_model_nexperia_sot762_1.py'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--pixels', type=int)
    parser.add_argument('--samples', type=int)
    args = parser.parse_args()
    model_file = renderer.ROOT / MODEL
    model_hash = renderer.digest(model_file)
    adapter_hash = renderer.digest(__file__)

    def locate(relative_path, model_root=None):
        if relative_path != MODEL or model_root is not None:
            raise ValueError('Only the reviewed procedural model is supported')
        return model_file

    def load(path, specification):
        if path != model_file or specification.get('sha256') != model_hash:
            raise ValueError('Procedural model changed')
        groups, lower, upper, counts = model.build()
        if set(groups) != {'coating', 'termination', 'pin_indicator'}:
            raise ValueError('Unexpected material roles')
        return groups, lower, upper, counts

    renderer.locate_model = locate
    renderer.load_coloured_step = load
    renderer.generate(PART, output=args.output, pixels=args.pixels, samples=args.samples, force=True)
    if renderer.digest(model_file) != model_hash or renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Procedural model or adapter changed during rendering')
    path = Path(args.output) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    manifest['model']['source_header'] = 'Procedural display-only geometry; see ' + MODEL
    manifest['model']['generator_sha256'] = model_hash
    manifest['model']['adapter_sha256'] = adapter_hash
    manifest['input_fingerprint'] = hashlib.sha256(
        (manifest['input_fingerprint'] + model_hash + adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
