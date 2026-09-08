"""Deterministically build JLCPCB production files from one KiCad PCB.

KiCad's supported command-line program performs the manufacturing exports.
This module supplies the small JLCPCB-specific layer around it: exact BOM/CPL
headers, OOMP and LCSC enrichment, simple per-project overrides, audit files,
and reproducible ZIP packaging.
"""

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path

import yaml

from kicad_agents.kicad_processing_agent import _parse_pcb
from kicad_agents.run_error_report import log_run_error
from kicad_agents.sexpr import child, children, load, tag, value


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIRECTORY_NAME = "production_auto_generate"
JLC_BOM_COLUMNS = ["Comment", "Designator", "Footprint", "LCSC Part #"]
JLC_CPL_COLUMNS = ["Designator", "Mid X", "Mid Y", "Rotation", "Layer"]
PUBLIC_OUTPUT_FILENAMES = ["gerbers_jlc.zip", "bom_jlc.csv", "cpl_jlc.csv", "bom_missing_lcsc.csv"]


def _natural_key(text):
    pieces = re.split(r"(\d+)", str(text))
    return [int(piece) if piece.isdigit() else piece.lower() for piece in pieces]


def _as_boolean(value_input, default=False):
    if isinstance(value_input, bool):
        return value_input
    if value_input is None or value_input == "":
        return default
    return str(value_input).strip().lower() in {"1", "true", "yes", "on"}


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as input_file:
        for block in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalized_property_name(name):
    return re.sub(r"[^a-z0-9]+", "", str(name).lower())


def _first_property(properties, names):
    normalized = {_normalized_property_name(key): value for key, value in properties.items()}
    for name in names:
        answer = str(normalized.get(_normalized_property_name(name), "")).strip()
        if answer != "":
            return answer
    return ""


def _properties(node):
    properties = {}
    for property_node in children(node, "property"):
        if len(property_node) >= 3:
            properties[str(property_node[1])] = str(property_node[2])
    for text_node in children(node, "fp_text"):
        if len(text_node) < 3:
            continue
        if text_node[1] == "reference" and properties.get("Reference", "") == "":
            properties["Reference"] = str(text_node[2])
        if text_node[1] == "value" and properties.get("Value", "") == "":
            properties["Value"] = str(text_node[2])
    return properties


def _board_flags(board_path):
    """Return native DNP/BOM/position flags not all exposed by older parsers."""
    root = load(board_path)
    flags = {}
    for footprint_node in children(root, "footprint"):
        properties = _properties(footprint_node)
        reference = properties.get("Reference", "")
        attributes_node = child(footprint_node, "attr")
        attributes = []
        if attributes_node is not None:
            attributes = [item for item in attributes_node[1:] if isinstance(item, str)]
        dnp_value = str(value(footprint_node, "dnp", "no")).strip().lower()
        flags[reference] = {
            "dnp": dnp_value == "yes" or "dnp" in attributes,
            "exclude_from_bom": "exclude_from_bom" in attributes,
            "exclude_from_position_files": "exclude_from_pos_files" in attributes,
        }
    return flags


def _available_gerber_layers(board_path):
    root = load(board_path)
    layers_node = child(root, "layers")
    available = []
    if layers_node is not None:
        for layer_node in layers_node[1:]:
            if not isinstance(layer_node, list) or len(layer_node) < 2:
                continue
            layer_name = str(layer_node[1])
            untranslated_name = str(layer_node[3]) if len(layer_node) > 3 else layer_name
            if layer_name in {"F.SilkS", "B.SilkS"}:
                untranslated_name = "F.Silkscreen" if layer_name == "F.SilkS" else "B.Silkscreen"
            available.append((layer_name, untranslated_name))

    wanted = []
    for layer_name, untranslated_name in available:
        if layer_name.endswith(".Cu"):
            wanted.append(untranslated_name)
    for layer_name in ["F.Paste", "B.Paste", "F.SilkS", "B.SilkS", "F.Mask", "B.Mask", "Edge.Cuts"]:
        for available_name, untranslated_name in available:
            if available_name == layer_name:
                wanted.append(untranslated_name)
                break
    return wanted


def find_kicad_cli():
    candidates = []
    configured = os.environ.get("KICAD_CLI", "").strip()
    if configured != "":
        candidates.append(Path(configured))
    discovered = shutil.which("kicad-cli")
    if discovered:
        candidates.append(Path(discovered))

    program_files = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
    kicad_root = program_files / "KiCad"
    if kicad_root.is_dir():
        version_directories = sorted(kicad_root.iterdir(), key=lambda item: _natural_key(item.name), reverse=True)
        for version_directory in version_directories:
            candidates.append(version_directory / "bin" / "kicad-cli.exe")

    checked = []
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in checked:
            continue
        checked.append(resolved)
        if resolved.is_file():
            return resolved
    return None


def _run_command(command, working_directory, accepted_return_codes=None):
    if accepted_return_codes is None:
        accepted_return_codes = {0}
    completed = subprocess.run(
        [str(item) for item in command],
        cwd=str(working_directory),
        capture_output=True,
        text=True,
        timeout=1100,
    )
    if completed.stdout.strip() != "":
        print(completed.stdout.strip())
    if completed.returncode not in accepted_return_codes:
        message = completed.stderr.strip() or completed.stdout.strip() or "KiCad command failed"
        raise RuntimeError(f"{message}\nCommand: {' '.join(str(item) for item in command)}")
    return completed


def _write_csv(path, columns, rows):
    with Path(path).open("w", newline="", encoding="utf-8-sig") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_yaml(path, data):
    Path(path).write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")


def _stable_zip(source_directory, zip_path):
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(Path(source_directory).iterdir(), key=lambda item: item.name.lower()):
            if not path.is_file():
                continue
            info = zipfile.ZipInfo(path.name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def _load_yaml(path):
    path = Path(path)
    if not path.is_file():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _load_json(path):
    path = Path(path)
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _conversion_board(data_directory, details):
    configured = str(details.get("production_oomp_metadata_board", "")).strip()
    if configured != "":
        candidate = Path(configured)
        if not candidate.is_absolute():
            candidate = data_directory.parent / candidate
        if candidate.is_file():
            return candidate.resolve()

    output_directory = data_directory / "oomp_design"
    basename = str(details.get("project_file_basename", "")).strip()
    if basename != "":
        candidate = output_directory / f"{basename}.kicad_pcb"
        if candidate.is_file():
            return candidate.resolve()
    candidates = sorted(output_directory.glob("*.kicad_pcb")) if output_directory.is_dir() else []
    return candidates[0].resolve() if candidates else None


def _project_match_map(data_directory, details, production_footprints):
    matches = {}

    project_data = _load_json(data_directory / "generated_data" / "project.json")
    for component in project_data.get("components", []):
        oomp = component.get("oomp", {})
        if oomp.get("accepted") and oomp.get("oomp_id"):
            matches[component.get("reference", "")] = oomp["oomp_id"]

    conversion_report = _load_yaml(data_directory / "oomp_design" / "conversion_report.yaml")
    for row in conversion_report.get("footprints", []):
        if row.get("reference") and row.get("oomp_id"):
            matches[row["reference"]] = row["oomp_id"]

    for footprint in production_footprints:
        footprint_name = footprint.get("library_id", "").split(":")[-1]
        if footprint_name.startswith(("electronic_", "mechanical_")):
            matches[footprint.get("reference", "")] = footprint_name

    for reference, oomp_id in dict(details.get("project_match_overrides", {})).items():
        if str(oomp_id).strip() != "":
            matches[str(reference)] = str(oomp_id)
    return matches


def _part_supplier_data(parts_directory, oomp_id):
    if not oomp_id:
        return {}
    part = _load_yaml(Path(parts_directory) / oomp_id / "working.yaml")
    return {
        "lcsc": str(part.get("part_number_lcsc", "")).strip(),
        "manufacturer": str(part.get("manufacturer", "")).strip(),
        "manufacturer_part_number": str(part.get("part_number_manufacturer", "")).strip(),
        "name": str(part.get("name_readable", part.get("name", ""))).strip(),
    }


def _parse_position_file(path):
    rows = []
    with Path(path).open("r", newline="", encoding="utf-8-sig") as input_file:
        for row in csv.DictReader(input_file):
            rows.append(
                {
                    "reference": str(row.get("Ref", "")).strip(),
                    "value": str(row.get("Val", "")).strip(),
                    "footprint": str(row.get("Package", "")).strip(),
                    "x": float(row.get("PosX", 0)),
                    "y": float(row.get("PosY", 0)),
                    "rotation": float(row.get("Rot", 0)),
                    "side": str(row.get("Side", "top")).strip().lower(),
                }
            )
    return rows


def _offset_for_reference(offsets, reference):
    offset = offsets.get(reference, [0, 0])
    if isinstance(offset, dict):
        return float(offset.get("x", 0)), float(offset.get("y", 0))
    if isinstance(offset, (list, tuple)) and len(offset) >= 2:
        return float(offset[0]), float(offset[1])
    return 0.0, 0.0


def _automatic_skip_reasons(reference, footprint):
    """Apply the repository's shared, conservative non-BOM policy."""
    reasons = []
    reference_upper = str(reference).strip().upper()
    value_upper = str(footprint.get("value", "")).strip().upper()
    if value_upper == "DNF":
        reasons.append("value is DNF")
    if footprint.get("is_mounting_hole", False):
        reasons.append("dedicated mounting-hole footprint")
    for prefix in ["SJ", "FID", "LOGO"]:
        if reference_upper.startswith(prefix):
            reasons.append(f"reference starts with {prefix}")
            break
    return reasons


def _drc_summary(drc_path):
    report = _load_json(drc_path)
    return {
        "violations": len(report.get("violations", [])),
        "unconnected_items": len(report.get("unconnected_items", [])),
        "schematic_parity_items": len(report.get("schematic_parity", [])),
    }


def _portable_commands(commands, build_directory, output_directory, part_directory):
    portable = []
    replacements = [
        (str(build_directory), str(output_directory.relative_to(part_directory)).replace("\\", "/")),
        (str(part_directory), "."),
    ]
    for command in commands:
        portable_command = []
        for item in command:
            text = str(item)
            for old_text, new_text in replacements:
                text = text.replace(old_text, new_text)
            portable_command.append(text.replace("\\", "/"))
        portable.append(portable_command)
    return portable


def build_component_rows(position_rows, production_footprints, metadata_footprints, details, parts_directory):
    """Build JLC rows plus OOMP/pad audit data using explicit, editable loops."""
    production_by_reference = {}
    for footprint in production_footprints:
        production_by_reference[footprint.get("reference", "")] = footprint
    metadata_by_reference = {}
    for footprint in metadata_footprints:
        metadata_by_reference[footprint.get("reference", "")] = footprint

    data_directory = Path(details["directory"]) / "data"
    matches = _project_match_map(data_directory, details, production_footprints)
    exclude_references = {str(item) for item in details.get("production_exclude_references", [])}
    lcsc_overrides = {str(key): str(item) for key, item in dict(details.get("production_lcsc_overrides", {})).items()}
    rotation_offsets = dict(details.get("production_rotation_offsets", {}))
    position_offsets = dict(details.get("production_position_offsets_mm", {}))
    flags = _board_flags(Path(details["production_board_resolved"]))

    cpl_rows = []
    components = []
    skipped = []
    unmatched = []
    for position in sorted(position_rows, key=lambda item: _natural_key(item["reference"])):
        reference = position["reference"]
        footprint = production_by_reference.get(reference, {})
        reference_flags = flags.get(reference, {})
        skip_reasons = []
        if reference in exclude_references:
            skip_reasons.append("listed in production_exclude_references")
        if reference_flags.get("dnp"):
            skip_reasons.append("KiCad DNP flag")
        if reference_flags.get("exclude_from_bom"):
            skip_reasons.append("KiCad exclude-from-BOM flag")
        if reference_flags.get("exclude_from_position_files"):
            skip_reasons.append("KiCad exclude-from-position-files flag")
        skip_reasons.extend(_automatic_skip_reasons(reference, footprint))
        if skip_reasons:
            skipped.append({"reference": reference, "reasons": skip_reasons})
            continue

        properties = footprint.get("properties", {})
        oomp_id = matches.get(reference, "")
        supplier = _part_supplier_data(parts_directory, oomp_id)
        lcsc = lcsc_overrides.get(reference, "").strip()
        if lcsc == "":
            lcsc = _first_property(properties, ["LCSC Part #", "LCSC", "JLCPCB Part #", "JLCPCB", "part_number_lcsc"])
        if lcsc == "":
            lcsc = supplier.get("lcsc", "")

        manufacturer_part_number = _first_property(
            properties,
            ["Manufacturer Part Number", "MPN", "Manufacturer PN", "part_number_manufacturer"],
        )
        if manufacturer_part_number == "":
            manufacturer_part_number = supplier.get("manufacturer_part_number", "")
        manufacturer = _first_property(properties, ["Manufacturer", "Mfr"])
        if manufacturer == "":
            manufacturer = supplier.get("manufacturer", "")

        x_offset, y_offset = _offset_for_reference(position_offsets, reference)
        rotation_offset = float(rotation_offsets.get(reference, 0))
        rotation = position["rotation"] + rotation_offset
        while rotation >= 360:
            rotation -= 360
        while rotation < -360:
            rotation += 360

        cpl_rows.append(
            {
                "Designator": reference,
                "Mid X": f"{position['x'] + x_offset:.4f}",
                "Mid Y": f"{position['y'] + y_offset:.4f}",
                "Rotation": f"{rotation:.2f}",
                "Layer": "Bottom" if position["side"] == "bottom" else "Top",
            }
        )

        metadata_footprint = metadata_by_reference.get(reference, footprint)
        pads = []
        for pad in metadata_footprint.get("pads", []):
            pads.append(
                {
                    "name": str(pad.get("number", "")),
                    "type": str(pad.get("type", "")),
                    "net": pad.get("net"),
                    "x_mm": pad.get("position", {}).get("x"),
                    "y_mm": pad.get("position", {}).get("y"),
                }
            )
        component = {
            "reference": reference,
            "value": footprint.get("value", position["value"]),
            "footprint": footprint.get("library_id", position["footprint"]),
            "oomp_id": oomp_id or None,
            "lcsc_part_number": lcsc or None,
            "manufacturer": manufacturer or None,
            "manufacturer_part_number": manufacturer_part_number or None,
            "position": {
                "x_mm": position["x"] + x_offset,
                "y_mm": position["y"] + y_offset,
                "rotation_degrees_counter_clockwise": rotation,
                "layer": "Bottom" if position["side"] == "bottom" else "Top",
            },
            "pad_name_source": "oomp_design" if reference in metadata_by_reference else "production_board",
            "pads": pads,
        }
        components.append(component)
        if lcsc == "":
            unmatched.append(
                {
                    "Designator": reference,
                    "Comment": component["value"],
                    "Footprint": component["footprint"],
                    "OOMP ID": oomp_id,
                    "Reason": "No verified LCSC part number",
                }
            )

    groups = defaultdict(list)
    for component in components:
        group_key = (
            component["value"],
            component["footprint"],
            component["lcsc_part_number"] or "",
        )
        groups[group_key].append(component["reference"])
    bom_rows = []
    for group_key in sorted(groups, key=lambda item: [str(value_input).lower() for value_input in item]):
        value_text, footprint_text, lcsc = group_key
        references = sorted(groups[group_key], key=_natural_key)
        bom_rows.append(
            {
                "Comment": value_text,
                "Designator": ",".join(references),
                "Footprint": footprint_text,
                "LCSC Part #": lcsc,
            }
        )
    return bom_rows, cpl_rows, components, skipped, unmatched


def _export_kicad_files(kicad_cli, board_path, build_directory):
    gerber_directory = build_directory / "gerbers"
    gerber_directory.mkdir(parents=True, exist_ok=True)
    layers = _available_gerber_layers(board_path)
    if "Edge.Cuts" not in layers:
        raise ValueError("The board has no Edge.Cuts layer to export.")

    gerber_command = [
        kicad_cli,
        "pcb",
        "export",
        "gerbers",
        "--output",
        gerber_directory,
        "--layers",
        ",".join(layers),
        "--subtract-soldermask",
        "--precision",
        "6",
        "--check-zones",
        board_path,
    ]
    _run_command(gerber_command, board_path.parent)

    drill_command = [
        kicad_cli,
        "pcb",
        "export",
        "drill",
        "--output",
        gerber_directory,
        "--format",
        "excellon",
        "--drill-origin",
        "absolute",
        "--excellon-zeros-format",
        "decimal",
        "--excellon-oval-format",
        "route",
        "--excellon-units",
        "mm",
        "--excellon-separate-th",
        "--generate-map",
        "--map-format",
        "gerberx2",
        "--generate-report",
        "--report-path",
        gerber_directory / "drill_report.txt",
        board_path,
    ]
    _run_command(drill_command, board_path.parent)

    raw_position_file = build_directory / "kicad_position_raw.csv"
    position_command = [
        kicad_cli,
        "pcb",
        "export",
        "pos",
        "--format",
        "csv",
        "--units",
        "mm",
        "--side",
        "both",
        "--exclude-dnp",
        "--output",
        raw_position_file,
        board_path,
    ]
    _run_command(position_command, board_path.parent)

    drc_command = [
        kicad_cli,
        "pcb",
        "drc",
        "--output",
        build_directory / "drc.json",
        "--format",
        "json",
        "--units",
        "mm",
        "--severity-all",
        board_path,
    ]
    drc_result = _run_command(drc_command, board_path.parent, accepted_return_codes={0})
    return layers, raw_position_file, [gerber_command, drill_command, position_command, drc_command], drc_result


def _source_board(part_directory, details):
    configured = str(details.get("production_board_source", "")).strip()
    if configured == "":
        return (part_directory / "data" / "kicad_file.kicad_pcb").resolve()
    candidate = Path(configured)
    if not candidate.is_absolute():
        candidate = part_directory / candidate
    return candidate.resolve()


def _replace_generated_directory(build_directory, output_directory):
    data_directory = output_directory.parent.resolve()
    if output_directory.resolve().parent != data_directory or output_directory.name != OUTPUT_DIRECTORY_NAME:
        raise ValueError(f"Refusing to replace unexpected output directory: {output_directory}")
    if output_directory.exists():
        shutil.rmtree(output_directory)
    build_directory.replace(output_directory)


def _validate_public_output_layout(build_directory):
    expected = {"data"}
    for filename in PUBLIC_OUTPUT_FILENAMES:
        expected.add(filename)
    actual = {path.name for path in Path(build_directory).iterdir()}
    if actual != expected:
        raise RuntimeError(f"Unexpected production root files: expected {sorted(expected)}, found {sorted(actual)}")


def _write_failure_status(output_directory, error):
    output_directory.mkdir(parents=True, exist_ok=True)
    status_directory = output_directory / "data"
    status_directory.mkdir(parents=True, exist_ok=True)
    status = {
        "generated_by": "kicad_agents.production_jlc_agent",
        "status": "failed",
        "message": str(error),
        "error_type": type(error).__name__,
    }
    (status_directory / "generation_status.yaml").write_text(
        yaml.safe_dump(status, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return status


def generate_jlc_production_files(details):
    part_directory = Path(details["directory"]).resolve()
    data_directory = part_directory / "data"
    output_directory = data_directory / OUTPUT_DIRECTORY_NAME
    try:
        board_path = _source_board(part_directory, details)
        if not board_path.is_file():
            raise FileNotFoundError(f"Production KiCad board is missing: {board_path}")
        kicad_cli = find_kicad_cli()
        if kicad_cli is None:
            raise FileNotFoundError("kicad-cli was not found. Install KiCad or set KICAD_CLI.")

        build_directory = Path(tempfile.mkdtemp(prefix="production_auto_generate_build_", dir=data_directory))
        try:
            internal_directory = build_directory / "data"
            internal_directory.mkdir(parents=True, exist_ok=True)
            layers, raw_position_file, commands, _ = _export_kicad_files(kicad_cli, board_path, internal_directory)
            production_board_data = _parse_pcb(board_path, part_directory)
            production_footprints = production_board_data["footprints"]

            metadata_board = _conversion_board(data_directory, details)
            metadata_footprints = []
            if metadata_board is not None:
                metadata_footprints = _parse_pcb(metadata_board, part_directory)["footprints"]

            action_details = dict(details)
            action_details["production_board_resolved"] = str(board_path)
            parts_directory = Path(details.get("parts_directory", "parts"))
            if not parts_directory.is_absolute():
                parts_directory = REPOSITORY_ROOT / parts_directory
            bom_rows, cpl_rows, components, skipped, unmatched = build_component_rows(
                _parse_position_file(raw_position_file),
                production_footprints,
                metadata_footprints,
                action_details,
                parts_directory,
            )

            _write_csv(build_directory / "bom_jlc.csv", JLC_BOM_COLUMNS, bom_rows)
            _write_csv(build_directory / "cpl_jlc.csv", JLC_CPL_COLUMNS, cpl_rows)
            unmatched_columns = ["Designator", "Comment", "Footprint", "OOMP ID", "Reason"]
            _write_csv(build_directory / "bom_missing_lcsc.csv", unmatched_columns, unmatched)
            component_data = {
                "format_version": 1,
                "source_board": str(board_path.relative_to(part_directory)).replace("\\", "/"),
                "oomp_metadata_board": (
                    str(metadata_board.relative_to(part_directory)).replace("\\", "/") if metadata_board else None
                ),
                "components": components,
                "skipped_components": skipped,
            }
            _write_json(internal_directory / "components.json", component_data)
            _write_yaml(internal_directory / "components.yaml", component_data)
            _stable_zip(internal_directory / "gerbers", build_directory / "gerbers_jlc.zip")

            cli_version = _run_command([kicad_cli, "version"], board_path.parent).stdout.strip()
            generated_files = []
            for generated_file in sorted(build_directory.rglob("*")):
                if not generated_file.is_file() or generated_file.name in {"manifest.json", "manifest.yaml", "generation_status.yaml"}:
                    continue
                generated_files.append(
                    {
                        "path": str(generated_file.relative_to(build_directory)).replace("\\", "/"),
                        "bytes": generated_file.stat().st_size,
                        "sha256": _sha256(generated_file),
                    }
                )
            drc_summary = _drc_summary(internal_directory / "drc.json")
            needs_drc_review = sum(drc_summary.values()) > 0
            needs_bom_review = len(unmatched) > 0
            if needs_bom_review and needs_drc_review:
                status = "generated_needs_review"
            elif needs_bom_review:
                status = "generated_needs_bom_review"
            elif needs_drc_review:
                status = "generated_needs_drc_review"
            else:
                status = "generated"
            manifest = {
                "format_version": 1,
                "generated_by": "kicad_agents.production_jlc_agent",
                "status": status,
                "strategy": "KiCad's native CLI exports fabrication and position data; Python writes JLCPCB CSVs and audit data.",
                "source_board": str(board_path.relative_to(part_directory)).replace("\\", "/"),
                "source_board_sha256": _sha256(board_path),
                "oomp_metadata_board": (
                    str(metadata_board.relative_to(part_directory)).replace("\\", "/") if metadata_board else None
                ),
                "kicad_cli": str(kicad_cli),
                "kicad_version": cli_version,
                "gerber_layers": layers,
                "jlc_bom_columns": JLC_BOM_COLUMNS,
                "jlc_cpl_columns": JLC_CPL_COLUMNS,
                "summary": {
                    "bom_groups": len(bom_rows),
                    "placed_components": len(cpl_rows),
                    "skipped_components": len(skipped),
                    "components_missing_lcsc": len(unmatched),
                    "gerber_files": len(list((internal_directory / "gerbers").glob("*"))),
                    "drc": drc_summary,
                },
                "settings": {
                    "production_exclude_references": list(details.get("production_exclude_references", [])),
                    "production_lcsc_overrides": dict(details.get("production_lcsc_overrides", {})),
                    "production_rotation_offsets": dict(details.get("production_rotation_offsets", {})),
                    "production_position_offsets_mm": dict(details.get("production_position_offsets_mm", {})),
                },
                "commands": _portable_commands(commands, build_directory, output_directory, part_directory),
                "files": generated_files,
            }
            _write_json(internal_directory / "manifest.json", manifest)
            _write_yaml(internal_directory / "manifest.yaml", manifest)
            generation_status = {
                "generated_by": "kicad_agents.production_jlc_action",
                "status": status,
                "message": "JLCPCB production files generated. Review manifest.yaml and all fabrication files before ordering.",
                "components_missing_lcsc": len(unmatched),
                "drc": drc_summary,
                "gerber_zip": "gerbers_jlc.zip",
                "bom": "bom_jlc.csv",
                "cpl": "cpl_jlc.csv",
                "manifest": "data/manifest.yaml",
            }
            _write_yaml(internal_directory / "generation_status.yaml", generation_status)
            _validate_public_output_layout(build_directory)
            _replace_generated_directory(build_directory, output_directory)
            print(f"JLCPCB production files: {output_directory}")
            return output_directory
        finally:
            if build_directory.exists() and output_directory.exists() is False:
                shutil.rmtree(build_directory, ignore_errors=True)
    except Exception as error:
        _write_failure_status(output_directory, error)
        log_run_error("production_jlc_agent", error)
        print(f"JLCPCB production generation failed: {error}")
        return None
