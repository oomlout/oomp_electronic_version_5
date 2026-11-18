import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_ralec_0603_2r7_queue import PART,reviewed_recipe

def test_ralec_marking_and_source_guards():
 record=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 r=reviewed_recipe(record,recipes,'hash');assert r['marking']['text']=='2R7' and r['marking']['underline'] and 'inferred' in r['marking']['appearance_status']
 for field in ('identity','listing','value','tolerance','footprint'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='value':bad['jlcpcb_selection']['ratings']['Resistance']='1Ω'
  if field=='tolerance':bad['jlcpcb_selection']['ratings']['Tolerance']='5%'
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
