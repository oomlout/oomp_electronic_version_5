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

from kicad_agents.contact_sheet import build_contact_sheet, is_outdated as sheet_is_outdated
from kicad_agents.run_error_report import log_run_error
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
        message = f"Missing generated part definition: {working_yaml}"
        log_run_error("component_svg_action", FileNotFoundError(message))
        print(message)
        return None

    working_svg.main(
        part_id=part_id,
        filter="",
        regenerate_pngs=_as_boolean(details.get("regenerate_pngs", False)),
    )
    assembly_svg = part_directory / "data" / "working_svg_assembly.svg"
    if not assembly_svg.is_file():
        message = f"SVG pipeline did not create {assembly_svg}"
        log_run_error("component_svg_action", RuntimeError(message))
        print(message)
        return None
    build_diagram_contact_sheet(part_directory, part_id, working_yaml)
    print(f"generated component diagrams for {part_id}")


def diagram_contact_sheet_cells(part_directory, working_yaml):
    """Every OOMP diagram PNG in svg_details order, with readable labels."""
    data_directory = part_directory / "data"
    order = []
    svg_details = working_yaml.get("svg_details", []) if isinstance(working_yaml, dict) else []
    for detail in svg_details:
        if isinstance(detail, dict):
            extra = str(detail.get("filename_extra", "")).strip()
            if extra:
                order.append(extra)
    ordered_extras = order + sorted(
        path.stem.replace("working_svg_", "")
        for path in data_directory.glob("working_svg_*.png")
        if not path.stem.endswith("_300")
        and path.stem != "working_svg_contact_sheet"
        and path.stem.replace("working_svg_", "") not in order
    )
    cells = []
    for extra in ordered_extras:
        png_path = data_directory / f"working_svg_{extra}.png"
        if png_path.is_file():
            cells.append((extra.replace("_", " "), png_path))
    return cells


def build_diagram_contact_sheet(part_directory, part_id, working_yaml_path):
    """Compose all of the part's OOMP diagrams into one review image."""
    import yaml

    working_yaml = {}
    if working_yaml_path.is_file():
        working_yaml = yaml.safe_load(working_yaml_path.read_text(encoding="utf-8")) or {}
    destination = part_directory / "data" / "working_svg_contact_sheet.png"
    cells = diagram_contact_sheet_cells(part_directory, working_yaml)
    if not cells:
        print(f"no diagram PNGs found for {part_id}; skipping contact sheet")
        return
    if sheet_is_outdated(destination, [png_path for _, png_path in cells]):
        build_contact_sheet(
            part_id,
            cells,
            destination,
            title="component diagrams",
        )
    if not destination.is_file():
        raise RuntimeError(f"Contact sheet was not created: {destination}.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate one OOMP component's diagrams as a Roboclick run_python action."
    )
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    try:
        build_component_diagrams(json.loads(arguments.kwargs))
    except Exception as error:
        log_run_error("component_svg_action", error)
        print(error)
        return


if __name__ == "__main__":
    main()
