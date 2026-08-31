"""Roboclick run_python action: extract a KiCad project and build its README bundle."""

import argparse
import json
import sys
from pathlib import Path

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from kicad_agents.kicad_processing_agent import process_project
from kicad_agents.project_summary_agent import generate_project_summary


def _as_boolean(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ["1", "true", "yes", "on"]


def compile_project_part(details):
    part_directory = Path(details["directory"]).resolve()
    parts_directory_value = details.get("parts_directory", "parts")
    parts_directory = Path(parts_directory_value).resolve()
    output_directory = part_directory / "generated_data"
    output_directory.mkdir(parents=True, exist_ok=True)
    regenerate_pngs = _as_boolean(details.get("regenerate_pngs", False))

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
    summary_data = generate_project_summary(
        part_directory,
        parts_directory=parts_directory,
        output_directory=output_directory,
        project_data=project_data,
        part_metadata=details,
        readme_output=part_directory / "README.md",
        regenerate_pngs=regenerate_pngs,
    )
    print(f"compiled {summary_data['project']['display_name']}")
    print(f"README: {part_directory / 'README.md'}")
    print(f"assets: {output_directory / 'src'}")


def main():
    parser = argparse.ArgumentParser(description="Compile an OOMP project part README.")
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    details = json.loads(arguments.kwargs)
    compile_project_part(details)


if __name__ == "__main__":
    main()
