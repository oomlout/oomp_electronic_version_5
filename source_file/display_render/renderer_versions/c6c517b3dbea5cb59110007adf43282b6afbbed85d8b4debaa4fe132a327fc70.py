"""Stage one unlit, unmarked generic 0201 blue LED package illustration."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_jscj_bzt52_sod123_composite import PILOT

PART = 'electronic_led_0201_blue'
MODEL_SHA = 'bcd380f55739b52e1c5111fcd4660667bb8fb66d0afc85738f969da7fa06d67b'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_LED_CONNECTOR_INVENTORY.md')


def prepare(recipes):
    source = ROOT / 'parts_source' / PART; record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') not in ('', None) or record.get('part_number_manufacturer') not in ('', None)
        or record.get('dimensions_mm') != {'length': .6, 'width': .3}
        or (record.get('kicad') or {}).get('machine_solder') != 'LED_SMD:LED_0201_0603Metric'
        or (source / 'datasheet.pdf').exists()):
        raise ValueError('Generic LED identity, footprint or local evidence changed')
    recipe = copy.deepcopy(recipes[PILOT]); recipe.update(family='led', package='0201_metric_0603',
        represented_manufacturer='Unspecified', represented_mpn='generic blue 0201 LED')
    recipe['disable_bump_for'] = ['ceramic', 'termination', 'pin_indicator']
    recipe['model'].update(relative_path='LED_SMD.3dshapes/LED_0201_0603Metric.step',
        source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/LED_SMD.3dshapes/LED_0201_0603Metric.step',
        copyright='2018 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[.65, .35, .2],
        required_roles=['ceramic', 'termination', 'pin_indicator'],
        role_by_source_colour={'0.895,0.891,0.813':'ceramic', '0.859,0.738,0.496':'termination', '0.340,0.680,0.445':'pin_indicator'})
    recipe['marking'] = {'policy':'unmarked_illustration', 'text':'', 'font_file':'arialbd.ttf',
        'evidence': {'file':EVIDENCE.as_posix(), 'sha256':hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest(),
            'document':'Generic LED model and source review', 'source_record':f'parts_source/{PART}/working.yaml'},
        'appearance_status':'Deliberately unmarked illustration: no manufacturer or exact part number is specified, so actual markings are unknown.'}
    recipe['appearance_status'] = ('Unlit generic KiCad 0201 LED package; blue describes emitted light, not necessarily lens colour. '
        'No exact manufacturer, lens appearance or local datasheet is specified. The 0.65 x 0.35 x 0.20 mm model is larger '
        'than the 0.60 x 0.30 mm nominal catalogue dimensions. Material finish is illustrative; not manufacturing CAD or a footprint.')
    return recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--add', action='store_true'); args=parser.parse_args()
    original=RECIPE_FILE.read_bytes(); recipes=json.loads(original.decode('utf8')); recipe=prepare(recipes)
    if PART in recipes and recipes[PART] != recipe: raise ValueError('Existing recipe differs')
    recipes[PART]=recipe
    if args.add:
        temp=None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                temp=Path(f.name); f.write((json.dumps(recipes,ensure_ascii=False,indent=2)+'\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes()!=original: raise RuntimeError('Recipes changed during validation')
            os.replace(temp,RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
    print('Generic 0201 LED candidate; preview and final review required')


if __name__ == '__main__': main()
