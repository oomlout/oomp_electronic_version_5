"""Display-only lead-length correction for an inspected KiCad TO-247 model.

The source leads extend 20.15 mm below the body, beyond the manufacturer's
14.2-16.1 mm lead range. Negative-z termination vertices are compressed about
z=0 so the lead tip is 15.15 mm below the unchanged body base z=4.32. Face
proportions and bend/radii remain approximate; this is not manufacturing CAD.
"""
import argparse,hashlib,json
from pathlib import Path
from kicad_agents import display_render as renderer
PART='electronic_transistor_to_247ac_mosfet_n_channel_enhancement_mode_100_volt_134_amp_infineon_technologies_irfp4310zpbf'
MODEL_SHA='ec0db59b04bcea2e0db6f976bf3ab8644e761c8b0059239f77f4febd6dc9eff4'
SOURCE_BOTTOM=-15.83
TARGET_BOTTOM=-10.83
FACTOR=TARGET_BOTTOM/SOURCE_BOTTOM
original_load=renderer.load_coloured_step

def load(path,specification):
 import numpy as np
 if renderer.digest(path)!=MODEL_SHA or specification.get('sha256')!=MODEL_SHA: raise ValueError('Unreviewed TO-247 model')
 groups,lower,upper,colours=original_load(path,specification)
 if not np.allclose(lower,[-2.5,-2.33,-15.83],atol=.005) or not np.allclose(upper,[13.4,2.7,25.27],atol=.005):raise ValueError('Unexpected TO-247 envelope')
 body=np.asarray(groups['coating']['vertices'])
 if not np.allclose(body.min(axis=0),[-2.5,-2.33,4.32],atol=.005):raise ValueError('Unexpected TO-247 body base')
 metal=groups['termination'];v=np.asarray(metal['vertices'],dtype=float);n=np.asarray(metal['normals'],dtype=float)
 mask=v[:,2]<0
 if int(mask.sum())!=72 or abs(v[:,2].min()-SOURCE_BOTTOM)>.005:raise ValueError(f'Unexpected TO-247 lead mesh: {int(mask.sum())}, minimum {v[:,2].min()}')
 v[mask,2]*=FACTOR
 n[mask,2]/=FACTOR
 lengths=np.linalg.norm(n,axis=1)
 if np.any(~np.isfinite(lengths)) or np.any(lengths<=0):raise ValueError('Invalid TO-247 mesh normals')
 n/=lengths[:,None];metal['vertices']=v.tolist();metal['normals']=n.tolist()
 lower=lower.copy();lower[2]=TARGET_BOTTOM
 colours=dict(colours,corrected_lead_vertices=int(mask.sum()))
 return groups,lower,upper,colours

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);p.add_argument('--pixels',type=int);p.add_argument('--samples',type=int);a=p.parse_args()
 digest=renderer.digest(__file__);renderer.load_coloured_step=load
 renderer.generate(PART,output=a.output,pixels=a.pixels,samples=a.samples,force=True)
 if renderer.digest(__file__)!=digest:raise RuntimeError('Adapter changed during render')
 path=Path(a.output)/'manifest.json';m=json.loads(path.read_text(encoding='utf8'));m['model']['adapter_sha256']=digest
 m['input_fingerprint']=hashlib.sha256((m['input_fingerprint']+digest).encode('ascii')).hexdigest()
 path.write_text(json.dumps(m,indent=2)+'\n',encoding='utf8')
if __name__=='__main__':main()


