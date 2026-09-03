import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml
from jinja2 import Environment, FileSystemLoader

from kicad_agents.project_usage_action import build_usage_index, refresh_project_usage


class ProjectUsageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.parts = Path(self.temporary.name) / "parts"
        self.project_id = "oomp_project_github_example_board_current"
        self.project = self.parts / self.project_id
        self.data_file = self.project / "data/generated_data/project.json"
        self.write_part(self.project_id, {
            "name_readable": "Example board current",
            "project_github_url": "https://github.com/example/boards",
            "project_board_url": "https://github.com/example/boards/tree/main/board",
        })
        self.write_part("resistor", {"custom_note": "keep me", "oomlout_test": {"actions": [
            {"command": "text_jinja_template", "dict_data": {"name_short": "Resistor"}},
        ]}})
        self.write_part("hole", {})
        self.write_part("unmatched", {})
        self.write_project([
            self.component("R10", "resistor"), self.component("R2", "resistor"),
            self.component("R2", "resistor"), self.component("U1", "unmatched", "unmatched"),
            self.component("H1", "hole", hole=True),
            self.component("R3", "resistor", exclude=True),
        ], [self.component("MH1", "hole", hole=True)])

    def write_part(self, part_id, data):
        file = self.parts / part_id / "working.yaml"
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(yaml.safe_dump(data), encoding="utf-8")

    def read_part(self, part_id):
        return yaml.safe_load((self.parts / part_id / "working.yaml").read_text(encoding="utf-8"))

    def write_project(self, components, holes=None):
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.data_file.write_text(json.dumps({"components": components, "mounting_hole_items": holes or []}), encoding="utf-8")

    def component(self, reference, part_id, status="matched", hole=False, exclude=False):
        return {"reference": reference, "pcb": {"is_mounting_hole": hole, "exclude_from_bom": exclude},
                "oomp": {"status": status, "accepted": status == "matched", "oomp_id": part_id}}

    def test_matches_holes_links_and_snapshots_are_idempotent(self):
        report = refresh_project_usage(self.parts, render_readmes=False)
        self.assertEqual(report["used_part_count"], 2)
        part = self.read_part("resistor")
        usage = part["used_in_projects"]
        self.assertEqual(usage[0]["references"], ["R2", "R10"])
        self.assertEqual(usage[0]["quantity"], 2)
        self.assertEqual(usage[0]["board_url"], "https://github.com/example/boards/tree/main/board")
        self.assertEqual(usage[0]["board_explorer_url"], f"https://oomlout.github.io/oomp_electronic_version_5/parts/{self.project_id}/board_explorer.html")
        self.assertEqual(part["oomlout_test"]["actions"][0]["dict_data"]["used_in_projects"], usage)
        self.assertEqual(part["custom_note"], "keep me")
        self.assertEqual(self.read_part("hole")["used_in_projects"][0]["references"], ["MH1"])
        self.assertNotIn("used_in_projects", self.read_part("unmatched"))
        file = self.parts / "resistor/working.yaml"
        before = (file.read_bytes(), file.stat().st_mtime_ns)
        self.assertEqual(refresh_project_usage(self.parts, render_readmes=False)["updated_part_ids"], [])
        self.assertEqual(before, (file.read_bytes(), file.stat().st_mtime_ns))

    def test_removes_stale_links_and_renders_affected_parts(self):
        refresh_project_usage(self.parts, render_readmes=False)
        self.write_project([])
        with patch("kicad_agents.readme_action.regenerate_readmes") as render:
            refresh_project_usage(self.parts)
        self.assertNotIn("used_in_projects", self.read_part("resistor"))
        self.assertNotIn("used_in_projects", self.read_part("resistor")["oomlout_test"]["actions"][0]["dict_data"])
        self.assertEqual(set(render.call_args.kwargs["part_ids"]), {"resistor", "hole"})

    def test_missing_extraction_keeps_usage_and_invalid_extraction_aborts(self):
        refresh_project_usage(self.parts, render_readmes=False)
        previous = self.read_part("resistor")
        self.data_file.unlink()
        report = refresh_project_usage(self.parts, render_readmes=False)
        self.assertEqual(report["unavailable_project_ids"], [self.project_id])
        self.assertEqual(previous, self.read_part("resistor"))
        self.data_file.write_text("not json", encoding="utf-8")
        with self.assertRaises(json.JSONDecodeError):
            refresh_project_usage(self.parts, render_readmes=False)
        self.assertEqual(previous, self.read_part("resistor"))

    def test_separate_project_versions_and_template(self):
        old_project = self.parts / "oomp_project_github_example_board_v1"
        self.write_part(old_project.name, {"name_readable": "Example board v1", "project_version": "v1"})
        old_data = old_project / "data/generated_data/project.json"
        old_data.parent.mkdir(parents=True)
        old_data.write_text(json.dumps({"components": [self.component("R1", "resistor")]}), encoding="utf-8")
        index, unavailable = build_usage_index(self.parts)
        self.assertEqual(unavailable, [])
        self.assertEqual(len(index["resistor"]), 2)
        part = {"name_short": "Resistor", "used_in_projects": index["resistor"], "part_page": {
            "oomp_id": "resistor", "summary": "Sample", "main_image": {"svg": "data/pinout.svg"},
            "quick_facts": [], "taxonomy": [], "identifiers": [], "pins": [], "has_datasheet": False,
            "file_previews": [], "repository_url": "", "navigation_link": "",
        }}
        template_folder = Path(__file__).resolve().parents[2] / "source_file/template_jinja/oomp_category/template_jinja_markdown"
        template = Environment(loader=FileSystemLoader(template_folder)).get_template("working.md.j2")
        markdown = template.render(p=part)
        self.assertIn("## Used in projects", markdown)
        self.assertIn(index["resistor"][0]["board_explorer_url"], markdown)
        self.assertNotIn("/blob/main/parts/", markdown)
        part.pop("used_in_projects")
        self.assertNotIn("## Used in projects", template.render(p=part))

    def test_usage_action_follows_project_compilation(self):
        import working_oomp
        part = {}
        working_oomp.add_project_actions(part, 0)
        for mode in part.values():
            scripts = [action.get("file_python") for action in mode["actions"]]
            if "kicad_agents/project_readme_action.py" in scripts:
                self.assertGreater(scripts.index("kicad_agents/project_usage_action.py"), scripts.index("kicad_agents/project_readme_action.py"))
                self.assertEqual(mode["file_test"], "")
                return
        self.fail("No project compile action found")


if __name__ == "__main__":
    unittest.main()
