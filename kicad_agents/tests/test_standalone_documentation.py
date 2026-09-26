import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from kicad_agents.standalone_documentation_action import (
    select_pcb,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MINIMAL_BOARD = """(kicad_pcb (version 20240108) (generator pcbnew)
  (general (thickness 1.6))
  (paper "A4")
  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (36 "B.SilkS" user "b.silkscreen")
    (37 "F.SilkS" user "f.silkscreen")
    (44 "Edge.Cuts" user)
  )
  (gr_rect (start 0 0) (end 20 10) (stroke (width 0.05) (type default)) (fill none) (layer "Edge.Cuts"))
)"""


class StandaloneDocumentationTests(unittest.TestCase):
    def test_select_pcb_requires_a_choice_when_multiple_projects_are_ambiguous(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            source = Path(temporary_directory)
            (source / "one.kicad_pcb").write_text(MINIMAL_BOARD, encoding="utf-8")
            (source / "two.kicad_pcb").write_text(MINIMAL_BOARD, encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "--project"):
                select_pcb(source)
            self.assertEqual(select_pcb(source, "two").name, "two.kicad_pcb")

    @unittest.skipUnless(os.name == "nt", "The portable launcher is a Windows batch file.")
    def test_batch_file_generates_local_documentation_bundle_from_current_directory(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            source = Path(temporary_directory)
            (source / "sample_board.kicad_pcb").write_text(MINIMAL_BOARD, encoding="utf-8")

            completed = subprocess.run(
                [
                    str(REPOSITORY_ROOT / "generate_oomp_documentation.bat"),
                    "--skip-interactive-bom",
                ],
                cwd=source,
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

            output = source / "oomp_documentation"
            self.assertEqual(output, source / "oomp_documentation")
            self.assertTrue((output / "README.md").is_file())
            self.assertTrue((output / "board_explorer.html").is_file())
            self.assertTrue((output / "generation_manifest.yaml").is_file())
            self.assertTrue((output / "data/kicad_file.kicad_pcb").is_file())
            self.assertTrue((output / "data/generated_data/project.yaml").is_file())
            self.assertTrue((output / "data/generated_data/src/board.svg").is_file())
            self.assertTrue((output / "data/generated_data/src/board_300.png").is_file())
            readme = (output / "README.md").read_text(encoding="utf-8")
            self.assertIn("[Open the offline board explorer](board_explorer.html)", readme)
            self.assertIn("data/generated_data/src/board.svg", readme)
            self.assertNotIn("github.io", readme)


if __name__ == "__main__":
    unittest.main()
