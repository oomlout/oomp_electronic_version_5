import copy
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from kicad_agents import kicad_sexpr as sx
from kicad_agents.kicad_library_agent import Masters, build_part, find_kicad_root, package_libraries, symbol_signature
from kicad_agents.kicad_project_action import convert_project, footprint_signature, preserve_originals
from kicad_agents.kicad_processing_agent import _reference
from kicad_agents.project_git_action import referenced_sheets
from kicad_agents.kicad_library_agent import retire_obsolete


class KiCadExpressionTests(unittest.TestCase):
    def test_hierarchical_reference_uses_current_project_not_stale_placeholder(self):
        symbol = sx.parse('(symbol (property "Reference" "LED?") (instances (project "old" (path "/old-root/sheet" (reference "LED999"))) (project "current" (path "/current-root/sheet" (reference "LED710")))))')
        self.assertEqual(_reference(symbol, 'current-root'), 'LED710')

    def test_nested_sheets_follow_references_not_unrelated_files(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / 'nested').mkdir()
            root = base / 'root.kicad_sch'
            root.write_text('(kicad_sch (sheet (property "Sheetfile" "nested/child.kicad_sch")))')
            nested = base / 'nested/child.kicad_sch'
            nested.write_text('(kicad_sch)')
            (base / 'unrelated.kicad_sch').write_text('(kicad_sch)')
            self.assertEqual(referenced_sheets(root), [nested.resolve()])

    def test_removed_library_entries_are_archived_not_left_active(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            old = base / 'OOMP.pretty/old.kicad_mod'
            old.parent.mkdir()
            old.write_text('old generated entry')
            retire_obsolete(base, ['OOMP.pretty/old.kicad_mod'], [])
            self.assertFalse(old.exists())
            copies = list((base / 'previous_generated').glob('*/OOMP.pretty/old.kicad_mod'))
            self.assertEqual(len(copies), 1)
            self.assertEqual(copies[0].read_text(), 'old generated entry')

    def test_round_trip_preserves_quotes_parentheses_escapes_and_numbers(self):
        text = '(symbol "(test)" (property "Value" "1\\\" \\\\ abc") (pin "01" (at -1.000 0 90)))'
        root = sx.parse(text)
        self.assertEqual(sx.dumps(sx.parse(sx.dumps(root))), sx.dumps(root))
        self.assertTrue(root[1].quoted)
        self.assertEqual(root[1], '(test)')
        with self.assertRaises(ValueError):
            sx.parse('(symbol "unfinished)')

    def test_footprint_guard_keeps_geometry_and_overrides(self):
        base = sx.parse('(footprint "example" (at 1 2 30) (layer "F.Cu") (pad "1" smd rect (at 0 0) (size 1 2) (net 1 "a")))')
        changed = copy.deepcopy(base)
        sx.child(changed, 'at')[1:] = [sx.Atom('50'), sx.Atom('60'), sx.Atom('0')]
        sx.child(sx.child(changed, 'pad'), 'net')[1:] = [sx.Atom('2'), sx.q('different net')]
        self.assertEqual(footprint_signature(base), footprint_signature(changed))
        sx.child(sx.child(changed, 'pad'), 'size')[1] = sx.Atom('1.1')
        self.assertNotEqual(footprint_signature(base), footprint_signature(changed))
        for override in ['(clearance 0.2)', '(solder_mask_margin 0.1)', '(zone_connect 0)']:
            changed = copy.deepcopy(base)
            changed.append(sx.parse(override))
            self.assertNotEqual(footprint_signature(base), footprint_signature(changed))

    def test_originals_refuse_edited_snapshots_and_archive_source_revisions(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory)
            source = data / 'kicad_file.kicad_pcb'
            source.write_text('original')
            preserve_originals(data)
            source.write_text('upstream revision')
            preserve_originals(data)
            checksum = hashlib.sha256(b'original').hexdigest()
            self.assertEqual((data / 'original/revisions' / checksum / source.name).read_text(), 'original')
            (data / 'original' / source.name).write_text('user edit')
            with self.assertRaisesRegex(RuntimeError, 'was edited'):
                preserve_originals(data)


class InstalledKiCadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.masters = Masters()
        except FileNotFoundError as error:
            raise unittest.SkipTest(str(error))

    def test_symbol_inheritance_and_graphic_change_guard(self):
        # KiCad uses this exact inheritance chain for many resistor variants.
        library = self.masters.symbol('Device:R_Small')
        changed = copy.deepcopy(library)
        unit = sx.children(changed, 'symbol')[-1]
        unit.append(sx.parse('(circle (center 0 0) (radius 0.3) (stroke (width 0) (type default)) (fill (type none)))'))
        self.assertNotEqual(symbol_signature(library), symbol_signature(changed))
        # Exercise inheritance deterministically, independent of release aliases.
        self.masters.symbols['OompTest'] = {
            'Parent': sx.parse('(symbol "Parent" (property "Value" "parent") (symbol "Parent_1_1" (pin passive line (at 0 0 0) (length 1) (name "A") (number "1"))))'),
            'Child': sx.parse('(symbol "Child" (extends "Parent") (property "Value" "child"))'),
        }
        child = self.masters.symbol('OompTest:Child')
        self.assertIsNone(sx.child(child, 'extends'))
        self.assertEqual(sx.property_value(child, 'Value'), 'child')
        self.assertEqual(sx.children(child, 'symbol')[0][1], 'Child_1_1')

    def test_kicad_format_normalisation_does_not_hide_pin_changes(self):
        original = self.masters.symbol('Device:R_Small')
        changed = copy.deepcopy(original)
        unit = next(node for node in sx.children(changed, 'symbol') if sx.children(node, 'pin'))
        pin = sx.children(unit, 'pin')[0]
        sx.child(pin, 'at')[1] = sx.Atom('9.123')
        self.masters.prepare_symbol_signatures([original, changed])
        self.assertNotEqual(self.masters.symbol_signature(original), self.masters.symbol_signature(changed))

    def test_full_conversion_front_back_modified_and_repeat(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parts = root / 'parts'
            part_id = 'electronic_resistor_0603_2200_ohm'
            part_directory = parts / part_id
            part_directory.mkdir(parents=True)
            part = {
                'id': part_id, 'taxonomy_1': 'electronic', 'taxonomy_2': 'resistor',
                'taxonomy_3': '0603', 'taxonomy_4': '2200_ohm',
                'name_readable': 'Resistor 2.2k 0603', 'md5_6_alpha_upper': '1X0XV',
            }
            (part_directory / 'working.yaml').write_text(yaml.safe_dump(part))
            manifest = build_part(part_directory, self.masters, {})
            self.assertEqual(manifest['status'], 'complete')
            self.assertEqual(len(manifest['assets']), 3)
            result = package_libraries(parts, root / 'libraries')
            self.assertEqual(result['assets'], 3)
            project = parts / 'oomp_project_test'
            data = project / 'data'
            data.mkdir(parents=True)
            pcb = data / 'kicad_file.kicad_pcb'
            script = r'''
import pcbnew, sys
board = pcbnew.BOARD()
for index in range(1, 4):
    fp = pcbnew.FootprintLoad(sys.argv[1], 'R_0603_1608Metric')
    fp.SetFPID(pcbnew.LIB_ID('Resistor_SMD', 'R_0603_1608Metric'))
    board.Add(fp)
    fp.SetReference('R' + str(index))
    fp.SetValue('2k2')
    fp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(index * 10), pcbnew.FromMM(20)))
    fp.SetOrientationDegrees(index * 90)
    if index == 2:
        fp.Flip(fp.GetPosition(), pcbnew.FLIP_DIRECTION_LEFT_RIGHT)
    if index == 3:
        pad = list(fp.Pads())[0]
        pad.SetSize(pcbnew.VECTOR2I(pcbnew.FromMM(1.234), pcbnew.FromMM(0.95)))
pcbnew.SaveBoard(sys.argv[2], board)
'''
            completed = subprocess.run([str(self.masters.root / 'bin/python.exe'), '-c', script,
                                        str(self.masters.root / 'share/kicad/footprints/Resistor_SMD.pretty'), str(pcb)],
                                       capture_output=True, text=True)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            before = pcb.read_bytes()
            original_pads = []
            for fp in sx.children(sx.parse(before.decode()), 'footprint'):
                original_pads.append((sx.property_value(fp, 'Reference'), [sx.dumps(pad) for pad in sx.children(fp, 'pad')]))
            symbol = self.masters.symbol('Device:R_Small')
            symbol[1] = sx.q('Device:R_Small')
            sch = sx.parse('(kicad_sch (version 20250114) (generator "oomp_test") (uuid "00000000-0000-0000-0000-000000000001") (paper "A4") (lib_symbols))')
            sx.child(sch, 'lib_symbols').append(symbol)
            for number in range(1, 4):
                sch.append(sx.parse(f'(symbol (lib_id "Device:R_Small") (at {number * 10} 20 0) (unit 1) (in_bom yes) (on_board yes) (uuid "00000000-0000-0000-0000-00000000000{number + 1}") (property "Reference" "R{number}") (property "Value" "2k2"))'))
            (data / 'kicad_file.kicad_sch').write_text(sx.document(sch))
            details = {'directory': str(project), 'parts_directory': str(parts),
                       'project_match_overrides': {'R1': part_id, 'R2': part_id, 'R3': part_id}}
            result = convert_project(details)
            self.assertEqual(result['summary']['footprints_converted'], 2, result['footprints'])
            self.assertEqual(result['summary']['symbols_converted'], 3, result['symbols'])
            self.assertEqual(pcb.read_bytes(), before)
            self.assertEqual((data / 'original/kicad_file.kicad_pcb').read_bytes(), before)
            output = data / 'oomp_design/kicad_file.kicad_pcb'
            after_first = output.read_bytes()
            generated = sx.parse(after_first.decode())
            for fp in sx.children(generated, 'footprint'):
                reference = sx.property_value(fp, 'Reference')
                pads = next(pads for ref, pads in original_pads if ref == reference)
                self.assertEqual([sx.dumps(pad) for pad in sx.children(fp, 'pad')], pads)
                marks = [item for item in sx.children(fp, 'fp_text') if len(item) > 2 and item[2] == '1X0XV']
                self.assertEqual(len(marks), 0 if reference == 'R3' else 1)
                if reference == 'R2':
                    self.assertEqual(sx.value(marks[0], 'layer'), 'B.SilkS')
            result = convert_project(details)
            self.assertEqual(output.read_bytes(), after_first)
            output.write_text(output.read_text() + '; user edit\n')
            with self.assertRaisesRegex(RuntimeError, 'was edited'):
                convert_project(details)


if __name__ == '__main__':
    unittest.main()
