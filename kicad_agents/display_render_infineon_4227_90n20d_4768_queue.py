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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_TO247_4227_90N20D_4768_RESEARCH.md')
PARTS = {
'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_65_amp_infineon_technologies_irfp4227pbf': ('IRFP4227PBF','IRFP4227','5acee2d999fe0b2f34804e0006d30472f673d00eb02fbbcbdc816a9b9bb23e0f'),
'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_94_amp_infineon_technologies_irfp90n20dpbf': ('IRFP90N20DPBF','IRFP90N20D','effdb2e7788c96c5d9081f5ddd49ffca48920316389a5c30aff94581a0edbc33'),
'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_250_volt_93_amp_infineon_technologies_irfp4768pbf': ('IRFP4768PBF','IRFP4768','e60c22facecfb51e49f42f27fd2106dc402e23ebfa57638e8a80f4330be6dc4b'),
}


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
