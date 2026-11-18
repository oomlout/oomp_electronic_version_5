import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_yageo_small_selected_queue import PARTS,reviewed_recipe

@pytest.mark.parametrize('part',PARTS)
def test_reference_and_identity_guards(part):
 size,mfr,mpn,lcsc,reference,tolerance,value=PARTS[part]
 record=yaml.safe_load((Path('parts_source')/part/'working.yaml').read_text(encoding='utf8'))
 recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 recipe=reviewed_recipe(part,record,recipes,'hash')
 assert recipe['represented_mpn']==reference and recipe['marking']['policy']=='none'
 assert mpn in recipe['appearance_status'] and 'unverified' in recipe['appearance_status'] and 'interchangeability' in recipe['appearance_status']
 for field in ('identity','listing','tolerance','footprint','value'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[x for x in bad['distributors'] if x.get('part_number')!=lcsc]
  if field=='tolerance':bad.setdefault('electrical',{})['tolerance']='2%'
  if field=='footprint':bad['kicad']['machine_solder']='other'
  if field=='value':
   if value is None:bad['electrical']['resistance']='other'
   else:bad['distributors'][0]['product_name']='other '+tolerance
  with pytest.raises(ValueError):reviewed_recipe(part,bad,recipes,'hash')
