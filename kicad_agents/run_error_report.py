import traceback
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def run_error_log_path():
    return REPOSITORY_ROOT / "report" / "errors_during_run.txt"


def log_run_error(stage, error, command=None):
    path = run_error_log_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"[{datetime.now(timezone.utc).isoformat()}] {stage}",
        f"Error type: {type(error).__name__}",
        f"Error message: {error}",
    ]
    if command is not None:
        lines.append(f"Command: {' '.join(str(value) for value in command)}")
    lines.extend([
        "Traceback:",
        traceback.format_exc(),
        "",
    ])
    with path.open("a", encoding="utf-8") as output_file:
        output_file.write("\n".join(lines))