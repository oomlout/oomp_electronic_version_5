"""Stage a reviewed ESP-12S display illustration based on KiCad ESP-12E."""
import argparse,copy,hashlib,json,os,tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_ic_microcontroller_wifi_bluetooth_module_esp_12s_espressif_esp_12s'
REF='electronic_ic_microcontroller_wifi_bluetooth_8_mb_flash_esp32_wroom_32e_espressif_esp32_wroom_32e_n8'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_ESP12S_RESEARCH.md')
SHA='984f7bce88206d1f9efd21f272d5cc12f0cb9556f6b2b29385b0d2f2f2011079'

def candidate(record,recipes):
    if record.get('manufacturer') or record.get('part_number_manufacturer') or record.get('dimensions_mm')!={'length':24.0,'width':16.0,'height':3.0} or (record.get('kicad') or {}).get('machine_solder')!='':
        raise ValueError('Source identity, dimensions or footprint changed')
    r=copy.deepcopy(recipes[REF]);r['package']='esp_12s_module_illustrative'
    model='RF_Module.3dshapes/ESP-12E.step'
    r['model'].update(relative_path=model,source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/'+model,
        expected_bounds_mm=[16.0,24.0,3.2],sha256=SHA,display_scale_xyz=[1.0,1.0,.9375],
        role_by_source_colour={'0.160,0.160,0.160':'ceramic','0.508,0.508,0.508':'pin_indicator','0.859,0.738,0.496':'termination','0.895,0.891,0.813':'ceramic','0.340,0.680,0.445':'ceramic'})
    r['represented_manufacturer']='Ai-Thinker (illustrative family reference; source does not identify manufacturer)'
    r['represented_mpn']='ESP-12S (illustrative family reference)'
    r['marking']={'policy':'illustrative_literal','text':'ESP-12S','font_file':'arialbd.ttf','rotation_degrees':0,
        'maximum_width_mm':8.0,'maximum_height_mm':1.3,
        'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
            'document':'ESP-12S family and KiCad ESP-12E display research','source_record':f'parts_source/{PART}/working.yaml'},
        'appearance_status':'ESP-12S is an illustrative family label; exact shield printing, logo, certifications, placement and production details are unverified.'}
    r['appearance_status']='Illustrative ESP-12S family appearance using a KiCad ESP-12E source model, with its six extra end contacts recoloured as PCB and height scaled from 3.2 to 3.0 mm. End notches, PCB antenna and component details remain approximate. Source identity does not establish module manufacturer; its pin drawing conflicts with its two-row description. Not a verified footprint or mechanical model.'
    return r

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--add',action='store_true');a=p.parse_args()
    old=RECIPE_FILE.read_bytes();recipes=json.loads(old.decode('utf8'))
    value=candidate(yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8')),recipes)
    if PART in recipes and recipes[PART]!=value:raise ValueError('Existing candidate differs')
    if a.add and PART not in recipes:
        recipes[PART]=value;tmp=None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                tmp=Path(f.name);f.write((json.dumps(recipes,ensure_ascii=False,indent=2)+'\n').encode('utf8'));f.flush();os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes()!=old:raise RuntimeError('Recipes changed during staging')
            os.replace(tmp,RECIPE_FILE)
        finally:
            if tmp is not None and tmp.exists():tmp.unlink()
    print(PART,'candidate only; geometry check and preview review required')
if __name__=='__main__':main()
