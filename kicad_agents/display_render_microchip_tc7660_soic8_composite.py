"""Use verified SOIC-8 passes for individually evidenced Infineon batch partials.

The TI pilot comparison must have passed before use. Review every image;
indirect reflections are approximate. A validator hash is recorded in output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from kicad_agents import display_render_ti_soic8_composite as base
from kicad_agents import display_render_microchip_tc7660_soic8 as batch

shared=base.shared
renderer=base.renderer


def read_recipe(part_id):
    recipes=json.loads(renderer.RECIPES.read_text(encoding='utf-8'))
    base.read_recipe(base.PART)  # Validate published independent pilot and evidence.
    candidates=batch.prepare(recipes)
    if part_id not in candidates or part_id not in recipes or recipes[part_id] != candidates[part_id]:
        raise ValueError('No exact reviewed Infineon batch partial recipe for this part')
    return recipes[part_id]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part_id'); parser.add_argument('--output',required=True)
    args=parser.parse_args()
    source_hash=renderer.digest(__file__); batch_hash=renderer.digest(batch.__file__)
    shared.read_recipe=read_recipe; shared.master_inputs=base.master_inputs
    shared.render(args.part_id,args.output)
    if renderer.digest(__file__) != source_hash or renderer.digest(batch.__file__) != batch_hash:
        raise RuntimeError('Candidate validator changed; do not publish output')
    path=Path(args.output)/'manifest.json'; manifest=json.loads(path.read_text(encoding='utf-8'))
    manifest['composite']['candidate_validator_sha256']=source_hash
    manifest['composite']['candidate_batch_sha256']=batch_hash
    manifest['input_fingerprint']=hashlib.sha256(
        (manifest['input_fingerprint'] + source_hash + batch_hash).encode('ascii')
    ).hexdigest()
    path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__': main()
