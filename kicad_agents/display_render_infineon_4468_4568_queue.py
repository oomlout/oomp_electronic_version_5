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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_4468_4568_TO247_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_290_amp_infineon_technologies_irfp4468pbf':
        ('IRFP4468PBF', 'IRFP4468', 'f1ec6fda95d9a163f8cbfe12335dbeb0a9586d2825f67e790aa91c0b38c0d0ef'),
    'electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_150_volt_171_amp_infineon_technologies_irfp4568pbf':
        ('IRFP4568PBF', 'IRFP4568', 'fc390da2bcba48050d046ce430413abb0567e53b28d86ac8959d2b025b639e4c'),
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
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-247 drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and variable production details are unverified. The drawing example is a different device.')
        recipe['appearance_status'] = ('KiCad TO-247 model laid face-up, with display-only lead adjustment from '
            '20.15 mm to 15.15 mm, within this drawing\'s 14.20–16.10 mm range. The 20.95 mm body height and '
            '15.9 mm width slightly exceed the drawing maxima. Lead features and finish are approximate; '
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
