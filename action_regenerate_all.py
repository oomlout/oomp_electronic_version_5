"""Fully regenerate OOMP outputs while skipping browser-driven Roboclick actions."""

import argparse
import copy
from pathlib import Path

import yaml

import oomlout_roboclick
import working_oomp
import working_oomp_populate
from kicad_agents.migrate_part_data_layout import migrate_parts


REPOSITORY_ROOT = Path(__file__).resolve().parent


def _is_browser_action(action):
    command = str(action.get("command", "")).lower()
    python_file = str(action.get("file_python", "")).lower()
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
    ]
    combined_text = " ".join([command, python_file])
    for browser_term in browser_terms:
        if browser_term in combined_text:
            return True
    return False


def _matches_filter(part_id, filter_text):
    if filter_text == "":
        return True
    return filter_text in part_id


def run_actions(filter_text=""):
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
                action_to_run["regenerate_pngs"] = True
                oomlout_roboclick.run_single_action(
                    action=action_to_run,
                    directory=str(part_directory.resolve()),
                    directory_absolute=str(part_directory.resolve()),
                    file_action=str(working_file.resolve()),
                    _discovered_actions=discovered_actions,
                )
                action_count += 1
    return action_count, skipped_browser_count


def regenerate_all(filter_text=""):
    populate_kwargs = {"regenerate_pngs": True}
    if filter_text != "":
        populate_kwargs["filter"] = filter_text
    working_oomp_populate.main(**populate_kwargs)
    working_oomp.main(**populate_kwargs)
    migration = migrate_parts(REPOSITORY_ROOT / "parts")
    action_count, skipped_browser_count = run_actions(filter_text=filter_text)
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
