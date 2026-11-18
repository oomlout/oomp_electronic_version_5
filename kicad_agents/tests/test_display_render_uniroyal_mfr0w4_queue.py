import copy,json
from pathlib import Path
import pytest,yaml
from kicad_agents.display_render_uniroyal_mfr0w4_queue import PARTS,reviewed_recipe

@pytest.mark.parametrize('part',PARTS)
def test_mfr_1_percent_selected_identity_and_band(part):
 record=yaml.safe_load((Path('parts_source')/part/'working.yaml').read_text(encoding='utf8'));recipes=json.loads(Path('source_file/display_render/recipes.json').read_text(encoding='utf8'));r=reviewed_recipe(part,record,recipes,'hash')
 assert r['marking']['bands'][-1]=='brown' and r['represented_mpn']==PARTS[part][0]
 assert r['marking']['bands']==({'electronic_resistor_quarter_watt_through_hole_12000_ohm':['brown','red','black','red','brown'],'electronic_resistor_quarter_watt_through_hole_82000_ohm':['grey','red','black','red','brown']}[part])
 for field in ('identity','listing','tolerance','footprint'):
  bad=copy.deepcopy(record)
  if field=='identity':bad['part_number_manufacturer']='other'
  if field=='listing':bad['distributors']=[]
  if field=='tolerance':bad['electrical']={'tolerance':'5%'}
  if field=='footprint':bad['kicad']['machine_solder']='other'
  with pytest.raises(ValueError):reviewed_recipe(part,bad,recipes,'hash')
