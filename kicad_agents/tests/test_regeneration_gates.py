import tempfile
import unittest
from pathlib import Path

import yaml

from action_regenerate_all import _normal_gate_is_complete
from action_regenerate_part import _check_files_complete


class RegenerationGateTests(unittest.TestCase):
    def test_failed_status_file_is_not_complete(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            part_directory = Path(temporary_directory)
            status_path = part_directory / "generation_status.yaml"
            status_path.write_text(
                yaml.safe_dump({"status": "failed"}), encoding="utf-8"
            )
            mode = {"file_test": "generation_status.yaml"}

            self.assertFalse(_check_files_complete(part_directory, mode))
            self.assertFalse(_normal_gate_is_complete(part_directory, mode))

    def test_generated_status_file_is_complete(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            part_directory = Path(temporary_directory)
            status_path = part_directory / "generation_status.yaml"
            status_path.write_text(
                yaml.safe_dump({"status": "generated"}), encoding="utf-8"
            )
            mode = {"file_test": "generation_status.yaml"}

            self.assertTrue(_check_files_complete(part_directory, mode))
            self.assertTrue(_normal_gate_is_complete(part_directory, mode))


if __name__ == "__main__":
    unittest.main()
