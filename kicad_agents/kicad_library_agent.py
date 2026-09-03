"""Build per-part assets and installable OOMP libraries from official masters.

Uses only local files. Missing or conflicting masters are recorded for review;
hand-solder pads are never synthesized by scaling a machine-solder footprint.
"""

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import yaml

from kicad_agents import kicad_sexpr as sx
from working_oomp_populate_kicad import add_kicad_details


def write_changed(path, content):
    path = Path(path)
    data = content.encode('utf-8') if isinstance(content, str) else content
    if not path.is_file() or path.read_bytes() != data:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def write_report(path, data):
    write_changed(Path(path).with_suffix('.json'), json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    write_changed(Path(path).with_suffix('.yaml'), yaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def retire_obsolete(output, old_files, new_files):
    """Archive previously generated assets no longer in the active manifest."""
    output = Path(output).resolve()
    for relative in sorted(set(old_files) - set(new_files)):
        target = (output / relative).resolve()
        if not target.is_relative_to(output):
            raise ValueError('Invalid path in previous generated-asset manifest')
        if target.is_file():
            payload = target.read_bytes()
            checksum = hashlib.sha256(payload).hexdigest()
            archive = output / 'previous_generated' / checksum / relative
            write_changed(archive, payload)
            target.unlink()


def find_kicad_root(configured=None):
    if configured or os.environ.get('OOMP_KICAD_ROOT'):
        candidates = [Path(configured or os.environ['OOMP_KICAD_ROOT'])]
    else:
        candidates = sorted(Path('C:/Program Files/KiCad').glob('*'),
                            key=lambda path: tuple(int(number) for number in re.findall(r'\d+', path.name)),
                            reverse=True)
    for candidate in candidates:
        if (candidate / 'share/kicad/symbols').is_dir() and (candidate / 'bin/python.exe').is_file():
            return candidate.resolve()
    raise FileNotFoundError('Official KiCad libraries not found; set OOMP_KICAD_ROOT to the KiCad installation directory.')


def rename_symbol(symbol, name):
    result = copy.deepcopy(symbol)
    result[1] = sx.q(name)
    for unit in sx.children(result, 'symbol'):
        suffix = re.search(r'_\d+_\d+$', str(unit[1]))
        if not suffix:
            raise ValueError(f'Unrecognised symbol unit name: {unit[1]}')
        unit[1] = sx.q(name.split(':')[-1] + suffix[0])
    return result


def symbol_signature(symbol):
    result = rename_symbol(symbol, 'comparison')
    # Placement fields, descriptive fields and footprint choices are instance
    # metadata. Pins, graphics, units and electrical flags must match exactly.
    result = [item for item in result if sx.tag(item) not in ['property', 'uuid', 'extends']]
    return sx.canonical(result)


class Masters:
    def __init__(self, root=None):
        self.root = find_kicad_root(root)
        self.symbols = {}
        self.symbol_signatures = {}

    def prepare_symbol_signatures(self, symbols):
        """Let KiCad itself normalise old syntax, implicit defaults and '~' names.

        This is a format upgrade of temporary copies, not a library update:
        changed pins or graphics remain changed and still fail comparison.
        """
        pending = {}
        for symbol in symbols:
            key = hashlib.sha256(sx.dumps(symbol).encode()).hexdigest()
            if key not in self.symbol_signatures:
                pending[key] = symbol
        if not pending:
            return
        library = sx.parse('(kicad_symbol_lib (version 20211014) (generator "oomp"))')
        keys = list(pending)
        for index, key in enumerate(keys):
            library.append(rename_symbol(pending[key], f'OompCompare{index}'))
        with tempfile.TemporaryDirectory(prefix='oomp_kicad_compare_') as temporary:
            source = Path(temporary) / 'input.kicad_sym'
            output = Path(temporary) / 'upgraded.kicad_sym'
            source.write_text(sx.document(library), encoding='utf-8')
            result = subprocess.run([str(self.root / 'bin/kicad-cli.exe'), 'sym', 'upgrade', '--force',
                                     '--output', str(output), str(source)], capture_output=True, text=True, timeout=120)
            if result.returncode or not output.is_file():
                raise RuntimeError('KiCad symbol comparison format upgrade failed: ' + result.stderr)
            upgraded = sx.parse(output.read_text(encoding='utf-8'))
        for node in sx.children(upgraded, 'symbol'):
            index = int(str(node[1]).replace('OompCompare', ''))
            self.symbol_signatures[keys[index]] = symbol_signature(node)

    def symbol_signature(self, symbol):
        self.prepare_symbol_signatures([symbol])
        return self.symbol_signatures[hashlib.sha256(sx.dumps(symbol).encode()).hexdigest()]

    def footprint_path(self, library_id):
        if ':' not in library_id:
            return None
        library, entry = library_id.split(':', 1)
        if any(char in library + entry for char in ['/','\\']) or '..' in library + entry:
            return None
        path = self.root / 'share/kicad/footprints' / f'{library}.pretty' / f'{entry}.kicad_mod'
        return path if path.is_file() else None

    def symbol(self, library_id, trail=None):
        if ':' not in library_id:
            raise KeyError(library_id)
        library, entry = library_id.split(':', 1)
        if any(char in library + entry for char in ['/','\\']) or '..' in library + entry:
            raise KeyError(library_id)
        if library not in self.symbols:
            path = self.root / 'share/kicad/symbols' / f'{library}.kicad_sym'
            if not path.is_file():
                raise KeyError(library_id)
            parsed = sx.parse(path.read_text(encoding='utf-8'))
            self.symbols[library] = {str(item[1]): item for item in sx.children(parsed, 'symbol')}
        if entry not in self.symbols[library]:
            raise KeyError(library_id)
        node = copy.deepcopy(self.symbols[library][entry])
        parent_name = sx.value(node, 'extends')
        if not parent_name:
            return node
        trail = list(trail or [])
        if library_id in trail:
            raise ValueError(f'Circular symbol inheritance: {library_id}')
        parent = self.symbol(f'{library}:{parent_name}', trail + [library_id])
        parent = rename_symbol(parent, entry)
        for item in node[2:]:
            name = sx.tag(item)
            if name == 'extends':
                continue
            if name in ['property', 'symbol']:
                identity = str(item[1])
                parent = [old for old in parent if not (sx.tag(old) == name and str(old[1]) == identity)]
            else:
                parent = [old for old in parent if sx.tag(old) != name]
            parent.append(copy.deepcopy(item))
        return parent

    def hand_solder(self, machine_id):
        path = self.footprint_path(machine_id)
        if path is None:
            return ''
        if 'HandSolder' in path.stem:
            return machine_id
        matches = sorted(path.parent.glob(path.stem + '_*HandSolder*.kicad_mod'))
        if len(matches) == 1:
            return machine_id.split(':')[0] + ':' + matches[0].stem
        return ''


def project_candidates(parts_directory):
    """Read approved component-to-OOMP matches; never turn unmatched items into parts."""
    candidates = {}
    for project in sorted(Path(parts_directory).glob('oomp_project_*/data/generated_data/project.json')):
        data = json.loads(project.read_text(encoding='utf-8'))
        for component in data.get('components', []):
            match = component.get('oomp', {})
            if match.get('status') != 'matched':
                continue
            record = candidates.setdefault(match['oomp_id'], {'symbols': [], 'footprints': []})
            library_id = (component.get('pcb') or {}).get('library_id', '')
            if library_id and library_id not in record['footprints']:
                record['footprints'].append(library_id)
            for unit in (component.get('schematic') or {}).get('units', []):
                library_id = unit.get('library_id', '')
                if library_id and library_id not in record['symbols']:
                    record['symbols'].append(library_id)
    return candidates


def select_sources(part, masters, candidates):
    add_kicad_details(part)
    selections = copy.deepcopy(part['kicad'])
    issues = []
    for field, candidate_key in [['symbol', 'symbols'], ['machine_solder', 'footprints']]:
        if selections.get(field):
            continue
        available = []
        for candidate in candidates.get(candidate_key, []):
            try:
                exists = masters.symbol(candidate) if field == 'symbol' else masters.footprint_path(candidate)
            except KeyError:
                exists = None
            if exists is not None and candidate not in available:
                available.append(candidate)
        if len(available) == 1:
            selections[field] = available[0]
        elif len(available) > 1:
            issues.append(f'Conflicting {field} masters: {", ".join(available)}. Define kicad.{field} in populate-extra.')
    machine = selections.get('machine_solder', '')
    if machine and 'HandSolder' in machine:
        selections['hand_solder'] = selections.get('hand_solder') or machine
        selections['machine_solder'] = ''
        issues.append('Only a hand-solder source is known; no machine-solder geometry guessed.')
    if not selections.get('hand_solder'):
        selections['hand_solder'] = masters.hand_solder(selections.get('machine_solder', ''))
    return selections, issues


def footprint_with_identity(source, part_id, mark, display_name):
    root = copy.deepcopy(source)
    root[1] = sx.q(part_id)
    for item in sx.children(root, 'property'):
        if item[1] == 'Value':
            item[2] = sx.q(part_id)
    # A conservative beside-the-body label. Include pad extents and all
    # drawing vertices so the code clears copper and the existing outline.
    min_y = 0.0
    def visit(node):
        nonlocal min_y
        for item in node:
            if not isinstance(item, list):
                continue
            if sx.tag(item) in ['start', 'end', 'center', 'xy'] and len(item) >= 3:
                min_y = min(min_y, float(item[2]))
            if sx.tag(item) == 'pad':
                position = sx.child(item, 'at')
                size = sx.child(item, 'size')
                if position and size:
                    # max size is conservative even for rotated pads.
                    min_y = min(min_y, float(position[2]) - max(float(size[1]), float(size[2])) / 2)
            if sx.tag(item) in ['property', 'fp_text'] and sx.value(item, 'layer') == 'F.SilkS':
                position = sx.child(item, 'at')
                effects = sx.child(item, 'effects')
                font = sx.child(effects, 'font') if effects else None
                size = sx.child(font, 'size') if font else None
                if position and size and sx.value(item, 'hide') != 'yes' and 'hide' not in item:
                    min_y = min(min_y, float(position[2]) - float(size[2]) / 2)
            if sx.tag(item) != 'model':
                visit(item)
    visit(root)
    mark_y = round(min_y - 1.5, 4)
    root.append(sx.parse(
        f'(fp_text user "{mark}" (at 0 {mark_y}) (layer "F.SilkS") '
        '(effects (font (size 0.8 0.8) (thickness 0.12))))'
    ))
    return root, mark_y


def build_part(part_directory, masters=None, candidates=None):
    directory = Path(part_directory).resolve()
    part_id = directory.name
    part = yaml.safe_load((directory / 'working.yaml').read_text(encoding='utf-8'))
    if part.get('taxonomy_1') not in ['electronic', 'mechanical']:
        return None
    masters = masters or Masters()
    if candidates is None:
        candidates = project_candidates(directory.parent)
    selections, issues = select_sources(part, masters, candidates.get(part_id, {}))
    output = directory / 'data/kicad'
    old_manifest_path = output / 'manifest.json'
    old_manifest = json.loads(old_manifest_path.read_text()) if old_manifest_path.is_file() else {'assets': []}
    assets = []
    mark = str(part.get('md5_6_alpha_upper', part.get('md5_6_alpha', ''))).upper()
    if not re.fullmatch(r'[A-Z0-9]{1,6}', mark):
        raise ValueError(f'{part_id}: missing existing MD5 alpha identifier')
    symbol_id = selections.get('symbol', '')
    try:
        symbol = masters.symbol(symbol_id)
        renamed = rename_symbol(symbol, part_id)
        for prop in sx.children(renamed, 'property'):
            if prop[1] == 'Value':
                prop[2] = sx.q(part.get('name_readable', part_id))
            if prop[1] == 'Footprint':
                if masters.footprint_path(selections.get('machine_solder', '')):
                    prop[2] = sx.q(f'OOMP_MachineSolder:{part_id}')
                elif masters.footprint_path(selections.get('hand_solder', '')):
                    prop[2] = sx.q(f'OOMP_HandSolder:{part_id}')
                else:
                    prop[2] = sx.q('')
            if prop[1] == 'ki_fp_filters':
                prop[2] = sx.q(f'OOMP*:{part_id}')
        symbol_root = sx.parse('(kicad_symbol_lib (version 20241209) (generator "oomp"))')
        symbol_root.append(renamed)
        filename = f'{part_id}.kicad_sym'
        write_changed(output / filename, sx.document(symbol_root))
        assets.append({'kind': 'symbol', 'source': symbol_id, 'file': filename,
                       'source_sha256': hashlib.sha256(sx.dumps(symbol).encode()).hexdigest()})
    except KeyError:
        issues.append(f'Official symbol master unavailable: {symbol_id or "not selected"}')
    for variant in ['machine_solder', 'hand_solder']:
        (output / variant).mkdir(parents=True, exist_ok=True)
        source_id = selections.get(variant, '')
        source_path = masters.footprint_path(source_id)
        if source_path is None:
            issues.append(f'Official {variant} footprint unavailable: {source_id or "not selected"}')
            write_changed(output / variant / 'README.md', f'# {variant.replace("_", " ").title()}\n\nNo verified official master is available. See [../manifest.yaml](../manifest.yaml). No pad geometry has been guessed.\n')
            continue
        source = sx.parse(source_path.read_text(encoding='utf-8'))
        footprint, mark_y = footprint_with_identity(source, part_id, mark, part.get('name_readable', part_id))
        filename = f'{variant}/{part_id}.kicad_mod'
        write_changed(output / filename, sx.document(footprint))
        write_changed(output / variant / 'README.md', f'# {variant.replace("_", " ").title()}\n\n[{part_id}]({part_id}.kicad_mod)\n\nSource: `{source_id}`. [License](../LICENSE.md).\n')
        assets.append({'kind': variant, 'source': source_id, 'file': filename,
                       'source_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
                       'mark': mark, 'mark_y_mm': mark_y})
    manifest = {'format_version': 1, 'oomp_id': part_id, 'master_installation': str(masters.root),
                'status': 'complete' if len(assets) == 3 else 'needs_review',
                'assets': assets, 'issues': issues,
                'license': 'Derived from KiCad official libraries; see https://www.kicad.org/libraries/license/'}
    for asset in assets:
        asset['sha256'] = hashlib.sha256((output / asset['file']).read_bytes()).hexdigest()
    retire_obsolete(output, [item['file'] for item in old_manifest['assets']], [item['file'] for item in assets])
    write_report(output / 'manifest', manifest)
    write_changed(output / 'LICENSE.md', (ROOT / 'source_file/kicad_library/LICENSE.md').read_bytes())
    links = []
    for asset in assets:
        links.append(f"- [{asset['kind'].replace('_', ' ').title()}]({asset['file']}) — `{asset['source']}`")
    review = '\n'.join('- ' + issue for issue in issues) or 'All three assets are available.'
    write_changed(output / 'README.md', f'# KiCad assets: {part_id}\n\n' + '\n'.join(links)
                  + f'\n\n## Review\n\n{review}\n\nSilkscreen code: `{mark}`. Source provenance: [manifest](manifest.yaml).\n'
                  + '\nDerived from the [official KiCad libraries](https://www.kicad.org/libraries/license/).\n')
    return manifest


def package_libraries(parts_directory, output_directory, part_ids=None):
    parts_directory = Path(parts_directory)
    output = Path(output_directory)
    old_manifest_path = output / 'manifest.json'
    old_manifest = json.loads(old_manifest_path.read_text()) if old_manifest_path.is_file() else {'entries': []}
    entries = []
    symbols = sx.parse('(kicad_symbol_lib (version 20241209) (generator "oomp"))')
    review = []
    for manifest_path in sorted(parts_directory.glob('*/data/kicad/manifest.json')):
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        part_id = manifest['oomp_id']
        if part_ids is not None and part_id not in part_ids:
            continue
        review.append({'oomp_id': part_id, 'status': manifest['status'], 'issues': manifest['issues']})
        for asset in manifest['assets']:
            source = manifest_path.parent / asset['file']
            if asset['kind'] == 'symbol':
                symbols.extend(sx.children(sx.parse(source.read_text(encoding='utf-8')), 'symbol'))
                entries.append({'oomp_id': part_id, 'kind': 'symbol', 'file': 'OOMP.kicad_sym'})
            else:
                library = 'OOMP_MachineSolder' if asset['kind'] == 'machine_solder' else 'OOMP_HandSolder'
                destination = f'{library}.pretty/{part_id}.kicad_mod'
                write_changed(output / destination, source.read_bytes())
                entries.append({'oomp_id': part_id, 'kind': asset['kind'], 'file': destination})
    write_changed(output / 'OOMP.kicad_sym', sx.document(symbols))
    for name in ['OOMP_MachineSolder', 'OOMP_HandSolder']:
        (output / f'{name}.pretty').mkdir(parents=True, exist_ok=True)
    write_changed(output / 'sym-lib-table', '(sym_lib_table (version 7)\n (lib (name "OOMP")(type "KiCad")(uri "${KIPRJMOD}/OOMP.kicad_sym")(options "")(descr "OOMP symbols"))\n)\n')
    table = '(fp_lib_table (version 7)\n'
    for name in ['OOMP_MachineSolder', 'OOMP_HandSolder']:
        table += f' (lib (name "{name}")(type "KiCad")(uri "${{KIPRJMOD}}/{name}.pretty")(options "")(descr "OOMP footprints"))\n'
    write_changed(output / 'fp-lib-table', table + ')\n')
    retire_obsolete(output, [item['file'] for item in old_manifest['entries']], [item['file'] for item in entries] + ['OOMP.kicad_sym'])
    write_report(output / 'manifest', {'entries': entries, 'parts': review})
    write_changed(output / 'LICENSE.md', (ROOT / 'source_file/kicad_library/LICENSE.md').read_bytes())
    review_lines = ['# KiCad assets needing review', '',
                    'These entries are incomplete. No missing footprint geometry or symbol pinout was guessed.', '',
                    '| OOMP part | Missing assets / reason |', '| --- | --- |']
    for row in review:
        if row['status'] != 'complete':
            part_id = row['oomp_id']
            link = f'https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts/{part_id}'
            reason = '; '.join(row['issues']).replace('|', '\\|')
            review_lines.append(f'| [{part_id}]({link}) | {reason} |')
    write_changed(output / 'NEEDS_REVIEW.md', '\n'.join(review_lines) + '\n')
    write_changed(output / 'README.md', '# OOMP KiCad libraries\n\n'
                  'In KiCad **Preferences → Manage Symbol Libraries**, add `OOMP.kicad_sym` as **OOMP**. '
                  'In **Manage Footprint Libraries**, add `OOMP_MachineSolder.pretty` and '
                  '`OOMP_HandSolder.pretty` using those exact nicknames.\n\n'
                  'For a portable project, place these files beside its `.kicad_pro` and use the included '
                  '`sym-lib-table` / `fp-lib-table`. Merge entries if tables already exist; do not overwrite them.\n\n'
                  'Missing assets are listed in [NEEDS_REVIEW.md](NEEDS_REVIEW.md) and [manifest.yaml](manifest.yaml); pads are never guessed. '
                  'Individual part sources live in `parts/<oomp_id>/data/kicad/`.\n\n'
                  'These derivatives retain the official KiCad library licensing, including its design exception. '
                  'See the [KiCad library license](https://www.kicad.org/libraries/license/). '
                  'Master source identifiers and checksums are recorded per part.\n')
    return {'parts': len(review), 'assets': len(entries), 'needs_review': sum(row['status'] != 'complete' for row in review)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--part', type=Path)
    parser.add_argument('--parts', type=Path, default=ROOT / 'parts')
    parser.add_argument('--output', type=Path, default=ROOT / 'kicad_libraries')
    parser.add_argument('--package-only', action='store_true')
    parser.add_argument('--kwargs', help='Roboclick action JSON')
    args = parser.parse_args()
    if args.kwargs:
        details = json.loads(args.kwargs)
        args.part = Path(details['directory'])
    if args.part:
        result = build_part(args.part)
        print(json.dumps(result, indent=2))
        return
    if not args.package_only:
        masters = Masters()
        candidates = project_candidates(args.parts)
        for directory in sorted(args.parts.iterdir()):
            if (directory / 'working.yaml').is_file():
                result = build_part(directory, masters, candidates)
                if result:
                    print(f"{directory.name}: {result['status']}", flush=True)
    print(package_libraries(args.parts, args.output))


if __name__ == '__main__':
    main()
