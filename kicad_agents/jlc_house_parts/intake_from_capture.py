"""Turn one locally saved browser capture into an editable intake observation.

The caller supplies the OOMP classification decision. This tool does not
choose a generic equivalence, edit populate files or promote a JLC choice.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from kicad_agents.jlc_house_parts_agent import build_intake_scaffold


DATA = Path(__file__).resolve().parent


def observation_from_capture(capture: dict, row: dict, *, part_id: str,
                             family: str, pin_count: int, compatibility_notes: str,
                             evidence_notes: list[str]) -> dict:
    if not re.fullmatch(r"electronic_[a-z0-9_]+", part_id):
        raise ValueError("Choose a valid explicit OOMP part ID")
    if not compatibility_notes.strip() or not evidence_notes:
        raise ValueError("Record the classification decision and evidence")
    omitted = {"Category", "Manufacturer", "Package"}
    result = {key: capture.get(key) for key in (
        "official_url", "code", "manufacturer", "mpn", "package",
        "tier_label", "description", "datasheet_url", "captured_on",
        "stock_observed", "purchase_moq_observed", "full_reel_observed",
        "available_order_qty_observed", "pcba_min_qty_observed")}
    result["specifications"] = {
        key: value for key, value in (capture.get("specifications") or {}).items()
        if key not in omitted
    }
    result.update(part_id=part_id, family=family, pin_count=pin_count,
                  compatibility_notes=compatibility_notes,
                  evidence_notes=evidence_notes + [
                      f"Full visible product-page text saved from the interactive browser "
                      f"in kicad_agents/jlc_house_parts/browser_staging/{row['code']}.json."
                  ])
    build_intake_scaffold(row, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code")
    parser.add_argument("--part-id", required=True)
    parser.add_argument("--family", required=True)
    parser.add_argument("--pin-count", type=int, required=True)
    parser.add_argument("--compatibility-notes", required=True)
    parser.add_argument("--evidence-note", action="append", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"C\d+", args.code):
        parser.error("Code must be a JLC C-number")
    queue = {item["code"]: item for item in json.loads((DATA / "queue.json").read_text(encoding="utf-8"))}
    row = queue.get(args.code)
    if row is None or row.get("retired"):
        parser.error("Code is not an active queue item")
    capture_path = DATA / "browser_staging" / f"{args.code}.json"
    capture = json.loads(capture_path.read_text(encoding="utf-8"))
    result = observation_from_capture(
        capture, row, part_id=args.part_id, family=args.family,
        pin_count=args.pin_count, compatibility_notes=args.compatibility_notes,
        evidence_notes=args.evidence_note)
    output = DATA / "observations" / f"{args.code}.json"
    if output.exists():
        raise SystemExit(f"Observation already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
