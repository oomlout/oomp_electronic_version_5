"""Build the deterministic, website-facing ``web.yaml`` for one OOMP part.

The action runs last in each part's Roboclick recipe.  It intentionally records
no timestamps or local absolute paths, so a no-change rebuild produces the same
file on every machine.
"""

from __future__ import annotations

import argparse
import copy
import fnmatch
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_FILE = REPOSITORY_ROOT / "config_web_manifest.yaml"

FILE_MIME_TYPES = {
    ".bat": "text/plain",
    ".c": "text/x-c",
    ".cpp": "text/x-c++",
    ".csv": "text/csv",
    ".gbr": "text/plain",
    ".ger": "text/plain",
    ".gif": "image/gif",
    ".h": "text/x-c",
    ".html": "text/html",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "text/javascript",
    ".drl": "text/plain",
    ".kicad_dru": "text/plain",
    ".kicad_mod": "text/plain",
    ".kicad_pcb": "text/plain",
    ".kicad_pro": "application/json",
    ".kicad_sch": "text/plain",
    ".kicad_sym": "text/plain",
    ".md": "text/markdown",
    ".json": "application/json",
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".pos": "text/csv",
    ".py": "text/x-python",
    ".step": "model/step",
    ".stp": "model/step",
    ".stl": "model/stl",
    ".svg": "image/svg+xml",
    ".txt": "text/plain",
    ".webp": "image/webp",
    ".wrl": "model/vrml",
    ".xml": "application/xml",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
    ".zip": "application/zip",
}


def _load_config(config_file: str | Path | None = None) -> dict:
    path = Path(config_file) if config_file else DEFAULT_CONFIG_FILE
    if not path.is_absolute():
        path = REPOSITORY_ROOT / path
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Web manifest config must be a YAML mapping: {path}")
    return loaded


def _matches(path: str, patterns: list[str]) -> bool:
    path_lower = path.lower()
    name_lower = Path(path).name.lower()
    for pattern in patterns:
        pattern_lower = str(pattern).replace("\\", "/").lower()
        has_wildcard = any(character in pattern_lower for character in "*?[")
        if fnmatch.fnmatch(path_lower, pattern_lower) or (
            has_wildcard and fnmatch.fnmatch(name_lower, pattern_lower)
        ):
            return True
    return False


def _github_urls(config: dict, part_id: str, relative_path: str = "") -> dict[str, str]:
    repository = config.get("repository", {})
    owner = repository.get("owner", "oomlout")
    name = repository.get("name", "oomp_electronic_version_5")
    branch = repository.get("branch", "main")
    parts_path = str(repository.get("parts_path", "parts")).strip("/")
    repository_path = "/".join(piece for piece in [parts_path, part_id, relative_path] if piece)
    encoded_path = quote(repository_path, safe="/")
    encoded_branch = quote(str(branch), safe="/")
    if relative_path:
        github_url = f"https://github.com/{owner}/{name}/blob/{encoded_branch}/{encoded_path}"
        raw_url = f"https://raw.githubusercontent.com/{owner}/{name}/{encoded_branch}/{encoded_path}"
    else:
        github_url = f"https://github.com/{owner}/{name}/tree/{encoded_branch}/{encoded_path}"
        raw_url = f"https://raw.githubusercontent.com/{owner}/{name}/{encoded_branch}/{encoded_path}"
    return {"github": github_url, "raw": raw_url}


def _web_url(config: dict, part_id: str, relative_path: str = "") -> str:
    pages_base = str(config.get("repository", {}).get("pages_base_url", "")).rstrip("/")
    suffix = "/".join(quote(piece) for piece in [part_id, *Path(relative_path).parts] if piece)
    return f"{pages_base}/{suffix}" if pages_base else ""


def _format_bytes(size_bytes: int) -> str:
    if size_bytes < 1000:
        return f"{size_bytes} B"
    value = float(size_bytes)
    for unit in ["kB", "MB", "GB", "TB"]:
        value /= 1000
        if value < 1000 or unit == "TB":
            return f"{value:.1f} {unit}" if value < 10 else f"{value:.0f} {unit}"
    return f"{size_bytes} B"


def _category_for(relative_path: str, config: dict) -> str:
    for category, patterns in config.get("inventory", {}).get("categories", {}).items():
        if _matches(relative_path, patterns or []):
            return str(category)
    return "other"


def _friendly_name(relative_path: str) -> str:
    stem = Path(relative_path).stem
    for prefix in ["working_svg_", "working_", "generation_"]:
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
    stem = stem.removesuffix("_300")
    return stem.replace("_", " ").replace("-", " ").strip().title() or Path(relative_path).name


def _description_for(relative_path: str, category: str, config: dict) -> str:
    descriptions = config.get("descriptions", {})
    exact = descriptions.get("exact", {})
    if relative_path in exact:
        return str(exact[relative_path])
    for pattern, description in descriptions.get("patterns", {}).items():
        if _matches(relative_path, [pattern]):
            return str(description)

    label = _friendly_name(relative_path)
    fallbacks = {
        "archive": f"Downloadable {label} archive.",
        "datasheet": f"Reference datasheet: {label}.",
        "document": f"Supporting document: {label}.",
        "documentation": f"Supporting documentation: {label}.",
        "image": f"Raster image: {label}.",
        "kicad": f"KiCad design asset: {label}.",
        "manufacturing": f"Manufacturing or assembly file: {label}.",
        "metadata": f"Structured metadata: {label}.",
        "model_3d": f"3D model: {label}.",
        "project_data": f"Generated project asset: {label}.",
        "upstream_source": f"Preserved upstream source: {label}.",
        "vector": f"Scalable vector artwork: {label}.",
    }
    return fallbacks.get(category, f"Project file: {label}.")


def _mime_type(path: Path) -> str:
    return FILE_MIME_TYPES.get(path.suffix.lower(), "application/octet-stream")


def _metadata_from_working(working: dict, config: dict) -> dict:
    metadata_config = config.get("metadata", {})
    excluded_fields = set(metadata_config.get("exclude_fields", []))
    excluded_prefixes = tuple(metadata_config.get("exclude_prefixes", []))
    return {
        key: copy.deepcopy(value)
        for key, value in working.items()
        if key not in excluded_fields and not str(key).startswith(excluded_prefixes)
    }


def _taxonomy(working: dict) -> list[dict]:
    values = []
    for level in range(1, 16):
        value = working.get(f"taxonomy_{level}", "")
        if value not in (None, ""):
            values.append({"level": level, "value": str(value), "label": str(value).replace("_", " ").title()})
    return values


def _declared_outputs(working: dict, part_directory: Path, config: dict) -> list[dict]:
    outputs: dict[str, dict] = {}
    for mode_name, mode in working.items():
        if not str(mode_name).startswith("oomlout_") or not isinstance(mode, dict):
            continue
        actions = mode.get("actions", []) if isinstance(mode.get("actions", []), list) else []
        if any(str(action.get("file_python", "")).replace("\\", "/").endswith("web_manifest_action.py") for action in actions if isinstance(action, dict)):
            continue
        candidates = []
        file_test = mode.get("file_test", "")
        candidates.extend(file_test if isinstance(file_test, list) else [file_test])
        for action in actions:
            if isinstance(action, dict):
                candidates.append(action.get("file_output", ""))
                candidates.append(action.get("file_destination", ""))
        for candidate in candidates:
            relative_path = str(candidate or "").replace("\\", "/").lstrip("./")
            if not relative_path or Path(relative_path).is_absolute():
                continue
            if relative_path not in outputs:
                urls = _github_urls(config, part_directory.name, relative_path)
                outputs[relative_path] = {
                    "path": relative_path,
                    "available": (part_directory / relative_path).is_file(),
                    "github_url": urls["github"],
                    "raw_url": urls["raw"],
                    "web_url": _web_url(config, part_directory.name, relative_path),
                }
    return [outputs[path] for path in sorted(outputs)]


def _inventory(part_directory: Path, output_filename: str, config: dict) -> tuple[list[dict], dict]:
    inventory_config = config.get("inventory", {})
    excluded = list(inventory_config.get("exclude", []))
    if output_filename not in excluded:
        excluded.append(output_filename)
    include_hidden = bool(inventory_config.get("include_hidden", False))
    files = []
    root = part_directory.resolve()

    for path in sorted(part_directory.rglob("*"), key=lambda item: item.as_posix().lower()):
        if not path.is_file() or not path.resolve().is_relative_to(root):
            continue
        relative_path = path.relative_to(part_directory).as_posix()
        if (not include_hidden and any(piece.startswith(".") for piece in Path(relative_path).parts)) or _matches(relative_path, excluded):
            continue
        category = _category_for(relative_path, config)
        urls = _github_urls(config, part_directory.name, relative_path)
        stat = path.stat()
        files.append(
            {
                "name": path.name,
                "path": relative_path,
                "directory": Path(relative_path).parent.as_posix() if "/" in relative_path else ".",
                "extension": path.suffix.lower(),
                "media_type": _mime_type(path),
                "category": category,
                "description": _description_for(relative_path, category, config),
                "size_bytes": stat.st_size,
                "size": _format_bytes(stat.st_size),
                "github_url": urls["github"],
                "raw_url": urls["raw"],
                "web_url": _web_url(config, part_directory.name, relative_path),
            }
        )

    category_counts = Counter(item["category"] for item in files)
    category_sizes = Counter()
    extension_counts = Counter(item["extension"] or "[no extension]" for item in files)
    extension_sizes = Counter()
    for item in files:
        category_sizes[item["category"]] += item["size_bytes"]
        extension_sizes[item["extension"] or "[no extension]"] += item["size_bytes"]
    largest = max(files, key=lambda item: (item["size_bytes"], item["path"])) if files else None
    stats = {
        "file_count": len(files),
        "total_size_bytes": sum(item["size_bytes"] for item in files),
        "total_size": _format_bytes(sum(item["size_bytes"] for item in files)),
        "by_category": {
            category: {
                "count": category_counts[category],
                "size_bytes": category_sizes[category],
                "size": _format_bytes(category_sizes[category]),
            }
            for category in sorted(category_counts)
        },
        "by_extension": {
            extension: {
                "count": extension_counts[extension],
                "size_bytes": extension_sizes[extension],
                "size": _format_bytes(extension_sizes[extension]),
            }
            for extension in sorted(extension_counts)
        },
        "largest_file": (
            {"path": largest["path"], "size_bytes": largest["size_bytes"], "size": largest["size"]}
            if largest else None
        ),
    }
    return files, stats


def _primary_assets(files: list[dict], config: dict) -> list[dict]:
    priorities = config.get("inventory", {}).get("primary_asset_priority", [])
    selected = []
    used = set()
    for pattern in priorities:
        for item in files:
            if item["path"] not in used and _matches(item["path"], [pattern]):
                selected.append(copy.deepcopy(item))
                used.add(item["path"])
                break
    return selected


def build_web_manifest(details: dict) -> dict:
    """Create and write a web manifest, returning its in-memory representation."""
    part_directory = Path(details.get("directory", "")).resolve()
    working_file = part_directory / "working.yaml"
    if not working_file.is_file():
        raise FileNotFoundError(f"Missing OOMP definition: {working_file}")
    working = yaml.safe_load(working_file.read_text(encoding="utf-8")) or {}
    if not isinstance(working, dict):
        raise ValueError(f"working.yaml must contain a YAML mapping: {working_file}")

    config = _load_config(details.get("manifest_config"))
    requested_output = Path(str(details.get("file_output") or config.get("output_filename", "web.yaml")))
    output_path = requested_output.resolve() if requested_output.is_absolute() else (part_directory / requested_output).resolve()
    if not output_path.is_relative_to(part_directory):
        raise ValueError("Web manifest output must stay inside the part directory.")
    output_filename = output_path.relative_to(part_directory).as_posix()

    files, stats = _inventory(part_directory, output_filename, config)
    part_id = str(working.get("id") or working.get("name") or part_directory.name)
    part_kind = "project" if working.get("taxonomy_1") == "oomp" and working.get("taxonomy_2") == "project" else "navigation" if working.get("taxonomy_1") == "navigation" else "component"
    taxonomy = _taxonomy(working)
    urls = _github_urls(config, part_directory.name)
    manifest_urls = _github_urls(config, part_directory.name, output_filename)
    pages_base = str(config.get("repository", {}).get("pages_base_url", "")).rstrip("/")
    modes = [mode for name, mode in working.items() if str(name).startswith("oomlout_") and isinstance(mode, dict)]
    action_count = sum(len(mode.get("actions", [])) for mode in modes if isinstance(mode.get("actions", []), list))

    manifest = {
        "schema_version": config.get("schema_version", 1),
        "id": part_id,
        "kind": part_kind,
        "name": working.get("name_readable") or working.get("name_short") or working.get("name_proper") or part_id.replace("_", " ").title(),
        "summary": (working.get("part_page", {}) or {}).get("summary") or working.get("description") or working.get("name_readable") or part_id.replace("_", " "),
        "taxonomy": {
            "path": [item["value"] for item in taxonomy],
            "breadcrumb": " / ".join(item["label"] for item in taxonomy),
            "items": taxonomy,
        },
        "links": {
            "github": urls["github"],
            "raw_base": urls["raw"].rstrip("/") + "/",
            "web_page": _web_url(config, part_directory.name) + "/" if pages_base else "",
            "manifest_github": manifest_urls["github"],
            "manifest_raw": manifest_urls["raw"],
        },
        "highlights": {
            "category": working.get("category", ""),
            "category_name": working.get("category_name", ""),
            "dimensions_mm": copy.deepcopy(working.get("dimensions_mm", {})),
            "pin_count": len(working.get("pins", {})) if isinstance(working.get("pins", {}), dict) else 0,
            "manufacturer_count": len(working.get("manufacturers", [])) if isinstance(working.get("manufacturers", []), list) else 0,
            "distributor_count": len(working.get("distributors", [])) if isinstance(working.get("distributors", []), list) else 0,
        },
        "primary_assets": _primary_assets(files, config),
        "file_stats": stats,
        "files": files,
        "generation": {
            "source": "working.yaml",
            "roboclick_mode_count": len(modes),
            "roboclick_action_count": action_count,
            "declared_outputs": _declared_outputs(working, part_directory, config),
            "manifest_action": {
                "command": "run_python",
                "file_python": "kicad_agents/web_manifest_action.py",
                "runs_last": True,
                "runs_on_every_regeneration": True,
            },
        },
        "metadata": _metadata_from_working(working, config),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = output_path.with_name(output_path.name + ".tmp")
    temporary_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    temporary_path.replace(output_path)
    print(f"wrote website manifest for {part_id}: {output_path} ({len(files)} files)")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kwargs", required=True, help="JSON action details supplied by Roboclick")
    arguments = parser.parse_args()
    build_web_manifest(json.loads(arguments.kwargs))


if __name__ == "__main__":
    main()
