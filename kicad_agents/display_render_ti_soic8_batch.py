"""Prepare individually evidenced TI SOIC-8 amplifier candidates.

Read-only unless --add is given after the independent NE5532DR pilot has been
reviewed and published. Each candidate still needs individual visual review.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml

from kicad_agents.display_render_ti_soic8_pilot_queue import (
    EVIDENCE, MODEL_SHA256, PART, ROOT, RECIPE_FILE,
)

EXTRA = 'kicad_agents/component_records/DISPLAY_RENDER_TI_SOIC8_ADDITIONAL_EVIDENCE.md'
DRIVERS = 'kicad_agents/component_records/DISPLAY_RENDER_TI_SOIC8_DRIVER_EVIDENCE.md'
FOOTPRINT = 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm'
CANDIDATES = (
    ('electronic_ic_amplifier_operational_amplifier_dual_soic_8_texas_instruments_lm358dr', 'LM358DR', 'LM358', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_dual_cmos_soic_8_texas_instruments_tlc27m2cdr', 'TLC27M2CDR', '27M2C', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_dual_jfet_input_soic_8_texas_instruments_tl072idr', 'TL072IDR', 'TL072I', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_dual_jfet_input_soic_8_texas_instruments_tl082idr', 'TL082IDR', 'TL082I', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_dual_rail_to_rail_soic_8_texas_instruments_tlc2272cdr', 'TLC2272CDR', '2272C', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_precision_soic_8_texas_instruments_op07cdr', 'OP07CDR', 'OP07C', EVIDENCE),
    ('electronic_ic_amplifier_operational_amplifier_dual_jfet_low_power_soic_8_texas_instruments_tl062idr', 'TL062IDR', 'TL062I', EXTRA),
    ('electronic_ic_amplifier_operational_amplifier_dual_low_power_soic_8_texas_instruments_tlc27l2cdr', 'TLC27L2CDR', '27L2C', EXTRA),
    ('electronic_ic_driver_dual_peripheral_driver_soic_8_texas_instruments_sn75453bdr', 'SN75453BDR', '75453B', DRIVERS),
    ('electronic_ic_driver_peripheral_driver_soic_8_texas_instruments_sn75451bdr', 'SN75451BDR', '75451B', DRIVERS),
    ('electronic_ic_interface_rs485_rs422_transceiver_soic_8_texas_instruments_sn75176bdr', 'SN75176BDR', '75176B', DRIVERS),
    ('electronic_ic_interface_rs_485_transceiver_soic_8_texas_instruments_sn65hvd3082edr', 'SN65HVD3082EDR', 'VP3082', DRIVERS),
)


def prepare(recipes):
    pilot = recipes[PART]
    if (pilot.get('represented_mpn') != 'NE5532DR' or pilot.get('marking', {}).get('text') != 'N5532'
        or pilot.get('model', {}).get('sha256') != MODEL_SHA256):
        raise ValueError('TI pilot changed; review before batch preparation')
    result = {}
    for part, mpn, text, evidence in CANDIDATES:
        record = yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf-8')) or {}
        dims = record.get('dimensions_mm') or {}
        if (record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
            or dims.get('length') != 4.9 or dims.get('width') != 3.9
            or dims.get('height') not in (None, 1.75)):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        raw = (ROOT/evidence).read_bytes()
        if not any(part in line and mpn in line and f'`{text}`' in line for line in raw.decode('utf-8').splitlines()):
            raise ValueError(f'Marking evidence changed for {part}')
        recipe = copy.deepcopy(pilot)
        recipe['represented_mpn'] = mpn
        mark = recipe['marking']
        mark['text'] = text
        mark['evidence'] = {'file': evidence, 'sha256': hashlib.sha256(raw).hexdigest(),
            'document': 'TI SOIC-8 manufacturer marking and package review',
            'source_record': f'parts_source/{part}/working.yaml'}
        mark['appearance_status'] = (f'TI lists {text} as the package marking. Typeface, placement, '
                                     'logos and variable lot/date details are illustrative.')
        if 'height' not in dims:
            recipe['appearance_status'] += ' Catalogue source does not specify height.'
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'Existing recipe differs for {part}; preserve it')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf-8'))
    additions = prepare(recipes)
    if args.add:
        manifest_path = ROOT/'parts'/PART/'data/display_render/manifest.json'
        if not manifest_path.is_file():
            raise ValueError('Inspect and publish the independent TI pilot first')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest.get('part_id') != PART or manifest.get('recipe') != recipes[PART]:
            raise ValueError('Published TI pilot differs from the current recipe')
        for part, recipe in additions.items():
            recipes.setdefault(part, recipe)
        updated = (json.dumps(recipes, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original:
            raise RuntimeError('Recipes changed during validation; refusing to overwrite')
        if updated != original:
            tmp = None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                    tmp = Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original:
                    raise RuntimeError('Recipes changed before replacement; refusing to overwrite')
                os.replace(tmp, RECIPE_FILE)
            finally:
                if tmp is not None and tmp.exists(): tmp.unlink()
    print(f'Validated {len(additions)} TI source identities; added={args.add}')


if __name__ == '__main__':
    main()
