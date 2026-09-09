import tempfile
import unittest
from pathlib import Path

import yaml

import working_oomp
from kicad_agents.web_manifest_action import build_web_manifest


class WebManifestTests(unittest.TestCase):
    def test_manifest_has_metadata_inventory_stats_descriptions_and_urls(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            part_directory = Path(temporary_directory) / "electronic_test_part"
            (part_directory / "data").mkdir(parents=True)
            working = {
                "id": "electronic_test_part",
                "name_readable": "Electronic test part",
                "taxonomy_1": "electronic",
                "taxonomy_2": "resistor",
                "dimensions_mm": {"length": 1.6, "width": 0.8},
                "pins": {"pin_1": {"name": "one"}, "pin_2": {"name": "two"}},
                "oomlout_ai_roboclick_1": {
                    "actions": [{"command": "example", "file_output": "data/missing.svg"}],
                    "file_test": "data/present.svg",
                },
            }
            (part_directory / "working.yaml").write_text(yaml.safe_dump(working), encoding="utf-8")
            (part_directory / "README.md").write_text("# Test\n", encoding="utf-8")
            (part_directory / "data" / "present.svg").write_text("<svg/>", encoding="utf-8")

            # Roboclick resolves file_output to an absolute path before it
            # launches run_python; cover that real invocation shape here.
            action_details = {
                "directory": str(part_directory),
                "file_output": str(part_directory / "web.yaml"),
            }
            manifest = build_web_manifest(action_details)
            first_render = (part_directory / "web.yaml").read_bytes()
            build_web_manifest(action_details)

            self.assertEqual((part_directory / "web.yaml").read_bytes(), first_render)
            self.assertEqual(manifest["id"], "electronic_test_part")
            self.assertEqual(manifest["highlights"]["pin_count"], 2)
            self.assertEqual(manifest["file_stats"]["file_count"], 3)
            self.assertTrue(manifest["file_stats"]["total_size"].endswith((" B", " kB", " MB", " GB", " TB")))
            self.assertNotIn("oomlout_ai_roboclick_1", manifest["metadata"])
            self.assertEqual([item["path"] for item in manifest["files"]], ["data/present.svg", "README.md", "working.yaml"])
            readme = next(item for item in manifest["files"] if item["path"] == "README.md")
            self.assertIn("Human-readable overview", readme["description"])
            self.assertTrue(readme["size"].endswith(" B"))
            self.assertEqual(readme["media_type"], "text/markdown")
            self.assertEqual(
                readme["github_url"],
                "https://github.com/oomlout/oomp_electronic_version_5/blob/main/parts/electronic_test_part/README.md",
            )
            self.assertTrue(manifest["links"]["manifest_github"].endswith("/electronic_test_part/web.yaml"))
            declared = {item["path"]: item for item in manifest["generation"]["declared_outputs"]}
            self.assertTrue(declared["data/present.svg"]["available"])
            self.assertFalse(declared["data/missing.svg"]["available"])

    def test_web_manifest_action_is_always_run_and_appended(self):
        part = {"oomlout_ai_roboclick_1": {"actions": []}}
        count = working_oomp.add_web_manifest_action(part, 1)

        self.assertEqual(count, 2)
        final_mode = part["oomlout_ai_roboclick_2"]
        self.assertTrue(final_mode["always_run_on_regeneration"])
        self.assertEqual(final_mode["file_test"], "")
        self.assertEqual(final_mode["actions"][0]["command"], "run_python")
        self.assertEqual(final_mode["actions"][0]["file_python"], "kicad_agents/web_manifest_action.py")
        self.assertEqual(final_mode["actions"][0]["manifest_config"], "config_web_manifest.yaml")


if __name__ == "__main__":
    unittest.main()
