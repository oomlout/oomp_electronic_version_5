"""Run one part's working.yaml actions; missing outputs only, or everything."""

import argparse
import copy
import os
from pathlib import Path

import oomlout_roboclick
import yaml

from action_regenerate_all import REPOSITORY_ROOT, _is_browser_action, _matches_filter
from kicad_agents.run_error_report import log_run_error


def _check_file_paths(part_directory, mode_details):
    file_test = mode_details.get("file_test", "")
    if file_test in (None, ""):
        return []
    if isinstance(file_test, (list, tuple)):
        entries = [str(item) for item in file_test if item not in (None, "")]
    else:
        entries = [str(file_test)]
    paths = []
    for entry in entries:
        path = Path(entry)
        if not path.is_absolute():
            path = part_directory / path
        paths.append(path)
    return paths


def _check_files_complete(part_directory, mode_details):
    if mode_details.get("always_run_on_regeneration", False):
        return False
    paths = _check_file_paths(part_directory, mode_details)
    if not paths:
        return False
    mode = str(mode_details.get("file_test_mode") or "exists")
    if mode == "exists":
        return all(path.exists() for path in paths)
    return any(path.exists() for path in paths)


def _delete_check_files(part_directory, mode_details):
    deleted = 0
    for path in _check_file_paths(part_directory, mode_details):
        resolved = path.resolve()
        if part_directory.resolve() not in resolved.parents:
            print(f"  not deleting check file outside the part directory: {path}")
            continue
        if resolved.is_file():
            resolved.unlink()
            deleted += 1
    return deleted


def regenerate_part(filter_text, everything=False):
    if not filter_text.strip():
        raise ValueError("Give a part ID or family prefix.")
    os.chdir(REPOSITORY_ROOT)
    regenerate_pngs = everything
    discovered_actions = oomlout_roboclick.build_action_lookup()
    parts_directory = REPOSITORY_ROOT / "parts"
    action_count = 0
    skipped_browser_count = 0
    skipped_modes = 0
    deleted_checks = 0
    matched = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or not _matches_filter(part_directory.name, filter_text):
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        matched += 1
        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        for mode_name, mode_details in workings.items():
            if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                continue
            if everything:
                deleted = _delete_check_files(part_directory, mode_details)
                deleted_checks += deleted
                if deleted:
                    print(f"{part_directory.name} {mode_name}: deleted {deleted} check file(s) to force a rerun")
            elif _check_files_complete(part_directory, mode_details):
                skipped_modes += 1
                print(f"{part_directory.name} {mode_name}: check files present, skipping")
                continue
            actions = mode_details.get("actions", [])
            if not isinstance(actions, list):
                continue
            for action in actions:
                if not isinstance(action, dict):
                    continue
                if _is_browser_action(action):
                    skipped_browser_count += 1
                    print(f"skipping browser action for {part_directory.name}: {action.get('command', '')}")
                    continue
                action_to_run = copy.deepcopy(action)
                action_to_run["regenerate_pngs"] = regenerate_pngs
                result = oomlout_roboclick.run_single_action(
                    action=action_to_run,
                    directory=str(part_directory.resolve()),
                    directory_absolute=str(part_directory.resolve()),
                    file_action=str(working_file.resolve()),
                    _discovered_actions=discovered_actions,
                )
                if result in ["exit", "exit_no_tab"]:
                    message = (
                        f"Regeneration stopped for {part_directory.name}: "
                        f"{action.get('command', '')} returned {result}"
                    )
                    log_run_error("action_regenerate_part", RuntimeError(message), command=[
                        str(action.get("command", "")),
                        str(action.get("file_python", "")),
                    ])
                    print(f"Logged and skipped failed action: {message}")
                    continue
                action_count += 1
    if not matched:
        raise ValueError(f"No parts under parts/ matched '{filter_text}'.")
    mode_word = "everything" if everything else "missing outputs only"
    print(
        f"Part regeneration ({mode_word}): {matched} part(s) matched, "
        f"{action_count} actions run, {skipped_modes} modes already complete, "
        f"{deleted_checks} check file(s) deleted, {skipped_browser_count} browser actions skipped."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", required=True, help="OOMP part ID or family prefix to regenerate")
    parser.add_argument(
        "--everything",
        action="store_true",
        help="Delete the working.yaml check files first so every step reruns (also regenerates PNGs)",
    )
    arguments = parser.parse_args()
    regenerate_part(filter_text=arguments.filter, everything=arguments.everything)


if __name__ == "__main__":
    main()
