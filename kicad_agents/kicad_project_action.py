"""Always-run Roboclick action: preserve originals and create a guarded OOMP copy."""

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import uuid as uuid_module
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import yaml

from kicad_agents import kicad_sexpr as sx
from kicad_agents.kicad_library_agent import (
    Masters, build_part, package_libraries, project_candidates, rename_symbol,
    symbol_signature, write_changed, write_report,
)


def footprint_signature(node):
    """Ignore only enumerated placement/annotation fields, never pad geometry.

    Normalisation of rotation/mirroring/coordinates is delegated to KiCad itself.
    Unknown fields remain in the signature and therefore fail closed.
    """
    result = copy.deepcopy(node)
    result[1] = sx.q('comparison')
    root_ignore = ['at', 'path', 'sheetname', 'sheetfile', 'property', 'descr', 'tags',
                   'version', 'generator', 'generator_version', 'embedded_fonts']
    result = [item for item in result if sx.tag(item) not in root_ignore]
    if 'locked' in result:
        result.remove('locked')
    def clean(items):
        cleaned = []
        for item in items:
            if not isinstance(item, list):
                cleaned.append(item)
                continue
            name = sx.tag(item)
            if name in ['uuid', 'tstamp', 'net', 'pinfunction', 'pintype']:
                continue
            if name == 'attr':
                instance_flags = ['exclude_from_pos_files', 'exclude_from_bom', 'board_only', 'dnp']
                item = [token for token in item if token not in instance_flags]
            if name == 'fp_text' and len(item) > 2 and item[2] in ['${REFERENCE}', '${VALUE}']:
                # KiCad's keep-upright handling may turn these automatic
                # instance labels by 180 degrees when a footprint is flipped.
                # Still compare their position, font, layer and visibility.
                position = sx.child(item, 'at')
                if position and len(position) > 3:
                    position[3] = sx.Atom(str(float(position[3]) % 180))
            cleaned.append(clean(item))
        return cleaned
    return sx.canonical(clean(result))


def footprint_difference_fields(placed, master):
    grouped = []
    for footprint in [placed, master]:
        fields = {}
        for item in footprint_signature(footprint)[2]:
            field = item[1][0][1]
            fields.setdefault(field, []).append(repr(item))
        grouped.append(fields)
    return sorted(field for field in set(grouped[0]) | set(grouped[1]) if grouped[0].get(field) != grouped[1].get(field))


def source_files(data_directory):
    """Current input files, preserving hierarchical paths in the portable copy."""
    files = {}
    for extension in ['kicad_pcb', 'kicad_sch', 'kicad_pro']:
        source = data_directory / f'kicad_file.{extension}'
        if source.is_file():
            files[source.name] = source
    sheet_directory = data_directory / 'kicad_file_sheets'
    if sheet_directory.is_dir():
        for source in sorted(sheet_directory.rglob('*.kicad_sch')):
            relative = source.relative_to(sheet_directory).as_posix()
            if relative in files:
                raise ValueError(f'Conflicting root/child schematic: {relative}')
            files[relative] = source
    for table_name in ['sym-lib-table', 'fp-lib-table']:
        source = data_directory / table_name
        if source.is_file():
            files[table_name] = source
    return files


def preserve_originals(data_directory):
    """Never overwrite an edited snapshot; retain previous revisions by hash."""
    files = source_files(data_directory)
    original = data_directory / 'original'
    manifest_path = original / 'manifest.json'
    previous = json.loads(manifest_path.read_text()) if manifest_path.is_file() else {'files': {}}
    records = {}
    for relative, source in files.items():
        payload = source.read_bytes()
        checksum = hashlib.sha256(payload).hexdigest()
        destination = original / relative
        if destination.is_file() and destination.read_bytes() != payload:
            old_bytes = destination.read_bytes()
            old_hash = hashlib.sha256(old_bytes).hexdigest()
            if previous['files'].get(relative, {}).get('sha256') != old_hash:
                raise RuntimeError(f'Original snapshot was edited; refusing to overwrite {destination}')
            write_changed(original / 'revisions' / old_hash / relative, old_bytes)
        write_changed(destination, payload)
        records[relative] = {'sha256': checksum, 'source': str(source)}
    write_report(original / 'manifest', {'files': records})
    return files, records


def references(symbol, project_uuid=''):
    result = []
    reference = sx.property_value(symbol, 'Reference')
    for instance in sx.children(symbol, 'instances'):
        for project in sx.children(instance, 'project'):
            for path in sx.children(project, 'path'):
                if project_uuid and not str(path[1]).startswith(f'/{project_uuid}'):
                    continue
                reference = sx.value(path, 'reference')
                if reference and '?' not in reference and reference not in result:
                    result.append(reference)
    if not result:
        reference = sx.property_value(symbol, 'Reference')
        if reference:
            result.append(reference)
    return result


def convert_schematic(root, parts_by_reference, manifests, parts_directory, masters, converted_footprints, project_uuid=''):
    library = sx.child(root, 'lib_symbols')
    rows = []
    if library is None:
        return rows
    embedded = {str(item[1]): item for item in sx.children(library, 'symbol')}
    comparison_symbols = []
    for library_id, symbol in embedded.items():
        try:
            master = masters.symbol(library_id)
        except KeyError:
            continue
        comparison_symbols.extend([symbol, master])
    for manifest in manifests.values():
        for asset in manifest['assets']:
            if asset['kind'] == 'symbol':
                comparison_symbols.append(masters.symbol(asset['source']))
    masters.prepare_symbol_signatures(comparison_symbols)
    additions = {}
    for symbol in sx.children(root, 'symbol'):
        refs = references(symbol, project_uuid)
        part_ids = []
        for reference in refs:
            part_id = parts_by_reference.get(reference)
            if part_id and part_id not in part_ids:
                part_ids.append(part_id)
        row = {'references': refs, 'source': sx.value(symbol, 'lib_id'), 'status': 'skipped'}
        rows.append(row)
        if len(part_ids) != 1 or any(reference not in parts_by_reference for reference in refs):
            row['reason'] = 'No single approved OOMP part for every instance of this symbol.'
            continue
        part_id = part_ids[0]
        row['oomp_id'] = part_id
        asset = next((item for item in manifests[part_id]['assets'] if item['kind'] == 'symbol'), None)
        if not asset:
            row['reason'] = 'OOMP symbol master unavailable.'
            continue
        try:
            master = masters.symbol(row['source'])
            target_master = masters.symbol(asset['source'])
        except KeyError:
            row['reason'] = 'Source is not a known official KiCad symbol.'
            continue
        current = embedded.get(row['source'])
        if current is None or masters.symbol_signature(current) != masters.symbol_signature(master):
            row['reason'] = 'Embedded symbol differs from the installed KiCad master.'
            continue
        if masters.symbol_signature(master) != masters.symbol_signature(target_master):
            row['reason'] = 'OOMP canonical symbol differs in graphics, pins or units.'
            continue
        target_id = f'OOMP:{part_id}'
        asset_path = parts_directory / part_id / 'data/kicad' / asset['file']
        target_symbol = sx.children(sx.parse(asset_path.read_text(encoding='utf-8')), 'symbol')[0]
        additions[target_id] = rename_symbol(target_symbol, target_id)
        sx.child(symbol, 'lib_id')[1] = sx.q(target_id)
        # Update this field only when every instance's PCB was also verified
        # and they all retain the same soldering variant.
        footprint_ids = [converted_footprints.get(reference) for reference in refs]
        if footprint_ids and all(item and item == footprint_ids[0] for item in footprint_ids):
            for prop in sx.children(symbol, 'property'):
                if prop[1] == 'Footprint':
                    prop[2] = sx.q(footprint_ids[0])
        row['status'] = 'converted'
        row['target'] = target_id
    library.extend(additions.values())
    return rows


def add_local_libraries(table, table_kind):
    """Keep existing custom library tables; reject nickname collisions."""
    names = ['OOMP'] if table_kind == 'sym_lib_table' else ['OOMP_MachineSolder', 'OOMP_HandSolder']
    for name in names:
        extension = '.kicad_sym' if name == 'OOMP' else '.pretty'
        uri = f'${{KIPRJMOD}}/libraries/{name}{extension}'
        existing = [node for node in sx.children(table, 'lib') if sx.value(node, 'name') == name]
        if existing:
            if sx.value(existing[0], 'uri') != uri:
                raise RuntimeError(f'Existing library nickname {name} points elsewhere; manual merge required.')
        else:
            table.append(sx.parse(f'(lib (name "{name}")(type "KiCad")(uri "{uri}")(options "")(descr "OOMP local library"))'))
    return table


def convert_project(details):
    directory = Path(details['directory']).resolve()
    data_directory = directory / 'data'
    parts_directory = Path(details.get('parts_directory', ROOT / 'parts')).resolve()
    masters = Masters(details.get('kicad_root'))
    files, originals = preserve_originals(data_directory)
    # Re-extract current inputs, not a previously generated OOMP design.
    from kicad_agents.kicad_processing_agent import process_project
    output_data = data_directory / 'generated_data'
    output_data.mkdir(parents=True, exist_ok=True)
    if isinstance(details.get('project_match_overrides'), dict):
        write_changed(output_data / 'match_overrides.yaml', yaml.safe_dump({'matches': details['project_match_overrides']}))
    project, _ = process_project(directory, parts_directory, output_directory=output_data)
    parts_by_reference = {}
    for component in project['components']:
        match = component.get('oomp', {})
        if match.get('status') == 'matched':
            parts_by_reference[component['reference']] = match['oomp_id']
    candidates = project_candidates(parts_directory)
    manifests = {}
    for part_id in sorted(set(parts_by_reference.values())):
        manifests[part_id] = build_part(parts_directory / part_id, masters, candidates)
    board_file = files.get('kicad_file.kicad_pcb')
    if board_file is None:
        raise FileNotFoundError('No source PCB for OOMP conversion')
    board = sx.parse(board_file.read_text(encoding='utf-8'))
    master_paths = {}
    marks = {}
    eligible = {}
    rows = []
    for footprint in sx.children(board, 'footprint'):
        reference = sx.property_value(footprint, 'Reference')
        if not reference:
            for text in sx.children(footprint, 'fp_text'):
                if text[1] == 'reference':
                    reference = str(text[2])
        source_id = str(footprint[1])
        row = {'reference': reference, 'source': source_id, 'status': 'skipped'}
        rows.append(row)
        part_id = parts_by_reference.get(reference)
        if not part_id:
            row['reason'] = 'No approved OOMP match.'
            continue
        row['oomp_id'] = part_id
        asset = next((item for item in manifests[part_id]['assets'] if item['kind'] != 'symbol' and item['source'] == source_id), None)
        master = masters.footprint_path(source_id)
        if asset is None or master is None:
            row['reason'] = 'Source is not an available official master for this OOMP part.'
            continue
        uuid = sx.value(footprint, 'uuid', sx.value(footprint, 'tstamp'))
        if not uuid:
            row['reason'] = 'Missing footprint UUID.'
            continue
        master_paths[source_id] = str(master)
        marks[uuid] = {'text': asset['mark'], 'y': asset['mark_y_mm']}
        eligible[uuid] = (footprint, asset, row)
    request = {'board': str(board_file), 'masters': master_paths, 'marks': marks}
    completed = subprocess.run(
        [str(masters.root / 'bin/python.exe'), str(ROOT / 'kicad_agents/kicad_pcb_compare.py')],
        input=json.dumps(request), text=True, encoding='utf-8', capture_output=True, timeout=180,
    )
    if completed.returncode:
        raise RuntimeError('KiCad comparison failed; no converted design written:\n' + completed.stderr)
    compared = json.loads(completed.stdout)
    converted_footprints = {}
    for uuid, (footprint, asset, row) in eligible.items():
        placed = compared['footprints'].get(uuid)
        master = compared['masters'][row['source']]
        if not placed or footprint_signature(sx.parse(placed['normalised'])) != footprint_signature(sx.parse(master)):
            row['reason'] = 'Footprint differs from the installed master; geometry/overrides left untouched.'
            if placed:
                row['differing_fields'] = footprint_difference_fields(sx.parse(placed['normalised']), sx.parse(master))
            continue
        library = 'OOMP_MachineSolder' if asset['kind'] == 'machine_solder' else 'OOMP_HandSolder'
        target_id = f"{library}:{row['oomp_id']}"
        footprint[1] = sx.q(target_id)
        # Copy only the added annotation. All original pads/nets/UUIDs and
        # project placement stay exactly as they were in the input expression.
        mark_node = sx.parse(placed['mark'])
        mark_uuid = sx.child(mark_node, 'uuid')
        if mark_uuid is not None:
            mark_uuid[1] = sx.q(str(uuid_module.uuid5(uuid_module.NAMESPACE_URL, 'oomp:' + uuid + ':' + asset['mark'])))
        footprint.append(mark_node)
        row.update(status='converted', target=target_id)
        converted_footprints[row['reference']] = target_id
    # Retain the upstream project basename in the editable copy: KiCad's
    # schematic instance records are keyed by this project name.
    basename = str(details.get('project_file_basename') or 'kicad_file')
    if Path(basename).name != basename or basename in ['.', '..']:
        raise ValueError('Invalid project_file_basename')
    project_uuid = sx.value(sx.parse(files['kicad_file.kicad_sch'].read_text(encoding='utf-8')), 'uuid')
    outputs = {f'{basename}.kicad_pcb': sx.document(board)}
    schematic_rows = []
    for relative, source in files.items():
        if source.suffix == '.kicad_sch':
            root = sx.parse(source.read_text(encoding='utf-8'))
            changes = convert_schematic(root, parts_by_reference, manifests, parts_directory, masters, converted_footprints, project_uuid)
            for row in changes:
                row['file'] = relative
            schematic_rows.extend(changes)
            destination = f'{basename}.kicad_sch' if relative == 'kicad_file.kicad_sch' else relative
            outputs[destination] = sx.document(root)
        elif source.suffix == '.kicad_pro':
            outputs[f'{basename}.kicad_pro'] = source.read_bytes()
    output_directory = data_directory / 'oomp_design'
    previous_path = output_directory / 'conversion_report.json'
    previous = json.loads(previous_path.read_text()) if previous_path.is_file() else {}
    for relative in outputs:
        target = output_directory / relative
        if target.is_file():
            saved_hash = previous.get('output_sha256', {}).get(relative)
            if saved_hash != hashlib.sha256(target.read_bytes()).hexdigest():
                raise RuntimeError(f'Generated design was edited; refusing to overwrite {target}')
    for table_file, table_kind in [['sym-lib-table', 'sym_lib_table'], ['fp-lib-table', 'fp_lib_table']]:
        source = files.get(table_file)
        root = sx.parse(source.read_text(encoding='utf-8')) if source else sx.parse(f'({table_kind} (version 7))')
        target = output_directory / table_file
        if target.is_file():
            old_hash = previous.get('output_sha256', {}).get(table_file)
            if old_hash != hashlib.sha256(target.read_bytes()).hexdigest():
                raise RuntimeError(f'Library table was edited; refusing to overwrite {target}')
        outputs[table_file] = sx.document(add_local_libraries(root, table_kind))
    package_libraries(parts_directory, output_directory / 'libraries', set(manifests))
    hashes = {}
    for relative, content in outputs.items():
        write_changed(output_directory / relative, content)
        hashes[relative] = hashlib.sha256((output_directory / relative).read_bytes()).hexdigest()
    for relative, checksum in previous.get('output_sha256', {}).items():
        old_file = (output_directory / relative).resolve()
        if relative not in outputs and old_file.is_file():
            if not old_file.is_relative_to(output_directory.resolve()):
                raise RuntimeError('Invalid old generated-file path in conversion report')
            if hashlib.sha256(old_file.read_bytes()).hexdigest() != checksum:
                raise RuntimeError(f'Obsolete generated file was edited; refusing to move {old_file}')
            archive = output_directory / 'previous_generated' / checksum / relative
            write_changed(archive, old_file.read_bytes())
            old_file.unlink()
    report = {'format_version': 1, 'kicad_version': compared['kicad_version'],
              'originals': originals, 'output_sha256': hashes,
              'summary': {'footprints_converted': sum(row['status'] == 'converted' for row in rows),
                          'footprints_skipped': sum(row['status'] != 'converted' for row in rows),
                          'symbols_converted': sum(row['status'] == 'converted' for row in schematic_rows),
                          'symbols_skipped': sum(row['status'] != 'converted' for row in schematic_rows)},
              'footprints': rows, 'symbols': schematic_rows}
    write_report(output_directory / 'conversion_report', report)
    from kicad_agents.kicad_validation_agent import validate_design
    try:
        report['validation'] = validate_design(directory, basename, masters)
    except Exception as error:
        report['validation'] = {'status': 'failed', 'error': str(error)}
        write_report(output_directory / 'conversion_report', report)
        write_report(output_directory / 'validation', report['validation'])
        raise
    write_report(output_directory / 'conversion_report', report)
    write_changed(output_directory / 'README.md', '# OOMP KiCad design copy\n\n'
                  f'Open `{basename}.kicad_pro` (or the `.kicad_pcb` / `.kicad_sch`) in KiCad. '
                  'Local OOMP libraries are under `libraries/`. Original inputs are preserved in '
                  '[../original/](../original/).\n\n'
                  'Only verified unchanged installed KiCad defaults were renamed. Modified, custom, '
                  'unmatched and unavailable items remain unchanged. Soldering variants are never '
                  'swapped during conversion. Existing pad coordinates, nets and UUIDs are preserved.\n\n'
                  'See [conversion_report.yaml](conversion_report.yaml) for every conversion and skip. '
                  'Copy this directory before editing; regeneration refuses to overwrite edited design files.\n')
    print(json.dumps(report['summary'], indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kwargs', required=True)
    args = parser.parse_args()
    convert_project(json.loads(args.kwargs))


if __name__ == '__main__':
    main()
