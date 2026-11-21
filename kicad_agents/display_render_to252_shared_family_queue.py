"""Stage reviewed DPAK candidates supported by existing sibling family PDFs."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TO252_SHARED_FAMILY_RESEARCH.md')
PILOT = 'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_10_amp_infineon_technologies_irlr120ntrpbf'
PARTS = {
    'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfr120ntrpbf':
        ('Infineon Technologies', 'IRFR120NTRPBF', 'IRFR120N', 'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfu120npbf', '83dc4858004a978949d3e5581a73af82953b8b90c6549b72f88c278bbf8506d9'),
    'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfr220ntrpbf':
        ('Infineon Technologies', 'IRFR220NTRPBF', 'IRFR220N', 'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_200_volt_5_amp_infineon_technologies_irfu220npbf', '7b8b6e32281bb5b9d3dfde103740646d3ca80293b6efbe9e0f637b920e5af154'),
    'electronic_transistor_to_252_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlr024ntrpbf':
        ('Infineon Technologies', 'IRLR024NTRPBF', 'IRLR024N', 'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlu024npbf', 'ff52b6382c5eabdd1e267f1d4cbdf0fbbd81d4a4854a20efdd77225fdae3ed4a'),
    'electronic_transistor_to_252_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfr5410trpbf':
        ('Infineon Technologies', 'IRFR5410TRPBF', 'IRFR5410', 'electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfu5410pbf', '89490495713f68cfef9d64778bfcba51014763eca5762c87f3edca55c5097228'),
    'electronic_transistor_to_252_bipolar_pnp_80_volt_8_amp_onsemi_mjd45h11g':
        ('onsemi', 'MJD45H11G', 'J4\n5H11G', 'electronic_transistor_to_251_bipolar_npn_80_volt_8_amp_onsemi_mjd44h11_1g', '4f95f0add038033491b7bc1c6a5db1e24b409d5572cc6ec42f1b33438a5d6176'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != 'IRLR120NTRPBF' or pilot.get('package') != 'to_252_2_dpak'
        or pilot.get('model', {}).get('sha256') != '3eb4c99603a4fe837c2fe9308bc174769ded87a785a0df48d2dc441432ee8b4c'):
        raise ValueError('DPAK pilot changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (manufacturer, mpn, marking, sibling, pdf_sha) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 2.3, 'length': 6.5, 'width': 6.1}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:TO-252-3_TabPin2'
            or (source / 'datasheet.pdf').exists()):
            raise ValueError(f'{mpn}: source identity, footprint, dimensions or PDF availability changed')
        pdf = ROOT / 'parts_source' / sibling / 'datasheet.pdf'
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != pdf_sha:
            raise ValueError(f'{mpn}: shared PDF changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = manufacturer
        recipe['represented_mpn'] = mpn
        recipe['marking'].update(text=marking, evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} shared family drawing and display review', 'source_record': f'parts_source/{part}/working.yaml'})
        if manufacturer == 'onsemi':
            recipe['marking'].update(policy='verified_literal', appearance_status='The fixed device code and G mark follow the onsemi family diagram; variable production codes are omitted. Typeface and placement are illustrative.')
        else:
            recipe['marking'].update(policy='illustrative_literal', appearance_status=f'{marking} is an illustrative partial identifier; exact top marking, typeface, placement and production details are unverified. The drawing example is a different device.')
        recipe['appearance_status'] += f' The family PDF is stored with {sibling}; this part has no separate local PDF.'
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; final image review required')
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
