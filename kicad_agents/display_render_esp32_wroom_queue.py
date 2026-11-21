"""Prepare reviewed display recipes for the two KiCad WROOM assemblies."""
import argparse, copy, hashlib, json, os, tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE

EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_ESP32_WROOM_MODULE_RESEARCH.md')
REFERENCE='electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr'
MODULES={
 'electronic_ic_microcontroller_wifi_bluetooth_8_mb_flash_esp32_wroom_32e_espressif_esp32_wroom_32e_n8': ('ESP32-WROOM-32E-N8','ESP32-WROOM-32E','57f41a512434023f19bef010df050e42a80a478b62cf87b8b96868b490791bee'),
 'electronic_ic_microcontroller_wifi_bluetooth_8_mb_flash_esp32_s3_wroom_1_espressif_esp32_s3_wroom_1_n8': ('ESP32-S3-WROOM-1-N8','ESP32-S3-WROOM-1','3e35bb7ba7d030d88855fcf968398c8670934c7dca08b4e30b2c578bc1e13954'),
}
def candidate(part, record, recipes):
    mpn, module, sha = MODULES[part]
    if (record.get('manufacturer') != 'Espressif' or record.get('part_number_manufacturer') != mpn
        or record.get('dimensions_mm') != {'length':18.0,'width':25.5,'height':3.1}
        or (record.get('kicad') or {}).get('machine_solder') != 'RF_Module:'+module):
        raise ValueError('Module source identity, dimensions or footprint changed')
    recipe=copy.deepcopy(recipes[REFERENCE])
    if recipe.get('family') != 'integrated_circuit':
        raise ValueError('Reference family changed')
    model='RF_Module.3dshapes/'+module+'.step'
    recipe['package']='rf_module_'+module.lower().replace('-','_')
    recipe['model'].update(relative_path=model, source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/'+model,
        expected_bounds_mm=[18.0,25.5,3.1],sha256=sha,required_roles=['ceramic','termination','pin_indicator','coating'],
        role_by_source_colour={'0.160,0.160,0.160':'ceramic','0.859,0.738,0.496':'termination','0.372,0.372,0.373':'pin_indicator'})
    recipe['represented_manufacturer']='Espressif'
    recipe['represented_mpn']=mpn
    recipe['marking']={'policy':'illustrative_literal','text':module,'font_file':'arialbd.ttf','rotation_degrees':0,
        'maximum_width_mm':11.0,'maximum_height_mm':1.4,
        'evidence':{'file':EVIDENCE.as_posix(),'sha256':hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest(),
        'document':'Espressif WROOM module display research','source_record':f'parts_source/{part}/working.yaml'},
        'appearance_status':'Illustrative family label on shield; actual typography, placement, production marks, logos and certifications are not verified.'}
    recipe['appearance_status']='Display-only KiCad RF module with assigned dark PCB, gold contacts and metallic shield; antenna trace detail and shield printing are illustrative. Model and text are not a verified production image or mechanical model.'
    recipe['disable_bump_for']=['ceramic','termination','pin_indicator','coating']
    return recipe

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add',action='store_true')
    args=parser.parse_args()
    original=RECIPE_FILE.read_bytes()
    recipes=json.loads(original.decode('utf8'))
    for part in MODULES:
        record=yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8'))
        value=candidate(part,record,recipes)
        if part in recipes and recipes[part] != value:
            raise ValueError('Existing module recipe differs')
        recipes[part]=value
        print(part,'candidate prepared; geometry check and preview required')
    if args.add:
        temp=None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as handle:
                temp=Path(handle.name)
                handle.write((json.dumps(recipes,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
                handle.flush(); os.fsync(handle.fileno())
            if RECIPE_FILE.read_bytes()!=original: raise RuntimeError('Recipes changed during validation')
            os.replace(temp,RECIPE_FILE)
        finally:
            if temp is not None and temp.exists(): temp.unlink()
if __name__=='__main__': main()
