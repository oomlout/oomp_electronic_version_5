"""Queue-driven agent for adding one GitHub PCB repository at a time."""

from __future__ import annotations

import argparse
from pathlib import Path

from kicad_agents.project_import_helpers import (
    DEFAULT_PROJECT_DATA,
    DEFAULT_QUEUE,
    DEFAULT_RUN_DIRECTORY,
    append_project_record,
    build_project_record,
    find_queue_repository,
    inspect_repository,
    load_decisions,
    mark_queue_added,
    mark_queue_too_old,
    run_timestamp,
    select_next_repository,
    write_yaml,
)


def _run_slug(full_name: str) -> str:
    return full_name.lower().replace("/", "_").replace("-", "_")


def prepare(
    queue_path: Path,
    project_data: Path,
    run_root: Path,
    repository: str | None = None,
) -> tuple[dict, Path]:
    if repository:
        entry = find_queue_repository(queue_path, repository)
        skipped_existing = []
    else:
        selection = select_next_repository(queue_path, project_data)
        entry = selection.entry
        skipped_existing = list(selection.skipped_existing)
    inspection = inspect_repository(entry)
    auto_excluded = []
    usable_boards = []
    for candidate in inspection["selected_boards"]:
        if candidate.get("auxiliary_words"):
            excluded = dict(candidate)
            excluded["exclude_reason"] = "automatic auxiliary source: " + ", ".join(candidate["auxiliary_words"])
            auto_excluded.append(excluded)
        else:
            usable_boards.append(candidate)
    inspection["selected_boards"] = usable_boards
    inspection["excluded_boards"] = inspection.get("excluded_boards", []) + auto_excluded
    usable_paths = {item["path"] for item in usable_boards}
    inspection["ambiguous"] = [
        item for item in inspection.get("ambiguous", []) if item["path"] in usable_paths
    ]
    inspection["review_required"] = bool(inspection["ambiguous"]) and inspection.get("ingestion_status") != "too_old"
    inspection["queue_rank"] = entry.get("rank")
    inspection["queue_updated_at"] = entry.get("updated_at")
    inspection["skipped_existing_queue_rows"] = skipped_existing
    inspection["prepared_at"] = run_timestamp()
    run_directory = run_root / _run_slug(inspection["repository"])
    inspection_path = write_yaml(run_directory / "inspection.yaml", inspection)
    if inspection["review_required"]:
        decision_template = {
            "repository": inspection["repository"],
            "include_paths": [item["path"] for item in inspection["selected_boards"]],
            "exclude_paths": [],
            "overrides": {},
            "note": "",
        }
        write_yaml(run_directory / "decision.yaml", decision_template)
    return inspection, inspection_path


def commit(
    inspection_path: Path,
    queue_path: Path,
    project_data: Path,
    decisions_path: Path | None = None,
    allow_unreviewed: bool = False,
) -> dict:
    import yaml

    inspection = yaml.safe_load(inspection_path.read_text(encoding="utf-8")) or {}
    if inspection.get("ingestion_status") == "too_old":
        note = inspection.get("ingest_note") or "too old: legacy binary Eagle source"
        mark_queue_too_old(queue_path, inspection["repository"], note)
        python_decisions = [
            {"kind": "queue_selection", "count": 1},
            {"kind": "temporary_git_clone", "count": 1},
            {"kind": "board_file_inventory", "count": inspection["board_file_count"]},
            {"kind": "legacy_eagle_binary_gate", "count": len(inspection["legacy_binary_files"])},
            {"kind": "queue_ingested_note", "count": 1},
        ]
        result = {
            "repository": inspection["repository"],
            "commit": inspection["commit"],
            "definition_file": None,
            "boards_added": [],
            "boards_excluded": inspection.get("selected_boards", []) + inspection.get("excluded_boards", []),
            "ingestion_status": "too_old",
            "ingest_note": note,
            "legacy_binary_files": inspection["legacy_binary_files"],
            "python_work": {
                "decision_units": sum(item["count"] for item in python_decisions),
                "details": python_decisions,
            },
            "llm_work": {"decision_units": 0, "details": []},
            "completed_at": run_timestamp(),
        }
        write_yaml(inspection_path.parent / "result.yaml", result)
        return result
    if inspection.get("review_required") and decisions_path is None and not allow_unreviewed:
        raise RuntimeError(
            f"Review required. Complete {inspection_path.parent / 'decision.yaml'} and rerun commit."
        )
    selected, llm_decisions = load_decisions(decisions_path, inspection)
    if not selected:
        import yaml

        decision_data = yaml.safe_load(decisions_path.read_text(encoding="utf-8")) if decisions_path else {}
        note = str((decision_data or {}).get("note") or "no importable source boards selected")
        mark_queue_too_old(queue_path, inspection["repository"], note)
        result = {
            "repository": inspection["repository"],
            "commit": inspection["commit"],
            "definition_file": None,
            "boards_added": [],
            "boards_excluded": inspection.get("selected_boards", []) + inspection.get("excluded_boards", []),
            "ingestion_status": "ingested_no_project",
            "ingest_note": note,
            "python_work": {
                "decision_units": 4,
                "details": [
                    {"kind": "queue_selection", "count": 1},
                    {"kind": "temporary_git_clone", "count": 1},
                    {"kind": "board_file_inventory", "count": inspection["board_file_count"]},
                    {"kind": "queue_ingested_note", "count": 1},
                ],
            },
            "llm_work": {
                "decision_units": sum(item.get("count", 1) for item in llm_decisions),
                "details": llm_decisions,
            },
            "completed_at": run_timestamp(),
        }
        write_yaml(inspection_path.parent / "result.yaml", result)
        return result
    selected_paths = {item["path"] for item in selected}
    decision_exclusions = [
        {
            "path": item["path"],
            "exclude_reason": "review decision",
        }
        for item in inspection["selected_boards"]
        if item["path"] not in selected_paths
    ]
    owner, _repository = inspection["repository"].split("/", 1)
    entry = {
        "full_name": inspection["repository"],
        "url": inspection["url"],
        "default_branch": inspection["default_branch"],
    }
    project = build_project_record(entry, selected)
    destination = append_project_record(owner, project, project_data)
    mark_queue_added(queue_path, inspection["repository"])
    python_decisions = [
        {"kind": "queue_selection", "count": 1},
        {"kind": "temporary_git_clone", "count": 1},
        {"kind": "board_file_inventory", "count": inspection["board_file_count"]},
        {"kind": "current_version_selection", "count": len(selected)},
        {"kind": "project_metadata_generation", "count": len(selected)},
        {"kind": "yaml_append_and_validation", "count": 1},
        {"kind": "queue_status_update", "count": 1},
    ]
    python_count = sum(item["count"] for item in python_decisions)
    llm_count = sum(item.get("count", 1) for item in llm_decisions)
    result = {
        "repository": inspection["repository"],
        "commit": inspection["commit"],
        "definition_file": str(destination),
        "boards_added": [
            {"board": item["board"], "path": item["path"], "format": item["source_format"]}
            for item in selected
        ],
        "boards_excluded": inspection.get("excluded_boards", []) + decision_exclusions,
        "python_work": {"decision_units": python_count, "details": python_decisions},
        "llm_work": {"decision_units": llm_count, "details": llm_decisions},
        "completed_at": run_timestamp(),
    }
    write_yaml(inspection_path.parent / "result.yaml", result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["next", "prepare", "commit", "run"])
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--project-data", type=Path, default=DEFAULT_PROJECT_DATA)
    parser.add_argument("--run-root", type=Path, default=DEFAULT_RUN_DIRECTORY)
    parser.add_argument("--inspection", type=Path)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--repository", help="Inspect a named queue repository, including an existing one")
    parser.add_argument("--allow-unreviewed", action="store_true")
    arguments = parser.parse_args()

    if arguments.command == "next":
        selection = select_next_repository(arguments.queue, arguments.project_data)
        print(selection.entry["full_name"])
        return
    if arguments.command == "prepare":
        inspection, inspection_path = prepare(
            arguments.queue, arguments.project_data, arguments.run_root, arguments.repository
        )
        print(inspection_path)
        print(f"review_required={inspection['review_required']}")
        return
    if arguments.command == "commit":
        if arguments.inspection is None:
            parser.error("commit requires --inspection")
        result = commit(
            arguments.inspection, arguments.queue, arguments.project_data,
            arguments.decisions, arguments.allow_unreviewed,
        )
        print(arguments.inspection.parent / "result.yaml")
        print(f"boards_added={len(result['boards_added'])}")
        return

    inspection, inspection_path = prepare(
        arguments.queue, arguments.project_data, arguments.run_root, arguments.repository
    )
    decisions = arguments.decisions
    if inspection["review_required"] and decisions is None and not arguments.allow_unreviewed:
        print(inspection_path)
        print(f"review_required=True; complete {inspection_path.parent / 'decision.yaml'}")
        raise SystemExit(2)
    result = commit(
        inspection_path, arguments.queue, arguments.project_data,
        decisions, arguments.allow_unreviewed,
    )
    print(inspection_path.parent / "result.yaml")
    print(f"boards_added={len(result['boards_added'])}")


if __name__ == "__main__":
    main()
