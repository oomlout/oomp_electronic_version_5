"""Stage three individually researched Infineon D2PAK display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_infineon_irf3205s_to263 import PART as PILOT, MODEL_SHA

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VISHAY_TO263_840A_840_9640_RESEARCH.md')
PARTS = {'electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840astrlpbf': ('IRF840ASTRLPBF', 'IRF840AS', '0d0d47cb473c1842d5a68b2ada3b84c59f610561462831ccc532c06a1dd7019a'), 'electronic_transistor_to_263_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840strlpbf': ('IRF840STRLPBF', 'IRF840S', 'a3bca7fa7e16110f20ace074d0b377c0b2104babe96115e9cdc633397e391783'), 'electronic_transistor_to_263_mosfet_p_channel_enhancement_mode_200_volt_6_8_amp_vishay_intertech_irf9640strlpbf': ('IRF9640STRLPBF', 'IRF9640S', '31f381baf2926f90533e23b67d6fcf2141e59209dc84ce7dc576d2306d2f803c')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != 'IRF3205STRLPBF'
        or pilot.get('package') != 'to_263_3_d2pak' or pilot.get('model', {}).get('sha256') != MODEL_SHA):
        raise ValueError('D2PAK reference changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Vishay Intertech' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 4.6, 'length': 10.0, 'width': 9.2}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:TO-263-3_TabPin2'
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = 'Vishay Intertech'
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} D2PAK package review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and production codes are unverified in the local family sheets.')
        if mpn == 'IRF9640STRLPBF':
            recipe['appearance_status'] += ' Catalogue 6.8 A is the datasheet rating at 100 C; the 25 C rating is 11 A.'
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; shared-master validation and image review required')
    if args.add:
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


if __name__ == '__main__':
    main()
