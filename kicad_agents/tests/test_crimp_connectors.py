"""Cable components must not acquire PCB geometry or lose compatibility links."""
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader

from kicad_agents import component_addition_agent as addition
from kicad_agents import kicad_library_agent as library
from working_oomp_populate_connector_crimp_data import PARTS, CONTACT_ID, HOUSING_ID

ROOT = Path(__file__).resolve().parents[2]


def record(row):
    return {'ledger_id': 'CRIMP_TEST', 'family': 'connector', 'package': 'header',
            'part_id': row['id'], 'exact_identity': True,
            'research': {'manufacturer': 'Harwin', 'manufacturer_part_number': row['mpn'],
                         'browser_sources': [row['product_url']], 'evidence_notes': ['Exact manufacturer pair']}}


def populated(row):
    return addition._load_populated_definition(record(row))


def test_repeated_enrichment_keeps_cable_parts_separate_from_pcb_headers():
    import working_oomp_populate_svg as svg
    import working_oomp_populate_kicad as kicad
    for row in PARTS:
        part = populated(row)
        for _ in range(2):
            svg.add_svg_details(part)
            kicad.add_kicad_details(part)
        assert 'header_dimensions_mm' not in part
        assert not part['kicad']['machine_solder'] and not part['kicad']['symbol']
        assert all('schematic' not in x['svg_name'] for x in part['svg_details'])
        assert part['dimension_reference']['manufacturer'] == 'Harwin'
    assert len(populated(PARTS[0])['pins']) == 1
    assert populated(PARTS[1])['pins'] == {}
    pcb = dict(taxonomy_1='electronic', taxonomy_2='connector', taxonomy_3='header',
               taxonomy_4='2_54_mm_pitch', taxonomy_5='through_hole', taxonomy_6='2_pin')
    svg.add_svg_details(pcb); kicad.add_kicad_details(pcb)
    assert pcb['header_dimensions_mm']['pin_pitch'] == 2.54
    assert 'PinHeader_1x02' in pcb['kicad']['machine_solder']


def test_nonpcb_manifest_needs_no_kicad_install_and_rejects_inconsistent_claims(tmp_path, monkeypatch):
    def forbidden():
        raise AssertionError('Cable items must not load installed PCB masters')
    monkeypatch.setattr(library, 'Masters', forbidden)
    path = tmp_path / HOUSING_ID; path.mkdir()
    part = populated(PARTS[1])
    target = path / 'working.yaml'
    target.write_text(yaml.safe_dump(part), encoding='utf-8')
    manifest = library.build_part(path)
    assert manifest['status'] == 'not_applicable' and manifest['assets'] == []
    assert not list(path.rglob('*.kicad_mod')) and not list(path.rglob('*.kicad_sym'))
    part['kicad']['machine_solder'] = 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical'
    target.write_text(yaml.safe_dump(part), encoding='utf-8')
    with pytest.raises(ValueError, match='cannot also select'):
        library.build_part(path)


def test_package_does_not_report_cable_items_as_missing_footprints(tmp_path):
    path = tmp_path / 'parts' / HOUSING_ID; path.mkdir(parents=True)
    (path/'working.yaml').write_text(yaml.safe_dump(populated(PARTS[1])), encoding='utf-8')
    library.build_part(path)
    result = library.package_libraries(tmp_path/'parts', tmp_path/'library')
    assert result == {'parts': 1, 'assets': 0, 'needs_review': 0}
    assert HOUSING_ID not in (tmp_path/'library/NEEDS_REVIEW.md').read_text(encoding='utf-8')


def test_reciprocal_links_and_empty_housing_are_rendered():
    import working_oomp
    import working_oomp_populate_svg
    env = Environment(loader=FileSystemLoader(str(ROOT/'source_file/template_jinja/oomp_category/template_jinja_markdown')))
    for row in PARTS:
        part = populated(row)
        part['name'] = row['id']
        working_oomp_populate_svg.add_svg_details(part)
        working_oomp.add_part_page_details(part)
        page = env.get_template('working.md.j2').render(p=part)
        for related in part['related_parts']:
            other = next(candidate for candidate in PARTS if candidate['id'] == related['oomp_id'])
            assert f"../{other['id']}/README.md" in page
            assert any(link['oomp_id'] == row['id'] for link in other['related_parts'])
            if row['role'] == 'cable_housing':
                assert related['quantity'] == row['positions']
        assert 'no PCB footprint' in page and 'Dimensioned envelope only' in page
        assert 'working_svg_square_schematic' not in page
        if row['role'] == 'cable_housing':
            assert '## Pins' not in page and 'contacts supplied separately' in page


def test_prepare_writes_only_selected_component(tmp_path, monkeypatch):
    source = tmp_path/'parts_source'; source.mkdir()
    sentinel = source/'unrelated.yaml'; sentinel.write_text('preserve', encoding='utf-8')
    monkeypatch.setattr(addition, 'REPOSITORY_ROOT', tmp_path)
    monkeypatch.setattr(addition, 'PARTS_SOURCE_DIRECTORY', source)
    before = Path.cwd()
    written = addition.prepare_component_source(record(PARTS[0]))
    assert Path.cwd() == before
    assert written.is_file()
    assert sentinel.read_text(encoding='utf-8') == 'preserve'
    assert {p.name for p in source.iterdir()} == {CONTACT_ID, 'unrelated.yaml'}


def test_dimensioned_views_never_use_pcb_header_geometry(monkeypatch):
    import working_svg as drawing
    def forbidden(*args, **kwargs):
        raise AssertionError('Cable item dispatched to PCB header dimension drawing')
    monkeypatch.setattr(drawing, '_add_header_dimensions', forbidden)
    monkeypatch.setattr(drawing, '_use_style_oomp', lambda *a, **k: None)
    monkeypatch.setattr(drawing, '_add_diagram_bounds', lambda *a, **k: None)
    monkeypatch.setattr(drawing, '_add_component_outline', lambda *a, **k: (20, 10))
    monkeypatch.setattr(drawing, '_add_component_dimensions', lambda *a, **k: None)
    notes = []
    monkeypatch.setattr(drawing, '_add_text', lambda part, text, *a, **k: notes.append(text))
    for row in PARTS:
        part = populated(row)
        drawing.get_oomp_component_dimensioned(part)
        drawing.get_oomp_component_dimensioned_titles(part)
    assert notes == ['Envelope only'] * (2 * len(PARTS))
    assert drawing._get_pin_labels(populated(PARTS[1])) == []


def test_filtered_navigation_preserves_siblings_and_unrelated_pages(tmp_path, monkeypatch):
    import action_generate_navigation as nav
    from oomp_populate_helper import build_oomp_id
    rows = [populated(row) for row in PARTS]
    rows.append(dict(taxonomy_1='electronic', taxonomy_2='resistor', taxonomy_3='0603', taxonomy_4='10000_ohm'))
    for part in rows:
        part['id'] = build_oomp_id(part)
        folder = tmp_path/'parts'/part['id']; folder.mkdir(parents=True)
        (folder/'working.yaml').write_text(yaml.safe_dump(part), encoding='utf-8')
    navigation = tmp_path/'navigation'
    untouched = navigation/'unrelated/README.md'; untouched.parent.mkdir(parents=True)
    untouched.write_text('preserve this page', encoding='utf-8')
    monkeypatch.setattr(nav, 'REPOSITORY_ROOT', tmp_path)
    monkeypatch.setattr(nav, 'NAVIGATION_ROOT', navigation)
    nav.generate(filter_text=[CONTACT_ID, HOUSING_ID])
    parent = (navigation/'electronic/connector/header/2_54_mm_pitch/README.md').read_text(encoding='utf-8')
    assert 'housing/README.md' in parent and 'crimp/README.md' in parent
    for row in PARTS[:2]:
        tokens = row['taxonomy']
        category = [tokens[f'taxonomy_{index}'] for index in range(2, 15)
                    if f'taxonomy_{index}' in tokens]
        assert row['id'] in navigation.joinpath('electronic', *category, 'README.md').read_text(encoding='utf-8')
    assert 'resistor/README.md' in (navigation/'electronic/README.md').read_text(encoding='utf-8')
    assert untouched.read_text(encoding='utf-8') == 'preserve this page'


def test_relationship_check_rejects_missing_targets_and_invalid_quantities(tmp_path, monkeypatch):
    item = record(PARTS[1]); item['datasheet_required'] = False
    monkeypatch.setattr(addition, 'PARTS_SOURCE_DIRECTORY', tmp_path)
    result = addition.validate_implementation(item)
    assert result['checks']['compatible_components'] == 'fail'
    for related in populated(PARTS[1])['related_parts']:
        target = tmp_path / related['oomp_id']
        target.mkdir()
        (target/'working.yaml').write_text('id: '+target.name, encoding='utf-8')
    assert addition.validate_implementation(item)['checks']['compatible_components'] == 'pass'
    data = populated(PARTS[1]); data['related_parts'][0]['quantity'] = 0
    monkeypatch.setattr(addition, '_load_populated_definition', lambda _: data)
    assert addition.validate_implementation(item)['checks']['compatible_components'] == 'fail'


def test_explorer_exposes_compatibility_and_connector_details():
    import importlib.util
    spec = importlib.util.spec_from_file_location('connector_display_test', ROOT/'webserver/services/electronics.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    details = module.component_details(populated(PARTS[1]))
    assert any(CONTACT_ID in item['url'] for item in details['links'])
    assert 'Connector details' in str(details)


def test_explicit_regeneration_bypasses_existing_preview_gate():
    import working_oomp
    for regenerate in (False, True):
        part = populated(PARTS[0])
        part['regenerate_pngs'] = regenerate
        working_oomp.add_part_build_actions(part, 0)
        mode = next(value for key, value in part.items()
                    if key.startswith('oomlout_ai_roboclick_')
                    and value['actions'][0].get('file_python') == 'kicad_agents/component_svg_action.py')
        assert bool(mode['file_test']) is not regenerate
        assert mode['actions'][0]['regenerate_pngs'] is regenerate
