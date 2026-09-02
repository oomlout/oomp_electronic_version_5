"""Roboclick action that deterministically builds one OOMP component's diagrams."""

import argparse
import json
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
repository_root_text = str(REPOSITORY_ROOT)
if repository_root_text in sys.path:
    sys.path.remove(repository_root_text)
sys.path.insert(0, repository_root_text)

import working_svg


def _as_boolean(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ["1", "true", "yes", "on"]


def build_component_diagrams(details):
    part_directory = Path(details.get("directory", "")).resolve()
    part_id = str(details.get("part_id", "")).strip()
    if part_id == "":
        part_id = part_directory.name
    if part_directory.name != part_id:
        raise ValueError(
            f"Roboclick part directory '{part_directory.name}' does not match part_id '{part_id}'."
        )

    working_yaml = part_directory / "working.yaml"
    if not working_yaml.is_file():
        raise FileNotFoundError(f"Missing generated part definition: {working_yaml}")

    working_svg.main(
        part_id=part_id,
        filter="",
        regenerate_pngs=_as_boolean(details.get("regenerate_pngs", False)),
    )
    assembly_svg = part_directory / "data" / "working_svg_assembly.svg"
    if not assembly_svg.is_file():
        raise RuntimeError(f"SVG pipeline did not create {assembly_svg}")
    print(f"generated component diagrams for {part_id}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate one OOMP component's diagrams as a Roboclick run_python action."
    )
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    build_component_diagrams(json.loads(arguments.kwargs))


if __name__ == "__main__":
    main()
