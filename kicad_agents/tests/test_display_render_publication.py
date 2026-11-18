import yaml
import pytest

from kicad_agents import readme_action
import working_oomp


def test_readme_only_publication_skips_label_actions(tmp_path, monkeypatch):
    part = tmp_path / 'electronic_example'
    part.mkdir()
    workings = {'oomlout_example': {'actions': [
        {'command': 'text_jinja_template', 'file_output': 'README.md'},
        {'command': 'text_jinja_template', 'file_output': 'label_drawer_3x2.svg'},
    ]}}
    (part / 'working.yaml').write_text(yaml.safe_dump(workings), encoding='utf-8')
    calls = []
    monkeypatch.setattr(readme_action.oomlout_roboclick, 'build_action_lookup', lambda: {})
    monkeypatch.setattr(readme_action.oomlout_roboclick, 'run_single_action',
                        lambda **kwargs: calls.append(kwargs['action']['file_output']))
    assert readme_action.regenerate_readmes(tmp_path, part_ids={'electronic_example'},
                                           output_names={'README.md'}) == 1
    assert calls == ['README.md']


def test_exact_compiler_selection_does_not_include_longer_variant(tmp_path, monkeypatch):
    base = 'electronic_resistor_0603_220_ohm'
    variant = base + '_5_percent'
    for name in (base, variant):
        folder = tmp_path / 'parts_source' / name
        folder.mkdir(parents=True)
        (folder / 'working.yaml').write_text(yaml.safe_dump({
            'taxonomy_1': 'electronic', 'taxonomy_2': 'resistor',
            'taxonomy_3': '0603', 'taxonomy_4': '220_ohm'}), encoding='utf-8')
    captured = []
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(working_oomp.oomp, 'add_part', lambda **part: captured.append(part) or None)
    working_oomp.main(exact_part_ids=[base], make_files=False, regenerate_pngs=False)
    assert [part['name'] for part in captured] == [base]
    assert 'exact_part_ids' not in captured[0]


def test_exact_compiler_rejects_empty_or_path_like_ids(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    for selection in ([], ['../bad']):
        with pytest.raises(ValueError, match='exact_part_ids'):
            working_oomp.main(exact_part_ids=selection, make_files=False)
