"""Prepare nine source-reviewed TI SOIC-8 power and timer recipes.

Read-only by default; --add requires the independent TI SOIC-8 pilot to have
been published. Each rendered candidate requires its own visual review.
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

from kicad_agents.display_render_ti_soic8_batch import FOOTPRINT
from kicad_agents.display_render_ti_soic8_pilot_queue import MODEL_SHA256, PART, ROOT, RECIPE_FILE

POWER='kicad_agents/component_records/DISPLAY_RENDER_TI_SOIC8_POWER_EVIDENCE.md'
TIMING='kicad_agents/component_records/DISPLAY_RENDER_TI_SOIC8_TIMING_EVIDENCE.md'
CANDIDATES=(
 ('electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tl431aidr','TL431AIDR','431AI',POWER),
 ('electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tl431cdr','TL431CDR','TL431C',POWER),
 ('electronic_ic_power_management_current_mode_pwm_controller_soic_8_texas_instruments_ucc38c40dr','UCC38C40DR','38C40',POWER),
 ('electronic_ic_power_management_current_mode_pwm_controller_soic_8_texas_instruments_ucc2802dtr','UCC2802DTR','UCC2802',POWER),
 ('electronic_ic_power_management_shunt_regulator_soic_8_texas_instruments_tlv431aidr','TLV431AIDR','TY431A',TIMING),
 ('electronic_ic_power_management_voltage_supervisor_5_volt_soic_8_texas_instruments_tl7705bidr','TL7705BIDR','7705BI',TIMING),
 ('electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_sa555dr','SA555DR','SA555',TIMING),
 ('electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_tlc555cdr','TLC555CDR','TL555C',TIMING),
 ('electronic_ic_timer_555_precision_timer_soic_8_texas_instruments_tlc555idr','TLC555IDR','TL555I',TIMING),
)


def prepare(recipes):
    pilot=recipes[PART]
    if (pilot.get('represented_mpn') != 'NE5532DR' or pilot.get('marking',{}).get('text') != 'N5532'
        or pilot.get('model',{}).get('sha256') != MODEL_SHA256):
        raise ValueError('TI pilot changed; review before preparing candidates')
    result={}
    for part,mpn,text,evidence in CANDIDATES:
        record=yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf-8')) or {}
        dims=record.get('dimensions_mm') or {}
        if (record.get('manufacturer') != 'Texas Instruments' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder') != FOOTPRINT
            or dims.get('length') != 4.9 or dims.get('width') != 3.9 or dims.get('height') is not None):
            raise ValueError(f'Identity, footprint or dimensions changed for {part}')
        raw=(ROOT/evidence).read_bytes()
        if not any(part in line and mpn in line and f'`{text}`' in line for line in raw.decode('utf-8').splitlines()):
            raise ValueError(f'Marking evidence changed for {part}')
        recipe=copy.deepcopy(pilot); recipe['represented_mpn']=mpn
        mark=recipe['marking']; mark['text']=text
        mark['evidence']={'file':evidence,'sha256':hashlib.sha256(raw).hexdigest(),
                          'document':'TI SOIC-8 exact marking and package review',
                          'source_record':f'parts_source/{part}/working.yaml'}
        mark['appearance_status']=(f'TI lists {text} as the package marking. Typeface, placement, '
                                   'logos and variable lot/date details are illustrative.')
        recipe['appearance_status']+=' Catalogue source does not specify height.'
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'Existing recipe differs for {part}; preserve it')
        result[part]=recipe
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--add',action='store_true')
    args=parser.parse_args(); original=RECIPE_FILE.read_bytes(); recipes=json.loads(original.decode('utf-8'))
    additions=prepare(recipes)
    if args.add:
        path=ROOT/'parts'/PART/'data/display_render/manifest.json'
        if not path.is_file(): raise ValueError('Inspect and publish the independent pilot first')
        manifest=json.loads(path.read_text(encoding='utf-8'))
        if manifest.get('part_id') != PART or manifest.get('recipe') != recipes[PART]:
            raise ValueError('Published TI pilot differs from its current recipe')
        for part,recipe in additions.items(): recipes.setdefault(part,recipe)
        updated=(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n').encode('utf-8')
        if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed during validation')
        if updated != original:
            temp=None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                    temp=Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes() != original: raise RuntimeError('Recipes changed before replacement')
                os.replace(temp,RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(f'Validated {len(additions)} TI power/timer identities; added={args.add}')


if __name__ == '__main__': main()
