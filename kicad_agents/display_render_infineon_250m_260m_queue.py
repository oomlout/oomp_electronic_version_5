"""Prepare two TO-247 recipes with drawing-specific lead lengths."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_infineon_4468_4568_queue import PILOT

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IRFP250M_260M_RESEARCH.md')
PARTS = {'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_30_amp_infineon_technologies_irfp250mpbf': ('IRFP250MPBF', 'IRFP250M', 'd673e0f247037243912d1b8b1fe94580867124c3959feb5525ee63fa0c064abd', True), 'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_200_volt_50_amp_infineon_technologies_irfp260mpbf': ('IRFP260MPBF', 'IRFP260M', 'dd921441b9a9c633874eeb7642180ec077cb574988a0ab6f1e2c9d8039a58583', True)}


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
    for part, (mpn, marking, pdf_sha, long_leads) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-247-3_Vertical'
            or record.get('dimensions_mm') != {'length': 15.9, 'width': 5.5, 'height': 15.6}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source identity, dimensions, footprint or drawing changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-247 drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and variable production details are unverified. The drawing example is a different device.')
        if long_leads:
            # This explicit model variant also prevents accidental reuse of the shortened-lead shared master.
            recipe['model']['display_lead_length_mm'] = 20.15
            recipe['marking']['offset_x_mm'] = -10.075
            recipe['disable_bump_for'] = ['coating']
            recipe['appearance_status'] = ('KiCad TO-247 model laid face-up with original 20.15 mm leads, within '
                'the drawing\'s 19.80–20.32 mm range. The original model body fits its stated drawing envelope. '
                'Finish, marking and fine details are approximate; not a verified manufacturing model or footprint. '
                'Body surface bump is omitted to avoid numerical instability in the rendering backend.')
        else:
            recipe['appearance_status'] = ('KiCad TO-247 model laid face-up, with display-only lead adjustment '
                'from 20.15 mm to 15.15 mm, within the drawing\'s 14.20–16.10 mm range. The 20.95 mm body '
                'height and 15.9 mm width slightly exceed drawing maxima. Finish and details are approximate; '
                'not a verified manufacturing model or footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; individual image review required')
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
