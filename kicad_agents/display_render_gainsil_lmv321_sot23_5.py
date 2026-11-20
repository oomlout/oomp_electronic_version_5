"""Validate the Gainsil LMV321 SOT-23-5 follow-on against the independently reviewed pilot."""
import argparse, copy, hashlib, json, os, re, tempfile
from pathlib import Path
import yaml
from kicad_agents.display_render_ti_sot23_5_pilot_queue import PART, ROOT, RECIPE_FILE, MODEL_SHA256
EVIDENCE = 'kicad_agents/component_records/DISPLAY_RENDER_GAINSIL_LMV321_SOT23_5_EVIDENCE.md'
ROW = re.compile(r'^\| `(electronic_[^`]+)` \| (TPS\w+) \| `([A-Z0-9]+)` \|')

def prepare(recipes):
    pilot=recipes[PART]
    if (pilot.get('represented_mpn') != 'TPS76333DBVR' or pilot.get('marking',{}).get('text') != 'PBEI'
        or pilot.get('model',{}).get('sha256') != MODEL_SHA256
        or pilot.get('model',{}).get('display_scale_xyz') != [1.0,1.0,1.45/1.55]
        or 'scaled' not in pilot.get('appearance_status','')):
        raise ValueError('SOT-23-5 pilot changed')
    raw=(ROOT/EVIDENCE).read_bytes()
    rows=[('electronic_ic_amplifier_operational_single_rail_to_rail_input_output_sot_23_5_gainsil_lmv321_tr','LMV321-TR','321',False)]
    for part,mpn,marking,_ in rows:
        if not all(x in raw.decode('utf8') for x in (part,mpn,marking)): raise ValueError('Evidence changed')
    result={}
    for part,mpn,marking,example in rows:
        record=yaml.safe_load((ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'Gainsil' or record.get('part_number_manufacturer') != mpn
            or (record.get('kicad') or {}).get('machine_solder')!='Package_TO_SOT_SMD:SOT-23-5'
            or record.get('dimensions_mm')!={'length':2.92,'width':2.8}):
            raise ValueError(f'Identity, footprint or dimensions changed: {part}')
        recipe=copy.deepcopy(pilot); recipe['represented_mpn']=mpn; recipe['represented_manufacturer']='Gainsil'
        recipe['appearance_status']=('Illustrative KiCad SOT-23-5 model vertically scaled from 1.55 mm to 1.45 mm as an unverified display approximation. Catalogue source omits height; not a verified mechanical or PCB model.')
        mark=recipe['marking']; mark['text']=marking; mark['policy']='verified_literal'
        mark['evidence']={'file':EVIDENCE,'sha256':hashlib.sha256(raw).hexdigest(),
          'document':'Gainsil LMV321 exact marking and package evidence','source_record':f'parts_source/{part}/working.yaml'}
        mark['appearance_status']=(f'Gainsil lists {marking} as the package marking. Typeface, orientation, placement and variable production details are illustrative.')
        if part in recipes and recipes[part]!=recipe: raise ValueError(f'Conflicting recipe: {part}')
        result[part]=recipe
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--add',action='store_true'); args=parser.parse_args()
    original=RECIPE_FILE.read_bytes(); recipes=json.loads(original.decode('utf8')); additions=prepare(recipes)
    if args.add:
        m=json.loads((ROOT/'parts'/PART/'data/display_render/manifest.json').read_text(encoding='utf8'))
        if m.get('part_id')!=PART or m.get('recipe')!=recipes[PART]: raise ValueError('Published pilot changed')
        for part,recipe in additions.items(): recipes.setdefault(part,recipe)
        updated=(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n').encode('utf8')
        if RECIPE_FILE.read_bytes()!=original: raise RuntimeError('Recipes changed during validation')
        if updated!=original:
            temp=None
            try:
                with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent,delete=False) as f:
                    temp=Path(f.name); f.write(updated); f.flush(); os.fsync(f.fileno())
                if RECIPE_FILE.read_bytes()!=original: raise RuntimeError('Recipes changed before replacement')
                os.replace(temp,RECIPE_FILE)
            finally:
                if temp is not None and temp.exists(): temp.unlink()
    print(f'Validated {len(additions)} Gainsil SOT-23-5 identities; added={args.add}')
if __name__=='__main__': main()
