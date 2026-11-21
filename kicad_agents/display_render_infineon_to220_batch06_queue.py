"""Prepare five individually researched Infineon TO-220 display recipes."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PILOT = 'electronic_transistor_to_220_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfb4110pbf'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_TO220_3307Z_3808_3207_3077_3607_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_128_amp_infineon_technologies_irfb3307zpbf':
        ('IRFB3307ZPBF', 'IRFB3307Z', '943df424f5930dd329185fa70540f48924babe4f02b352b9528e1b0b7d8d010d'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_140_amp_infineon_technologies_irf3808pbf':
        ('IRF3808PBF', 'IRF3808', '7e05b9d8637d7239f32badba4a7fc1dc28507a4afc697f21a7b4dc56614bc1b9'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_180_amp_infineon_technologies_irfb3207pbf':
        ('IRFB3207PBF', 'IRFB3207', 'ff3d70e907ae828fdc22927d250773e416bd516a04adb82b7cfc1c978c05d5df'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_210_amp_infineon_technologies_irfb3077pbf':
        ('IRFB3077PBF', 'IRFB3077', '0e11e02561b2b921589f084a2bf25a2c4de7d35641f89e1363209d41230bec0c'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_75_volt_80_amp_infineon_technologies_irfb3607pbf':
        ('IRFB3607PBF', 'IRFB3607', '86d87046d5bbb81516c88a6e4ec7cf7387ce2190588deb6fbb784f1598e77aa0'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != 'IRFB4110PBF' or pilot.get('package') != 'to_220_3'
        or pilot.get('model', {}).get('sha256') != '7cb065d935df5771f0ba6e48ddd180863a121af76483dad7f18e667a7b68204a'):
        raise ValueError('Reference recipe changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-220-3_Vertical'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 4.4, 'height': 9.2}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source, footprint, dimensions or PDF changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['policy'] = 'illustrative_literal'
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-220 drawing review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact marking, typeface, logo and lot/date are unverified.')
        recipe['appearance_status'] = ('KiCad TO-220-3 model is laid face-up and measures 10.25 x 4.455 x 28.525 mm '
            'including leads. Source dimensions are generic; lead proportions and finish are approximate, '
            'not a verified mechanical model or footprint.')
        if mpn == 'IRFB3207PBF':
            recipe['appearance_status'] += ' The local family PDF does not independently confirm the PbF orderable suffix.'
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
