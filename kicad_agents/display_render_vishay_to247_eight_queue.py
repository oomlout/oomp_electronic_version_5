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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VISHAY_TO247_EIGHT_RESEARCH.md')
PARTS = {'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_1000_volt_6_1_amp_vishay_intertech_irfpg50pbf': ('IRFPG50PBF', 'IRFPG50', '5eb9a82d8f5b96c9692bda5b31f2b78623d4fb47aa24da177ece02756e8cb6ee'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_20_amp_vishay_intertech_irfp240pbf': ('IRFP240PBF', 'IRFP240', 'ad047f63577c64af0dd345027fa71f490ec609b5ac7711d767640639b5fce005'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_400_volt_16_amp_vishay_intertech_irfp350pbf': ('IRFP350PBF', 'IRFP350', '35f0f047fd6dc4d1e4222c8c0ef54871b71125117a6f3249f701a2d679fd8b80'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_20_amp_vishay_intertech_irfp460apbf': ('IRFP460APBF', 'IRFP460A', '28cc93d2e5d770ca25dd2a8ff9d43bccc0ff4d22957d65a75814d6f2a95bd594'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_20_amp_vishay_intertech_irfp460pbf': ('IRFP460PBF', 'IRFP460', '0281a22d9bbf49618f051fe9f8dbb948964c8769d8fc17bb7d1bc00e91b9426b'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_500_volt_8_7_amp_vishay_intertech_irfp450pbf': ('IRFP450PBF', 'IRFP450', 'f19963c186b86847209ca919683a9a44635c95b393be94c9b0ec76808f2bcd5b'), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_600_volt_16_amp_vishay_intertech_irfpc60lcpbf': ('IRFPC60LCPBF', 'IRFPC60LC', '5f6e6ff956e36db31bf36948d7ff0828cddfad85af47e53db5757adc4caabf25'), 'electronic_transistor_to_247ac_mosfet_p_channel_enhancement_mode_200_volt_12_amp_vishay_intertech_irfp9240pbf': ('IRFP9240PBF', 'IRFP9240', '003f28e7d50fcda89b7fa7bf8473470b3e30916b2af79184b577c5dc5a02c10b')}


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
        if (record.get('manufacturer') != 'Vishay Intertech' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-247-3_Vertical'
            or record.get('dimensions_mm') != {'length': 15.9, 'width': 5.5, 'height': 15.6}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source identity, dimensions, footprint or drawing changed')
        recipe = copy.deepcopy(pilot)
        recipe['model']['display_lead_length_mm'] = 14.5
        recipe['represented_manufacturer'] = 'Vishay Intertech'
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['offset_x_mm'] = -7.575
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-247 drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and variable production details are unverified. The drawing example is a different device.')
        recipe['appearance_status'] = ('KiCad TO-247 model laid face-up, with display-only lead adjustment from '
            '20.15 mm to 14.50 mm, within this drawing\'s 14.20–16.25 mm range. The 20.95 mm body height '
            'exceeds the drawing maximum by 0.13 mm and the 15.9 mm width exceeds it by 0.03 mm. Lead features and finish are approximate; '
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
