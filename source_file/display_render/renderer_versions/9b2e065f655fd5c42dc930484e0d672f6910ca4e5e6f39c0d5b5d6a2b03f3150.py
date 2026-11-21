"""Prepare four individually evidenced Infineon SO-8 display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_ti_soic8_pilot_queue import MODEL_SHA256, PART as PILOT, ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_SO8_MOSFETS_RESEARCH.md')
PARTS = {
    'electronic_transistor_so_8_mosfet_n_channel_enhancement_mode_30_volt_13_amp_infineon_technologies_irf7413trpbf': ('IRF7413TRPBF', 'IRF7413'),
    'electronic_transistor_so_8_mosfet_n_channel_enhancement_mode_30_volt_20_amp_infineon_technologies_irf7832trpbf': ('IRF7832TRPBF', 'IRF7832'),
    'electronic_transistor_so_8_mosfet_p_channel_enhancement_mode_20_volt_6_7_amp_infineon_technologies_irf7404trpbf': ('IRF7404TRPBF', 'IRF7404'),
    'electronic_transistor_so_8_mosfet_p_channel_enhancement_mode_30_volt_10_amp_infineon_technologies_irf7416trpbf': ('IRF7416TRPBF', 'IRF7416'),
}


def prepare(recipes):
    pilot = recipes[PILOT]
    if pilot.get('represented_mpn') != 'NE5532DR' or pilot['model']['sha256'] != MODEL_SHA256:
        raise ValueError('Reviewed SOIC-8 pilot changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, (mpn, text) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
            or (record.get('kicad') or {}).get('machine_solder') != '' or (source / 'datasheet.pdf').exists()):
            raise ValueError(f'{mpn}: source identity, dimensions, footprint or PDF availability changed')
        recipe = copy.deepcopy(pilot)
        recipe.update(represented_manufacturer='Infineon Technologies', represented_mpn=mpn)
        recipe['marking'].update(policy='illustrative_literal', text=text, evidence={'file': EVIDENCE.as_posix(),
            'sha256': evidence_sha, 'document': f'Infineon {mpn} SO-8 identity and family package review',
            'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status=f'{text} is an illustrative partial identifier; exact top marking, typeface, logo, placement and production details are unverified.')
        recipe['appearance_status'] = ('KiCad SOIC-8 6.0 x 4.9 x 1.75 mm overall model approximates the manufacturer SO-8 package. The catalogue 10 x 5 mm dimensions differ from the package. This part has no separate local PDF. Finish and details are illustrative; not manufacturing CAD or a footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    additions = prepare(recipes)
    if args.add:
        for part, recipe in additions.items():
            recipes.setdefault(part, recipe)
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print('SO-8 candidates', len(additions), 'added', args.add, flush=True)


if __name__ == '__main__':
    main()
