"""Roboclick run_python action: extract a KiCad project and build its README bundle."""

import argparse
import json
import sys
from pathlib import Path

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
repository_root_text = str(REPOSITORY_ROOT)
if repository_root_text in sys.path:
    sys.path.remove(repository_root_text)
sys.path.insert(0, repository_root_text)

from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.project_summary_agent import generate_project_summary
from kicad_agents.project_html_agent import generate_board_explorer
from kicad_agents.project_review_agent import write_lcsc_review
from kicad_agents.browser_research_agent import write_browser_research_queue


def _as_boolean(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ["1", "true", "yes", "on"]


def compile_project_part(details):
    part_directory = Path(details["directory"]).resolve()
    parts_directory_value = details.get("parts_directory", "parts")
    parts_directory = Path(parts_directory_value).resolve()
    output_directory = part_directory / "data" / "generated_data"
    output_directory.mkdir(parents=True, exist_ok=True)
    regenerate_pngs = _as_boolean(details.get("regenerate_pngs", False))

    part_metadata = {}
    working_yaml = part_directory / "working.yaml"
    if working_yaml.is_file():
        loaded_metadata = yaml.safe_load(working_yaml.read_text(encoding="utf-8")) or {}
        if isinstance(loaded_metadata, dict):
            part_metadata.update(loaded_metadata)
    part_metadata.update(details)

    match_overrides = details.get("project_match_overrides", {})
    match_override_data = {
        "matches": match_overrides if isinstance(match_overrides, dict) else {},
        "help": "Project-specific mappings are defined in working_oomp_populate_project.py.",
    }
    with (output_directory / "match_overrides.yaml").open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(match_override_data, output_file, sort_keys=False, allow_unicode=True)

    project_data, output_directory = process_project(
        part_directory,
        parts_directory,
        output_directory=output_directory,
    )
    write_lcsc_review(project_data, output_directory)
    write_browser_research_queue(project_data, output_directory)
    summary_data = generate_project_summary(
        part_directory,
        parts_directory=parts_directory,
        output_directory=output_directory,
        project_data=project_data,
        part_metadata=part_metadata,
        readme_output=part_directory / "README.md",
        regenerate_pngs=regenerate_pngs,
    )
    explorer_path = generate_board_explorer(
        part_directory,
        project_data,
        summary_data,
        output_directory=output_directory,
    )
    print(f"compiled {summary_data['project']['display_name']}")
    print(f"README: {part_directory / 'README.md'}")
    print(f"assets: {output_directory / 'src'}")
    print(f"explorer: {explorer_path}")


def main():
    parser = argparse.ArgumentParser(description="Compile an OOMP project part README.")
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    details = json.loads(arguments.kwargs)
    compile_project_part(details)


if __name__ == "__main__":
    main()
