"""Stage the MDD ES2J SMA display with an illustrative identifier."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_diode_fast_recovery_sma_mdd_microdiode_semiconductor_es2j'
PILOT = 'electronic_diode_schottky_sma_mdd_microdiode_semiconductor_ss14'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_ES2J_RESEARCH.md')
PDF_SHA = 'b3a7e1d0f678d0f19e646287a373916161994dda07e31e658ab7cbac28d7f778'
MODEL_SHA = '1cfddd4e3b1bf22b8fc6ee3258c2aade882ed7b85b528e23b9db42437775a1db'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    source = ROOT / 'parts_source' / PART
    d = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
    if (d.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or d.get('part_number_manufacturer') != 'ES2J'
        or d.get('dimensions_mm') != {'length': 10.0, 'width': 5.0}
        or (d.get('kicad') or {}).get('machine_solder') != '' or digest(source / 'datasheet.pdf') != PDF_SHA):
        raise ValueError('ES2J source or drawing changed')
    recipe = copy.deepcopy(recipes[PILOT])
    if recipe['model']['sha256'] != MODEL_SHA: raise ValueError('SMA pilot model changed')
    recipe['represented_mpn'] = 'ES2J'
    recipe['marking'].update(policy='illustrative_literal', text='ES2J',
        evidence={'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                  'document': 'Local MDD ES2A–ES2J datasheet page 1', 'source_record': f'parts_source/{PART}/working.yaml'},
        appearance_status='Illustrative ES2J identifier; the manufacturer drawing does not establish a physical text marking.')
    recipe['appearance_status'] = ('KiCad SMA model has 5.0 x 2.7 x 2.22 mm bounds and cathode band; '
        'its body is about 0.06 mm longer than the drawing maximum. Source 10 x 5 mm dimensions conflict with the drawing. '
        'ES2J lettering is illustrative because the manufacturer marking code is not established. '
        'Display illustration only; not manufacturer CAD or a PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()

if __name__ == '__main__':
    main()
