"""Populate project parts from user-owned YAML definitions.

Each ``project_data/<github-user>/working.yaml`` file owns the projects for one
GitHub user. Keep the data declarative: project matching belongs in the
matching agent, never in a project definition.
"""

from pathlib import Path, PurePosixPath
import re

import yaml


PROJECT_DATA_DIRECTORY = Path(__file__).resolve().parent / "project_data"
PROJECT_FILE_EXTENSIONS = [".kicad_pcb", ".kicad_sch", ".kicad_pro"]


def _normalize_project_slug(value):
    if value is None:
        return ""
    normalized = str(value).strip()
    normalized = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", normalized)
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def _select_active_version(versions):
    """Keep the historic behaviour: current wins, otherwise newest wins."""
    if not versions:
        return {"version": "current", "git_ref": "main"}
    current_versions = [
        details for details in versions
        if str(details.get("version", "current")).strip().lower() == "current"
    ]
    if current_versions:
        return current_versions[0]
    ranked = []
    for details in versions:
        digits = [int(part) for part in re.findall(r"\d+", str(details.get("version", "")))]
        ranked.append((digits, details))
    return max(ranked, key=lambda item: item[0] or [0])[1]


def _collapse_historical_versions(versions):
    labels = [str(details.get("version", "current")).strip() for details in versions]
    return list(versions) if len(set(labels)) <= 1 else [_select_active_version(versions)]


def _normalise_version(version, path):
    """Fill the redundant path fields from the one required source path."""
    details = dict(version)
    source_path = str(details.get("project_file_path", "")).strip().replace("\\", "/")
    folder = str(details.get("project_file_folder", "")).strip().replace("\\", "/")
    basename = str(details.get("project_file_basename", "")).strip()
    if not source_path and basename:
        source_path = f"{folder.rstrip('/')}/{basename}" if folder else basename
    if not source_path:
        raise ValueError(f"{path}: every version needs project_file_path or project_file_basename")
    source = PurePosixPath(source_path)
    details["project_file_path"] = source_path
    if not details.get("project_file_basename"):
        details["project_file_basename"] = source.name
    if not details.get("project_file_folder"):
        details["project_file_folder"] = "" if str(source.parent) == "." else str(source.parent)
    return details


def _load_project_files(data_directory=PROJECT_DATA_DIRECTORY):
    """Load and validate every user definition in a stable order."""
    project_files = sorted(Path(data_directory).glob("*/working.yaml"))
    if not project_files:
        raise FileNotFoundError(f"No project definitions found in {data_directory}")

    projects = []
    for path in project_files:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        github_user = data.get("github_user")
        if not isinstance(github_user, str) or not github_user.strip():
            raise ValueError(f"{path}: github_user is required")
        entries = data.get("projects")
        if not isinstance(entries, list):
            raise ValueError(f"{path}: projects must be a list")
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError(f"{path}: every projects entry must be a mapping")
            repository = entry.get("github_repository")
            if not isinstance(repository, str) or not repository.strip():
                raise ValueError(f"{path}: github_repository is required for every project")
            versions = entry.get("versions")
            if not isinstance(versions, list) or not versions:
                raise ValueError(f"{path}: {repository} must define at least one version")
            if not all(isinstance(version, dict) for version in versions):
                raise ValueError(f"{path}: {repository} versions must be mappings")
            github_url = entry.get("github_url") or f"https://github.com/{github_user}/{repository}"
            projects.append({
                "github_user": github_user,
                "github_repository": repository,
                "github_url": github_url,
                "repository_url": entry.get("repository_url") or f"{github_url}.git",
                "versions": [_normalise_version(version, path) for version in versions],
            })
    return projects


def main(**kwargs):
    options = kwargs.get("options", [])
    for project in _load_project_files():
        for version_details in _collapse_historical_versions(project["versions"]):
            version_details = dict(version_details)
            option = {
                "taxonomy_1": "oomp",
                "taxonomy_2": "project",
                "taxonomy_3": "github",
                "taxonomy_4": _normalize_project_slug(project["github_user"]),
                "taxonomy_5": _normalize_project_slug(project["github_repository"]),
                "project_github_user": _normalize_project_slug(project["github_user"]),
                "project_github_repository": project["github_repository"],
                "project_github_url": project["github_url"],
                "project_git_url": project["repository_url"],
                "project_git_ref": version_details.get("git_ref", "main"),
                "project_sparse_checkout": bool(version_details.get("sparse_checkout", False)),
                "project_version": version_details.get("version", "current"),
                "project_file_folder": version_details.get("project_file_folder", ""),
                "project_file_basename": version_details.get("project_file_basename", ""),
                "project_file_path": version_details.get("project_file_path", ""),
                "project_file_path_original": version_details.get("project_file_path_original", ""),
                "project_file_extensions": list(PROJECT_FILE_EXTENSIONS),
                "project_match_overrides": {},
                "project_match_blocked": dict(version_details.get("match_blocked", {})),
                "project_review_notes": list(version_details.get("review_notes", [])),
                "production_board_source": version_details.get("production_board_source", ""),
                "production_oomp_metadata_board": version_details.get("production_oomp_metadata_board", ""),
                "production_exclude_references": list(version_details.get("production_exclude_references", [])),
                "production_lcsc_overrides": dict(version_details.get("production_lcsc_overrides", {})),
                "production_rotation_offsets": dict(version_details.get("production_rotation_offsets", {})),
                "production_position_offsets_mm": dict(version_details.get("production_position_offsets_mm", {})),
            }
            board = _normalize_project_slug(version_details.get("board", ""))
            if board:
                option["taxonomy_6"] = board
                option["taxonomy_7"] = _normalize_project_slug(version_details.get("version", "current"))
                option["project_board"] = board
                option["project_board_name"] = version_details.get("board_name", board.replace("_", " "))
                option["project_board_url"] = version_details.get("board_url", "")
            else:
                option["taxonomy_6"] = _normalize_project_slug(version_details.get("version", "current"))
            if str(version_details.get("source_format", "kicad")).strip().lower() != "kicad":
                option["project_source_format"] = version_details["source_format"]
            options.append(option)


if __name__ == "__main__":
    main()
