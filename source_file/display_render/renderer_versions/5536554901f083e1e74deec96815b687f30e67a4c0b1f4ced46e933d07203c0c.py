"""Stage the MDD SF28 DO-15 diode illustration."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging
PART = 'electronic_diode_fast_recovery_do_15_mdd_microdiode_semiconductor_sf28_tape'
PILOT = 'electronic_diode_rectifier_do_41_mdd_microdiode_semiconductor_1n4001'
MODEL_SHA = '71d21632cb4f83434a45f5380edd2d52c82ad56284fc49178326aa333117e6ed'
PDF_SHA = 'f0651df053f0d230253e4fa975e4ae9c18f29887a61c319aa232f05c663e00a9'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_SF28_TAPE_RESEARCH.md')

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    d = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (d.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or d.get('part_number_manufacturer') != 'SF28 Tape'
        or d.get('dimensions_mm') != {'height': 4.0, 'length': 7.6, 'width': 3.6}
        or (d.get('kicad') or {}).get('machine_solder') != 'Diode_THT:D_DO-15_P10.16mm_Horizontal'
        or digest(source / 'datasheet.pdf') != PDF_SHA): raise ValueError('SF28 source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT]); recipe.update(package='do_15_bent', represented_mpn='SF28 Tape')
    model = 'Diode_THT.3dshapes/D_DO-15_P10.16mm_Horizontal.step'
    recipe['model'].update(relative_path=model, source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model,
        copyright='2017 kicad StepUp', sha256=MODEL_SHA, expected_bounds_mm=[11.06,3.62,6.61])
    recipe['marking'].update(policy='illustrative_literal', text='SF28', maximum_width_mm=2.1, maximum_height_mm=.6, offset_x_mm=.85,
        evidence={'file':EVIDENCE.as_posix(),'sha256':digest(ROOT / EVIDENCE), 'document':'MDD SF28 family drawing page 1',
                  'source_record':f'parts_source/{PART}/working.yaml'},
        appearance_status='SF28 is an illustrative identifier; its physical marking code is not established.')
    recipe['appearance_status'] = ('KiCad DO-15 model has bent leads at 10.16 mm pitch; manufacturer drawing shows straight leads. '
        'Model body diameter is approximately 3.62 mm, 0.02 mm above drawing maximum. Source 4 mm height is not the specified body diameter. '
        'Display illustration only; not manufacturer CAD or PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()
if __name__ == '__main__': main()
