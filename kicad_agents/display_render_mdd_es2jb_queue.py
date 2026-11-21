"""Stage the MDD ES2JB SMA display with an illustrative identifier."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_diode_fast_recovery_smb_mdd_microdiode_semiconductor_es2jb'
PILOT = 'electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_ES2JB_RESEARCH.md')
PDF_SHA = '3f81111d69c355c8972019e971d12763200fe0429ca4c32ff89db5f86094cde8'
PILOT_MODEL_SHA = '1cfddd4e3b1bf22b8fc6ee3258c2aade882ed7b85b528e23b9db42437775a1db'
MODEL_SHA = '029466277d91e9f5492556be93e46611049e07115c7913880c547afa96058ed4'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    d = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (d.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or d.get('part_number_manufacturer') != 'ES2JB'
        or d.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (d.get('kicad') or {}).get('machine_solder') != '' or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('ES2JB source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    if recipe['model']['sha256'] != PILOT_MODEL_SHA: raise ValueError('SMA pilot model changed')
    recipe['represented_mpn'] = 'ES2JB'; recipe['package'] = 'smb'
    model = 'Diode_SMD.3dshapes/D_SMB.step'
    recipe['model'].update(relative_path=model, source_url='https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + model, sha256=MODEL_SHA, expected_bounds_mm=[5.3,3.55,2.15])
    recipe['marking'].update(policy='illustrative_literal', text='ES2JB',
        evidence={'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                  'document': 'Local MDD ES2AB–ES2JB datasheet page 1', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Illustrative ES2JB identifier; the manufacturer drawing does not establish a physical text marking.')
    recipe['appearance_status'] = ('KiCad SMB model has 5.30 x 3.55 x 2.15 mm bounds and cathode band; '
        'Source 10 x 5 mm dimensions conflict with the drawing. '
        'ES2JB lettering is illustrative because the manufacturer marking code is not established. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()

if __name__ == '__main__':
    main()
