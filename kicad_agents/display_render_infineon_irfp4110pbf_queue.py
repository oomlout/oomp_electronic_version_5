"""Prepare the reviewed IRFP4110PBF TO-247 display candidate."""
import argparse,copy,hashlib,json,os,tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_180_amp_infineon_technologies_irfp4110pbf'
REF='electronic_ic_power_management_linear_voltage_regulator_5_volt_to_220_stmicroelectronics_l7805cv_dg'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_INFINEON_IRFP4110PBF_RESEARCH.md')
SHA='ec0db59b04bcea2e0db6f976bf3ab8644e761c8b0059239f77f4febd6dc9eff4'

def candidate(record,recipes):
 if record.get('manufacturer')!='Infineon Technologies' or record.get('part_number_manufacturer')!='IRFP4110PBF' or record.get('dimensions_mm')!={'length':15.9,'width':5.5,'height':15.6} or (record.get('kicad') or {}).get('machine_solder')!='Package_TO_SOT_THT:TO-247-3_Vertical':raise ValueError('Source identity, dimensions or footprint changed')
 r=copy.deepcopy(recipes[REF]);model='Package_TO_SOT_THT.3dshapes/TO-247-3_Vertical.step'
 r['package']='to_247_3';r['model'].update(relative_path=model,source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/'+model,expected_bounds_mm=[15.9,5.03,41.1],sha256=SHA,required_roles=['coating','termination'])
 r['represented_manufacturer']='Infineon Technologies';r['represented_mpn']='IRFP4110PBF'
 r['marking']={'policy':'illustrative_literal','text':'IRFP4110','font_file':'arialbd.ttf','rotation_degrees':90,'maximum_width_mm':10.0,'maximum_height_mm':1.8,'offset_x_mm':-7.575,
  'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),'document':'Infineon IRFP4110 TO-247 display research','source_record':f'parts_source/{PART}/working.yaml'},
  'appearance_status':'IRFP4110 is an illustrative family identifier; exact package marking, typeface, logo, orientation, placement and variable lot/date details are unverified.'}
 r['appearance_status']='KiCad TO-247 model laid face-up, with display-only lead adjustment from 20.15 mm to 15.15 mm below body. Lead features and transition remain approximate, and the 20.95 mm body height and 15.9 mm width slightly exceed the local drawing maxima. Source generic dimensions differ. The datasheet marking illustration is an unrelated example. Not a verified mechanical model or footprint.'
 return r

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--add',action='store_true');a=p.parse_args();original=RECIPE_FILE.read_bytes();recipes=json.loads(original.decode('utf8'))
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
