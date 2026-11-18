"""Refresh one existing component page after an explicit, validated display render."""
import argparse
from pathlib import Path
import re
import os

import yaml
from working_oomp_populate_display_render import ROOT, apply_extras


def publish(part_id):
    if not re.fullmatch(r'electronic_[a-z0-9_]+', part_id):
        raise ValueError('Select one exact electronic component ID')
    os.chdir(ROOT)
    source = ROOT / 'parts_source' / part_id / 'working.yaml'
    if not source.is_file():
        raise FileNotFoundError(f'No source record for {part_id}')
    part = yaml.safe_load(source.read_text(encoding='utf-8'))
    apply_extras({part_id: part})
    if not part.get('display_render'):
        raise ValueError('Render is missing, outdated or damaged. Re-render and inspect it before publishing.')
    # Only display metadata changes. Preserve source notes, local overrides and
    # datasheet-sharing pointers rather than repopulating the whole catalogue.
    source.write_text(yaml.safe_dump(part, allow_unicode=True), encoding='utf-8')
    import working_oomp
    from kicad_agents.readme_action import regenerate_readmes
    from kicad_agents.web_manifest_action import build_web_manifest
    working_oomp.main(exact_part_ids=[part_id], regenerate_pngs=False)
    regenerate_readmes(part_ids={part_id}, output_names={'README.md'})
    build_web_manifest({'directory': str(ROOT / 'parts' / part_id)})
    print(f'Updated only {part_id}. No taxonomy or library indexes changed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id')
    publish(parser.parse_args().part_id)


if __name__ == '__main__':
    main()
