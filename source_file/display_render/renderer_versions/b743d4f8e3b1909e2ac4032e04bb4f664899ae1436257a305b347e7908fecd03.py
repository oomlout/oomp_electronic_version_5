"""Stage a deliberately unmarked Bourns MF-FSMF family illustration."""
import copy
import hashlib
from pathlib import Path
import yaml
from kicad_agents.display_render_kangnex_wj127_2p_queue import ROOT
from kicad_agents import display_render_kangnex_wj127_2p_queue as staging

PART = 'electronic_fuse_0603_resettable_bourns_mf_fsmf'
MODEL = 'kicad_agents/display_model_littelfuse_minismdc.py'
MODEL_SHA = 'd66c0fb6a77d89c60317f8c1ebb0ee00e38d759757afd72d9f4cc982d979abbb'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_BOURNS_MF_FSMF_RESEARCH.md')
PILOT = 'electronic_resistor_0603_10000_ohm'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(recipes):
    record = yaml.safe_load((ROOT / 'parts_source' / PART / 'working.yaml').read_text(encoding='utf8')) or {}
    if (record.get('manufacturer') != 'Bourns' or record.get('part_number_manufacturer') != 'MF-FSMF'
        or record.get('dimensions_mm') != {'length': 1.6, 'width': .8}
        or (record.get('kicad') or {}).get('machine_solder') != 'Fuse:Fuse_0603_1608Metric'):
        raise ValueError('Bourns family identity or size changed')
    if digest(ROOT / MODEL) != MODEL_SHA:
        raise ValueError('Procedural fuse model changed')
    recipe = copy.deepcopy(recipes[PILOT])
    recipe.update(family='fuse', package='bourns_mf_fsmf_family', represented_manufacturer='Bourns', represented_mpn='MF-FSMF')
    recipe['disable_bump_for'] = ['coating', 'termination']
    recipe['model'] = {'relative_path': MODEL, 'source_url': 'https://github.com/oomlout/oomp_electronic_version_5/blob/main/' + MODEL,
        'copyright': 'Procedural model generated in this repository', 'license': 'Project source; procedural display geometry',
        'expected_bounds_mm': [4.55, 3.24, .76], 'dimension_tolerance_mm': .015, 'sha256': MODEL_SHA,
        'display_scale_xyz': [1.6/4.55, .8/3.24, .65/.76], 'required_roles': ['coating', 'termination']}
    recipe['marking'] = {'policy': 'unmarked_illustration', 'text': '', 'font_file': 'arialbd.ttf',
        'evidence': {'file': EVIDENCE.as_posix(), 'sha256': digest(ROOT / EVIDENCE),
                     'document': 'Bourns MF-FSMF manufacturer family datasheet online',
                     'source_record': f'parts_source/{PART}/working.yaml'},
        'appearance_status': 'Unmarked illustration: the unspecified current variant determines the actual marking.'}
    recipe['appearance_status'] = ('Family-level 1.6 x 0.8 x 0.65 mm concave-end illustration; actual current variant and marking are unspecified. '
        'The real device is marked according to its variant; this illustration deliberately omits the mark. '
        'Body shade, exact notch shape and gold-coloured terminal finish are illustrative. '
        'Display only; not manufacturer CAD or a PCB footprint.')
    return recipe

def main():
    staging.PART, staging.prepare = PART, prepare
    staging.main()

if __name__ == '__main__':
    main()
