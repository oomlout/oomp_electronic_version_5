"""Prepare the reviewed A733-TA(RANGE:200-400) TO-220 display candidate."""
import argparse,copy,hashlib,json,os,tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_transistor_to_92_bipolar_pnp_50_volt_100_milliamp_jiangsu_changjing_electronics_technology_co_ltd_a733_ta_range_200_400'
REF='electronic_ic_power_management_adjustable_shunt_voltage_reference_to_92_3_texas_instruments_tl431aclp'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_TO92_A733_TA_RANGE_200_400_RESEARCH.md')
SHA='f0b61c32ecbf0067157adc5a3d4966ceadf5d6dafe93c51af35f76c41c71a54a'

def candidate(record,recipes):
    if record.get('manufacturer')!='Jiangsu Changjing Electronics Technology Co., Ltd.' or record.get('part_number_manufacturer')!='A733-TA(RANGE:200-400)' or record.get('dimensions_mm')!={'length':5.2,'width':4.2,'height':5.2} or (record.get('kicad') or {}).get('machine_solder')!='Package_TO_SOT_THT:TO-92_Inline':
        raise ValueError('Source identity, dimension or footprint changed')
    r=copy.deepcopy(recipes[REF])
    if r['model']['sha256']!=SHA or r['model'].get('display_orientation')!='to220_face_up':raise ValueError('Reference model or orientation changed')
    r['represented_manufacturer']='Jiangsu Changjing Electronics Technology Co., Ltd.';r['represented_mpn']='A733-TA(RANGE:200-400)'
    r['marking']={'policy':'illustrative_literal','text':'A733','font_file':'arialbd.ttf','rotation_degrees':0,
        'maximum_width_mm':3.5,'maximum_height_mm':.9,'offset_x_mm':-2.5,
        'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
            'document':'Infineon A733-TA(RANGE:200-400) TO-220 display research','source_record':f'parts_source/{PART}/working.yaml'},
        'appearance_status':'A733 is an illustrative device identifier; the exact marking, typeface, logo, orientation and variable lot/date details are unverified.'}
    r['appearance_status']='Generic KiCad TO-92 model lies flat-face-up; 5.0 mm straight leads are shorter than typical uncut leads, and source body dimensions differ. Local PDF is JCST rather than JSCJ. Single-line device code is illustrative and omits gain and variable production codes. Not a verified mechanical model or footprint.'
    return r

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--add',action='store_true');a=p.parse_args()
    original=RECIPE_FILE.read_bytes();recipes=json.loads(original.decode('utf8'))
    value=candidate(yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8')),recipes)
    if PART in recipes and recipes[PART]!=value:raise ValueError('Existing candidate differs')
    if a.add and PART not in recipes:
        recipes[PART]=value;tmp=None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                tmp=Path(f.name);f.write((json.dumps(recipes,ensure_ascii=False,indent=2)+'\n').encode('utf8'));f.flush();os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes()!=original:raise RuntimeError('Recipes changed during staging')
            os.replace(tmp,RECIPE_FILE)
        finally:
            if tmp is not None and tmp.exists():tmp.unlink()
    print(PART,'candidate only; inspect preview and final')
if __name__=='__main__':main()
