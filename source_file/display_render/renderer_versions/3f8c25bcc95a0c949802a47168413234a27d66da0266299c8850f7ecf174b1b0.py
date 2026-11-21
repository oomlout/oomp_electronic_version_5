"""Prepare unmarked SOT-23 illustrations for generic transistor entries."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

REFERENCE = 'electronic_transistor_sot_23_bipolar_npn_25_volt_1_5_amp_jsmsemi_ss8050'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_GENERIC_TRANSISTOR_PACKAGES_RESEARCH.md')
PARTS = {
    'electronic_transistor_sot_23_bipolar_npn': 'generic NPN transistor',
    'electronic_transistor_sot_23_bipolar_pnp': 'generic PNP transistor',
    'electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode': 'generic N-channel MOSFET',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    for part, label in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8'))
        if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
            or record.get('dimensions_mm') != {'length': 2.9, 'width': 2.6}
            or (record.get('kicad') or {}).get('machine_solder') != '' or (source / 'datasheet.pdf').exists()):
            raise ValueError(f'{part}: source identity, footprint or PDF availability changed')
        recipe = copy.deepcopy(recipes[REFERENCE])
        if (recipe['model']['sha256'] != 'dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'
            or recipe['model'].get('display_scale_xyz') != [1., 1., .9166666666666666]):
            raise ValueError('Reviewed SOT-23 model changed')
        recipe.update(represented_manufacturer='Unspecified', represented_mpn=label)
        recipe['marking'].update(policy='unmarked_illustration', text='', evidence={'file': EVIDENCE.as_posix(),
            'sha256': hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
            'document': f'{label} generic SOT-23 package review', 'source_record': f'parts_source/{part}/working.yaml'},
            appearance_status='Deliberately unmarked illustration: no manufacturer or part number is specified, and actual devices may carry different codes.')
        recipe['appearance_status'] = ('Generic KiCad SOT-23 2.5 x 3.0 x 1.2 mm model is vertically scaled to 1.1 mm. No exact manufacturer or device is specified and there is no separate local PDF. Finish and fine details are illustrative; not manufacturing CAD or a footprint.')
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
        print(label, 'unmarked illustration candidate; final review required')
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
