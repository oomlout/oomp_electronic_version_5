"""Fully regenerate OOMP outputs while skipping browser-driven Roboclick actions."""

import argparse
import copy
from pathlib import Path

import yaml

import oomlout_roboclick
import working_oomp
import working_oomp_populate
from kicad_agents.migrate_part_data_layout import migrate_parts
from kicad_agents.run_error_report import log_run_error


REPOSITORY_ROOT = Path(__file__).resolve().parent


def _is_browser_action(action):
    command = str(action.get("command", "")).lower()
    python_file = str(action.get("file_python", "")).lower()
    browser_commands = [
        "new_chat", "close_tab", "query", "add_image", "add_file", "ai_save_image",
        "save_image_search_result",
    ]
    if command in browser_commands:
        return True
    browser_terms = [
        "browser",
        "chrome",
        "firefox",
        "playwright",
        "selenium",
        "ai_add_image",
        "ai_query",
        "ai_continue_chat",
        "ai_new_chat",
        "ai_from_directory",
        "ai_image_",
        "ai_file_",
        "ai_save_text",
        "ai_set_mode",
        "ai_text_",
        "google_doc_",
    ]
    combined_text = " ".join([command, python_file])
    for browser_term in browser_terms:
        if browser_term in combined_text:
            return True
    return False


def _matches_filter(part_id, filter_text):
    if isinstance(filter_text, list):
        for entry in filter_text:
            if _matches_filter(part_id, entry):
                return True
        return False
    if filter_text == "":
        return True
    return filter_text in part_id


def _normal_gate_is_complete(part_directory, mode_details):
    file_test = mode_details.get("file_test", "")
    if file_test in [None, ""]:
        return False
    file_tests = file_test if isinstance(file_test, (list, tuple)) else [file_test]
    paths = []
    for file_test_entry in file_tests:
        path = Path(str(file_test_entry))
        if not path.is_absolute():
            path = part_directory / path
        paths.append(path)
    mode = str(mode_details.get("file_test_mode") or "exists")
    if mode == "exists":
        return all(path.exists() for path in paths)
    return any(path.exists() for path in paths)


def run_actions(filter_text="", regenerate_pngs=True, honour_normal_gates=False):
    discovered_actions = oomlout_roboclick.build_action_lookup()
    parts_directory = REPOSITORY_ROOT / "parts"
    action_count = 0
    skipped_browser_count = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or not _matches_filter(part_directory.name, filter_text):
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        for mode_name, mode_details in workings.items():
            if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                continue
            if (
                honour_normal_gates
                and mode_details.get("honour_gate_in_normal_run", False)
                and _normal_gate_is_complete(part_directory, mode_details)
            ):
                print(f"{part_directory.name} {mode_name}: gate present, skipping normal run")
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
                    log_run_error("action_regenerate_all", RuntimeError(message), command=[
                        str(action.get("command", "")),
                        str(action.get("file_python", "")),
                    ])
                    print(f"Logged and skipped failed action: {message}")
                    continue
                action_count += 1
    return action_count, skipped_browser_count


def regenerate_all(filter_text=""):
    # Force images only for this run, not for every future routine action.
    # run_actions applies the force flag to an in-memory action copy.
    populate_kwargs = {"regenerate_pngs": False}
    if filter_text != "":
        populate_kwargs["filter"] = filter_text
    working_oomp_populate.main(**populate_kwargs)
    working_oomp.main(**populate_kwargs)
    migration = migrate_parts(REPOSITORY_ROOT / "parts")
    action_count, skipped_browser_count = run_actions(filter_text=filter_text)
    from kicad_agents.kicad_library_agent import package_libraries
    package_libraries(REPOSITORY_ROOT / "parts", REPOSITORY_ROOT / "kicad_libraries")
    print(
        f"Full regeneration complete: {action_count} deterministic actions, "
        f"{skipped_browser_count} browser actions skipped, "
        f"{migration['items']} legacy root items migrated."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="", help="Optional part-ID substring for a smaller regeneration run")
    arguments = parser.parse_args()
    regenerate_all(filter_text=arguments.filter)


if __name__ == "__main__":
    main()
