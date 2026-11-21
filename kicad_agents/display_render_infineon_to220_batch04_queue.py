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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_TO220_3415_4321_4020_260N_4227_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_150_volt_43_amp_infineon_technologies_irf3415pbf':
        ('IRF3415PBF', 'IRF3415', '7e2892980ab19f8cff67436c09a32b0c760938862826aced94cd9b768adef80e'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_150_volt_85_amp_infineon_technologies_irfb4321pbf':
        ('IRFB4321PBF', 'IRFB4321', '907310172833e06e17a2453ac73d5af61caadd71bfd7ede53645762abb97ee0c'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_18_amp_infineon_technologies_irfb4020pbf':
        ('IRFB4020PBF', 'IRFB4020', '067db60a56d8267be70f6a7f277798f1625f4456c46991191c1debe653b19002'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_56_amp_infineon_technologies_irfb260npbf':
        ('IRFB260NPBF', 'IRFB260N', '8e8635b817dede5b2b6db855bb9c4f19bfe055c61143df9c47172bee9b084992'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_200_volt_65_amp_infineon_technologies_irfb4227pbf':
        ('IRFB4227PBF', 'IRFB4227', '24c25a389825ead7e9595904bbab8daa71ef8a67002d6bdc19b7f674814998f0'),
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
        if mpn in ('IRF3415PBF', 'IRFB260NPBF'):
            recipe['appearance_status'] += ' The model lead projection is about 0.035 mm shorter than the drawing minimum.'
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
