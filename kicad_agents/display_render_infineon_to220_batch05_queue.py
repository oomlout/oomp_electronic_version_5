"""Prepare four individually researched Infineon TO-220 display recipes."""
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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_TO220_4229_3306_3206_1010E_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_250_volt_46_amp_infineon_technologies_irfb4229pbf':
        ('IRFB4229PBF', 'IRFB4229', '897e32ff2ec11adf865d4ac7296f5c78d105aa4cded9004e1864feaf656bbd9e'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_160_amp_infineon_technologies_irfb3306pbf':
        ('IRFB3306PBF', 'IRFB3306', '3a42104e8b332cf0efd4c6b9b6d73746ac790dab82b6e4b623e6ca6b7f794a0a'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_210_amp_infineon_technologies_irfb3206pbf':
        ('IRFB3206PBF', 'IRFB3206', '01d48711bec8bc03eab9638341c609cf73fb014f6831f67601f54e88740cb484'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_60_volt_83_amp_infineon_technologies_irf1010epbf':
        ('IRF1010EPBF', 'IRF1010E', '7f0abaa51fc109f421ba747bc91b764da4693995b102df5494b02b9b05e02ab6'),
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
        recipe['marking']['policy'] = 'verified_literal' if mpn in ('IRFB3306PBF', 'IRFB3206PBF') else 'illustrative_literal'
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-220 drawing review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (
            f'{marking} follows the manufacturer family marking example; typeface, logo, placement and lot/date are approximate.'
            if mpn in ('IRFB3306PBF', 'IRFB3206PBF') else
            f'{marking} is an illustrative partial identifier; exact marking, typeface, logo and lot/date are unverified.')
        recipe['appearance_status'] = ('KiCad TO-220-3 model is laid face-up and measures 10.25 x 4.455 x 28.525 mm '
            'including leads. Source dimensions are generic; lead proportions and finish are approximate, '
            'not a verified mechanical model or footprint.')
        if mpn == 'IRF1010EPBF':
            recipe['appearance_status'] += ' The model lead projection is about 0.035 mm shorter than the drawing minimum.'
        if mpn == 'IRF1010EPBF':
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
