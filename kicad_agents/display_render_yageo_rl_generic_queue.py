"""Prepare two documented Yageo RL references for unsourced low-ohm parts."""
import argparse,copy,hashlib,json
from pathlib import Path
import yaml
from kicad_agents.display_render_resistor_queue import ROOT,RECIPE_FILE
EVIDENCE=Path('kicad_agents/component_records/DISPLAY_RENDER_YAGEO_RL_GENERIC_REFERENCES.md')
PARTS={
 'electronic_resistor_1210_0_1_ohm':('1210','RL1210FR-070R1L','R100','R_1210_3225Metric.step','44b152a107ee844595f54f1205cd4e0e37cebb9635affbe45f530daada41d245',[3.2,2.5,.55],1.52,1.0),
 'electronic_resistor_2512_0_015_ohm':('2512','RL2512FK-070R015L','R015','R_2512_6332Metric.step','76b2052a3c120193de7cdc0af99157b6f375e9a4af7721e3e3d012968c877f27',[6.3,3.2,.6],3.0,1.25),
}

def reviewed_recipe(part,record,recipes,sha):
 if part not in PARTS:raise ValueError('Unreviewed ID')
 size,reference,mark,step,model_sha,bounds,width,height=PARTS[part]
 if any(record.get(x) for x in ('manufacturer','part_number_manufacturer','manufacturers','distributors')):raise ValueError('Supplier identity changed')
 if any((record.get('electrical') or {}).get(k) for k in ('tolerance','power')) or any(((record.get('jlcpcb_selection') or {}).get('ratings') or {}).get(k) for k in ('Tolerance','Power(Watts)')):raise ValueError('Tolerance or power changed')
 metric={'1210':'3225','2512':'6332'}[size]
 if record.get('kicad',{}).get('machine_solder')!=f'Resistor_SMD:R_{size}_{metric}Metric':raise ValueError('Footprint changed')
 r=copy.deepcopy(recipes['electronic_resistor_2512_0_2_ohm']);r['package']=size+'_imperial';r['model'].update(relative_path='Resistor_SMD.3dshapes/'+step,source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/Resistor_SMD.3dshapes/'+step,expected_bounds_mm=bounds,sha256=model_sha)
 r.update(represented_manufacturer='YAGEO',represented_mpn=reference)
 r['marking']={'policy':'verified_literal','text':mark,'evidence':{'file':EVIDENCE.as_posix(),'sha256':sha,'document':'Yageo RL marking table and exact reference specifications (reviewed online)','source_record':f'parts_source/{part}/working.yaml','rule':f'Yageo {reference} RL E24 code {mark} denotes this nominal value.'},'maximum_width_mm':width,'maximum_height_mm':height,'font_file':'arialbd.ttf','appearance_status':'Documented Yageo RL code; ink, typeface and placement are illustrative.'}
 r['appearance_status']=(f'Illustrates Yageo {reference}, a 1% current-sense example; this generic entry has no selected manufacturer, tolerance or power rating. The example does not establish interchangeability. Generic KiCad geometry and materials are illustrative.' + (' The KiCad 1210 body length is at the manufacturer tolerance limit.' if size=='1210' else ''))
 return r

def discover():
 recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'));sha=hashlib.sha256((ROOT/EVIDENCE).read_bytes()).hexdigest()
 return {p:reviewed_recipe(p,yaml.safe_load((ROOT/'parts_source'/p/'working.yaml').read_text(encoding='utf8')) or {},recipes,sha) for p in PARTS if p not in recipes and (ROOT/'parts'/p/'working.yaml').is_file()}

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--add',action='store_true');args=parser.parse_args();found=discover()
 if args.add:
  recipes=json.loads(RECIPE_FILE.read_text(encoding='utf8'))
  if any(p in recipes for p in found):raise ValueError('Existing recipe preserved')
  recipes.update(found);RECIPE_FILE.write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 for p,r in found.items():print(p,r['represented_mpn'],r['marking']['text'])
 print(len(found),'reviewed references')
if __name__=='__main__':main()
