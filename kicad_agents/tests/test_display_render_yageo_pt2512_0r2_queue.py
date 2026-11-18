import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_yageo_pt2512_0r2_queue import PART,reviewed_recipe

def test_2512_pt_selected_value_and_marking():
 d=yaml.safe_load((Path('parts_source')/PART/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'));r=reviewed_recipe(d,recipes,'hash')
 assert r['marking']['text']=='R200' and r['represented_mpn']=='PT2512FK-7W0R2L' and r['model']['expected_bounds_mm']==[6.3,3.2,.6]
 for field in ('identity','listing','tolerance','resistance','power','footprint'):
  bad=copy.deepcopy(d)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='tolerance':bad['electrical']['tolerance']='5%'
  if field=='resistance':bad['electrical']['resistance']='2 Ω'
  if field=='power':bad['electrical']['power']='1 W'
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(bad,recipes,'hash')
