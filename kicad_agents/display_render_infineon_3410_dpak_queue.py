"""Prepare two individually documented IR 3410 DPAK display candidates."""
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_st_l78m05_dpak_queue import reviewed_recipe

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_3410_DPAK_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_17_amp_infineon_technologies_irlr3410trpbf':
        ('IRLR3410TRPBF', 'IRLR3410', '8b69599e659b38f3005c381517377511de273c0222928bb5ede95a288486ffe5'),
    'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_31_amp_infineon_technologies_irfr3410trpbf':
        ('IRFR3410TRPBF', 'IRFR3410', '7015efbc3d08d5b97943d7f394847205de662585a8201cf59a1764a6d070c155'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    reference = {'manufacturer': 'STMicroelectronics', 'part_number_manufacturer': 'L78M05ABDT-TR',
                 'kicad': {'machine_solder': ''}, 'dimensions_mm': {'length': 10.0, 'width': 5.0}}
    for part, (mpn, marking, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'Infineon Technologies' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:TO-252-3_TabPin2'
            or record.get('dimensions_mm') != {'length': 6.5, 'width': 6.1, 'height': 2.3}
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source identity, dimensions, footprint or drawing changed')
        recipe = reviewed_recipe(reference, recipes, evidence_sha)
        recipe['family'] = 'transistor'
        recipe['represented_manufacturer'] = 'Infineon Technologies'
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} DPAK drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and variable production details are unverified. The drawing example is a different device.')
        recipe['appearance_status'] = ('The KiCad TO-252-2 display model approximates the drawing with two full leads, '
            'a short centre stub and a metal tab; its overall bounds are 9.9 x 6.5 x 2.32 mm. The catalogue footprint '
            'remains TO-252-3_TabPin2. Stub dimensions, finish and marking are approximate; not a manufacturing model.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; preview review required')
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
