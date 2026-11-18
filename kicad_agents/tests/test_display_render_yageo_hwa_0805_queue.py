import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_yageo_hwa_0805_queue import PARTS,reviewed_recipe

@pytest.mark.parametrize('part',PARTS)
def test_reviewed_reference(part):
 ref,mark,lcsc,value,selected,tolerance=PARTS[part]
 record=yaml.safe_load((Path('parts_source')/part/'working.yaml').read_text(encoding='utf8'))
 recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'))
 r=reviewed_recipe(part,record,recipes,'hash')
 assert r['represented_mpn']==ref and r['marking']['text']==mark
 assert selected in r['appearance_status'] and 'unverified' in r['appearance_status']
 assert tolerance in r['appearance_status'] and tolerance in r['marking']['evidence']['rule']
 for field in ('identity','listing','value','tolerance','footprint'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors'][0]['part_number']='other'
  if field=='value':bad['distributors'][0]['product_name']='different '+tolerance
  if field=='tolerance':bad['electrical']={'tolerance':'2%'}
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(part,bad,recipes,'hash')
