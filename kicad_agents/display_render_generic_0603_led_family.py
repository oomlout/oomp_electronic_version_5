"""Apply the validated shared-image workflow to reviewed generic 0603 LEDs."""
import json
import sys
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_generic_0201_led_family as shared
from kicad_agents import display_render_generic_0603_led_family_queue as batch


def main():
    # The shared parser and strict visual-input checks remain unchanged.
    adapter_hash = renderer.digest(__file__)
    shared.batch = batch
    shared.main()
    args = sys.argv[1:]
    if '--output' not in args or args.index('--output') + 1 >= len(args):
        raise ValueError('Expected output path')
    path = Path(args[args.index('--output') + 1]) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    if renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Family adapter changed during preparation')
    manifest['render']['reuse_family_adapter_sha256'] = adapter_hash
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
