"""Create the standard presentation images for a generated PCB project."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path

from kicad_agents.kicad_cli import find_kicad_cli
from kicad_agents.run_error_report import log_run_error


def _kicad_cli(details):
    return find_kicad_cli(details.get("project_kicad_cli"))


def _render_board(kicad_cli, board_file, destination, extra_arguments):
    command = [
        kicad_cli,
        "pcb",
        "render",
        "--output",
        str(destination),
        "--width",
        "1600",
        "--height",
        "1200",
        *extra_arguments,
        str(board_file),
    ]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=600)
    except FileNotFoundError as error:
        message = "KiCad CLI is required to render project images."
        log_run_error("project_images_action", RuntimeError(message), command=command)
        print(message)
        return None
    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "KiCad 3D render failed"
        log_run_error("project_images_action", RuntimeError(f"{message}\nCommand: {' '.join(command)}"), command=command)
        print(message)
        return None
    if not destination.is_file():
        message = f"KiCad CLI reported success but did not create {destination}"
        log_run_error("project_images_action", RuntimeError(message), command=command)
        print(message)
        return None
    return command


def render_project_images(details):
    """Write front, back, isometric, and populated-3D images at part root."""
    part_directory = Path(details["directory"]).resolve()
    data_directory = part_directory / "data"
    source_directory = data_directory / "generated_data" / "src"
    board_file = data_directory / "kicad_file.kicad_pcb"
    images_directory = part_directory / "images"
    front_source = source_directory / "board.png"
    back_source = source_directory / "board_bottom.png"

    required_files = [board_file, front_source, back_source]
    missing = [path for path in required_files if not path.is_file()]
    if missing:
        message = "Project image generation needs: " + ", ".join(str(path) for path in missing)
        log_run_error("project_images_action", FileNotFoundError(message))
        print(message)
        return None

    images_directory.mkdir(parents=True, exist_ok=True)
    front_destination = images_directory / "pcb_front.png"
    back_destination = images_directory / "pcb_back.png"
    isometric_destination = images_directory / "pcb_isometric.png"
    populated_destination = images_directory / "pcb_3d_populated.png"
    shutil.copy2(front_source, front_destination)
    shutil.copy2(back_source, back_destination)

    kicad_cli = _kicad_cli(details)
    isometric_command = _render_board(
        kicad_cli,
        board_file,
        isometric_destination,
        ["--side", "top", "--rotate", "315,0,45", "--background", "transparent", "--quality", "basic"],
    )
    if isometric_command is None:
        return None

    populated_command = _render_board(
        kicad_cli,
        board_file,
        populated_destination,
        [
            "--side", "top", "--rotate", "315,0,45", "--zoom", "0.75", "--perspective", "--floor",
            "--background", "opaque", "--quality", "high",
        ],
    )
    if populated_command is None:
        return None

    print(f"wrote project images to {images_directory}")
    return {
        "front": front_destination,
        "back": back_destination,
        "isometric": isometric_destination,
        "populated_3d": populated_destination,
        "commands": [isometric_command, populated_command],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    render_project_images(json.loads(arguments.kwargs))


if __name__ == "__main__":
    main()
