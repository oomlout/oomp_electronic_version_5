"""Reuse one verified unmarked Fenghua 1206 illustration within its reviewed family."""
import json
import sys
from pathlib import Path

from kicad_agents import display_render as renderer
from kicad_agents import display_render_generic_0201_led_family as shared
from kicad_agents import display_render_fenghua_cmi321609_queue as queue

PILOT = 'electronic_inductor_1206_10_micro_henry'
PARTS = {part: mpn for part, mpn in queue.PARTS.items() if part != PILOT}
MODEL_SHA = queue.MODEL_HASH
prepare = queue.prepare


def main():
    adapter_hash = renderer.digest(__file__)
    shared.batch = sys.modules[__name__]
    shared.main()
    args = sys.argv[1:]
    if '--output' not in args or args.index('--output') + 1 >= len(args):
        raise ValueError('Expected output path')
    path = Path(args[args.index('--output') + 1]) / 'manifest.json'
    manifest = json.loads(path.read_text(encoding='utf8'))
    if renderer.digest(__file__) != adapter_hash:
        raise RuntimeError('Family adapter changed during preparation')
    manifest['render']['reuse_family_adapter_sha256'] = adapter_hash
    manifest['render']['reuse_family_queue_sha256'] = renderer.digest(queue.__file__)
    manifest['render']['reused_image']['reason'] = ('Same reviewed unmarked model, material, studio, output and empty marking; '
                                                     'no independent path trace.')
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
