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
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_VISHAY_TO220_520_710_740_830_830A_840A_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_100_volt_9_2_amp_vishay_intertech_irf520pbf':
        ('IRF520PBF', 'IRF520', '798bb2f284c04062ff4c0aa81cd28bb0c6df17c7f8f875b3da6e3f65008f82a5'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_400_volt_2_amp_vishay_intertech_irf710pbf':
        ('IRF710PBF', 'IRF710', '0de15d2793793a6c0aa3137889dddbef1400a8cc811fe3e60d5ba7abbff8a262'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_400_volt_10_amp_vishay_intertech_irf740pbf':
        ('IRF740PBF', 'IRF740', '65e85050397c1ed9b63762f645404792da3d99a8c8ae4da9ab98ea609d92af81'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_4_5_amp_vishay_intertech_irf830pbf':
        ('IRF830PbF', 'IRF830', '238cfc9e35cf1b2959b64d96b4854e03d2af899cb11af2f6eb00f15845caa45e'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_5_amp_vishay_intertech_irf830apbf':
        ('IRF830APBF', 'IRF830A', '0b238432a65dde04f1a69e31456caccb2ad81d628f46cef3e17617d8391cd175'),
    'electronic_transistor_to_220ab_mosfet_n_channel_enhancement_mode_500_volt_8_amp_vishay_intertech_irf840apbf':
        ('IRF840APBF', 'IRF840A', 'aa81820697f003a0dd6c7054c4ce2664f36be88c51243904f336577fc59d77ed'),
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
        if (record.get('manufacturer') != 'Vishay Intertech' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-220-3_Vertical'
            or record.get('dimensions_mm') != {'length': 10.0, 'width': 4.4, 'height': 9.2}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source, footprint, dimensions or PDF changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = 'Vishay Intertech'
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['policy'] = 'illustrative_literal'
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-220 drawing review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact marking, typeface, logo and lot/date are unverified.')
        recipe['appearance_status'] = ('KiCad TO-220-3 model is laid face-up and measures 10.25 x 4.455 x 28.525 mm '
            'including leads. Source dimensions are generic; lead proportions and finish are approximate, '
            'not a verified mechanical model or footprint.')
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
