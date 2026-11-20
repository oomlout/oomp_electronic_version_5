"""Render a reviewed 4N33 DIP-6 against the verified onsemi lighting master."""
import hashlib,json
from pathlib import Path
import yaml
from kicad_agents import display_render_onsemi_dip6_composite as base
from kicad_agents import display_render_onsemi_4n33_dip6_queue as q

def read_recipe(part):
    recipes=json.loads(base.renderer.RECIPES.read_text(encoding='utf8'))
    base_original(base.PART)
    if part!=q.PART: raise ValueError('Only reviewed 4N33 candidate is supported')
    record=yaml.safe_load((base.renderer.ROOT/'parts_source'/part/'working.yaml').read_text(encoding='utf8'))
    candidate=q.reviewed_recipe(record,recipes,base.renderer.digest(base.renderer.ROOT/q.EVIDENCE))
    if recipes.get(part)!=candidate or candidate['model']!=recipes[base.PART]['model']: raise ValueError('Candidate or model changed')
    return candidate

base_original=base.read_recipe
if __name__=='__main__':
    import sys
    source_hash=base.renderer.digest(__file__); queue_hash=base.renderer.digest(q.__file__)
    base.read_recipe=read_recipe
    base.main()
    if base.renderer.digest(__file__)!=source_hash or base.renderer.digest(q.__file__)!=queue_hash: raise RuntimeError('Validator changed')
    output=Path(sys.argv[sys.argv.index('--output')+1]); path=output/'manifest.json'; m=json.loads(path.read_text(encoding='utf8'))
    m['composite']['candidate_validator_sha256']=source_hash; m['composite']['candidate_batch_sha256']=queue_hash
    m['input_fingerprint']=hashlib.sha256((m['input_fingerprint']+source_hash+queue_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(m,indent=2)+'\n',encoding='utf8')
