"""Current-data electronic drawer labels: SVG only, two physical sizes."""
from __future__ import annotations
import argparse
import copy
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import textwrap
import xml.etree.ElementTree as ET

from jinja2 import Environment, StrictUndefined
from PIL import ImageFont
import yaml

ROOT=Path(__file__).resolve().parent
TEMPLATES=Path('source_file/template_jinja/label_drawer')
FORMATS={'3x2':(76.2,50.8,2),'1_5x1':(38.1,25.4,1)}
CONTEXT='data/label_drawer.yaml'
LOADER=getattr(yaml,'CSafeLoader',yaml.SafeLoader)
DUMPER=getattr(yaml,'CSafeDumper',yaml.SafeDumper)


def load(path):
    return yaml.load(Path(path).read_text(encoding='utf-8'),Loader=LOADER) or {}


def merge(base,update):
    result=dict(base)
    for k,v in update.items():
        result[k]=merge(result.get(k,{}),v) if isinstance(v,dict) and isinstance(result.get(k,{}),dict) else v
    return result


@lru_cache(maxsize=1)
def font():
    for directory in (Path(os.environ.get('WINDIR',r'C:\Windows'))/'Fonts',
                      Path(os.environ.get('LOCALAPPDATA',''))/'Microsoft/Windows/Fonts'):
        path=directory/'arialnb.ttf'
        if path.is_file():return ImageFont.truetype(str(path),1000)
    raise RuntimeError('Install Arial Narrow Bold (ARIALNB.TTF) to generate drawer labels with correct spacing.')


def width(text,size):return font().getlength(str(text))/1000*size

def fit(text,size,available=34.5):return round(min(size,available/max(width(text,1),.01)),4)


def clean(value):
    if value is None or isinstance(value,(dict,list,bool)):return ''
    value=str(value).strip()
    if not value or any(x in value.lower() for x in ('see live','see datasheet','not specified','unknown','not available')):return ''
    for old,new in [('Ω','Ohm'),('Ω','Ohm'),('µ','u'),('μ','u'),('±','+/-'),('+-','+/-'),('×','x'),('、',' / '),('℃',' C'),('–','-'),('−','-')]:value=value.replace(old,new)
    value=value.replace('_',' ')
    value=re.sub(r'\s+',' ',value)
    return value.strip()


def token(value):
    value=str(value or '')
    replacements={'quarter_watt_through_hole':'THT 1/4 W','through_hole':'THT','surface_mount':'SMD',
                  'right_angle':'RA','electrolytic':'Electrolytic','n_channel':'N-channel','p_channel':'P-channel',
                  'millimeter':'mm','mega_ohm':'MOhm','kilo_ohm':'kOhm',
                  'micro_farad':'uF','nano_farad':'nF','pico_farad':'pF','micro_henry':'uH','nano_henry':'nH',
                  'milli_henry':'mH','milliamp':'mA','amp':'A','volt':'V','ohm':'Ohm','mhz':'MHz','khz':'kHz',
                  'ghz':'GHz','pf':'pF','inch':'in','pin':'pin','diameter':'dia','tall':'high','aligator':'alligator',
                  'operational_amplifier':'op amp'}
    # Only collapse decimal runs inside an otherwise numeric quantity.
    value=re.sub(r'(?<![\w])([0-9]+)_([0-9]+)(?=_(?:mm|ohm|kilo|mega|pico|nano|micro|volt|amp|mhz|khz|inch))',r'\1.\2',value)
    for old,new in replacements.items():value=re.sub(r'(?<![a-zA-Z])'+re.escape(old)+r'(?![a-zA-Z])',lambda _:new,value)
    return clean(value)


def quantity(value):
    s=clean(value)
    # Drop only explanatory value-code parentheses, never rating conditions.
    s=re.sub(r'\s*\([^)]*\)\s*$','',s)
    m=re.fullmatch(r'([0-9.]+)\s*(Ohm|ohm)',s)
    if m:
        n=float(m[1])
        if n>=1e6:return f'{n/1e6:g} MOhm'
        if n>=1e3:return f'{n/1e3:g} kOhm'
        return f'{n:g} Ohm'
    return s


def identifier(part):
    return str(part.get('id') or '_'.join(str(part.get(f'taxonomy_{i}','')) for i in range(1,16) if part.get(f'taxonomy_{i}')))


@lru_cache(maxsize=1)
def words():return (ROOT/TEMPLATES/'bip_39_wordlist.txt').read_text().split()


def bip39(part):
    existing=part.get('bip_39_3_word_space') or ' '.join(part.get('bip_39_3_word_array',[]))
    if existing:
        if len(existing.split())!=3:raise ValueError('BIP39 identifier must contain three words')
        return ' '.join(existing.split())
    digest=part.get('md5') or hashlib.md5(identifier(part).encode()).hexdigest()
    bits=f'{int(digest,16):0128b}'
    return ' '.join(words()[int(bits[i:i+11],2)] for i in (0,11,22))


def content(part):
    kind=part.get('taxonomy_2','component')
    t={i:str(part.get(f'taxonomy_{i}','')) for i in range(3,14)}
    e=part.get('electrical') or {}
    def get(*keys):return next((clean(e[k]) for k in keys if clean(e.get(k))), '')
    def val(*suffixes):return next((token(v) for v in t.values() if v.endswith(suffixes)), '')
    def join(*values):return ' | '.join(v for v in values if v)
    def rated(label,*keys):
        value=get(*keys)
        return f'{label} {value}' if value else ''
    def rating(value):return value if len(value)<=70 else ''
    mpn=clean(part.get('part_number_manufacturer') or part.get('part_number_generic') or str(part.get('taxonomy_15','')).upper())
    package=token(t[3]).upper()
    if kind in ('diode','sensor','switch'):package=token(t[4]).upper()
    if kind=='potentiometer':package=token(part.get('taxonomy_form_factor') or t[3]).upper()
    # Long package descriptions belong in supporting text, not tiny header type.
    package_detail=''
    if width(package,1.85)>24:
        package_detail=package
        package='SMD' if any(x in package for x in ('SMD','SOT','SOIC','LGA','QFN','QFP')) else ('THT' if 'THT' in package else '')
    hero=mpn or token(t[4]) or token(t[3]) or clean(part.get('name_short'))
    details=[]
    if kind in ('resistor','resistor_array','potentiometer','ntc_thermistor'):
        hero=quantity(get('resistance') or val('_ohm'))
        details=[join(get('tolerance'),rating(get('power_per_element','power'))),package_detail]
        if kind=='resistor_array':details.insert(0,join(f"{e['elements']} resistors" if e.get('elements') else token(t[3]),val('_pin')))
        if kind=='potentiometer':details.insert(0,token(t[3]).upper())
        if kind=='ntc_thermistor':details.insert(0,val('_a','_amp','_milliamp'))
    elif kind=='capacitor':
        hero=quantity(get('capacitance') or val('_farad'))
        details=[join(get('rated_voltage','voltage') or val('_volt'),get('dielectric'),get('tolerance')),package_detail]
        if e.get('polarized') is True:details.insert(1,'POLARIZED')
    elif kind=='connector':
        hero=val('_pin','_pin_dual_row') or mpn or token(t[3]).upper()
        if not val('_pin','_pin_dual_row') and part.get('pins'):hero=f"{len(part['pins'])} pin"
        package=token(t[3]).upper()
        details=[join(token(t[4]),token(t[5]),token(t[7])),rated('Rated','current_rating')]
        # Some imported MPN fields include a prose description, even a stale
        # pin count. Keep the actual code and use taxonomy for the pin count.
        mpn=re.split(r'(?i)(?=\d+(?:\.\d+)?\s*mm pitch|Straight IDC)',mpn)[0].strip()
    elif kind=='crystal':
        hero=get('frequency') or val('_mhz','_khz','_hz') or mpn
        details=[join(rated('CL','load_capacitance') or val('_pf'),val('_ohm_esr')),join(val('_pin'),token(t[4])),package_detail]
    elif kind in ('inductor','ferrite_bead'):
        hero=quantity(get('inductance','impedance_at_100_mhz') or val('_henry','_ohm'))
        details=[join('@ 100 MHz' if kind=='ferrite_bead' and e.get('impedance_at_100_mhz') else '',get('maximum_rated_current','max_dc_current') or val('_milliamp','_amp'),get('inductance_tolerance','impedance_tolerance')),rated('DCR','maximum_dc_resistance','max_dc_resistance')]
    elif kind=='led':
        hero=(get('led_color') or token(t[4])).split('(',1)[0].strip().upper()
        details=[join(token(t[5]),rated('Vf','forward_voltage'),rated('If','forward_current')),rating(get('luminous_intensity')),package_detail]
    elif kind in ('ic','diode','transistor','sensor'):
        if kind=='ic':
            function=get('device_type') or token(t[5]) or token(t[4])
            details=[function,join(rated('Supply','supply_voltage','supply'),rated('Out','output_voltage'),rated('Iout','output_current','maximum_output_current'))]
        elif kind=='diode':
            details=[token(t[3]).upper(),join(rated('Vz','zener_voltage_nominal') or rated('Vr','maximum_dc_reverse_voltage','repetitive_peak_reverse_voltage') or rated('VRWM','reverse_standoff_voltage'),rated('If','forward_current','maximum_rectified_current','output_rectified_current'))]
        elif kind=='transistor':
            details=[join(get('transistor_polarity','polarity') or token(t[5]),token(t[4]),token(t[6])),join(rated('Vds','maximum_drain_source_voltage') or rated('Vce','maximum_collector_emitter_voltage','collector_emitter_breakdown_voltage') or val('_volt'),rated('Id','maximum_continuous_drain_current') or rated('Ic','collector_current','maximum_continuous_collector_current') or val('_amp','_milliamp'))]
        else:details=[token(t[3]).upper(),join(rated('Supply','supply_voltage'),get('interface'))]
        details.append(package_detail)
    elif kind=='fuse':
        hero=get('current_rating') or mpn or token(t[3])
        details=[join(token(t[4]).upper(),rated('Rated','voltage_rating')),package_detail]
    elif kind=='relay':
        hero=(get('coil_voltage')+' COIL') if get('coil_voltage') else val('_volt_coil') or mpn
        details=[token(t[5]).upper() or get('contact_form'),rated('Contacts','contact_rating')]
    elif kind=='switch':
        hero=token(t[3]).upper()
        details=[join(get('circuit'),f"{e['positions']} pos" if e.get('positions') else ''),join(get('current_rating'),get('voltage_rating')),package_detail]
    elif kind=='display':
        hero=val('_pixel') or mpn or token(t[3]).upper()
        details=[join(token(t[4]),token(t[6]).upper(),token(t[7]).upper()),rated('Logic','logic_supply_range','logic_supply_typical')]
    elif kind=='heatsink':
        hero=mpn or token(t[3]);details=['Dimensions mm']
    elif kind=='prototyping':
        hero=token(t[4]);details=[token(t[3]).upper(),token(t[5])]
    elif kind=='wire':
        hero=token(t[7]) or token(t[4]);details=[join(token(t[5]),token(t[6])),token(t[8])]
    else:
        # Antennas, batteries, buzzers and optical devices retain their identity
        # plus all available form/frequency/size data, without invented ratings.
        details=[join(*(token(t[i]) for i in range(4,9) if t[i])),join(get('frequency'),get('voltage','rated_voltage','supply_voltage')),package_detail]
    if not hero:hero=mpn or clean(part.get('name_short')) or token(kind).upper()
    if mpn and mpn.casefold()!=hero.casefold():details.append(mpn)
    lcsc=clean(part.get('part_number_lcsc'))
    if lcsc:details.append('LCSC '+lcsc)
    overrides=part.get('label_drawer_overrides') or {}
    return dict(type=clean(overrides.get('type',token(kind).upper())),package=clean(overrides.get('package',package)),
                primary=clean(overrides.get('primary',hero)),details=overrides.get('details',[v for v in details if v]),bip39=bip39(part))


def wrap_width(text,size,available):
    lines=[]
    for word in text.split():
        if lines and width(lines[-1]+' '+word,size)<=available:lines[-1]+=' '+word
        else:lines.append(word)
    return lines


def layout(part):
    c=content(part)
    primary=c['primary']
    hero_size=fit(primary,6.2)
    if hero_size>=3.6:hero=[dict(text=primary,size=hero_size,y=11.5)]
    else:
        lines=wrap_width(primary,3.6,34.5)
        if len(lines)==1:
            # Long part codes remain intact on one line; never insert ambiguous separators.
            hero=[dict(text=primary,size=hero_size,y=11.5)]
        else:
            split=max(1,len(primary.split())//2)
            lines=[' '.join(primary.split()[:split]),' '.join(primary.split()[split:])]
            hero=[dict(text=v,size=fit(v,3.6),y=8.6+i*3.6) for i,v in enumerate(lines)]
    rows=[];omitted=[]
    for value in c['details']:
        value=clean(value)
        if not value or value in [r['text'] for r in rows]:continue
        lines=wrap_width(value,2.2,34.5)
        if len(lines)>2 or len(rows)+len(lines)>3:
            if len(rows)<3 and fit(value,2.2)>=1.65:lines=[value]
            else:omitted.append(value);continue
        for line in lines:
            rows.append(dict(text=line,size=fit(line,2.3 if not rows else 2.15),y=15.4+len(rows)*2.7))
    type_size=fit(c['type'],2.55,21.5)
    return dict(c,hero=hero,rows=rows,omitted_details=omitted,type_size=type_size,
                package_size=fit(c['package'],2.1,34.5-width(c['type'],type_size)-1.2),bip39_size=fit(c['bip39'],2.85),
                full_details='; '.join(c['details']))


def is_component(part):return part.get('taxonomy_1')=='electronic'


def is_manifest(block):
    return any(str(a.get('file_python','')).replace('\\','/').endswith('web_manifest_action.py') for a in block.get('actions',[]))


def add_actions(part,count=0,root=ROOT):
    if not is_component(part):return count
    # Keep the manifest last, including when this is called on existing metadata.
    manifests={k:part.pop(k) for k in list(part) if k.startswith('oomlout_ai_roboclick_') and isinstance(part[k],dict) and is_manifest(part[k])}
    for k in list(part):
        if k.startswith('oomlout_ai_roboclick_') and any(a.get('file_output')==CONTEXT for a in part[k].get('actions',[])):del part[k]
    indices=[int(k.rsplit('_',1)[1]) for k in part if re.fullmatch(r'oomlout_ai_roboclick_\d+',k)]
    index=max([count]+indices)+1
    actions=[{'command':'run_python','description':'Read current component details and prepare drawer labels; remove stale label PDFs',
              'file_python':str(Path(root).resolve()/'working_drawer_labels.py'),'file_output':CONTEXT,'timeout':'120'}]
    for size in FORMATS:
        actions.append({'command':'text_jinja_template','description':f'Drawer label {size}',
                        'file_template':str(Path(root).resolve()/TEMPLATES/f'{size}.svg.j2'),
                        'file_output':f'label_drawer_{size}.svg','dict_data_yaml_files':{'label_drawer':CONTEXT},
                        'convert_to_pdf':False,'convert_to_png':False})
    part[f'oomlout_ai_roboclick_{index}']={'file_test':'','always_run_on_regeneration':True,'actions':actions}
    for block in manifests.values():
        index+=1;part[f'oomlout_ai_roboclick_{index}']=block
    return index


def current_part(directory,root=ROOT):
    directory=Path(directory).resolve();root=Path(root).resolve()
    if not directory.is_relative_to(root/'parts'):raise ValueError('Part directory must be inside this repository parts folder')
    part=load(directory/'working.yaml') if (directory/'working.yaml').exists() else {}
    source=root/'parts_source'/directory.name/'working.yaml'
    if source.exists():part=merge(part,load(source))
    manual=directory/'working_manual.yaml'
    if manual.exists():part=merge(part,load(manual))
    return part


def clean_renders(directory):
    removed=0;directory=Path(directory).resolve()
    for folder in (directory,directory/'data'):
        for size in FORMATS:
            for ext in ('pdf','png'):
                path=folder/f'label_drawer_{size}.{ext}'
                if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(directory):
                    path.unlink();removed+=1
    return removed


def prepare(directory,root=ROOT):
    directory=Path(directory).resolve()
    part=current_part(directory,root)
    if not is_component(part):raise ValueError('Drawer labels require an electronic component')
    context=layout(part)
    path=directory/CONTEXT;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(yaml.dump(context,Dumper=DUMPER,sort_keys=False,allow_unicode=True),encoding='utf-8')
    clean_renders(directory)
    return context


@lru_cache(maxsize=8)
def template(path):return Environment(undefined=StrictUndefined).from_string(Path(path).read_text(encoding='utf-8'))


def render(context,size,root=ROOT):
    svg=template(str(Path(root)/TEMPLATES/f'{size}.svg.j2')).render(p={'label_drawer':context})
    ET.fromstring(svg)
    return svg


def regenerate(root=ROOT,filter_text=''):
    root=Path(root).resolve();count=0
    names=sorted({p.parent.name for p in (root/'parts_source').glob('*/working.yaml')}|{p.parent.name for p in (root/'parts').glob('*/working.yaml')})
    for name in names:
        if filter_text and filter_text not in name:continue
        source=root/'parts_source'/name/'working.yaml'
        if source.exists() and not is_component(load(source)):continue
        directory=root/'parts'/name
        part=current_part(directory,root)
        if not is_component(part):continue
        directory.mkdir(parents=True,exist_ok=True)
        path=directory/'working.yaml'
        metadata=load(path) if path.exists() else dict(part)
        add_actions(metadata,root=root)
        path.write_text(yaml.dump(metadata,Dumper=DUMPER,sort_keys=False,allow_unicode=True),encoding='utf-8')
        context=layout(part)
        data=directory/CONTEXT;data.parent.mkdir(parents=True,exist_ok=True)
        data.write_text(yaml.dump(context,Dumper=DUMPER,sort_keys=False,allow_unicode=True),encoding='utf-8')
        for size in FORMATS:(directory/f'label_drawer_{size}.svg').write_text(render(context,size,root),encoding='utf-8')
        clean_renders(directory)
        count+=1
        if count%250==0:print(f'Regenerated {count} components...',flush=True)
    if not count:raise ValueError('No matching electronic components')
    print(f'Generated {count*2} SVG drawer labels for {count} components. PDF generation disabled.',flush=True)
    return count


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kwargs',help='Roboclick action arguments')
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--filter',default='')
    args=parser.parse_args()
    if args.kwargs:prepare(json.loads(args.kwargs)['directory'],args.root)
    else:regenerate(args.root,args.filter)
