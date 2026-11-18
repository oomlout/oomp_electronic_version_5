"""Build and validate one researched OOMP component at a time.

This agent deliberately performs no online research.  An AI agent or person uses
the available interactive browser, records the verified result in a small YAML
file, and imports the browser-downloaded datasheet.  This module then provides a
single deterministic entry point for the repetitive local work:

* verify that the family populate and populate-extra files contain the part;
* regenerate only the selected OOMP part;
* run only that part's Roboclick actions;
* refresh its navigation ancestors and repackage the KiCad library;
* confirm identifiers, pins, dimensions, datasheet provenance, README, diagrams
  and conservative PNG state;
* report requested project integration as a separate external review.
"""

from __future__ import annotations

import argparse
import contextlib
import os
import time
import importlib
import io
import json
import re
from pathlib import Path

import yaml

from oomp_populate_helper import build_oomp_id
from working_oomp_metadata import taxonomy_values
from component_taxonomy import is_function_first_ic_id, validate_ic_taxonomy


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
RECORD_DIRECTORY = REPOSITORY_ROOT / "kicad_agents" / "component_records"
REPORT_DIRECTORY = REPOSITORY_ROOT / "kicad_agents" / "generated" / "component_additions"
PARTS_SOURCE_DIRECTORY = REPOSITORY_ROOT / "parts_source"
PARTS_DIRECTORY = REPOSITORY_ROOT / "parts"


def _read_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def _write_yaml(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(data, output_file, sort_keys=False, allow_unicode=True)


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
        validate_ic_taxonomy(candidate)
        if build_oomp_id(candidate) == part_id:
            matches.append(candidate)
    if len(matches) != 1:
        raise ValueError(
            f"Expected one {family} population record for {part_id}, found {len(matches)}."
        )

    extras = {part_id: dict(matches[0])}
    extra_module.main(extras_dict=extras)
    return extras[part_id]


def validate_record(record):
    errors = []
    warnings = []
    required_text_fields = ["ledger_id", "family", "part_id", "package"]
    for field_name in required_text_fields:
        if str(record.get(field_name) or "").strip() == "":
            errors.append(f"research record is missing {field_name}")

    part_id = str(record.get("part_id") or "")
    if record.get("family") == "ic" and not is_function_first_ic_id(part_id):
        errors.append("IC part_id must use function, subtype, package, manufacturer, MPN order; package-first IDs are retired")
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


def prepare_component_source(record):
    """Populate only the selected source record, preserving unrelated components."""
    from oomp_populate_helper import write_extras
    import working_oomp_populate_svg
    import working_oomp_populate_category
    import working_oomp_populate_kicad
    import working_oomp_metadata

    errors, _ = validate_record(record)
    if errors:
        raise ValueError('; '.join(errors))
    definition = _load_populated_definition(record)
    working_oomp_populate_svg.add_svg_details(definition)
    working_oomp_populate_category.add_category(definition)
    working_oomp_populate_kicad.add_kicad_details(definition)
    working_oomp_metadata.add_readable_metadata([definition])
    original_directory = Path.cwd()
    try:
        os.chdir(REPOSITORY_ROOT)
        write_extras([definition])
    finally:
        os.chdir(original_directory)
    return PARTS_SOURCE_DIRECTORY / record['part_id'] / 'working.yaml'


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

    generic_part_number = str(research.get("generic_part_number") or "").strip()
    if generic_part_number != "":
        if definition.get("part_number_generic") != generic_part_number:
            errors.append("populate-extra generic part number does not match the research record")
        else:
            checks["generic_part_number"] = "pass"

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

    related_parts = definition.get('related_parts') or []
    if related_parts:
        related_errors = []
        for related in related_parts:
            target = str(related.get('oomp_id', ''))
            if not re.fullmatch(r'[a-z0-9_]+', target) or target == part_id:
                related_errors.append('compatible component needs a different canonical OOMP ID')
                continue
            if not (PARTS_SOURCE_DIRECTORY / target / 'working.yaml').is_file():
                related_errors.append(f'prepare the compatible component source before building: {target}')
            if not related.get('evidence_url') or not related.get('relationship'):
                related_errors.append(f'compatible component lacks relationship/evidence: {target}')
            quantity = related.get('quantity')
            if quantity is not None and (type(quantity) is not int or quantity < 1):
                related_errors.append(f'compatible component quantity must be a positive integer: {target}')
        errors.extend(related_errors)
        checks['compatible_components'] = 'fail' if related_errors else 'pass'

    datasheet_required = bool(record.get("datasheet_required", True))
    source_directory = PARTS_SOURCE_DIRECTORY / part_id
    source_datasheet = source_directory / "datasheet.pdf"
    source_provenance = source_directory / "datasheet_source.yaml"
    # Parts whose datasheet is byte-identical to another part's keep one shared
    # PDF and record its folder in oomp_datasheet_common_with.
    common_with = str(definition.get("oomp_datasheet_common_with", "")).strip()
    if not common_with and (source_directory / "working.yaml").is_file():
        common_with = str(_read_yaml(source_directory / "working.yaml").get("oomp_datasheet_common_with", "")).strip()
    if common_with:
        shared_directory = PARTS_SOURCE_DIRECTORY / common_with
        shared_datasheet = shared_directory / "datasheet.pdf"
        if shared_datasheet.is_file():
            source_datasheet = shared_datasheet
            if not source_provenance.is_file():
                source_provenance = shared_directory / "datasheet_source.yaml"
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
        expected_sources = {expected_source}
        if common_with:
            expected_sources.add(f"parts_source/{common_with}/datasheet.pdf")
        if not any(item.get("file_source") in expected_sources for item in file_copies if isinstance(item, dict)):
            errors.append("populate-extra is missing the datasheet file_copy action")

    reference_names = [str(item) for item in (record.get("project_references") or [])]
    checks["project_reference_review"] = {
        "status": "external_review_required" if reference_names else "not_requested",
        "references": reference_names,
        "repository": "https://github.com/oomlout/oomp_electronic_project_version_5",
    }

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
            "working_svg_assembly.png",
            "working_svg_assembly_pins.svg",
            "working_svg_assembly_pins.png",
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


def navigation_part_ids(definition):
    """Return only this part's navigation ancestors, in root-to-leaf order."""
    identifiers = ["navigation"]
    current = "navigation"
    for value in taxonomy_values(definition)[:-1]:
        current += "_" + value
        identifiers.append(current)
    return identifiers


def _action_modes(working):
    modes = []
    for key, value in working.items():
        if str(key).startswith("oomlout_ai_roboclick_") and isinstance(value, dict):
            if isinstance(value.get("actions"), list):
                modes.append(str(key))
    return sorted(modes)


def _refresh_component_indexes(record, skip_shared_refresh=False):
    """Refresh ancestor READMEs and the library package without rebuilding boards."""
    import working_oomp
    import oomlout_roboclick
    from kicad_agents.kicad_library_agent import package_libraries

    # Definitions are lightweight; refresh the generated navigation tree via the
    # dedicated action instead of synthesizing navigation parts in parts/.
    if skip_shared_refresh:
        # Batch mode: the full-tree navigation sweep and the kicad_libraries
        # packaging are shared outputs; the batch driver runs them once at the
        # end instead of once per part.
        return [], {"status": "deferred to batch shared refresh"}
    import action_generate_navigation
    action_generate_navigation.generate(filter_text=record['part_id'])
    identifiers = navigation_part_ids(_load_populated_definition(record))
    for identifier in identifiers:
        directory = PARTS_DIRECTORY / identifier
        # Navigation pages now render into the top-level navigation/ tree
        # (refreshed above); only ancestors that are real part folders keep
        # roboclick-run index actions.
        if not (directory / "working.yaml").is_file():
            continue
        working = _read_yaml(directory / "working.yaml")
        oomlout_roboclick.run_folder(folder=str(directory), mode=_action_modes(working))
    library_report = package_libraries(PARTS_DIRECTORY, REPOSITORY_ROOT / "kicad_libraries")
    return identifiers, library_report


def build_component(record, regenerate_pngs=False, skip_shared_refresh=False, skip_populate=False):
    initial_report = validate_implementation(record, require_generated=False)
    if initial_report["status"] != "pass":
        write_report(initial_report)
        raise ValueError("Component definition validation failed before build: " + "; ".join(initial_report["errors"]))

    part_id = record["part_id"]

    import working_oomp_populate
    import working_oomp
    import oomlout_roboclick

    if skip_populate and (PARTS_DIRECTORY.parent / "parts_source" / part_id / "working.yaml").is_file():
        # single-part fast path: the caller just wrote this part's
        # parts_source record; skip the whole-tree populate rewrite (and the
        # cross-worker lock that only guards that rewrite)
        pass
    else:
        # populate.main() rewrites the whole parts_source tree (including the
        # datasheet dedupe pass); serialize it across parallel batch workers so
        # concurrent writes cannot collide on Windows or race the dedupe.
        _populate_lock = PARTS_DIRECTORY.parent / "tmp" / "populate_main.lock"
        _populate_lock.parent.mkdir(exist_ok=True)
        import time as _time
        _lock_start = _time.time()
        while True:
            try:
                _lock_fd = os.open(str(_populate_lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                break
            except FileExistsError:
                # a lock older than 15 minutes belongs to a dead worker
                try:
                    if _time.time() - _populate_lock.stat().st_mtime > 900:
                        _populate_lock.unlink(missing_ok=True)
                        continue
                except OSError:
                    pass  # raced away; just retry
                if _time.time() - _lock_start > 1800:
                    raise RuntimeError("populate lock unavailable for 30 minutes")
                _time.sleep(2)
        try:
            working_oomp_populate.main()
        finally:
            os.close(_lock_fd)
            _populate_lock.unlink(missing_ok=True)
    population_output = io.StringIO()
    with contextlib.redirect_stdout(population_output):
        working_oomp.load_parts(filter=part_id, regenerate_pngs=regenerate_pngs)
    part_directory = PARTS_DIRECTORY / part_id
    generated_working = _read_yaml(part_directory / "working.yaml")
    action_modes = _action_modes(generated_working)
    if action_modes == []:
        raise ValueError(f"No deterministic component Roboclick actions found for {part_id}.")
    oomlout_roboclick.run_folder(folder=str(part_directory), mode=action_modes)
    # Always return generated YAML to the normal conservative PNG state.
    with contextlib.redirect_stdout(population_output):
        working_oomp.load_parts(filter=part_id, regenerate_pngs=False)

    navigation_ids, library_report = _refresh_component_indexes(record, skip_shared_refresh)

    report = validate_implementation(record, require_generated=True)
    report["validation_scope"] = "component; project integration is reviewed separately"
    report["navigation_ancestors_refreshed"] = navigation_ids
    report["kicad_library_package"] = library_report
    report_path = write_report(report)
    if report["status"] != "pass":
        raise ValueError("Component validation failed after build: " + "; ".join(report["errors"]))
    return report, report_path


def main():
    parser = argparse.ArgumentParser(description="Build and validate one browser-researched OOMP component.")
    parser.add_argument("command", choices=["prepare", "check", "build"])
    parser.add_argument("record", help="YAML record in kicad_agents/component_records")
    parser.add_argument("--regenerate-pngs", action="store_true")
    parser.add_argument("--skip-shared-refresh", action="store_true",
                        help="defer the navigation sweep and kicad_libraries packaging "
                             "to a batch-end shared refresh")
    parser.add_argument("--skip-populate", action="store_true",
                        help="parts_source was just regenerated for this part; "
                             "skip the whole-tree populate rewrite")
    arguments = parser.parse_args()

    record_path = Path(arguments.record).resolve()
    record = _read_yaml(record_path)
    if arguments.command == "prepare":
        print(f"wrote {prepare_component_source(record)}")
    if arguments.command == "check":
        report = validate_implementation(record, require_generated=False)
        report_path = write_report(report)
        print(json.dumps(report, indent=2))
        print(f"wrote {report_path}")
        if report["status"] != "pass":
            raise SystemExit(1)
    if arguments.command == "build":
        report, report_path = build_component(
            record, regenerate_pngs=arguments.regenerate_pngs,
            skip_shared_refresh=arguments.skip_shared_refresh,
            skip_populate=arguments.skip_populate)
        print(json.dumps(report, indent=2))
        print(f"wrote {report_path}")


if __name__ == "__main__":
    main()
