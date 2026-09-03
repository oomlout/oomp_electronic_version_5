"""Build and validate one researched OOMP component at a time.

This agent deliberately performs no online research.  An AI agent or person uses
the available interactive browser, records the verified result in a small YAML
file, and imports the browser-downloaded datasheet.  This module then provides a
single deterministic entry point for the repetitive local work:

* verify that the family populate and populate-extra files contain the part;
* regenerate only the selected OOMP part;
* run only that part's Roboclick actions;
* confirm identifiers, pins, dimensions, datasheet provenance, project match
  overrides, README, diagrams and conservative PNG state;
* confirm that deferred project pages were not changed by the component build.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib
import io
import json
import re
from pathlib import Path

import yaml

from oomp_populate_helper import build_oomp_id


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
RECORD_DIRECTORY = REPOSITORY_ROOT / "kicad_agents" / "component_records"
REPORT_DIRECTORY = REPOSITORY_ROOT / "kicad_agents" / "generated" / "component_additions"
PARTS_SOURCE_DIRECTORY = REPOSITORY_ROOT / "parts_source"
PARTS_DIRECTORY = REPOSITORY_ROOT / "parts"
PROJECT_PART_PREFIX = "oomp_project_"


def _read_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def _write_yaml(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(data, output_file, sort_keys=False, allow_unicode=True)


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as input_file:
        while True:
            block = input_file.read(1024 * 1024)
            if block == b"":
                break
            digest.update(block)
    return digest.hexdigest()


def _project_file_state():
    """Return content hashes for generated project pages and board assets.

    A component build must not touch these while project regeneration is
    deferred.  Hashing content instead of timestamps avoids false positives.
    """
    state = {}
    if not PARTS_DIRECTORY.is_dir():
        return state
    for project_directory in PARTS_DIRECTORY.iterdir():
        if not project_directory.is_dir() or not project_directory.name.startswith(PROJECT_PART_PREFIX):
            continue
        candidates = [project_directory / "README.md", project_directory / "board_explorer.html"]
        generated_directory = project_directory / "data" / "generated_data"
        if generated_directory.is_dir():
            for pattern in ["board_explorer.html", "src/board*.svg", "src/board*.png"]:
                candidates.extend(generated_directory.glob(pattern))
        for candidate in candidates:
            if candidate.is_file():
                relative = candidate.relative_to(REPOSITORY_ROOT).as_posix()
                state[relative] = _sha256(candidate)
    return state


def _load_populated_definition(record):
    family = str(record.get("family") or "").strip()
    part_id = str(record.get("part_id") or "").strip()
    populate_module = importlib.import_module(f"working_oomp_populate_{family}")
    extra_module = importlib.import_module(f"working_oomp_populate_{family}_extra")

    options = []
    populate_module.main(options=options)
    matches = []
    for option in options:
        candidate = dict(option)
        if str(candidate.get("taxonomy_1") or "") == "":
            candidate["taxonomy_1"] = "electronic"
        if build_oomp_id(candidate) == part_id:
            matches.append(candidate)
    if len(matches) != 1:
        raise ValueError(
            f"Expected one {family} population record for {part_id}, found {len(matches)}."
        )

    extras = {part_id: dict(matches[0])}
    extra_module.main(extras_dict=extras)
    return extras[part_id]


def _find_project_overrides(reference_names, part_id):
    if reference_names == []:
        return [], []
    project_module = importlib.import_module("working_oomp_populate_project")
    project_options = []
    project_module.main(options=project_options)
    matched = []
    missing = []
    for reference_name in reference_names:
        reference_found = False
        for project_option in project_options:
            overrides = project_option.get("project_match_overrides") or {}
            if overrides.get(reference_name) == part_id:
                matched.append(reference_name)
                reference_found = True
                break
        if not reference_found:
            missing.append(reference_name)
    return matched, missing


def validate_record(record):
    errors = []
    warnings = []
    required_text_fields = ["ledger_id", "family", "part_id", "package"]
    for field_name in required_text_fields:
        if str(record.get(field_name) or "").strip() == "":
            errors.append(f"research record is missing {field_name}")

    part_id = str(record.get("part_id") or "")
    if part_id != part_id.lower() or re.fullmatch(r"[a-z0-9_]+", part_id) is None:
        errors.append("part_id must contain only lowercase letters, numbers and underscores")

    research = record.get("research") or {}
    exact_identity = bool(record.get("exact_identity", True))
    if exact_identity:
        if str(research.get("manufacturer") or "").strip() == "":
            errors.append("exact component record is missing research.manufacturer")
        if str(research.get("manufacturer_part_number") or "").strip() == "":
            errors.append("exact component record is missing research.manufacturer_part_number")

    lcsc_part_number = str(research.get("lcsc_part_number") or "").strip()
    if lcsc_part_number != "" and re.fullmatch(r"C[0-9]+", lcsc_part_number) is None:
        errors.append("research.lcsc_part_number must be blank or use the form C123456")
    if lcsc_part_number == "" and str(research.get("lcsc_decision") or "").strip() == "":
        warnings.append("no LCSC number is recorded; add lcsc_decision explaining why")

    browser_sources = research.get("browser_sources") or []
    if len(browser_sources) == 0:
        errors.append("research.browser_sources must contain the pages verified in the browser")
    evidence_notes = research.get("evidence_notes") or []
    if len(evidence_notes) == 0:
        errors.append("research.evidence_notes must record the exact-identity decision")
    return errors, warnings


def validate_implementation(record, require_generated=False):
    errors, warnings = validate_record(record)
    checks = {}
    part_id = str(record.get("part_id") or "")
    research = record.get("research") or {}

    try:
        definition = _load_populated_definition(record)
        checks["population_definition"] = "pass"
    except Exception as exception:
        definition = {}
        errors.append(str(exception))
        checks["population_definition"] = "fail"

    manufacturer_part_number = str(research.get("manufacturer_part_number") or "").strip()
    if manufacturer_part_number != "":
        if definition.get("part_number_manufacturer") != manufacturer_part_number:
            errors.append("populate-extra manufacturer part number does not match the research record")
        else:
            checks["manufacturer_part_number"] = "pass"

    lcsc_part_number = str(research.get("lcsc_part_number") or "").strip()
    if lcsc_part_number != "":
        if definition.get("part_number_lcsc") != lcsc_part_number:
            errors.append("populate-extra LCSC number does not match the research record")
        else:
            checks["lcsc_part_number"] = "pass"
    elif "part_number_lcsc" in definition:
        errors.append("populate-extra assigns an LCSC number that the research record does not confirm")

    expected_pin_count = int(record.get("pin_count") or 0)
    pins = definition.get("pins") or {}
    if expected_pin_count > 0 and len(pins) != expected_pin_count:
        errors.append(f"expected {expected_pin_count} populated pins, found {len(pins)}")
    elif expected_pin_count > 0:
        checks["pin_count"] = "pass"
    pin_numbers = []
    for pin in pins.values():
        pin_number = str((pin or {}).get("number") or "").strip()
        pin_name = str((pin or {}).get("name") or "").strip()
        if pin_number == "" or pin_name == "":
            errors.append("every populated pin needs a number and name")
        pin_numbers.append(pin_number)
    if len(pin_numbers) != len(set(pin_numbers)):
        errors.append("populated pin numbers are not unique")

    dimensions_present = False
    for dimension_field in [
        "dimensions_mm",
        "transistor_dimensions_mm",
        "connector_dimensions_mm",
        "ic_dimensions_mm",
        "display_dimensions_mm",
        "package_dimensions_mm",
    ]:
        if isinstance(definition.get(dimension_field), dict) and definition.get(dimension_field) != {}:
            dimensions_present = True
    if not dimensions_present:
        errors.append("populate-extra has no dimensional data for drawing generation")
    else:
        checks["dimensions"] = "pass"

    datasheet_required = bool(record.get("datasheet_required", True))
    source_directory = PARTS_SOURCE_DIRECTORY / part_id
    source_datasheet = source_directory / "datasheet.pdf"
    source_provenance = source_directory / "datasheet_source.yaml"
    if datasheet_required:
        if not source_datasheet.is_file():
            errors.append("parts_source datasheet.pdf is missing")
        elif source_datasheet.read_bytes()[:5] != b"%PDF-":
            errors.append("parts_source datasheet.pdf does not have a PDF header")
        else:
            checks["source_datasheet"] = "pass"
        if not source_provenance.is_file():
            errors.append("datasheet_source.yaml is missing; import the browser download through the agent")
        else:
            checks["datasheet_provenance"] = "pass"
        file_copies = definition.get("file_copy") or []
        expected_source = f"parts_source/{part_id}/datasheet.pdf"
        if not any(item.get("file_source") == expected_source for item in file_copies if isinstance(item, dict)):
            errors.append("populate-extra is missing the datasheet file_copy action")

    reference_names = [str(item) for item in (record.get("project_references") or [])]
    matched_references, missing_references = _find_project_overrides(reference_names, part_id)
    checks["project_references_matched"] = matched_references
    if missing_references != []:
        errors.append("missing project match overrides: " + ", ".join(missing_references))

    if require_generated:
        part_directory = PARTS_DIRECTORY / part_id
        required_files = [
            "working.yaml",
            "README.md",
        ]
        data_files = [
            "working_svg_outline.svg",
            "working_svg_outline.png",
            "working_svg_outline_300.png",
            "working_svg_assembly.svg",
            "working_svg_assembly_pins.svg",
            "working_svg_square_pins.png",
            "working_svg_square_pins_300.png",
        ]
        if datasheet_required:
            data_files.append("datasheet.pdf")
        missing_files = []
        for required_file in required_files:
            if not (part_directory / required_file).is_file():
                missing_files.append(required_file)
        for data_file in data_files:
            if not (part_directory / "data" / data_file).is_file():
                missing_files.append(f"data/{data_file}")
        if missing_files != []:
            errors.append("generated part is missing: " + ", ".join(missing_files))
        else:
            checks["generated_artifacts"] = "pass"
        working_path = part_directory / "working.yaml"
        if working_path.is_file():
            working = _read_yaml(working_path)
            if bool(working.get("regenerate_pngs", False)):
                errors.append("generated working.yaml still has regenerate_pngs enabled")
            else:
                checks["conservative_png_state"] = "pass"

    return {
        "format_version": 1,
        "ledger_id": str(record.get("ledger_id") or ""),
        "part_id": part_id,
        "status": "pass" if errors == [] else "fail",
        "checks": checks,
        "errors": errors,
        "warnings": warnings,
    }


def write_report(report):
    ledger_id = report.get("ledger_id") or "component"
    report_path = REPORT_DIRECTORY / f"{ledger_id}.yaml"
    _write_yaml(report_path, report)
    return report_path


def build_component(record, regenerate_pngs=False):
    initial_report = validate_implementation(record, require_generated=False)
    if initial_report["status"] != "pass":
        write_report(initial_report)
        raise ValueError("Component definition validation failed before build: " + "; ".join(initial_report["errors"]))

    project_state_before = _project_file_state()
    part_id = record["part_id"]

    import working_oomp_populate
    import working_oomp
    import oomlout_roboclick

    working_oomp_populate.main()
    population_output = io.StringIO()
    with contextlib.redirect_stdout(population_output):
        working_oomp.load_parts(filter=part_id, regenerate_pngs=regenerate_pngs)
    part_directory = PARTS_DIRECTORY / part_id
    generated_working = _read_yaml(part_directory / "working.yaml")
    action_modes = []
    for key in generated_working:
        value = generated_working.get(key)
        if str(key).startswith("oomlout_ai_roboclick_") and isinstance(value, dict):
            if isinstance(value.get("actions"), list):
                action_modes.append(str(key))
    action_modes.sort()
    if action_modes == []:
        raise ValueError(f"No deterministic component Roboclick actions found for {part_id}.")
    oomlout_roboclick.run_folder(folder=str(part_directory), mode=action_modes)
    # Always return generated YAML to the normal conservative PNG state.
    with contextlib.redirect_stdout(population_output):
        working_oomp.load_parts(filter=part_id, regenerate_pngs=False)

    project_state_after = _project_file_state()
    if project_state_before != project_state_after:
        changed_paths = []
        all_paths = sorted(set(project_state_before) | set(project_state_after))
        for path in all_paths:
            if project_state_before.get(path) != project_state_after.get(path):
                changed_paths.append(path)
        raise RuntimeError(
            "Component build changed deferred project output: " + ", ".join(changed_paths)
        )

    report = validate_implementation(record, require_generated=True)
    report["project_output_guard"] = "pass"
    report_path = write_report(report)
    if report["status"] != "pass":
        raise ValueError("Component validation failed after build: " + "; ".join(report["errors"]))
    return report, report_path


def main():
    parser = argparse.ArgumentParser(description="Build and validate one browser-researched OOMP component.")
    parser.add_argument("command", choices=["check", "build"])
    parser.add_argument("record", help="YAML record in kicad_agents/component_records")
    parser.add_argument("--regenerate-pngs", action="store_true")
    arguments = parser.parse_args()

    record_path = Path(arguments.record).resolve()
    record = _read_yaml(record_path)
    if arguments.command == "check":
        report = validate_implementation(record, require_generated=False)
        report_path = write_report(report)
        print(json.dumps(report, indent=2))
        print(f"wrote {report_path}")
        if report["status"] != "pass":
            raise SystemExit(1)
    if arguments.command == "build":
        report, report_path = build_component(record, regenerate_pngs=arguments.regenerate_pngs)
        print(json.dumps(report, indent=2))
        print(f"wrote {report_path}")


if __name__ == "__main__":
    main()
