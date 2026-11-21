"""Stage the MDD 1N5401 DO-201AD diode illustration."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging
PART = 'electronic_diode_rectifier_do_201ad_mdd_microdiode_semiconductor_1n5401'
PILOT = 'electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001'
MODEL_SHA = '9673cb3150b924995e254392adfba026ca7b81e7a347bdd933badb143b0c30ae'
PDF_SHA = '477cf8f0f369adc3206c920678e393081bb35d78ba232811597cff22e43a5b86'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_1N5401_RESEARCH.md')

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    d = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (d.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or d.get('part_number_manufacturer') != '1N5401'
        or d.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (d.get('kicad') or {}).get('machine_solder') != ''
        or digest(source / 'datasheet.pdf') != PDF_SHA): raise ValueError('1N5401 source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT]); recipe.update(package='do_201ad_bent', represented_mpn='1N5401')
    model = 'Diode_THT.3dshapes/D_DO-201AD_P12.70mm_Horizontal.step'
    recipe['model'].update(relative_path=model, source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model,
        copyright='2017 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[14.0,5.22,8.21])
    recipe['marking'].update(text='1N5401', maximum_width_mm=2.1, maximum_height_mm=.6, offset_x_mm=.85,
        evidence={'file':EVIDENCE.as_posix(),'sha256':digest(ROOT / EVIDENCE), 'document':'MDD 1N5401 family drawing page 1',
                  'source_record':f'parts_source/{PART}/working.yaml'},
        appearance_status='1N5401 is the documented identifier, with MDD logo omitted; actual typography and placement are illustrative.')
    recipe['appearance_status'] = ('KiCad DO-201AD model has bent leads at 12.70 mm pitch; manufacturer drawing shows straight leads. '
        'Model width is 5.22 mm, within the drawing body diameter range. Source 10 x 5 mm dimensions and missing footprint do not match the manufacturer drawing. '
        'Display illustration only; not manufacturer CAD or PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()
if __name__ == '__main__': main()
