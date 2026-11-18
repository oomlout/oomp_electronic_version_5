"""Locate the KiCad command-line executable consistently across actions."""

import os
import re
import shutil
from pathlib import Path


def _natural_key(value):
    return [
        int(piece) if piece.isdigit() else piece.lower()
        for piece in re.split(r"(\d+)", str(value))
    ]


def installation_directories():
    """Find machine-wide and per-user Windows installations, newest first."""
    configured = os.environ.get('OOMP_KICAD_ROOT', '').strip()
    if configured:
        yield Path(configured)
    bases = [Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'KiCad']
    local = os.environ.get('LOCALAPPDATA')
    if local:
        bases.append(Path(local) / 'Programs' / 'KiCad')
    candidates = [version for base in bases if base.is_dir() for version in base.iterdir() if version.is_dir()]
    yield from sorted(candidates, key=lambda item: _natural_key(item.name), reverse=True)


def find_kicad_cli(configured=None):
    """Return an explicit command, a discovered install, or the standard name.

    Generated project actions deliberately use an empty string when no
    per-project override is configured.  An empty first argument is not a
    usable process name on Windows, so it must be treated as unset.
    """
    explicit = str(configured or os.environ.get("KICAD_CLI") or "").strip()
    if explicit:
        return explicit

    discovered = shutil.which("kicad-cli")
    if discovered:
        return discovered

    for version_directory in installation_directories():
        candidate = version_directory / "bin" / "kicad-cli.exe"
        if candidate.is_file():
            return str(candidate.resolve())

    return "kicad-cli"
