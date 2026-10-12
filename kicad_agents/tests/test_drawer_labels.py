"""Electronic drawer labels: semantics, native regeneration, fit and cleanup."""
import copy
import importlib.util
from pathlib import Path
import shutil
import sys
import xml.etree.ElementTree as ET
import yaml
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
import working_drawer_labels as labels


def sample(kind='resistor'):
    return {'taxonomy_1':'electronic','taxonomy_2':kind,'taxonomy_3':'0805','taxonomy_4':'10000_ohm',
            'bip_39_3_word_space':'cart vault uniform','electrical':{'resistance':'10 kOhm','tolerance':'+/-1%','power':'1/8 W'}}


def test_type_specific_priorities():
    assert labels.content(sample())['primary']=='10 kOhm'
    cap=dict(sample('capacitor'),electrical={'capacitance':'100 nF (104)','rated_voltage':'50 V','dielectric':'X7R'})
    assert labels.content(cap)['primary']=='100 nF'
    assert labels.content(cap)['details'][0]=='50 V | X7R'
    conn=dict(sample('connector'),taxonomy_3='jst_ph',taxonomy_4='2_mm_pitch',taxonomy_5='through_hole_right_angle',taxonomy_6='7_pin',electrical={})
    assert labels.content(conn)['primary']=='7 pin'
    assert '2 mm pitch | THT RA' in labels.content(conn)['details']
    ic=dict(sample('ic'),taxonomy_3='soic_8',taxonomy_4='amplifier',taxonomy_5='operational_amplifier_dual_jfet_input',part_number_manufacturer='TL072CDT',electrical={})
    assert labels.content(ic)['primary']=='TL072CDT'
    assert 'op amp dual jfet input' in labels.content(ic)['details']
    led=dict(sample('led'),taxonomy_4='red',electrical={'led_color':'red (dominant wavelength 615-630 nm)'})
    assert labels.content(led)['primary']=='RED'
    assert not any('V' in d for d in labels.content(led)['details'])
    assert labels.quantity('1000000 Ohm (1004)')=='1 MOhm'
    assert labels.token('0_015_ohm')=='0.015 Ohm'


def test_actions_always_redraw_before_manifest_and_are_repeatable():
    part=sample()
    part['oomlout_ai_roboclick_1']={'actions':[{'command':'unrelated'}]}
    part['oomlout_ai_roboclick_2']={'actions':[{'command':'run_python','file_python':'kicad_agents/web_manifest_action.py'}]}
    labels.add_actions(part)
    before=copy.deepcopy(part)
    labels.add_actions(part)
    assert part==before
    blocks=[v for k,v in part.items() if k.startswith('oomlout_ai_roboclick_')]
    assert labels.is_manifest(blocks[-1])
    block=blocks[-2]
    assert block['file_test']=='' and block['always_run_on_regeneration'] is True
    assert [a['command'] for a in block['actions']]==['run_python','text_jinja_template','text_jinja_template']
    for a in block['actions'][1:]:
        assert a['convert_to_pdf'] is False and a['convert_to_png'] is False
        assert 'dict_data' not in a
    for tax in ['navigation','oomp','mechanical']:
        record={'taxonomy_1':tax}
        assert labels.add_actions(record,count=4)==4 and record=={'taxonomy_1':tax}


def test_native_pipeline_and_selective_cleanup(tmp_path):
    shutil.copy2(ROOT/'working_drawer_labels.py',tmp_path/'working_drawer_labels.py')
    shutil.copytree(ROOT/labels.TEMPLATES,tmp_path/labels.TEMPLATES)
    directory=tmp_path/'parts'/'electronic_resistor_test';directory.mkdir(parents=True)
    source=tmp_path/'parts_source'/directory.name/'working.yaml';source.parent.mkdir(parents=True)
    part=sample();labels.add_actions(part,root=tmp_path)
    (directory/'working.yaml').write_text(yaml.safe_dump(part),encoding='utf-8')
    source.write_text(yaml.safe_dump({'taxonomy_1':'electronic','electrical':{'resistance':'22 kOhm'}}),encoding='utf-8')
    (directory/'working_manual.yaml').write_text('electrical:\n  tolerance: +/-5%\n',encoding='utf-8')
    (directory/'label_drawer_3x2.pdf').write_bytes(b'stale')
    (directory/'datasheet.pdf').write_bytes(b'keep')
    (directory/'other.png').write_bytes(b'keep')
    roboclick=Path(r'C:\gh\oomlout_roboclick');sys.path.insert(0,str(roboclick))
    modules={}
    for command in ('run_python','text_jinja_template'):
        spec=importlib.util.spec_from_file_location('native_'+command,roboclick/'actions'/('roboclick_action_'+command)/'working.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);modules[command]=module
    for action in part['oomlout_ai_roboclick_1']['actions']:
        assert modules[action['command']].old(action=action,directory=str(directory))!='exit_no_tab'
    for size in labels.FORMATS:
        svg=ET.parse(directory/f'label_drawer_{size}.svg').getroot()
        assert svg.find(".//*[@id='primary-1']").text=='22 kOhm'
        assert '+/-5%' in svg.find(".//*[@id='detail-1']").text
    assert not (directory/'label_drawer_3x2.pdf').exists()
    assert (directory/'datasheet.pdf').read_bytes()==b'keep'
    assert (directory/'other.png').read_bytes()==b'keep'
    assert labels.load(directory/labels.CONTEXT)['bip39']=='cart vault uniform'


def test_entire_generated_catalogue_fit_and_physical_sizes():
    files=list((ROOT/'parts').glob('electronic_*/label_drawer_1_5x1.svg'))
    assert files
    for small in files:
        for size,(w,h,scale) in labels.FORMATS.items():
            svg=ET.parse(small.parent/f'label_drawer_{size}.svg').getroot()
            assert (svg.get('width'),svg.get('height'),svg.get('viewBox'))==(f'{w}mm',f'{h}mm',f'0 0 {w} {h}')
            assert len(svg.find(".//*[@id='bip39']").text.split())==3
            boxes=[]
            for n in svg.iter():
                if n.get('fill'):assert n.get('fill') in ('#000000','#ffffff')
                if not n.tag.endswith('}text') or not n.text:continue
                s=float(n.get('font-size'));x=float(n.get('x'));y=float(n.get('y'))
                x-=labels.width(n.text,s) if n.get('text-anchor')=='end' else 0
                l,t,r,b=labels.font().getbbox(n.text,anchor='ls')
                box=(x+l/1000*s,y+t/1000*s,x+r/1000*s,y+b/1000*s)
                assert box[0]>=.8 and box[2]<=37.3 and box[1]>=.8 and box[3]<25,(small,n.text,box)
                for previous in boxes:
                    assert not (min(box[2],previous[2])>max(box[0],previous[0]) and min(box[3],previous[3])>max(box[1],previous[1])),(small,n.text,box,previous)
                boxes.append(box)
