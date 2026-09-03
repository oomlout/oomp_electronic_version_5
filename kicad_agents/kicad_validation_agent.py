"""Reproducible KiCad netlist and PCB-invariant checks for an OOMP design copy."""

import argparse
import copy
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree

from kicad_agents import kicad_sexpr as sx
from kicad_agents.kicad_library_agent import Masters, write_report


def netlist_snapshot(path):
    root = ElementTree.parse(path).getroot()
    components = {}
    nets = {}
    for component in root.findall('./components/comp'):
        components[component.attrib['ref']] = (component.findtext('value'), component.findtext('tstamps'))
    for net in root.findall('./nets/net'):
        nets[net.attrib['name']] = sorted((node.attrib['ref'], node.attrib['pin']) for node in net.findall('node'))
    return components, nets


def pcb_invariants(source, output, report):
    """Assert all board fields except approved IDs/new text are unchanged."""
    before = sx.parse(source.read_text(encoding='utf-8'))
    after = sx.parse(output.read_text(encoding='utf-8'))
    source_footprints = {sx.value(fp, 'uuid', sx.value(fp, 'tstamp')): fp for fp in sx.children(before, 'footprint')}
    for fp in sx.children(after, 'footprint'):
        key = sx.value(fp, 'uuid', sx.value(fp, 'tstamp'))
        original = source_footprints[key]
        if fp[1] != original[1]:
            # Conversion appends precisely one silkscreen annotation, after
            # all untouched original fields; reject any other alterations.
            if len(fp) != len(original) + 1 or sx.tag(fp[-1]) != 'fp_text':
                raise AssertionError(f'Unexpected footprint changes: {key}')
            fp.pop()
            fp[1] = copy.deepcopy(original[1])
    if sx.canonical(before) != sx.canonical(after):
        raise AssertionError('PCB data changed beyond library IDs and new annotations')


def validate_design(project_directory, basename, masters=None):
    project_directory = Path(project_directory).resolve()
    data = project_directory / 'data'
    original = data / 'original'
    output = data / 'oomp_design'
    masters = masters or Masters()
    manifest = json.loads((original / 'manifest.json').read_text())
    report = json.loads((output / 'conversion_report.json').read_text())
    pcb_invariants(original / 'kicad_file.kicad_pcb', output / f'{basename}.kicad_pcb', report)
    snapshots = []
    with tempfile.TemporaryDirectory(prefix='oomp_kicad_validate_') as temporary:
        baseline = Path(temporary) / 'baseline'
        baseline.mkdir()
        for relative in manifest['files']:
            destination = baseline / relative
            if relative.startswith('kicad_file.'):
                destination = baseline / (basename + Path(relative).suffix)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original / relative, destination)
        for label, source in [('original', baseline / f'{basename}.kicad_sch'), ('oomp', output / f'{basename}.kicad_sch')]:
            netlist = Path(temporary) / f'{label}.net.xml'
            result = subprocess.run([str(masters.root / 'bin/kicad-cli.exe'), 'sch', 'export', 'netlist',
                                     '--format', 'kicadxml', '--output', str(netlist), str(source)],
                                    capture_output=True, text=True, timeout=180)
            if result.returncode or not netlist.is_file():
                raise RuntimeError(f'KiCad cannot export the {label} netlist: {result.stderr}')
            snapshots.append(netlist_snapshot(netlist))
    if snapshots[0] != snapshots[1]:
        raise AssertionError('OOMP schematic netlist differs from the original')
    result = {'status': 'passed', 'pcb_invariants': 'unchanged except approved IDs and added annotations',
              'netlist_components': len(snapshots[0][0]), 'netlist_nets': len(snapshots[0][1]),
              'netlist_comparison': 'component values/UUIDs and named-net pin memberships match exactly'}
    write_report(output / 'validation', result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project_directory', type=Path)
    parser.add_argument('--basename', required=True)
    args = parser.parse_args()
    print(validate_design(args.project_directory, args.basename))


if __name__ == '__main__':
    main()
