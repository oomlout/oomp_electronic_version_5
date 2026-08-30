"""Roboclick run_python action: refresh a project repository and copy KiCad files."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def _run_git(arguments, working_directory=None):
    command = ["git"]
    for argument in arguments:
        command.append(str(argument))
    completed = subprocess.run(
        command,
        cwd=str(working_directory) if working_directory else None,
        capture_output=True,
        text=True,
    )
    if completed.stdout.strip() != "":
        print(completed.stdout.strip())
    if completed.returncode != 0:
        message = completed.stderr.strip() or "git command failed"
        raise RuntimeError(f"{message}\nCommand: {' '.join(command)}")


def refresh_project_files(details):
    part_directory = Path(details["directory"]).resolve()
    repository_url = str(details.get("project_git_url", "")).strip()
    repository_name = str(details.get("project_github_repository", "")).strip()
    git_reference = str(details.get("project_git_ref", "main")).strip()
    project_version = str(details.get("project_version", "current")).strip()
    source_folder = str(details.get("project_file_folder", "")).strip()
    source_basename = str(details.get("project_file_basename", "")).strip()
    extensions = details.get("project_file_extensions", [])

    required_strings = [repository_url, repository_name, source_basename]
    if "" in required_strings:
        raise ValueError("project_git_url, project_github_repository, and project_file_basename are required")
    if not isinstance(extensions, list) or extensions == []:
        raise ValueError("project_file_extensions must be a non-empty list")

    git_parent = part_directory / "git"
    repository_directory = git_parent / repository_name
    git_metadata = repository_directory / ".git"

    if not git_metadata.is_dir():
        if repository_directory.exists() and any(repository_directory.iterdir()):
            raise RuntimeError(f"Refusing to clone over non-empty directory: {repository_directory}")
        git_parent.mkdir(parents=True, exist_ok=True)
        _run_git(["clone", repository_url, repository_directory])
    else:
        _run_git(["-C", repository_directory, "fetch", "--all", "--tags", "--prune"])

    if project_version == "current":
        _run_git(["-C", repository_directory, "checkout", git_reference])
        _run_git(["-C", repository_directory, "pull", "--ff-only"])
    else:
        _run_git(["-C", repository_directory, "checkout", "--detach", git_reference])

    copied_files = []
    for extension in extensions:
        extension_text = str(extension)
        if not extension_text.startswith("."):
            extension_text = f".{extension_text}"
        source_file = repository_directory / source_folder / f"{source_basename}{extension_text}"
        destination_file = part_directory / f"kicad_file{extension_text}"
        if not source_file.is_file():
            raise FileNotFoundError(f"Required KiCad source file not found: {source_file}")
        shutil.copy2(source_file, destination_file)
        copied_files.append(
            {
                "source": str(source_file),
                "destination": str(destination_file),
            }
        )
        print(f"copied {source_file.name} -> {destination_file.name}")

    return copied_files


def main():
    parser = argparse.ArgumentParser(description="Refresh Git project files for an OOMP project part.")
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    details = json.loads(arguments.kwargs)
    refresh_project_files(details)


if __name__ == "__main__":
    main()
