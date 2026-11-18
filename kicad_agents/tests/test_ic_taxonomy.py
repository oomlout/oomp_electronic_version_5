"""IC identity and package semantics must survive future population/intake."""
import hashlib
import json
from pathlib import Path

import pytest

from component_identity import refresh_ic_identity
from component_taxonomy import package_token, validate_ic_taxonomy
from oomp_populate_helper import build_oomp_id as build_part_id


ROOT = Path(__file__).resolve().parents[2]


def test_all_ic_definitions_match_the_migration_and_keep_device_data():
    import working_oomp_populate_ic
    options = []
    working_oomp_populate_ic.main(options=options)
    rows = json.loads((ROOT / 'migrations/ic_package_last_ids.json').read_text())['renames']
    expected = {row['new']: row for row in rows}
    assert len(options) == len(expected) == 600
    actual = set()
    for option in options:
        part = dict(option, taxonomy_1='electronic')
        validate_ic_taxonomy(part)
        identifier = build_part_id(part)
        actual.add(identifier)
        row = expected[identifier]
        assert [part[f'taxonomy_{n}'] for n in (3, 4, 5)] == [row['function'], row['subtype'], row['package']]
    assert actual == set(expected)


def test_package_first_and_fields_after_package_are_rejected():
    old = dict(taxonomy_1='electronic', taxonomy_2='ic', taxonomy_3='soic_8',
               taxonomy_4='amplifier', taxonomy_5='operational_dual')
    with pytest.raises(ValueError, match='function'):
        validate_ic_taxonomy(old)
    current = dict(old, taxonomy_3='amplifier', taxonomy_4='operational_dual', taxonomy_5='soic_8')
    validate_ic_taxonomy(current)
    with pytest.raises(ValueError, match='last regular'):
        validate_ic_taxonomy(dict(current, taxonomy_6='extra'))
    assert package_token(current) == 'soic_8'
    assert package_token(dict(taxonomy_2='resistor', taxonomy_3='0603', taxonomy_5='1_percent')) == '0603'


def test_ingestion_rejects_retired_ic_identifiers():
    from kicad_agents.component_addition_agent import validate_record
    row = json.loads((ROOT / 'migrations/ic_package_last_ids.json').read_text())['renames'][0]
    result = validate_record({'family': 'ic', 'part_id': row['old']})
    assert 'package-first IDs are retired' in str(result)
    result = validate_record({'family': 'ic', 'part_id': row['new']})
    assert 'package-first IDs are retired' not in str(result)


def test_category_link_does_not_confuse_function_and_subtype():
    from working_oomp_metadata import navigation_link_for_part
    part = dict(taxonomy_1='electronic', taxonomy_2='ic', taxonomy_3='logic',
                taxonomy_4='comparator', taxonomy_5='soic_8', taxonomy_15='lm393')
    assert navigation_link_for_part(part) == '../../navigation/electronic/ic/logic/comparator/soic_8/README.md'


def test_package_drawing_and_kicad_selection_use_level_five():
    import working_svg
    import working_oomp_populate_kicad
    part = dict(taxonomy_1='electronic', taxonomy_2='ic', taxonomy_3='amplifier',
                taxonomy_4='operational_dual', taxonomy_5='soic_8')
    assert working_svg._get_package_pin_count(part) == 8
    working_oomp_populate_kicad.add_kicad_details(part)
    assert 'SOIC-8' in part['kicad']['machine_solder']


def test_drawer_label_field_selection_without_font_rendering(monkeypatch):
    import working_drawer_labels as labels
    monkeypatch.setattr(labels, 'width', lambda text, size: 0)
    part = dict(id='electronic_ic_amplifier_operational_dual_soic_8_example',
                taxonomy_1='electronic', taxonomy_2='ic', taxonomy_3='amplifier',
                taxonomy_4='operational_dual', taxonomy_5='soic_8',
                part_number_manufacturer='EXAMPLE')
    content = labels.content(part)
    assert 'SOIC 8' in str(content)
    assert 'operational dual' in str(content).lower()


def test_population_recomputes_codes_from_canonical_id():
    import oomp
    row = json.loads((ROOT / 'migrations/ic_package_last_ids.json').read_text())['renames'][0]
    # Use a real current definition so manufacturer and MPN remain exact.
    import working_oomp_populate_ic
    options = []
    working_oomp_populate_ic.main(options=options)
    definition = next(p for p in options if build_part_id(dict(p, taxonomy_1='electronic')) == row['new'])
    part = oomp.add_part(**dict(definition, taxonomy_1='electronic', make_files=False))
    refresh_ic_identity(part)
    assert part['id'] == row['new']
    assert 'identity_seed' not in part
    assert part['md5'] == hashlib.md5(row['new'].encode()).hexdigest()
    assert oomp.parts_md5_6[part['md5_6']] == row['new']
    assert oomp.parts[row['new']]['md5'] == part['md5']
    part['identity_seed'] = row['old']
    part['md5'] = row['old_md5']
    refresh_ic_identity(part)
    assert part['md5'] == row['new_md5']
    assert 'identity_seed' not in part
