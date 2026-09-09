"""Delete generated action gates and project render outputs.

This script deletes each roboclick mode's ``file_test`` gate file
(``data/kicad/manifest.yaml``, ``data/working_svg_square_pins_300.png``,
``data/datasheet.pdf``, ``data/original/manifest.yaml``, ...) in every
filtered part folder.  The generated files are left absent so the normal
generation pipeline can be run separately afterward.  Source files and
``working.yaml`` are preserved.

Project folders are included by default.  Use ``--exclude-projects`` only when
you deliberately want to limit the deletion to ordinary component parts.

Set ``FULL_RESET = True`` below, or pass ``--full-reset``, for a broader reset
that also removes generated PNGs.  PNGs under ``data/git`` and ``data/original``
are treated as source snapshots and are preserved.

Every non-empty ``file_test`` declared by a generation mode is treated as a
gate and removed, including list-valued ``file_test`` entries.
"""

import argparse
import os

import yaml

from action_regenerate_all import REPOSITORY_ROOT, _matches_filter


# Default remains the minimal gate-only reset.  Set this to True when preparing
# the repository for a complete local regeneration, or use --full-reset.
FULL_RESET = True
#FULL_RESET = False


# A few run_python actions contain their own generated-file checks instead of
# expressing those files as the mode's file_test gate.  Keep this list narrow:
# these are cached outputs or failure markers that can prevent a fresh run.
# Do not include source inputs or edit-protection/state manifests here.
RUN_PYTHON_RESET_FILES = {
    "kicad_agents/project_git_action.py": {
        "data/error.txt",
    },
    "kicad_agents/project_readme_action.py": {
        "data/generated_data/src/board.png",
        "data/generated_data/src/board_pins.png",
        "data/generated_data/src/board_bottom.png",
        "data/generated_data/src/board_pins_bottom.png",
        "data/generated_data/src/board_mechanical.png",
    },
    "kicad_agents/production_jlc_action.py": {
        "data/error.txt",
    },
}


def _run_python_reset_files(part_directory, workings):
    """Delete narrowly identified hidden run_python cache/skip markers."""
    requested = set()
    for mode_details in workings.values():
        if not isinstance(mode_details, dict):
            continue
        for action in mode_details.get("actions", []):
            if not isinstance(action, dict) or action.get("command") != "run_python":
                continue
            file_python = str(action.get("file_python", "")).replace("\\", "/")
            requested.update(RUN_PYTHON_RESET_FILES.get(file_python, set()))

    deleted = 0
    for relative in sorted(requested):
        candidate = (part_directory / relative).resolve()
        if not candidate.is_relative_to(part_directory.resolve()):
            continue
        if candidate.is_file():
            candidate.unlink()
            deleted += 1
    return deleted


def delete_gate_files(part_directory, workings):
    """Remove generated gate files inside the part folder."""
    deleted = 0
    for mode_details in workings.values():
        if not isinstance(mode_details, dict):
            continue
        file_test = mode_details.get("file_test", "")
        if file_test in (None, ""):
            continue
        file_tests = file_test if isinstance(file_test, (list, tuple)) else [file_test]
        for file_test_entry in file_tests:
            if file_test_entry in (None, ""):
                continue
            gate = (part_directory / str(file_test_entry)).resolve()
            # Only generated files inside the part folder are gates; the
            # part's own working.yaml is pipeline input and is never deleted.
            if not gate.is_relative_to(part_directory.resolve()) or gate.name == "working.yaml":
                continue
            if gate.is_file():
                gate.unlink()
                deleted += 1
    return deleted


def delete_all_generated_pngs(part_directory):
    """Delete PNG outputs while preserving project source snapshots."""
    deleted = 0
    protected_directories = {"git", "original"}
    for candidate in part_directory.rglob("*"):
        if not candidate.is_file() or candidate.suffix.lower() != ".png":
            continue
        relative_parts = candidate.relative_to(part_directory).parts
        if protected_directories.intersection(relative_parts):
            continue
        candidate.unlink()
        deleted += 1
    return deleted


def delete_generated_files(filter_text="", include_projects=True, full_reset=None):
    """Delete generated files and return a summary dictionary.

    This function is intentionally callable from other Python modules while the
    script also remains runnable from the command line via ``main()``.
    """
    if full_reset is None:
        full_reset = FULL_RESET
    os.chdir(REPOSITORY_ROOT)
    parts_directory = REPOSITORY_ROOT / "parts"
    deleted_files = 0
    touched_parts = 0
    for part_directory in sorted(parts_directory.iterdir(), key=lambda path: path.name.lower()):
        if not part_directory.is_dir() or not _matches_filter(part_directory.name, filter_text):
            continue
        working_file = part_directory / "working.yaml"
        if not working_file.is_file():
            continue
        if part_directory.name.startswith("oomp_project_") and not include_projects:
            continue

        workings = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
        deleted_here = delete_gate_files(part_directory, workings)
        reset_deleted_here = _run_python_reset_files(part_directory, workings)
        png_deleted_here = delete_all_generated_pngs(part_directory) if full_reset else 0
        deleted_files += deleted_here + reset_deleted_here + png_deleted_here
        if deleted_here or reset_deleted_here or png_deleted_here:
            touched_parts += 1
            print(
                f"{part_directory.name}: deleted {deleted_here} generated gate file(s), "
                f"{reset_deleted_here} run_python reset file(s), "
                f"{png_deleted_here} generated PNG file(s)"
            )

    print(
        f"Generated-file deletion complete: {touched_parts} part(s) touched, "
        f"{deleted_files} generated file or artifact set(s) deleted."
    )
    return {
        "filter_text": filter_text,
        "include_projects": include_projects,
        "full_reset": full_reset,
        "touched_parts": touched_parts,
        "deleted_files": deleted_files,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", default="", help="OOMP part ID or family prefix; omit for every part")
    parser.add_argument(
        "--exclude-projects",
        action="store_false",
        dest="include_projects",
        help="Skip oomp_project_* folders (projects are included by default)",
    )
    parser.add_argument(
        "--full-reset",
        action="store_true",
        help="Also delete generated PNG files; source snapshots under data/git and data/original are preserved",
    )
    arguments = parser.parse_args(argv)
    delete_generated_files(
        filter_text=arguments.filter,
        include_projects=arguments.include_projects,
        full_reset=FULL_RESET or arguments.full_reset,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
