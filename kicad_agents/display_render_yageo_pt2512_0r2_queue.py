"""Prepare the corrected 2512 0.2-ohm Yageo PT current-sense render."""
import argparse,copy,hashlib,json
from pathlib import Path
import re
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
PART='electronic_resistor_2512_0_2_ohm'
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_PT2512_0R2_EVIDENCE.md')
MODEL_SHA='76b2052a3c120193de7cdc0af99157b6f375e9a4af7721e3e3d012968c877f27'

def reviewed_recipe(record,recipes,sha):
 mpn='PT2512FK-7W0R2L'
 if record.get('manufacturer')!='YAGEO' or record.get('part_number_manufacturer')!=mpn:raise ValueError('Selected identity changed')
 if not any(x.get('manufacturer')=='YAGEO' and x.get('part_number')==mpn for x in record.get('manufacturers',[]) if isinstance(x,dict)):raise ValueError('Manufacturer entry changed')
 if not any(x.get('key')=='lcsc' and x.get('part_number')=='C309535' and all(t in str(x.get('product_name','')) for t in ('0.2Ω','1%','2W','2512')) for x in record.get('distributors',[]) if isinstance(x,dict)):raise ValueError('Supplier rating changed')
 e=record.get('electrical') or {}
 if e.get('resistance')!='0.2 Ω' or not re.search(r'(?<![0-9.])1(?:\.0+)?\s*%',str(e.get('tolerance',''))) or not str(e.get('power','')).startswith('2 W'):raise ValueError('Selected electrical ratings changed')
 if record.get('kicad',{}).get('machine_solder')!='Resistor_SMD:R_2512_6332Metric':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_1206_133000_ohm']);r['package']='2512_imperial'
 r['model'].update(relative_path='Resistor_SMD.3dshapes/R_2512_6332Metric.step',source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Resistor_SMD.3dshapes/R_2512_6332Metric.step',expected_bounds_mm=[6.3,3.2,.6],sha256=MODEL_SHA)
 r.update(represented_manufacturer='YAGEO',represented_mpn=mpn)
 r['marking']={'policy':'verified_literal','text':'R200','evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Yageo PT series and exact-part specifications (reviewed online)','source_record':f'parts_source/{PART}/working.yaml','rule':'Yageo PT2512 four-character code R200 denotes 0.2 Ω.'},'maximum_width_mm':3.0,'maximum_height_mm':1.25,'font_file':'arialbd.ttf','appearance_status':'Documented PT value code; ink, typeface and placement are illustrative.'}
 r['appearance_status']='Generic KiCad 2512 geometry with illustrative materials. Represents Yageo PT current-sense part; other characteristics must be checked for the intended design.'
 return r

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
 if PART in recipes:print('Already prepared');return
 record=yaml.safe_load((ROOT/'parts_source'/PART/'working.yaml').read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest();r=reviewed_recipe(record,recipes,sha)
 if args.add:recipes[PART]=r;RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(PART,r['represented_mpn'],r['marking']['text'])
if __name__=='__main__':main()
