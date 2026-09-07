"""Regenerate project processing + summary + board explorer for matching projects."""
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.project_summary_agent import generate_project_summary
from kicad_agents.project_html_agent import generate_board_explorer
from kicad_agents.project_review_agent import write_lcsc_review
from kicad_agents.browser_research_agent import write_browser_research_queue

tokens = [token.lower() for token in sys.argv[1:]]

directories = []
for part_directory in sorted((ROOT / "parts").iterdir(), key=lambda path: path.name.lower()):
    generated = part_directory / "data" / "generated_data"
    if not (generated / "project.json").is_file():
        continue
    if not (part_directory / "data" / "kicad_file.kicad_pcb").is_file():
        continue
    if tokens and not all(token in part_directory.name.lower() for token in tokens):
        continue
    directories.append(part_directory)

print(f"regenerating {len(directories)} projects")
failures = []
for index, part_directory in enumerate(directories, start=1):
    parts_directory = ROOT / "parts"
    output_directory = part_directory / "data" / "generated_data"
    try:
        match_override_data = {
            "matches": {},
            "blocked": {},
            "review_notes": [],
            "help": "Project-specific mappings are defined in working_oomp_populate_project.py.",
        }
        # Preserve the existing overrides file content where present.
        overrides_path = output_directory / "match_overrides.yaml"
        import yaml
        if overrides_path.is_file():
            existing = yaml.safe_load(overrides_path.read_text(encoding="utf-8")) or {}
            if isinstance(existing, dict):
                match_override_data["matches"] = existing.get("matches") or {}
                match_override_data["blocked"] = existing.get("blocked") or {}
                match_override_data["review_notes"] = existing.get("review_notes") or []
        with overrides_path.open("w", encoding="utf-8") as output_file:
            yaml.safe_dump(match_override_data, output_file, sort_keys=False, allow_unicode=True)

        part_metadata = yaml.safe_load((part_directory / "working.yaml").read_text(encoding="utf-8")) or {}
        project_data, output_directory = process_project(part_directory, parts_directory, output_directory=output_directory)
        if project_data is None:
            print(f"[{index}/{len(directories)}] {part_directory.name} skipped (no kicad files)")
            continue
        write_lcsc_review(project_data, output_directory)
        write_browser_research_queue(project_data, output_directory)
        summary_data = generate_project_summary(
            part_directory,
            parts_directory=parts_directory,
            output_directory=output_directory,
            project_data=project_data,
            part_metadata=part_metadata,
            readme_output=part_directory / "README.md",
            regenerate_pngs=False,
        )
        generate_board_explorer(part_directory, project_data, summary_data, output_directory=output_directory)
        print(f"[{index}/{len(directories)}] {part_directory.name} ok", flush=True)
    except Exception as error:
        failures.append((part_directory.name, str(error)))
        print(f"[{index}/{len(directories)}] {part_directory.name} FAILED: {error}", flush=True)
        traceback.print_exc()
print("DONE failures:", failures)
