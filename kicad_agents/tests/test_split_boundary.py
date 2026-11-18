import json
from pathlib import Path
import pytest
import yaml
from kicad_agents.kicad_library_agent import Masters,build_part,project_candidates

ROOT=Path(__file__).resolve().parents[2]

def test_fallback_evidence_is_local_and_retains_ambiguity():
    expected=json.loads((ROOT/'source_file/kicad_library/project_fallback_candidates.json').read_text())
    assert project_candidates(Path('nonexistent-project-checkout'))==expected['candidates']
    assert any(len(row['footprints'])>1 for row in expected['candidates'].values())

def test_native_component_library_build_needs_no_project_checkout(tmp_path):
    try:
        masters=Masters()
    except FileNotFoundError as error:
        pytest.skip(str(error))
    identifier='electronic_resistor_0603_2200_ohm'
    part=tmp_path/identifier; part.mkdir()
    (part/'working.yaml').write_text(yaml.safe_dump({'id':identifier,'taxonomy_1':'electronic',
        'taxonomy_2':'resistor','taxonomy_3':'0603','taxonomy_4':'2200_ohm',
        'name_readable':'Resistor 2.2k 0603','md5_6_alpha_upper':'1X0XV'}))
    report=build_part(part,masters,project_candidates(ROOT/'parts'))
    assert report['status']=='complete'
    assert len(report['assets'])==3
    assert (part/'data/kicad/manifest.yaml').is_file()

@pytest.mark.parametrize('entrypoint',['delete_generated_files','regenerate_diagrams'])
def test_component_reset_commands_leave_project_files_untouched(tmp_path,monkeypatch,entrypoint):
    component=tmp_path/'parts/electronic_demo'
    project=tmp_path/'parts/oomp_project_demo'
    for directory in (component,project):
        (directory/'data').mkdir(parents=True)
        (directory/'working.yaml').write_text('{}')
        (directory/'data/working_svg_demo.png').write_bytes(b'saved preview')
    monkeypatch.chdir(tmp_path)
    if entrypoint=='delete_generated_files':
        import action_delete_generated_files as command
        monkeypatch.setattr(command,'REPOSITORY_ROOT',tmp_path)
        command.delete_generated_files(full_reset=True)
    else:
        import action_regenerate_all_delete_current_diagrams as command
        monkeypatch.setattr(command,'REPOSITORY_ROOT',tmp_path)
        monkeypatch.setattr(command,'_recompile_parts',lambda _:None)
        monkeypatch.setattr(command.oomlout_roboclick,'build_action_lookup',lambda:{})
        command.regenerate_diagrams()
    assert not (component/'data/working_svg_demo.png').exists()
    assert (component/'working.yaml').is_file()
    assert (project/'data/working_svg_demo.png').read_bytes()==b'saved preview'
