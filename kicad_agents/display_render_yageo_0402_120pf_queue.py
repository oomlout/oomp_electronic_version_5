"""Prepare the exact Yageo 0402 120 pF display illustration."""
import argparse, copy, hashlib, json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
PART = 'electronic_capacitor_0402_120_pico_farad'
PILOT = 'electronic_capacitor_0402_100_pico_farad'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_0402_120PF_EVIDENCE.md')

def reviewed_recipe(part, record, recipes, sha):
    if part != PART or record.get('manufacturer') != 'YAGEO' or record.get('part_number_manufacturer') != 'CC0402JRNPO9BN121': raise ValueError('Identity changed')
    if not any(x.get('manufacturer') == 'YAGEO' and x.get('part_number') == 'CC0402JRNPO9BN121' for x in record.get('manufacturers', []) if isinstance(x, dict)): raise ValueError('Manufacturer changed')
    if not any(x.get('part_number') == 'C106996' for x in record.get('distributors', []) if isinstance(x, dict)): raise ValueError('Supplier changed')
    if record.get('kicad',{}).get('machine_solder') != 'Capacitor_SMD:C_0402_1005Metric': raise ValueError('Footprint changed')
    if record.get('dimensions_mm') != {'length':1.0,'width':0.5}: raise ValueError('Source dimensions changed')
    if record.get('electrical'): raise ValueError('Source electrical fields changed; review needed')
    r=copy.deepcopy(recipes[PILOT])
    if r.get('family') != 'chip_capacitor' or r.get('package') != '0402_imperial_1005_metric' or r.get('model',{}).get('expected_bounds_mm') != [1.0,0.5,0.5]: raise ValueError('Unexpected source model')
    r.update(represented_manufacturer='YAGEO',represented_mpn='CC0402JRNPO9BN121')
    r['marking']['evidence']={'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Exact Yageo specification reviewed online','source_record':f'parts_source/{part}/working.yaml'}
    r['appearance_status']='Generic KiCad 0402 model matches the exact selected Yageo part’s nominal dimensions; colour and termination finish are illustrative. The source record lacks electrical fields; ratings were checked against the manufacturer specification.'
    return r

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--add',action='store_true');args=ap.parse_args()
    recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
    if PART in recipes: raise ValueError('Existing recipe preserved')
    record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'))
    sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();recipe=reviewed_recipe(PART,record,recipes,sha)
    if args.add:
        recipes[PART]=recipe;RECIPE_FILE.write_text(json.dumps(recipes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(PART)

if __name__=='__main__':main()
