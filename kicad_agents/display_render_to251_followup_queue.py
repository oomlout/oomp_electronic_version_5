"""Stage five individually researched TO-251 display candidates."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_infineon_irfu220n_to251_queue import PART as PILOT, MODEL_SHA

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_TO251_FOLLOWUP_RESEARCH.md')
PARTS = {
    'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_16_amp_infineon_technologies_irfu3910pbf': ('IRFU3910PBF', 'IRFU3910', '2ab4bf8282d54922c1cb81bea73e53183abef4a44a8e305e8c1f291c3c9ee3f7', 'Infineon Technologies'),
    'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_100_volt_9_4_amp_infineon_technologies_irfu120npbf': ('IRFU120NPBF', 'IRFU120N', '83dc4858004a978949d3e5581a73af82953b8b90c6549b72f88c278bbf8506d9', 'Infineon Technologies'),
    'electronic_transistor_to_251_mosfet_n_channel_enhancement_mode_55_volt_17_amp_infineon_technologies_irlu024npbf': ('IRLU024NPBF', 'IRLU024N', 'ff52b6382c5eabdd1e267f1d4cbdf0fbbd81d4a4854a20efdd77225fdae3ed4a', 'Infineon Technologies'),
    'electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_100_volt_13_amp_infineon_technologies_irfu5410pbf': ('IRFU5410PBF', 'IRFU5410', '89490495713f68cfef9d64778bfcba51014763eca5762c87f3edca55c5097228', 'Infineon Technologies'),
    'electronic_transistor_to_251_mosfet_p_channel_enhancement_mode_60_volt_8_8_amp_vishay_intertech_irfu9024pbf': ('IRFU9024PBF', 'IRFU9024', '82e0db9093d479da7bb32be0903e9a4aa356705fbfb07abd1d8b3467fef72bb0', 'Vishay Intertech'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    pilot = recipes[PILOT]
    if (pilot.get('represented_mpn') != 'IRFU220NPBF' or pilot.get('package') != 'to_251_3_ipak'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA):
        raise ValueError('TO-251 reference changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking, pdf_sha, manufacturer) in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != manufacturer or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 2.5, 'length': 6.6, 'width': 6.2}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-251-3_Vertical'
            or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != pdf_sha):
            raise ValueError(f'{mpn}: source or drawing changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = manufacturer
        recipe['represented_mpn'] = mpn
        recipe['marking']['text'] = marking
        recipe['marking']['evidence'] = {'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
            'document': f'{mpn} TO-251 package review', 'source_record': f'parts_source/{part}/working.yaml'}
        recipe['marking']['appearance_status'] = (f'{marking} is an illustrative partial identifier; exact top marking, '
            'typeface, placement and production codes are unverified in the family drawing.')
        if mpn == 'IRFU3910PBF':
            recipe['appearance_status'] += ' The local family PDF does not independently confirm the exact full orderable suffix.'
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{mpn}: existing recipe differs')
        recipes[part] = recipe
        print(mpn, 'candidate only; shared-master validation and image review required')
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
