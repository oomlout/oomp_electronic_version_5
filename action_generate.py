"""Normal populate -> working_oomp -> Roboclick generation; preserve PNGs."""

import argparse
import os

from action_regenerate_all import REPOSITORY_ROOT, run_actions
import working_oomp
import working_oomp_populate


def generate(filter_text):
    if not filter_text.strip():
        raise ValueError("Give a part ID or family prefix; use action_regenerate_all.bat for a full rebuild.")
    os.chdir(REPOSITORY_ROOT)
    # Navigation is lightweight and must include new parts and all ancestors.
    filters = [filter_text, "navigation"]
    working_oomp_populate.main()
    working_oomp.main(filter=filters, regenerate_pngs=False)
    action_count, skipped = run_actions(filter_text=filters, regenerate_pngs=False)
    from kicad_agents.kicad_library_agent import package_libraries
    package_libraries(REPOSITORY_ROOT / "parts", REPOSITORY_ROOT / "kicad_libraries")
    print(f"Generated {filter_text}: {action_count} actions; {skipped} browser actions skipped. Existing PNGs retained.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter", required=True, help="OOMP part ID or family prefix to generate")
    args = parser.parse_args()
    generate(args.filter)


if __name__ == "__main__":
    main()
