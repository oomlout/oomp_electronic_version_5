import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    os.chdir(ROOT)

    kicad_bin = Path(r"C:\Program Files\KiCad\10.0\bin")
    current_path = os.environ.get("PATH", "")
    if str(kicad_bin) not in current_path.split(os.pathsep):
        os.environ["PATH"] = str(kicad_bin) + os.pathsep + current_path

    filter_value = "oomp_project_github_sparkfun_adxl345_breakout_adxl345_breakout_current"
    print("Running the full SparkFun ADXL345 Breakout import and generation process...")
    print()

    try:
        from action_generate import generate

        generate(filter_value)
        print()
        print("ADXL345 generation completed successfully.")
        return 0
    except Exception as exc:  # pragma: no cover - simple debug wrapper
        print()
        print(f"ADXL345 generation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
