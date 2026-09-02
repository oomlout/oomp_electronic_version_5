"""Prepare browser-only component research and safely import browser downloads.

This module intentionally has no HTTP client.  It writes explicit research
tasks for a human or an AI agent controlling the available browser.  A browser
download can then be validated and imported into ``parts_source``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from urllib.parse import quote_plus

import yaml


def _component_value(component):
    pcb = component.get("pcb") or {}
    schematic = component.get("schematic") or {}
    units = schematic.get("units") or []
    value = str(pcb.get("value") or "").strip()
    if value == "" and len(units) > 0:
        value = str(units[0].get("value") or "").strip()
    return value


def _should_research(component):
    pcb = component.get("pcb") or {}
    reference = str(component.get("reference") or "").upper()
    value = _component_value(component)
    if pcb == {} or pcb.get("exclude_from_bom", False):
        return False
    if value.upper() == "DNF":
        return False
    if (
        reference.startswith("FID")
        or reference.startswith("H")
        or reference.startswith("LOGO")
        or reference.startswith("SJ")
        or pcb.get("is_mounting_hole", False)
    ):
        return False
    status = str((component.get("oomp") or {}).get("status") or "")
    return status in ["unmatched", "ambiguous"]


def _research_query(component):
    pcb = component.get("pcb") or {}
    match = component.get("oomp") or {}
    inferred = match.get("inferred") or {}
    query_sections = [
        _component_value(component),
        str(inferred.get("mpn") or ""),
        str(pcb.get("library_id") or ""),
    ]
    unique_sections = []
    for query_section in query_sections:
        query_section = query_section.strip()
        if query_section != "" and query_section not in unique_sections:
            unique_sections.append(query_section)
    return " ".join(unique_sections)


def build_browser_research_queue(project_data):
    tasks = []
    grouped = {}
    for component in project_data.get("components", []):
        if not _should_research(component):
            continue
        pcb = component.get("pcb") or {}
        value = _component_value(component)
        footprint = str(pcb.get("library_id") or "")
        group_key = (value, footprint)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(component)

    grouped_keys = list(grouped.keys())
    grouped_keys.sort(key=lambda key: (key[0].lower(), key[1].lower()))
    for task_number in range(len(grouped_keys)):
        group_key = grouped_keys[task_number]
        components = grouped[group_key]
        first_component = components[0]
        match = first_component.get("oomp") or {}
        query = _research_query(first_component)
        references = [str(component.get("reference") or "") for component in components]
        references.sort()
        tasks.append(
            {
                "task_id": f"component_research_{task_number + 1}",
                "status": "needs_browser_research",
                "priority": "high",
                "references": references,
                "value": group_key[0],
                "footprint": group_key[1],
                "query": query,
                "browser_urls": {
                    "lcsc_search": f"https://www.lcsc.com/search?q={quote_plus(query)}",
                    "datasheet_search": f"https://www.google.com/search?q={quote_plus(query + ' datasheet pdf')}",
                },
                "current_match_status": str(match.get("status") or ""),
                "proposed_oomp_id": str(match.get("proposed_oomp_id") or ""),
                "candidate_oomp_ids": [
                    str(candidate.get("oomp_id") or "")
                    for candidate in match.get("candidates", [])
                    if str(candidate.get("oomp_id") or "") != ""
                ],
                "required_result": {
                    "manufacturer": "",
                    "manufacturer_part_number": "",
                    "lcsc_part_number": "",
                    "datasheet_url": "",
                    "confirmed_oomp_id": "",
                    "confidence": "",
                    "evidence_notes": "",
                },
            }
        )

    return {
        "format_version": 1,
        "generated_by": "kicad_agents.browser_research_agent",
        "network_policy": {
            "research_surface": "available interactive browser",
            "python_http_clients_allowed": False,
            "download_method": "browser download followed by validated local import",
        },
        "instructions": [
            "Open the supplied URLs with the available browser; do not replace this with requests, urllib, curl, or an unofficial API.",
            "Confirm exact package, suffix, pinout, and dimensions from the manufacturer datasheet before accepting a match.",
            "Record uncertain results as unresolved instead of guessing.",
            "Download PDFs with the browser, then import them with the import-datasheet command documented in AGENT_GUIDE.md.",
        ],
        "task_count": len(tasks),
        "tasks": tasks,
    }


def _write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=2, ensure_ascii=False)
        output_file.write("\n")


def _write_yaml(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as output_file:
        yaml.safe_dump(data, output_file, sort_keys=False, allow_unicode=True)


def _write_markdown(path, queue):
    lines = [
        "# Browser component research queue",
        "",
        "This queue is generated by Python. Research and downloads must be performed with the available interactive browser.",
        "",
        f"Open tasks: **{queue['task_count']}**",
        "",
        "| Task | References | Value | Footprint | LCSC | Datasheet |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for task in queue["tasks"]:
        references = ", ".join(task["references"])
        lines.append(
            f"| `{task['task_id']}` | {references} | {task['value']} | `{task['footprint']}` | "
            f"[search]({task['browser_urls']['lcsc_search']}) | "
            f"[search]({task['browser_urls']['datasheet_search']}) |"
        )
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_browser_research_queue(project_data, output_directory):
    output_directory = Path(output_directory).resolve()
    queue = build_browser_research_queue(project_data)
    _write_json(output_directory / "browser_research_queue.json", queue)
    _write_yaml(output_directory / "browser_research_queue.yaml", queue)
    _write_markdown(output_directory / "browser_research_queue.md", queue)
    return queue


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as input_file:
        while True:
            block = input_file.read(1024 * 1024)
            if block == b"":
                break
            digest.update(block)
    return digest.hexdigest()


def import_browser_datasheet(part_id, downloaded_file, source_url, parts_source_directory, replace=False):
    downloaded_file = Path(downloaded_file).resolve()
    parts_source_directory = Path(parts_source_directory).resolve()
    if not downloaded_file.is_file():
        raise FileNotFoundError(f"Browser download not found: {downloaded_file}")
    if downloaded_file.suffix.lower() != ".pdf":
        raise ValueError("Datasheet imports must be PDF files.")
    with downloaded_file.open("rb") as input_file:
        if input_file.read(5) != b"%PDF-":
            raise ValueError("Downloaded file does not have a PDF header.")

    destination_directory = parts_source_directory / part_id
    destination_directory.mkdir(parents=True, exist_ok=True)
    destination = destination_directory / "datasheet.pdf"
    downloaded_sha256 = _sha256(downloaded_file)
    if destination.exists() and not replace:
        if _sha256(destination) != downloaded_sha256:
            raise FileExistsError(f"Datasheet already exists: {destination}; pass --replace to update it.")
        # Re-importing the same browser download is safe and useful when an
        # earlier manual copy omitted provenance.
    else:
        shutil.copyfile(downloaded_file, destination)
    provenance = {
        "source_url": source_url,
        "acquisition_method": "interactive_browser",
        "file": "datasheet.pdf",
        "original_filename": downloaded_file.name,
        "file_size_bytes": destination.stat().st_size,
        "sha256": downloaded_sha256,
        "validated_pdf_header": True,
    }
    _write_yaml(destination_directory / "datasheet_source.yaml", provenance)
    return destination


def main():
    parser = argparse.ArgumentParser(description="Prepare browser research or import a browser-downloaded datasheet.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    queue_parser = subparsers.add_parser("queue", help="Build a browser research queue from generated project.json.")
    queue_parser.add_argument("project_json")
    queue_parser.add_argument("--output-dir")

    import_parser = subparsers.add_parser("import-datasheet", help="Validate and import a PDF downloaded with the browser.")
    import_parser.add_argument("part_id")
    import_parser.add_argument("downloaded_file")
    import_parser.add_argument("--source-url", required=True)
    import_parser.add_argument("--parts-source-dir", default="parts_source")
    import_parser.add_argument("--replace", action="store_true")

    arguments = parser.parse_args()
    if arguments.command == "queue":
        project_json = Path(arguments.project_json).resolve()
        project_data = json.loads(project_json.read_text(encoding="utf-8"))
        output_directory = Path(arguments.output_dir).resolve() if arguments.output_dir else project_json.parent
        queue = write_browser_research_queue(project_data, output_directory)
        print(f"wrote {queue['task_count']} browser research tasks to {output_directory}")
    if arguments.command == "import-datasheet":
        destination = import_browser_datasheet(
            arguments.part_id,
            arguments.downloaded_file,
            arguments.source_url,
            arguments.parts_source_dir,
            replace=arguments.replace,
        )
        print(f"imported browser datasheet to {destination}")


if __name__ == "__main__":
    main()
