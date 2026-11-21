"""Prepare the reviewed IRF5305PBF TO-220 display candidate."""
import argparse,copy,hashlib,json,os,tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_transistor_to_220ab_mosfet_p_channel_enhancement_mode_55_volt_31_amp_infineon_technologies_irf5305pbf'
REF='electronic_ic_power_management_linear_voltage_regulator_5_volt_to_220_stmicroelectronics_l7805cv_dg'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_TO220_IRF5305PBF_RESEARCH.md')
SHA='7cb065d935df5771f0ba6e48ddd180863a121af76483dad7f18e667a7b68204a'

def candidate(record,recipes):
    if record.get('manufacturer')!='Infineon Technologies' or record.get('part_number_manufacturer')!='IRF5305PBF' or record.get('dimensions_mm')!={'length':10.0,'width':4.4,'height':9.2} or (record.get('kicad') or {}).get('machine_solder')!='Package_TO_SOT_THT:TO-220-3_Vertical':
        raise ValueError('Source identity, dimension or footprint changed')
    r=copy.deepcopy(recipes[REF])
    if r['model']['sha256']!=SHA or r['model'].get('display_orientation')!='to220_face_up':raise ValueError('Reference model or orientation changed')
    r['represented_manufacturer']='Infineon Technologies';r['represented_mpn']='IRF5305PBF'
    r['marking']={'policy':'illustrative_literal','text':'IRF5305','font_file':'arialbd.ttf','rotation_degrees':90,
        'maximum_width_mm':7.0,'maximum_height_mm':1.3,'offset_x_mm':-3.52,
        'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
            'document':'Infineon IRF5305PBF TO-220 display research','source_record':f'parts_source/{PART}/working.yaml'},
        'appearance_status':'IRF5305 is an illustrative device identifier; the exact marking, typeface, logo, orientation and variable lot/date details are unverified.'}
    r['appearance_status']='KiCad TO-220-3 model is laid face-up for display and measures 10.25 x 4.455 x 28.525 mm including leads. Source dimensions are generic body measurements. The local manufacturer PDF identifies IRF5305PbF but does not establish the exact device marking. Lead proportions and finish are illustrative, not a verified mechanical model or footprint.'
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
