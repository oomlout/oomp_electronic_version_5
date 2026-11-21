"""Stage an explicitly illustrative generic 2N7002 display candidate."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002'
REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_2N7002_RESEARCH.md')
PDF_SHA = 'cc9c275457670c3cbbf2e56f5a75c800d3b5f0b396fabc798cf18cb639646475'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    source = ROOT / 'parts_source' / PART
    record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
    if (record.get('manufacturer') != 'Generic' or record.get('part_number_manufacturer') not in ('', None)
        or record.get('dimensions_mm') != {'length': 2.9, 'width': 2.3}
        or (record.get('kicad') or {}).get('machine_solder') != 'Package_TO_SOT_SMD:SOT-23'
        or hashlib.sha256((source / 'datasheet.pdf').read_bytes()).hexdigest() != PDF_SHA):
        raise ValueError('Generic source record or example datasheet changed')
    recipe = copy.deepcopy(recipes[REFERENCE])
    if (recipe['model']['sha256'] != 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'
        or recipe['model'].get('display_scale_xyz') != [1., 1., .9166666666666666]):
        raise ValueError('Reviewed SOT-23 model changed')
    recipe.update(represented_manufacturer='Generic (exact manufacturer unspecified)', represented_mpn='2N7002 family')
    recipe['marking'].update(policy='illustrative_literal', text='12', evidence={'file': EVIDENCE.as_posix(),
        'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
        'document': 'Nexperia 2N7002 family example and SOT-23 package review', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='12 is an illustrative Nexperia family example, not a verified marking for this generic record. The manufacturing-site code, typeface and placement are illustrative or omitted.')
    recipe['appearance_status'] = ('Generic 2N7002 record has no specified manufacturer or exact orderable; the local Nexperia PDF provides an example. KiCad SOT-23 2.5 x 3.0 x 1.2 mm display model is scaled vertically to 1.1 mm. Finish and fine details are illustrative; not manufacturing CAD or a footprint.')
    if PART in recipes and recipes[PART] != recipe:
        raise ValueError('Existing recipe differs')
    recipes[PART] = recipe
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
    print('Generic 2N7002 illustrative candidate; final review required')


if __name__ == '__main__':
    main()
