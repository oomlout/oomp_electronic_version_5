import copy
import unittest
from kicad_agents import kicad_sexpr as sx
from kicad_agents.kicad_library_agent import Masters, symbol_signature

class InstalledKiCadTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.masters = Masters()
        except FileNotFoundError as error:
            raise unittest.SkipTest(str(error))

    def test_symbol_inheritance_and_graphic_change_guard(self):
        library = self.masters.symbol('Device:R_Small')
        changed = copy.deepcopy(library)
        unit = sx.children(changed, 'symbol')[-1]
        unit.append(sx.parse('(circle (center 0 0) (radius 0.3) (stroke (width 0) (type default)) (fill (type none)))'))
        self.assertNotEqual(symbol_signature(library), symbol_signature(changed))
        self.masters.symbols['OompTest'] = {'Parent': sx.parse('(symbol "Parent" (property "Value" "parent") (symbol "Parent_1_1" (pin passive line (at 0 0 0) (length 1) (name "A") (number "1"))))'), 'Child': sx.parse('(symbol "Child" (extends "Parent") (property "Value" "child"))')}
        child = self.masters.symbol('OompTest:Child')
        self.assertIsNone(sx.child(child, 'extends'))
        self.assertEqual(sx.property_value(child, 'Value'), 'child')
        self.assertEqual(sx.children(child, 'symbol')[0][1], 'Child_1_1')

    def test_kicad_format_normalisation_does_not_hide_pin_changes(self):
        original = self.masters.symbol('Device:R_Small')
        changed = copy.deepcopy(original)
        unit = next((node for node in sx.children(changed, 'symbol') if sx.children(node, 'pin')))
        pin = sx.children(unit, 'pin')[0]
        sx.child(pin, 'at')[1] = sx.Atom('9.123')
        self.masters.prepare_symbol_signatures([original, changed])
        self.assertNotEqual(self.masters.symbol_signature(original), self.masters.symbol_signature(changed))
if __name__ == '__main__':
    unittest.main()
