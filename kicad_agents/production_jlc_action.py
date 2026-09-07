"""Roboclick run_python entry point for the JLCPCB production pipeline."""

import argparse
import json
from pathlib import Path

import yaml

from kicad_agents.production_jlc_agent import OUTPUT_DIRECTORY_NAME, generate_jlc_production_files
from kicad_agents.run_error_report import log_run_error


def _write_failure_status(details, error):
    part_directory = Path(details.get("directory", ".")).resolve()
    output_directory = part_directory / "data" / OUTPUT_DIRECTORY_NAME
    status_directory = output_directory / "data"
    status_directory.mkdir(parents=True, exist_ok=True)
    status = {
        "generated_by": "kicad_agents.production_jlc_action",
        "status": "failed",
        "message": str(error),
    }
    (status_directory / "generation_status.yaml").write_text(
        yaml.safe_dump(status, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def _project_sources_ready(details):
    """Gate production generation when canonical KiCad source files are missing."""
    part_directory = Path(details.get("directory", ".")).resolve()
    data_directory = part_directory / "data"
    required = [
        data_directory / "kicad_file.kicad_sch",
        data_directory / "kicad_file.kicad_pcb",
    ]
    missing = [path.name for path in required if not path.is_file()]
    if missing:
        return False, (
            f"Skipping production_jlc_action for {part_directory.name}: missing required source file(s): "
            + ", ".join(missing)
        )

    upstream_error = data_directory / "error.txt"
    if upstream_error.is_file():
        return False, (
            f"Skipping production_jlc_action for {part_directory.name}: upstream fetch error marker exists "
            f"({upstream_error})."
        )
    return True, ""


def run(details):
    ready, message = _project_sources_ready(details)
    if not ready:
        error = RuntimeError(message)
        _write_failure_status(details, error)
        log_run_error("production_jlc_action", error)
        print(message)
        return None
    try:
        return generate_jlc_production_files(details)
    except Exception as error:
        _write_failure_status(details, error)
        log_run_error("production_jlc_action", error)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    run(json.loads(arguments.kwargs))


if __name__ == "__main__":
    main()
