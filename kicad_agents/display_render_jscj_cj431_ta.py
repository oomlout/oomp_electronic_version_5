"""Display CJ431-TA with representative formed TO-92 leads.

The moulding comes from the pinned KiCad model. Three rectangular lead prisms
replace its short straight leads: nominal 14.3 mm long, 1.27 mm centres at the
body, spreading to 2.5 mm centres. Bend placement is illustrative, not a PCB
footprint or a mechanical drawing. No meshes are retained in the catalogue.
"""
import argparse
import hashlib
import json
from pathlib import Path
from kicad_agents import display_render as renderer

PART='electronic_ic_power_management_voltage_reference_to_92_3_jiangsu_changjing_electronics_technology_co_ltd_cj431_ta'
MODEL_SHA='f0b61c32ecbf0067157adc5a3d4966ceadf5d6dafe93c51af35f76c41c71a54a'
original_load=renderer.load_coloured_step

def load(path, specification):
    import cadquery as cq
    import numpy as np
    if renderer.digest(path)!=MODEL_SHA or specification.get('sha256')!=MODEL_SHA:
        raise ValueError('Unreviewed TO-92 model')
    groups,lower,upper,colours=original_load(path,specification)
    coating=np.asarray(groups['coating']['vertices'])
    metal=np.asarray(groups['termination']['vertices'])
    if not np.allclose(coating.min(axis=0),[-1.14472435,-1.33,2.5],atol=.003) or not np.allclose(coating.max(axis=0),[3.68472435,2.415,7.3],atol=.003):
        raise ValueError('Unreviewed TO-92 body')
    if not np.allclose(metal.min(axis=0),[-.24,-.19,-2.5],atol=.003) or not np.allclose(metal.max(axis=0),[2.78,.19,2.5],atol=.003):
        raise ValueError('Unreviewed source leads')
    lead={'vertices':[],'normals':[],'triangles':[]}
    for index in range(3):
        x=index*1.27
        end=1.27+(index-1)*2.5
        w=.24
        points=[(x-w,2.5),(x-w,1.5),(end-w,-.5),(end-w,-11.8),
                (end+w,-11.8),(end+w,-.5),(x+w,1.5),(x+w,2.5)]
        solid=cq.Workplane('XZ').polyline(points).close().extrude(.19,both=True).val()
        if not solid.isValid(): raise ValueError('Invalid formed lead')
        for face in solid.Faces():
            verts,triangles=face.tessellate(.003,.08)
            offset=len(lead['vertices'])
            lead['vertices'].extend(v.toTuple() for v in verts)
            lead['normals'].extend(face.normalAt(v).toTuple() for v in verts)
            lead['triangles'].extend(tuple(offset+i for i in triangle) for triangle in triangles)
    groups['termination']=lead
    all_vertices=np.vstack([np.asarray(g['vertices']) for g in groups.values()])
    low,high=all_vertices.min(axis=0),all_vertices.max(axis=0)
    if not np.allclose(low,[-1.47,-1.33,-11.8],atol=.005) or not np.allclose(high,[4.01,2.415,7.3],atol=.005):
        raise ValueError(f'Unexpected formed-lead bounds {low} {high}')
    return groups,low,high,dict(colours,formed_leads=3)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    parser.add_argument('--pixels',type=int)
    parser.add_argument('--samples',type=int)
    a=parser.parse_args()
    adapter_hash=renderer.digest(__file__)
    renderer.load_coloured_step=load
    renderer.generate(PART,output=a.output,pixels=a.pixels,samples=a.samples,force=True)
    if renderer.digest(__file__)!=adapter_hash: raise RuntimeError('Adapter changed while rendering')
    path=Path(a.output)/'manifest.json'
    m=json.loads(path.read_text(encoding='utf8'))
    m['model']['adapter_sha256']=adapter_hash
    m['input_fingerprint']=hashlib.sha256((m['input_fingerprint']+adapter_hash).encode('ascii')).hexdigest()
    path.write_text(json.dumps(m,indent=2)+'\n',encoding='utf8')
if __name__=='__main__': main()
