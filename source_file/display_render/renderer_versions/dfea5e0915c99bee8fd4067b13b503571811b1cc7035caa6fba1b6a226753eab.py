"""Stage two MDD KBL bridges using a reviewed generic KiCad model."""
import argparse
import copy
import hashlib
import json
import os
import tempfile
from pathlib import Path

import yaml
from kicad_agents.display_render_resistor_queue import ROOT, RECIPE_FILE
from kicad_agents.display_render_mdd_kbp_queue import PARTS as KBP_PARTS

PREFIX = 'electronic_diode_bridge_rectifier_kbl_mdd_microdiode_semiconductor_'
PARTS = {PREFIX + n.lower(): n for n in ('KBL406', 'KBL410')}
PILOT = next(part for part, mpn in KBP_PARTS.items() if mpn == 'KBP206')
MODEL = 'Diode_THT.3dshapes/Diode_Bridge_Vishay_KBL.step'
MODEL_SHA = '91f63058c59299ffaf82533f5eb26d1d825185c689c0877b710f01e11fa70b81'
PDF_SHA = '573c5f78e440cb38f2fe43f7cbd5bd394fbe38f1fd1a52dc3dd584afd5ff590f'
EVIDENCE = Path('kicad_agents/component_records/DISPLAY_RENDER_MDD_KBL_KBU_MODELS.md')


def prepare(recipes):
    source_pdf = ROOT / 'parts_source' / (PREFIX + 'kbl406') / 'datasheet.pdf'
    if hashlib.sha256(source_pdf.read_bytes()).hexdigest() != PDF_SHA:
        raise ValueError('Reviewed MDD KBL family drawing changed')
    evidence_hash = hashlib.sha256((ROOT / EVIDENCE).read_bytes()).hexdigest()
    result = {}
    for part, mpn in PARTS.items():
        source = ROOT / 'parts_source' / part
        record = yaml.safe_load((source / 'working.yaml').read_text(encoding='utf8')) or {}
        if (record.get('manufacturer') != 'MDD(Microdiode Semiconductor)' or record.get('part_number_manufacturer') != mpn
            or record.get('dimensions_mm') != {'height': 4.0, 'length': 28.6, 'width': 7.3}
            or (record.get('kicad') or {}).get('machine_solder') != 'Diode_THT:Diode_Bridge_Vishay_KBL'):
            raise ValueError(f'{mpn}: source identity, dimensions or footprint changed')
        if mpn == 'KBL410' and (source / 'datasheet.pdf').exists():
            raise ValueError('KBL410 gained a local PDF; review it')
        recipe = copy.deepcopy(recipes[PILOT])
        recipe.update(package='kbl_kicad_face_up', represented_mpn=mpn)
        recipe['model'] = {'relative_path': MODEL,
            'source_url': 'https://gitlab.com/kicad/libraries/kicad-packages3D/-/blob/master/' + MODEL,
            'copyright': 'KiCad 3D Model Libraries contributors', 'license': 'CC-BY-SA 4.0 with KiCad library exception',
            'expected_bounds_mm': [19.5, 6.5, 29.05], 'dimension_tolerance_mm': .02,
            'sha256': MODEL_SHA, 'required_roles': ['coating', 'termination'],
            'role_by_source_colour': {'0.148,0.145,0.145': 'coating', '0.824,0.820,0.781': 'termination'}}
        recipe['marking'] = {'policy': 'illustrative_literal', 'text': mpn + '\n+  ~  ~  -', 'font_file': 'arialbd.ttf',
            'maximum_width_mm': 10.0, 'maximum_height_mm': 2.0,
            'evidence': {'file': EVIDENCE.as_posix(), 'sha256': evidence_hash,
                'document': 'MDD KBL family marking, outline and KiCad model review', 'source_record': f'parts_source/{part}/working.yaml'},
            'appearance_status': (f'{mpn} is a partial MDD family identifier; the logo is omitted. The +, ~, ~, - layout '
                'follows the manufacturer drawing and selected KiCad pad numbering. Typeface, placement and finish are illustrative.')}
        if mpn == 'KBL410':
            recipe['marking']['appearance_status'] += ' No local KBL410 PDF is stored; the KBL406 family PDF covers it.'
        recipe['appearance_status'] = ('Generic KiCad KBL model shown with its broad face up; its 19.5 mm body width is at '
            'the MDD drawing maximum. Model leads project about 14 mm rather than the drawing minimum 16.4 mm. '
            'Source 28.6 x 7.3 x 4.0 mm dimensions differ from the drawing body envelope. '
            'Display illustration only; not manufacturer CAD or a PCB footprint.')
        result[part] = recipe
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--add', action='store_true')
    args = parser.parse_args()
    original = RECIPE_FILE.read_bytes()
    recipes = json.loads(original.decode('utf8'))
    for part, recipe in prepare(recipes).items():
        if part in recipes and recipes[part] != recipe:
            raise ValueError(f'{part}: existing recipe differs')
        recipes[part] = recipe
    if args.add:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(dir=RECIPE_FILE.parent, delete=False) as f:
                temp = Path(f.name)
                f.write((json.dumps(recipes, ensure_ascii=False, indent=2) + '\n').encode('utf8'))
                f.flush()
                os.fsync(f.fileno())
            if RECIPE_FILE.read_bytes() != original:
                raise RuntimeError('Recipes changed during validation')
            os.replace(temp, RECIPE_FILE)
        finally:
            if temp is not None and temp.exists():
                temp.unlink()
    print('Two KBL candidates; inspect orientation and polarity before publication')


if __name__ == '__main__':
    main()
