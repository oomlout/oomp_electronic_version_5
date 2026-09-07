"""Delete every part's current working_svg diagrams and regenerate them.

Runs the normal compile step first (working_oomp.main) so diagram gallery and
part page changes in working_oomp.py reach parts/<id>/working.yaml before the
actions are replayed.  With --include-projects, project board drawings and
board explorers are also rebuilt so they pick up the refreshed part diagrams.
"""

import argparse
import copy
import os
from pathlib import Path

import oomlout_roboclick
import yaml

from action_regenerate_all import REPOSITORY_ROOT, _is_browser_action, _matches_filter


def _recompile_parts(filter_text):
    """Rewrite parts/<id>/working.yaml from parts_source with current code."""
    print("Recompiling part definitions (working_oomp.main)...")
    import working_oomp

    working_oomp.main(filter=filter_text, regenerate_pngs=False)


def _run_actions(actions, part_directory, working_file, discovered_actions):
    ran = 0
    for action in actions:
        if not isinstance(action, dict):
            continue
        if _is_browser_action(action):
            continue
        action_to_run = copy.deepcopy(action)
        action_to_run["regenerate_pngs"] = True
        result = oomlout_roboclick.run_single_action(
            action=action_to_run,
            directory=str(part_directory.resolve()),
            directory_absolute=str(part_directory.resolve()),
            file_action=str(working_file.resolve()),
            _discovered_actions=discovered_actions,
        )
        if result in ["exit", "exit_no_tab"]:
            raise RuntimeError(
                f"Diagram regeneration stopped for {part_directory.name}: "
                f"{action.get('command', '')} returned {result}"
            )
        ran += 1
    return ran


def regenerate_diagrams(filter_text="", include_projects=False):
    os.chdir(REPOSITORY_ROOT)
    discovered_actions = oomlout_roboclick.build_action_lookup()
    _recompile_parts(filter_text)
    parts_directory = REPOSITORY_ROOT / "parts"
    action_count = 0
    deleted_files = 0
    touched_parts = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or not _matches_filter(part_directory.name, filter_text):
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        is_project = part_directory.name.startswith("oomp_project_")
        if is_project and not include_projects:
            continue
        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}

        if is_project:
            # The board mode is gated by one of its rendered previews; remove
            # the generated board drawings so that mode reruns and embeds the
            # refreshed part diagrams.  Other project modes are untouched.
            deleted_here = 0
            for board_file in sorted(part_directory.glob("data/generated_data/src/board*")):
                if board_file.is_file():
                    board_file.unlink()
                    deleted_here += 1
            if deleted_here == 0:
                continue
            deleted_files += deleted_here
            ran_here = 0
            for mode_name, mode_details in workings.items():
                if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                    continue
                file_test = str(mode_details.get("file_test", ""))
                if "generated_data/src" not in file_test:
                    continue
                ran_here += _run_actions(
                    mode_details.get("actions", []), part_directory, working_file, discovered_actions
                )
            action_count += ran_here
            touched_parts += 1
            print(f"{part_directory.name}: deleted {deleted_here} board file(s), ran {ran_here} action(s)")
            continue

        # Remove the current diagrams; the svg mode's check file is one of
        # them, so that mode is forced to rerun and rewrite every diagram.
        deleted_here = 0
        for diagram in sorted(part_directory.glob("data/working_svg_*")):
            if diagram.is_file():
                diagram.unlink()
                deleted_here += 1
        deleted_files += deleted_here

        ran_here = 0
        for mode_name, mode_details in workings.items():
            if not str(mode_name).startswith("oomlout_") or not isinstance(mode_details, dict):
                continue
            ran_here += _run_actions(
                mode_details.get("actions", []), part_directory, working_file, discovered_actions
            )
        action_count += ran_here
        if deleted_here or ran_here:
            touched_parts += 1
            print(f"{part_directory.name}: deleted {deleted_here} diagram file(s), ran {ran_here} action(s)")
    print(
        f"Diagram regeneration complete: {touched_parts} part(s) refreshed, "
        f"{deleted_files} generated file(s) deleted, {action_count} actions run."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="", help="OOMP part ID or family prefix; omit for every part")
    parser.add_argument(
        "--include-projects",
        action="store_true",
        help="Also rebuild oomp_project_* board drawings and board explorers from the refreshed part diagrams",
    )
    arguments = parser.parse_args()
    regenerate_diagrams(filter_text=arguments.filter, include_projects=arguments.include_projects)


if __name__ == "__main__":
    main()
