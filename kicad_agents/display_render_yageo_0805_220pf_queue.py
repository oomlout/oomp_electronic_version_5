"""Prepare a Yageo 0805 display with evidence and catalogue discrepancies."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

PART = 'electronic_capacitor_0805_220_pico_farad'
PILOT = 'electronic_capacitor_0805_10_micro_farad_16_volt'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0805_220PF_EVIDENCE.md')

def reviewed_recipe(record, recipes, sha):
    if record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != 'CC0805KRX7R9BB221': raise ValueError('Identity changed')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == 'CC0805KRX7R9BB221' for x in record.get('manufacturers', []) if isinstance(x, dict)): raise ValueError('Manufacturer entry changed')
    if not any(x.get('part_number') == 'C107145' for x in record.get('distributors', []) if isinstance(x, dict)): raise ValueError('Supplier changed')
    if record.get('kicad', {}).get('machine_solder') != 'Capacitor_SMD:C_0805_2012Metric': raise ValueError('Footprint changed')
    d = record.get('dimensions_mm') or {}
    if (d.get('length'), d.get('width'), d.get('height')) != (2.0, 1.25, 1.25): raise ValueError('Reviewed source dimensions changed')
    e = record.get('electrical') or {}
    for k,v in (('capacitance','220 pF'),('rated_voltage','50 V'),('dielectric','X7R'),('tolerance','10%')):
        if v not in str(e.get(k,'')): raise ValueError(f'{k} changed')
    r = copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0805_imperial_2012_metric' or r.get('model',{}).get('expected_bounds_mm') != [2.0,1.25,1.25]: raise ValueError('Unexpected source model')
    r.update(represented_manufacturer='YAGEO', represented_mpn='CC0805KRX7R9BB221')
    r['model']['display_scale_xyz'] = [1.0,1.0,0.48]
    r['marking'].update(policy='unmarked_illustration', evidence={'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Yageo exact-part specification reviewed online','source_record':f'parts_source/{PART}/working.yaml'}, appearance_status='Unmarked body is illustrative; the selected part’s no-marking policy has not been verified.')
    r['appearance_status'] = ('Generic KiCad 0805 model scaled to the manufacturer’s nominal 0.6 mm height; edge radii, termination proportions, colour and finish are illustrative. The source record states 1.25 mm and its attached 01005 datasheet is for a different package; both require catalogue review.')
    return r

def main():
    a=argparse.ArgumentParser(); a.add_argument('--add',action='store_true'); args=a.parse_args()
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes: raise ValueError('Existing recipe preserved')
    record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'))
    sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(); recipe=reviewed_recipe(record,recipes,sha)
    if args.add:
        recipes[PART]=recipe; RECIPE_FILE.write_text(json.dumps(recipes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(PART)

if __name__=='__main__': main()
