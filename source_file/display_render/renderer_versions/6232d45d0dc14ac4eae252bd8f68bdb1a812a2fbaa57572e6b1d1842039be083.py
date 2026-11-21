"""Stage the MDD HER204 DO-15 diode illustration."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging
PART = 'electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_her204'
PILOT = 'electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001'
MODEL_SHA = '71d21632cb4f83434a45f5380edd2d52c82ad56284fc49178326aa333117e6ed'
PDF_SHA = '9b810f6b89dd395874c3779b849db05531fdd78beb38bdd09a8c809e13f68d74'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_HER204_RESEARCH.md')

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    d = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (d.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or d.get('part_number_manufacturer') != 'HER204'
        or d.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (d.get('kicad') or {}).get('machine_solder') != ''
        or digest(source / 'datasheet.pdf') != PDF_SHA): raise ValueError('HER204 source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT]); recipe.update(package='do_15_bent', represented_mpn='HER204')
    model = 'Diode_THT.3dshapes/D_DO-15_P10.16mm_Horizontal.step'
    recipe['model'].update(relative_path=model, source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model,
        copyright='2017 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[11.06,3.62,6.61])
    recipe['marking'].update(text='HER204', maximum_width_mm=2.1, maximum_height_mm=.6, offset_x_mm=.85,
        evidence={'file':EVIDENCE.as_posix(),'sha256':digest(ROOT / EVIDENCE), 'document':'MDD HER204 family drawing page 1',
                  'source_record':f'parts_source/{PART}/working.yaml'},
        appearance_status='HER204 is the documented identifier, with MDD logo omitted; actual typography and placement are illustrative.')
    recipe['appearance_status'] = ('KiCad DO-15 model has bent leads at 10.16 mm pitch; manufacturer drawing shows straight leads. '
        'Model body diameter is approximately 3.62 mm, 0.02 mm above drawing maximum. Source 10 x 5 mm dimensions and missing footprint conflict with the drawing. '
        'Display illustration only; not manufacturer CAD or PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()
if __name__ == '__main__': main()
