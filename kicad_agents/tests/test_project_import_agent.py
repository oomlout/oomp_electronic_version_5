import tempfile
from pathlib import Path
import unittest

import yaml

from kicad_agents.project_import_helpers import (
    _assign_board_names,
    _candidate,
    _select_current_candidates,
    append_project_record,
    build_project_record,
    eagle_storage_format,
    load_decisions,
    mark_queue_added,
    mark_queue_too_old,
    select_next_repository,
)


class ProjectImportAgentTests(unittest.TestCase):
    def test_selects_first_todo_not_already_declared(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            queue = root / "queue.yaml"
            project_data = root / "project_data"
            owner = project_data / "adafruit"
            owner.mkdir(parents=True)
            queue.write_text(
                "repositories:\n"
                "- full_name: adafruit/already\n  status: TODO\n"
                "- full_name: adafruit/next\n  status: TODO\n",
                encoding="utf-8",
            )
            (owner / "working.yaml").write_text(
                "github_user: adafruit\nprojects:\n- github_repository: already\n  versions:\n  - project_file_path: board\n",
                encoding="utf-8",
            )
            selection = select_next_repository(queue, project_data)
        self.assertEqual(selection.entry["full_name"], "adafruit/next")
        self.assertEqual(selection.skipped_existing, ("adafruit/already",))

    def test_keeps_newest_revision_and_separate_boards(self):
        paths = {
            path.lower(): path for path in [
                "Hardware/Sensor rev A.kicad_pcb",
                "Hardware/Sensor rev B.kicad_pcb",
                "Hardware/Other.kicad_pcb",
            ]
        }
        candidates = [_candidate(path, paths) for path in paths.values()]
        selected, excluded = _select_current_candidates(candidates)
        _assign_board_names(selected)
        self.assertEqual(
            {item["path"] for item in selected},
            {"Hardware/Sensor rev B.kicad_pcb", "Hardware/Other.kicad_pcb"},
        )
        self.assertEqual(excluded[0]["path"], "Hardware/Sensor rev A.kicad_pcb")

    def test_build_and_append_preserves_one_current_per_board(self):
        with tempfile.TemporaryDirectory() as temporary:
            project_data = Path(temporary)
            owner = project_data / "sparkfun"
            owner.mkdir()
            working = owner / "working.yaml"
            working.write_text("github_user: sparkfun\nprojects: []\n", encoding="utf-8")
            candidate = {
                "board": "test_board",
                "board_name": "Test Board",
                "path": "Hardware/Test Board.kicad_pcb",
                "folder": "Hardware",
                "project_file_path": "Hardware/Test Board",
                "project_file_extensions": [".kicad_pcb"],
                "source_format": "kicad",
            }
            entry = {
                "full_name": "sparkfun/Test",
                "url": "https://github.com/sparkfun/Test",
                "default_branch": "main",
            }
            project = build_project_record(entry, [candidate])
            append_project_record("sparkfun", project, project_data)
            loaded = yaml.safe_load(working.read_text(encoding="utf-8"))
        version = loaded["projects"][0]["versions"][0]
        self.assertEqual(version["version"], "current")
        self.assertEqual(version["project_file_extensions"], [".kicad_pcb"])

    def test_marks_only_matching_queue_entry_added(self):
        with tempfile.TemporaryDirectory() as temporary:
            queue = Path(temporary) / "queue.yaml"
            queue.write_text(
                "repositories:\n"
                "  - rank: 1\n    full_name: \"adafruit/one\"\n    status: \"TODO\"\n"
                "  - rank: 2\n    full_name: \"adafruit/two\"\n    status: \"TODO\"\n",
                encoding="utf-8",
            )
            mark_queue_added(queue, "adafruit/two")
            loaded = yaml.safe_load(queue.read_text(encoding="utf-8"))
        self.assertEqual(loaded["repositories"][0]["status"], "TODO")
        self.assertEqual(loaded["repositories"][1]["status"], "ADDED")

    def test_marks_legacy_eagle_repository_ingested_with_note(self):
        with tempfile.TemporaryDirectory() as temporary:
            queue = Path(temporary) / "queue.yaml"
            queue.write_text(
                "repositories:\n"
                "  - rank: 1\n    full_name: \"adafruit/old\"\n    status: \"TODO\"\n",
                encoding="utf-8",
            )
            mark_queue_too_old(queue, "adafruit/old", "too old: binary Eagle files")
            loaded = yaml.safe_load(queue.read_text(encoding="utf-8"))["repositories"][0]
        self.assertEqual(loaded["status"], "INGESTED")
        self.assertEqual(loaded["ingest_note"], "too old: binary Eagle files")

    def test_eagle_storage_format_detects_xml_and_binary(self):
        self.assertEqual(eagle_storage_format(b"<?xml version='1.0'?><eagle/>"), "xml")
        self.assertEqual(eagle_storage_format(b"<eagle version='9.0'></eagle>"), "xml")
        self.assertEqual(eagle_storage_format(b"\x10\x00\x08\xfflegacy"), "legacy_binary")

    def test_prefilled_include_list_is_not_counted_as_llm_work(self):
        inspection = {
            "repository": "adafruit/Test",
            "selected_boards": [{"path": "one.brd"}, {"path": "two.brd"}],
        }
        with tempfile.TemporaryDirectory() as temporary:
            decisions = Path(temporary) / "decision.yaml"
            decisions.write_text(
                "repository: adafruit/Test\n"
                "include_paths: [one.brd, two.brd]\n"
                "exclude_paths: [two.brd]\n"
                "overrides: {}\n",
                encoding="utf-8",
            )
            selected, llm_decisions = load_decisions(decisions, inspection)
        self.assertEqual([item["path"] for item in selected], ["one.brd"])
        self.assertEqual(llm_decisions, [{"kind": "exclude_paths", "count": 1}])


if __name__ == "__main__":
    unittest.main()
