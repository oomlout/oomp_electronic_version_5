"""Prepare individually researched TO-247 candidates for reviewed shared passes."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_134_amp_infineon_technologies_irfp4310zpbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_TO247_054N_3206_4368_9140N_RESEARCH.md')
PARTS = {'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_55_volt_81_amp_infineon_technologies_irfp054npbf': ('IRFP054NPBF', 'IRFP054N', '0840b3c5837940c22e751362f68d0709836c504169bab4156109e3b4fefdc8fb'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_60_volt_200_amp_infineon_technologies_irfp3206pbf': ('IRFP3206PBF', 'IRFP3206', 'c83661a9de11a87ba1410287d2d594ae57b59749da2b7be00e07e5fbb0d1eae6'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_75_volt_195_amp_infineon_technologies_irfp4368pbf': ('IRFP4368PBF', 'IRFP4368', 'b13fb07dec10cdaf9f8f3f6328360dedf6465f12e11489243c428489ecc5d7ac'), 'electronic_transistor_to_247ac_mosfet_p_channel_enhancement_mode_100_volt_23_amp_infineon_technologies_irfp9140npbf': ('IRFP9140NPBF', 'IRFP9140N', '72388b6a21765aaa8cd2b9893b884170b71a26d1a00973f75b7d5d8d96eb76c5')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != 'IRFP4310ZPBF' or pilot.get('package') != 'to_247_3'
        or pilot.get('model', {}).get('sha256') != 'ec0db59b04bcea2e0db6f976bf3ab8644e761c8b0059239f77f4febd6dc9eff4'):
        raise ValueError('Reference recipe changed; review again')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-247-3_Vertical'
            or record.get('dimensions_mm') != {'length': 15.9, 'width': 5.5, 'height': 15.6}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source identity, dimensions, footprint or drawing changed')
        recipe = copy.deepcopy(pilot)
        recipe['model']['display_lead_length_mm'] = 14.5
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['offset_x_mm'] = -7.575
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-247 drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and variable production details are unverified. The drawing example is a different device.')
        recipe['appearance_status'] = ('KiCad TO-247 model laid face-up, with display-only lead adjustment from '
            '20.15 mm to 14.50 mm, within this drawing\'s 14.20–16.10 mm range. The 20.95 mm body height '
            'exceeds the drawing maximum by 0.25 mm and the 15.9 mm width exceeds it by 0.03 mm. Lead features and finish are approximate; '
            'not a verified manufacturing model or footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; image review required')
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
