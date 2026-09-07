"""Full regeneration: delete every part's action gate files and replay actions.

Where action_regenerate_all_delete_current_diagrams.py only deletes the
diagrams, this script deletes each roboclick mode's `file_test` gate file
(data/kicad/manifest.yaml, data/working_svg_square_pins_300.png,
data/datasheet.pdf, data/original/manifest.yaml, ...) in every filtered part
folder, so every non-browser action mode reruns from scratch.  The compile
step (working_oomp.main) runs first so parts/<id>/working.yaml is rebuilt
from parts_source with the current populate code.  Modes without a
`file_test` (for example the README template render) have no gate and rerun
with every replay.

With --include-projects, project outputs also drop generated KiCad
production bundles and generated schematic render artifacts before replay:
data/production_auto_generate/, data/generated_data/src/schematic.svg, and
data/generated_data/src/schematic_parts/.

A mode whose gate cannot be rebuilt is never unlocked: only modes holding at
least one non-browser action lose their gate file.  Failures are collected
per part; the run continues and reports them at the end.
"""

import argparse
import copy
import os
import shutil
from pathlib import Path

import oomlout_roboclick
import yaml

from action_regenerate_all import REPOSITORY_ROOT, _is_browser_action, _matches_filter
from kicad_agents.run_error_report import log_run_error


def _recompile_parts(filter_text):
    """Rewrite parts/<id>/working.yaml from parts_source with current code."""
    print("Recompiling part definitions (working_oomp.main)...")
    import working_oomp

    working_oomp.main(filter=filter_text, regenerate_pngs=False)


def _mode_is_replayable(mode_details):
    """A mode can be forced by gate deletion only if an action can rebuild it."""
    for action in mode_details.get("actions", []):
        if isinstance(action, dict) and not _is_browser_action(action):
            return True
    return False


def delete_gate_files(part_directory, workings):
    """Remove every replayable mode's file_test gate inside the part folder."""
    deleted = 0
    for mode_details in workings.values():
        if not isinstance(mode_details, dict):
            continue
        file_test = str(mode_details.get("file_test", ""))
        if not file_test or not _mode_is_replayable(mode_details):
            continue
        gate = (part_directory / file_test).resolve()
        # Only generated files inside the part folder are gates; the part's
        # own working.yaml is pipeline input and is never a gate.
        if not gate.is_relative_to(part_directory.resolve()) or gate.name == "working.yaml":
            continue
        if gate.is_file():
            gate.unlink()
            deleted += 1
    return deleted


def delete_generated_project_kicad_outputs(part_directory):
    """Delete generated project KiCad outputs while preserving source inputs."""
    deleted = 0
    production_directory = part_directory / "data" / "production_auto_generate"
    if production_directory.is_dir():
        shutil.rmtree(production_directory)
        deleted += 1

    schematic_file = part_directory / "data" / "generated_data" / "src" / "schematic.svg"
    if schematic_file.is_file():
        schematic_file.unlink()
        deleted += 1

    schematic_parts_directory = (
        part_directory / "data" / "generated_data" / "src" / "schematic_parts"
    )
    if schematic_parts_directory.is_dir():
        shutil.rmtree(schematic_parts_directory)
        deleted += 1

    return deleted


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
            message = (
                f"{part_directory.name}: {action.get('command', '')} returned {result}"
            )
            log_run_error("action_regenerate_all_delete_generate_files", RuntimeError(message), command=[
                str(action.get("command", "")),
                str(action.get("file_python", "")),
            ])
            print(f"Logged and skipped failed action: {message}")
            continue
        ran += 1
    return ran


def regenerate_parts(filter_text="", include_projects=False):
    os.chdir(REPOSITORY_ROOT)
    discovered_actions = oomlout_roboclick.build_action_lookup()
    _recompile_parts(filter_text)
    parts_directory = REPOSITORY_ROOT / "parts"
    action_count = 0
    deleted_files = 0
    touched_parts = 0
    failures = []
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or not _matches_filter(part_directory.name, filter_text):
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        if part_directory.name.startswith("oomp_project_") and not include_projects:
            continue
        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        generated_deleted_here = 0
        if part_directory.name.startswith("oomp_project_"):
            generated_deleted_here = delete_generated_project_kicad_outputs(part_directory)
        deleted_here = delete_gate_files(part_directory, workings)
        deleted_files += deleted_here + generated_deleted_here
        ran_here = 0
        try:
            for mode_details in workings.values():
                if not isinstance(mode_details, dict):
                    continue
                ran_here += _run_actions(
                    mode_details.get("actions", []), part_directory, working_file, discovered_actions
                )
        except RuntimeError as error:
            failures.append(str(error))
        action_count += ran_here
        if generated_deleted_here or deleted_here or ran_here:
            touched_parts += 1
            print(
                f"{part_directory.name}: deleted {generated_deleted_here} project generated artifact set(s), "
                f"{deleted_here} gate file(s), ran {ran_here} action(s)"
            )
    print(
        f"Full regeneration complete: {touched_parts} part(s) refreshed, "
        f"{deleted_files} gate file(s) deleted, {action_count} actions run, "
        f"{len(failures)} failure(s)."
    )
    for failure in failures:
        print(f"  FAILED: {failure}")
    return len(failures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="", help="OOMP part ID or family prefix; omit for every part")
    parser.add_argument(
        "--include-projects",
        action="store_true",
        help="Also rebuild oomp_project_* parts (boards, explorers, KiCad assets) alongside regular parts",
    )
    arguments = parser.parse_args()
    failures = regenerate_parts(filter_text=arguments.filter, include_projects=arguments.include_projects)
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
