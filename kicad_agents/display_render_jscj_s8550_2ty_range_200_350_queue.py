"""Prepare the reviewed S8550 2TY(RANGE:200-350) SOT-23 transistor display candidate."""
import argparse,copy,hashlib,json,os,tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_transistor_sot_23_bipolar_pnp_25_volt_500_milliamp_jiangsu_changjing_electronics_technology_co_ltd_s8550_2ty_range_200_350'
REF='electronic_ic_power_management_voltage_reference_sot_23_jiangsu_changjing_electronics_technology_co_ltd_cj431'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_JSCJ_S8550_2TY_RANGE_200_350_RESEARCH.md')
SHA='dd5d1711204e1d8d26cd11490923bd84340820baa69538c385a4300ec2539bc0'

def candidate(record,recipes):
    if record.get('manufacturer')!='Jiangsu Changjing Electronics Technology Co., Ltd.' or record.get('part_number_manufacturer')!='S8550 2TY(RANGE:200-350)' or record.get('dimensions_mm')!={'length':2.9,'width':1.3,'height':1.1} or (record.get('kicad') or {}).get('machine_solder')!='Package_TO_SOT_SMD:SOT-23':
        raise ValueError('Source identity, dimensions or selected footprint changed')
    r=copy.deepcopy(recipes[REF])
    if r['model']['sha256']!=SHA or r['model']['display_scale_xyz']!=[1,1,.9166666666666666]:raise ValueError('Reference model or scale changed')
    r['model']['role_by_source_colour']['0.691,0.664,0.598']='coating'
    r['model']['required_roles']=['coating','termination']
    r['represented_manufacturer']='Jiangsu Changjing Electronics Technology Co., Ltd.'
    r['represented_mpn']='S8550 2TY(RANGE:200-350)'
    r['marking']={'policy':'illustrative_literal','text':'2TY','font_file':'arialbd.ttf','rotation_degrees':90,
        'maximum_width_mm':1.5,'maximum_height_mm':.5,
        'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
            'document':'S8550 2TY(RANGE:200-350) SOT-23 display research','source_record':f'parts_source/{PART}/working.yaml'},
        'appearance_status':'2TY is illustrative, taken from the local JCST family sheet, not verified for the listed JSCJ manufacturer; typeface and placement are illustrative.'}
    r['appearance_status']='KiCad SOT-23 2.5 x 3.0 x 1.2 mm overall display model is scaled vertically to 1.1 mm; generic source body dimensions differ from overall bounds. The local linked PDF is JCST rather than JSCJ; the shown 2TY marking is an illustrative family reference, not verified for JSCJ. Appearance is illustrative, not a verified mechanical model or footprint.'
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
