"""Roboclick run_python action: refresh a project repository and copy KiCad files."""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def referenced_sheets(root_file):
    """Follow actual hierarchical references, retaining their relative folders."""
    from kicad_agents import kicad_sexpr as sx
    root_file = Path(root_file).resolve()
    base = root_file.parent
    pending = [root_file]
    found = []
    while pending:
        source = pending.pop(0)
        if source in found:
            continue
        found.append(source)
        root = sx.parse(source.read_text(encoding='utf-8'))
        for sheet in sx.children(root, 'sheet'):
            filename = sx.property_value(sheet, 'Sheetfile') or sx.property_value(sheet, 'Sheet file')
            target = (source.parent / filename).resolve()
            if not filename or not target.is_relative_to(base):
                raise ValueError(f'External or invalid hierarchical sheet reference: {filename}')
            if not target.is_file():
                raise FileNotFoundError(f'Missing hierarchical sheet: {target}')
            pending.append(target)
    return found[1:]

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
    data_directory = part_directory / "data"
    repository_url = str(details.get("project_git_url", "")).strip()
    repository_name = str(details.get("project_github_repository", "")).strip()
    git_reference = str(details.get("project_git_ref", "main")).strip()
    project_version = str(details.get("project_version", "current")).strip()
    source_folder = str(details.get("project_file_folder", "")).strip()
    sparse_checkout = bool(details.get("project_sparse_checkout", False))
    source_basename = str(details.get("project_file_basename", "")).strip()
    extensions = details.get("project_file_extensions", [])

    required_strings = [repository_url, repository_name, source_basename]
    if "" in required_strings:
        raise ValueError("project_git_url, project_github_repository, and project_file_basename are required")
    if not isinstance(extensions, list) or extensions == []:
        raise ValueError("project_file_extensions must be a non-empty list")

    git_parent = data_directory / "git"
    repository_directory = git_parent / repository_name
    git_metadata = repository_directory / ".git"

    if not git_metadata.is_dir():
        if repository_directory.exists() and any(repository_directory.iterdir()):
            raise RuntimeError(f"Refusing to clone over non-empty directory: {repository_directory}")
        git_parent.mkdir(parents=True, exist_ok=True)
        clone_arguments = ["clone"]
        if sparse_checkout:
            clone_arguments.extend(["--filter=blob:none", "--no-checkout"])
        clone_arguments.extend([repository_url, repository_directory])
        _run_git(clone_arguments)
    else:
        _run_git(["-C", repository_directory, "fetch", "--all", "--tags", "--prune"])

    # Windows can reject unrelated repository paths before Git reaches the
    # selected KiCad directory.  Sparse checkout keeps the working tree small
    # and, importantly, makes the chosen project folder explicit and editable.
    if sparse_checkout:
        _run_git(["-C", repository_directory, "config", "core.longpaths", "true"])
        _run_git(["-C", repository_directory, "sparse-checkout", "init", "--cone"])
        _run_git(["-C", repository_directory, "sparse-checkout", "set", source_folder])

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
        destination_file = data_directory / f"kicad_file{extension_text}"
        destination_file.parent.mkdir(parents=True, exist_ok=True)
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

    # Hierarchical KiCad projects keep the component-bearing sheets beside the
    # root schematic.  Copy them into a stable nested directory so the parser
    # can digest the complete design without depending on the ignored clone.
    sheet_directory = data_directory / "kicad_file_sheets"
    source_project_directory = repository_directory / source_folder
    schematic_files = referenced_sheets(source_project_directory / f"{source_basename}.kicad_sch")
    for schematic_file in schematic_files:
        if schematic_file.name.lower() == f"{source_basename}.kicad_sch".lower():
            continue
        sheet_directory.mkdir(parents=True, exist_ok=True)
        destination_file = sheet_directory / schematic_file.relative_to(source_project_directory)
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(schematic_file, destination_file)
        copied_files.append(
            {
                "source": str(schematic_file),
                "destination": str(destination_file),
            }
        )
        print(f"copied sheet {schematic_file.name} -> kicad_file_sheets/{schematic_file.name}")

    # Preserve the untouched input set before any downstream OOMP action.
    from kicad_agents.kicad_project_action import preserve_originals
    for table_name in ['sym-lib-table', 'fp-lib-table']:
        table = source_project_directory / table_name
        if table.is_file():
            shutil.copy2(table, data_directory / table_name)
    preserve_originals(data_directory)
    return copied_files


def main():
    parser = argparse.ArgumentParser(description="Refresh Git project files for an OOMP project part.")
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    details = json.loads(arguments.kwargs)
    refresh_project_files(details)


if __name__ == "__main__":
    main()
