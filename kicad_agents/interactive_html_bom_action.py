"""Roboclick action for headless InteractiveHtmlBom generation."""

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
INTERACTIVE_HTML_BOM_SCRIPT = (
    REPOSITORY_ROOT
    / "tools"
    / "interactive_html_bom"
    / "InteractiveHtmlBom"
    / "generate_interactive_bom.py"
)


def _candidate_python_executables():
    candidates = []
    configured_python = os.environ.get("KICAD_PYTHON", "").strip()
    if configured_python != "":
        candidates.append(Path(configured_python))

    program_files = Path(os.environ.get("ProgramFiles", "C:/Program Files"))
    kicad_directory = program_files / "KiCad"
    if kicad_directory.is_dir():
        versions = sorted(kicad_directory.iterdir(), reverse=True)
        for version_directory in versions:
            for executable_name in ["python.exe", "python3.exe"]:
                candidates.append(version_directory / "bin" / executable_name)

    if importlib.util.find_spec("pcbnew") is not None:
        candidates.append(Path(sys.executable))

    unique_candidates = []
    for candidate in candidates:
        candidate_resolved = candidate.resolve()
        if candidate_resolved not in unique_candidates:
            unique_candidates.append(candidate_resolved)
    return unique_candidates


def _write_status(output_directory, status, message, command=None):
    output_directory.mkdir(parents=True, exist_ok=True)
    status_data = {
        "generated_by": "kicad_agents.interactive_html_bom_action",
        "status": status,
        "message": message,
        "output": "ibom.html",
    }
    if command is not None:
        status_data["command"] = [str(value) for value in command]
    status_path = output_directory / "generation_status.yaml"
    status_path.write_text(
        yaml.safe_dump(status_data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return status_path


def generate_interactive_html_bom(details):
    part_directory = Path(details["directory"]).resolve()
    data_directory = part_directory / "data"
    pcb_file = data_directory / "kicad_file.kicad_pcb"
    output_directory = data_directory / "interactivehtmlbom"
    output_file = output_directory / "ibom.html"

    if not pcb_file.is_file():
        raise FileNotFoundError(f"KiCad PCB file is missing: {pcb_file}")
    if not INTERACTIVE_HTML_BOM_SCRIPT.is_file():
        raise FileNotFoundError(
            "InteractiveHtmlBom is not set up. Expected "
            f"{INTERACTIVE_HTML_BOM_SCRIPT}"
        )

    python_executable = None
    for candidate in _candidate_python_executables():
        if candidate.is_file():
            python_executable = candidate
            break

    if python_executable is None:
        message = (
            "InteractiveHtmlBom requires KiCad's bundled Python with the pcbnew module. "
            "Install KiCad or set KICAD_PYTHON to that python.exe, then rerun this action."
        )
        _write_status(output_directory, "waiting_for_kicad_python", message)
        print(message)
        return None

    output_directory.mkdir(parents=True, exist_ok=True)
    command = [
        str(python_executable),
        str(INTERACTIVE_HTML_BOM_SCRIPT),
        "--no-browser",
        "--dest-dir",
        "interactivehtmlbom",
        "--name-format",
        "ibom",
        str(pcb_file),
    ]
    completed = subprocess.run(
        command,
        cwd=str(data_directory),
        capture_output=True,
        text=True,
    )
    if completed.stdout.strip() != "":
        print(completed.stdout.strip())
    if completed.returncode != 0:
        message = completed.stderr.strip() or "InteractiveHtmlBom generation failed"
        _write_status(output_directory, "failed", message, command=command)
        raise RuntimeError(message)
    if not output_file.is_file():
        _write_status(
            output_directory,
            "failed",
            f"InteractiveHtmlBom exited successfully but did not create {output_file}",
            command=command,
        )
        raise RuntimeError(f"InteractiveHtmlBom output is missing: {output_file}")

    _write_status(output_directory, "generated", "InteractiveHtmlBom generated successfully.", command=command)
    print(f"InteractiveHtmlBom: {output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description="Generate InteractiveHtmlBom for one OOMP project part.")
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    generate_interactive_html_bom(json.loads(arguments.kwargs))


if __name__ == "__main__":
    main()
