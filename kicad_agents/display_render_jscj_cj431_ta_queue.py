"""Prepare the display-only CJ431-TA formed-lead TO-92 candidate."""
import argparse, copy, hashlib, json, os, tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
PART='electronic_ic_power_management_voltage_reference_to_92_3_jiangsu_changjing_electronics_technology_co_ltd_cj431_ta'
REF='electronic_ic_power_management_adjustable_shunt_voltage_reference_to_92_3_texas_instruments_tl431aclp'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_CJ431_TA_TO92_RESEARCH.md')
SHA='f0b61c32ecbf0067157adc5a3d4966ceadf5d6dafe93c51af35f76c41c71a54a'

def candidate(record,recipes):
    if record.get('manufacturer')!='Jiangsu Changjing Electronics Technology Co., Ltd.' or record.get('part_number_manufacturer')!='CJ431-TA' or record.get('dimensions_mm')!={'length':10.0,'width':5.0} or (record.get('kicad') or {}).get('machine_solder')!='':
        raise ValueError('Source identity, dimension or footprint changed')
    r=copy.deepcopy(recipes[REF])
    if r['model']['sha256']!=SHA or r['model'].get('display_orientation')!='to220_face_up': raise ValueError('Reference model changed')
    r['represented_manufacturer']='Jiangsu Changjing Electronics Technology Co., Ltd.'
    r['represented_mpn']='CJ431-TA'
    r['marking']={'policy':'illustrative_literal','text':'CJ\nTL431','font_file':'arialbd.ttf','rotation_degrees':0,
       'maximum_width_mm':3.5,'maximum_height_mm':1.5,'offset_x_mm':-7.15,
       'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
       'document':'CJ431 TO-92 source and taped lead drawing','source_record':f'parts_source/{PART}/working.yaml'},
       'appearance_status':'CJ and TL431 are fixed family marking portions; line layout, typeface, placement and omitted production code are illustrative. Optional green-material dot is omitted.'}
    r['appearance_status']='KiCad TO-92 body with representative formed leads: 1.27 mm at the body, 2.5 mm spread and 14.3 mm body-to-tip extent. Bend positions and taped lead length are approximate; body is slightly larger than the source drawing. Source 10 x 5 mm dimensions are generic. Display is not a verified footprint or mechanical model.'
    return r

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--add',action='store_true');a=p.parse_args()
    old=RECIPE_FILE.read_bytes(); recipes=json.loads(old.decode('utf8'))
    record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'))
    value=candidate(record,recipes)
    if PART in recipes and recipes[PART]!=value: raise ValueError('Existing recipe differs')
    if a.add and PART not in recipes:
        recipes[PART]=value; tmp=None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                tmp=Path(f.name); f.write((json.dumps(recipes,ensure_ascii=False,indent=2)+'\n').encode('utf8')); f.flush(); os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes()!=old: raise RuntimeError('Recipes changed during staging')
            os.replace(tmp,RECIPE_FILE)
        finally:
            if tmp is not None and tmp.exists(): tmp.unlink()
    print(PART,'candidate only; visual review required')
if __name__=='__main__': main()
