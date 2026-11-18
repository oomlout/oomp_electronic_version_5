"""Generate the missing two-way housing with the shared Harwin housing builder.
Render its STEP with render_wire_catalogue.py in the OOBB electronic project.
"""
import hashlib
from pathlib import Path
import shutil
import yaml
from working_oomp_populate_connector_crimp_data import PARTS, apply_extras

ROOT = Path(__file__).resolve().parents[1]


def refresh_metadata():
    import os
    import working_oomp
    from oomp_populate_helper import write_extras
    from jinja2 import Environment, FileSystemLoader
    row = next(r for r in PARTS if r['mpn'] == 'M20-1060200')
    previous = Path.cwd()
    try:
        os.chdir(ROOT)
        source = ROOT / 'parts_source' / row['id'] / 'working.yaml'
        option = yaml.safe_load(source.read_text(encoding='utf-8'))
        apply_extras({row['id']: option})
        write_extras([option])
        working_oomp.main(filter=row['id'])
        part = ROOT / 'parts' / row['id']
        details = yaml.safe_load((part/'working.yaml').read_text(encoding='utf-8'))
        template = Environment(loader=FileSystemLoader(ROOT/'source_file/template_jinja/oomp_category/template_jinja_markdown')).get_template('working.md.j2')
        (part/'README.md').write_text(template.render(p=details), encoding='utf-8')
    finally:
        os.chdir(previous)


def main():
    import cadquery as cq
    from kicad_agents.crimp_3d import housing_model, verify_solid
    row = next(r for r in PARTS if r['mpn'] == 'M20-1060200')
    source = ROOT / 'parts_source' / row['id']
    data = ROOT / 'parts' / row['id'] / 'data'
    shape = housing_model(row)
    verify_solid(shape, row)
    cq.exporters.export(shape, str(source / 'model_3d.step'))
    verify_solid(cq.importers.importStep(str(source / 'model_3d.step')).val(), row)
    record = dict(mpn=row['mpn'], dimensions_mm=row['dimensions_mm'], pitch_mm=2.54,
                  positions=2, drawing_url=row['datasheet_url'],
                  drawing_sha256=hashlib.sha256((source/'datasheet.pdf').read_bytes()).hexdigest(),
                  generator='kicad_agents/wire_housing_3d.py using crimp_3d.housing_model',
                  limitations='Simplified cavity, taper and retention geometry.')
    (source / 'model_3d_source.yaml').write_text(yaml.safe_dump(record),encoding='utf-8')
    for name in ('model_3d.step','model_3d_source.yaml'):
        shutil.copyfile(source/name,data/name)
    print('Verified two-way housing STEP.')
    refresh_metadata()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metadata-only', action='store_true')
    if parser.parse_args().metadata_only:
        refresh_metadata()
    else:
        main()
