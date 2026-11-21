"""Stage two evidence-backed onsemi IPAK display candidates."""
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

EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_ONSEMI_MJD44H11_MJD45H11_TO251_RESEARCH.md')
SOURCE = 'electronic_transistor_to_251_bipolar_npn_80_volt_8_amp_onsemi_mjd44h11_1g'
PARTS = {
    SOURCE: ('MJD44H11-1G', 'J4\n4H11G'),
    'electronic_transistor_to_251_bipolar_pnp_80_volt_8_amp_onsemi_mjd45h11_1g': ('MJD45H11-1G', 'J4\n5H11G'),
}
PDF_SHA = '4f95f0add038033491b7bc1c6a5db1e24b409d5572cc6ec42f1b33438a5d6176'


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
    if hashlib.sha256((ROOT / 'parts_source' / SOURCE / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Shared onsemi datasheet changed')
    evidence_sha = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    for part, (mpn, marking) in PARTS.items():
        record = yaml.safe_load((ROOT / 'parts_source' / part / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') != 'onsemi' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 2.5, 'length': 6.6, 'width': 6.2}
            or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_THT:TO-251-3_Vertical'):
            raise ValueError(f'{mpn}: source changed')
        recipe = copy.deepcopy(pilot)
        recipe['represented_manufacturer'] = 'onsemi'
        recipe['represented_mpn'] = mpn
        recipe['marking'].update(policy='verified_literal', text=marking,
            evidence={'file': EVIDENCE.as_posix(), 'sha256': evidence_sha,
                'document': f'{mpn} onsemi shared datasheet marking and package review',
                'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status='The fixed device code and G mark follow the onsemi family diagram; variable assembly and date codes are omitted. Typeface and placement are illustrative.')
        if part != SOURCE:
            recipe['appearance_status'] += ' The family PDF is stored with MJD44H11-1G; this part has no separate local PDF.'
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
