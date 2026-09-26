"""Offline JLC house-part intake queue. Browser research precedes population edits.

Run from the repository: python -m kicad_agents.jlc_house_parts_agent next
No network access, automatic equivalence decisions, or bulk population writes.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import contextlib
from copy import deepcopy
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import io
import json
import math
from pathlib import Path
import re
import sys
import time
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "kicad_agents/jlc_house_parts"
SOURCE = DATA / "sources/catalogue-browser-official-2026-09-26.json"
CLAIMS = DATA / "claims"
LOCKS = DATA / "locks"
STAGING = DATA / "browser_staging"
HOUSE_TIER_LABELS = ("Basic", "Preferred", "Promotional")
TIER_LABELS = HOUSE_TIER_LABELS + ("Extended",)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_capture(capture):
    """Parse saved visible table rows; reject truncation, duplicates and schema drift."""
    result, seen = [], set()
    for raw in capture:
        c = raw["cells"]
        if len(c) != 16:
            raise ValueError("Expected 16 catalogue columns")
        code = c[0].split()[0]
        if not re.fullmatch(r"C[0-9]+", code) or code in seen:
            raise ValueError(f"Invalid or duplicate catalogue code: {code}")
        seen.add(code)
        if c[1] not in ("base", "expand 👍") or c[15] not in ("0", "1"):
            raise ValueError(f"Unknown class/deletion flag: {code}")
        links = raw["links"]
        product = next(x["url"] for x in links if x["text"] == code)
        result.append(dict(
            code=code, tier="basic" if c[1] == "base" else "preferred_extended",
            retired=c[15] == "1", category=c[2], manufacturer=c[3], mpn=c[4],
            package=c[5], description=c[6], original_description=c[7],
            price_snapshot=c[8], stock_snapshot=int(c[9]), purchase_moq=c[10],
            pcba_min_qty=c[11], pcba_min_price=c[12], first_seen=c[13], last_seen=c[14],
            jlcpcb_url=product,
            datasheet_url=next((x["url"] for x in links if x["text"] == "doc"), ""),
        ))
    return sorted(result, key=lambda x: int(x["code"][1:]))


def population():
    """Evaluate the real population chain without writing generated files."""
    import working_oomp_populate as populate
    from oomp_populate_helper import build_oomp_id
    with contextlib.redirect_stdout(io.StringIO()), patch.object(populate, "write_extras") as output:
        populate.main()
    records = output.call_args.args[0]
    counts = Counter(build_oomp_id(x) for x in records)
    return {build_oomp_id(x): x for x in records if x.get("taxonomy_1") == "electronic"}, {
        key: count for key, count in counts.items() if count > 1
    }


def generic_hint(row):
    """Only size/value hints. These deliberately do NOT establish compatibility."""
    package, description = row["package"], row["description"]
    if package not in ("0201", "0402", "0603", "0805", "1206", "1210", "2010", "2512"):
        return ""
    if row["category"] == "Resistors: Chip Resistor - Surface Mount":
        match = re.search(r"(?<![\w.])(\d+(?:\.\d+)?)([kM]?)Ω", description)
        if match:
            value = Decimal(match[1]) * {"": 1, "k": 1000, "M": 1000000}[match[2]]
            token = format(value.normalize(), "f").replace(".", "_")
            return f"electronic_resistor_{package}_{token}_ohm"
    if row["category"] == "Capacitors: Multilayer Ceramic Capacitors MLCC - SMD/SMT":
        match = re.search(r"(?<![\w.])(\d+(?:\.\d+)?)([pnuµ])F", description)
        if match:
            value = Decimal(match[1]) * {"p": 1, "n": 1000, "u": 1000000, "µ": 1000000}[match[2]]
            scale, unit = (1000000, "micro") if value >= 1000000 else ((1000, "nano") if value >= 1000 else (1, "pico"))
            token = format((value / scale).normalize(), "f").replace(".", "_")
            return f"electronic_capacitor_{package}_{token}_{unit}_farad"
    return ""


def code_options(part):
    codes = {str(v) for k, v in part.items() if k.startswith("part_number_lcsc") and isinstance(v, str)}
    codes.update(str(x.get("part_number", "")) for x in part.get("part_numbers_lcsc", []) if isinstance(x, dict))
    return {x for x in codes if re.fullmatch(r"C\d+", x)}


def prepare():
    catalogue = normalize_capture(read_json(SOURCE))
    if len(catalogue) != 3452 or sum(not x["retired"] for x in catalogue) != 1574:
        raise ValueError("Captured snapshot count mismatch; check browser truncation or intentionally update the snapshot contract")
    parts, duplicates = population()
    by_code, by_mpn = defaultdict(set), defaultdict(set)
    for part_id, part in parts.items():
        for code in code_options(part):
            by_code[code].add(part_id)
        mpns = [part.get("part_number_manufacturer", "")]
        mpns += [x.get("part_number", "") for x in part.get("part_numbers_manufacturer", []) if isinstance(x, dict)]
        for mpn in filter(None, mpns):
            by_mpn[str(mpn).casefold()].add(part_id)
    queue = []
    for row in catalogue:
        if row["retired"]:
            continue
        hint = generic_hint(row)
        candidates = []
        for part_id in sorted(by_code[row["code"]] | by_mpn[row["mpn"].casefold()] | ({hint} if hint in parts else set())):
            part = parts[part_id]
            reasons = []
            if part_id in by_code[row["code"]]: reasons.append("existing_lcsc_code")
            if part_id in by_mpn[row["mpn"].casefold()]: reasons.append("mpn_text_only")
            if part_id == hint: reasons.append("generic_size_value_only")
            candidates.append(dict(part_id=part_id, reasons=reasons,
                                   current_lcsc=part.get("part_number_lcsc", ""),
                                   current_mpn=part.get("part_number_manufacturer", "")))
        queue.append(dict(row, ledger_id="JLC_" + row["code"], candidates=candidates,
                          generic_id_hint=hint, requires_official_verification=True))
    queue.sort(key=lambda x: (x["tier"] != "basic", not bool(x["candidates"]), x["category"], int(x["code"][1:])))
    write_json(DATA / "catalogue.json", catalogue)
    write_json(DATA / "queue.json", queue)
    # Phase two covers ALL existing OOMP components, including non-house JLC listings.
    audit = [dict(part_id=key, lcsc_codes=sorted(code_options(p)),
                  jlcpcb_code=p.get("part_number_jlcpcb", ""),
                  action="verify_jlc_listing" if code_options(p) else "research_missing_supplier")
             for key, p in sorted(parts.items())]
    write_json(DATA / "existing_parts_audit.json", audit)
    summary = dict(source_url="https://jlcpcb.com/parts/basic_parts",
                   csv_url="",
                   captured_on="2026-09-26", source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                   total=len(catalogue), active=len(queue), retired=len(catalogue)-len(queue),
                   tiers=dict(Counter(x["tier"] for x in queue)),
                   categories=dict(Counter(x["category"] for x in queue)),
                   candidates_with_existing_oomp_hints=sum(bool(x["candidates"]) for x in queue),
                   existing_electronic_parts=len(parts),
                   existing_parts_with_lcsc=sum(bool(code_options(x)) for x in parts.values()),
                   duplicate_population_ids=duplicates,
                   completeness="2026-09-26 browser crawl of the official Basic & Promotional Extended category (64 pages, 25 rows each); 1574 active rows captured, 20 page-boundary duplicates removed, 6 non-standard listings without a readable class badge excluded (C3116 C4650 C4662 C4664 C4688 C4689); the official category was re-curated since 2026-09-18, so 1460 dated-snapshot codes no longer listed are retired here and only 126 codes survive; category/package fields are kept from the dated mirror for surviving codes and empty for new ones.")
    write_json(DATA / "summary.json", summary)
    lines = ["# JLC house-part analysis queue", "", "Snapshot: 18 September 2026; captured 24 September. Candidates, not approved substitutions.", "", "| Code | Class | Manufacturer / MPN | Package | OOMP candidates |", "| --- | --- | --- | --- | --- |"]
    for x in queue:
        clean = lambda value: str(value).replace("|", "/").replace("\n", " ")
        lines.append(f"| [{x['code']}]({x['jlcpcb_url']}) | {x['tier']} | {clean(x['manufacturer'])} / {clean(x['mpn'])} | {clean(x['package'])} | {', '.join(c['part_id'] for c in x['candidates']) or 'Needs matching / new entry'} |")
    (DATA / "BACKLOG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def progress_for(code):
    path = DATA / "progress" / (code + ".json")
    if not path.exists():
        return {"code": code, "intake": {"status": "pending"}, "full": {"status": "pending"}}
    state = read_json(path)
    if "intake" not in state:
        # Compatibility with progress from the original single-pass worker.
        old = state.get("status", "pending")
        state = {"code": code,
                 "intake": {"status": "complete" if old == "complete" else old},
                 "full": {"status": old}}
    return state


def claim_records(stage):
    """Active worker claims for one stage: code -> claim payload."""
    claims = {}
    if CLAIMS.is_dir():
        prefix = stage + "_"
        for path in CLAIMS.glob(f"{prefix}C*.json"):
            try:
                claims[path.stem[len(prefix):]] = read_json(path)
            except (ValueError, OSError):
                continue
    return claims


def claim_code(code, stage, worker):
    """Claim one queue item atomically: exclusive file creation decides the winner."""
    CLAIMS.mkdir(parents=True, exist_ok=True)
    payload = {"worker": worker, "stage": stage,
               "claimed_at": datetime.now(timezone.utc).isoformat()}
    try:
        with open(CLAIMS / f"{stage}_{code}.json", "x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
    except FileExistsError:
        return False
    return True


def release_claim(code, stage):
    with contextlib.suppress(FileNotFoundError):
        (CLAIMS / f"{stage}_{code}.json").unlink()


def acquire_lock(name, owner, wait_seconds=600):
    """Hold an exclusive local lock file across one shared-file critical section."""
    LOCKS.mkdir(parents=True, exist_ok=True)
    path = LOCKS / f"{name}.lock"
    deadline = time.monotonic() + wait_seconds
    while True:
        try:
            with open(path, "x", encoding="utf-8") as handle:
                json.dump({"owner": owner, "acquired_at": datetime.now(timezone.utc).isoformat()}, handle, indent=2)
                handle.write("\n")
            return path
        except FileExistsError:
            if time.monotonic() >= deadline:
                try:
                    holder = read_json(path).get("owner", "unknown")
                except (ValueError, OSError):
                    holder = "unknown"
                raise SystemExit(f"Lock {name} is held by {holder}; retry later or clear an abandoned lock with release --stale")
            time.sleep(2)


def release_lock(path):
    with contextlib.suppress(FileNotFoundError):
        Path(path).unlink()


def release_stale(max_age_hours):
    """Remove claim and lock files untouched for max_age_hours (crashed workers)."""
    removed = []
    cutoff = time.time() - max_age_hours * 3600
    for directory in (CLAIMS, LOCKS):
        if not directory.is_dir():
            continue
        for path in directory.iterdir():
            if path.is_file() and path.stat().st_mtime < cutoff:
                path.unlink()
                removed.append(str(path.relative_to(DATA)))
    return sorted(removed)


def staged_capture_path(code):
    return STAGING / f"{code}.json"


def staged_capture_fresh(code, max_age_hours):
    path = staged_capture_path(code)
    return path.is_file() and (time.time() - path.stat().st_mtime) <= max_age_hours * 3600


def load_staged_capture(code, *, max_age_hours):
    if not staged_capture_fresh(code, max_age_hours):
        raise SystemExit(f"No fresh staged browser capture for {code}; a browser reader must stage one first")
    return read_json(staged_capture_path(code))


def plan_workers(queue, stage, workers):
    """Balance pending categories across workers; oversized categories are shared.

    Sharing a category between workers is safe: claims arbitrate individual
    codes, and the family edit lock serialises populate-file changes.
    """
    pending = [row for row in queue if progress_for(row["code"])[stage]["status"] == "pending"]
    counts = Counter(row["category"] for row in pending)
    target = max(1, -(-len(pending) // workers))
    assignments = [[] for _ in range(workers)]
    loads = [0] * workers
    for category, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        if count > target:
            chosen = sorted(range(workers), key=lambda index: (loads[index], index))[:max(1, round(count / target))]
        else:
            chosen = [min(range(workers), key=lambda index: (loads[index], index))]
        for index in chosen:
            assignments[index].append(category)
            loads[index] += count / len(chosen)
    plan = []
    for index, categories in enumerate(assignments, start=1):
        worker = f"W{index}"
        command = f"python -m kicad_agents.jlc_house_parts_agent next --stage {stage} --claim --worker {worker}"
        if categories:
            command += f' --categories "{";".join(sorted(categories))}"'
        plan.append(dict(worker=worker, categories=sorted(categories),
                         pending_pool=sum(counts[c] for c in categories), claim_command=command))
    return dict(stage=stage, pending=len(pending), target_per_worker=target, workers=plan)


def build_intake_scaffold(row, observed):
    """Build editable intake evidence from facts transcribed from the live browser page.

    This deliberately does not decide whether a generic part is compatible and
    does not promote a purchasing choice. The worker must supply that decision.
    """
    required = ("official_url", "code", "manufacturer", "mpn", "package",
                "tier_label", "description", "captured_on", "part_id", "family",
                "pin_count", "compatibility_notes", "evidence_notes")
    missing = [key for key in required if not observed.get(key)]
    if missing:
        raise ValueError("Missing browser/worker facts: " + ", ".join(missing))
    # An empty queued package means "not yet verified"; the live page adopts it.
    for key, expected in (("code", row["code"]), ("manufacturer", row["manufacturer"]),
                          ("mpn", row["mpn"]), ("package", row["package"]),
                          ("official_url", row["jlcpcb_url"])):
        if observed[key] != expected and not (key == "package" and not expected):
            raise ValueError(f"Observed {key} differs from queued candidate; resolve identity")
    tier = {"Basic": "basic", "Preferred": "preferred_extended",
            "Promotional": "preferred_extended"}.get(observed["tier_label"])
    if tier != row["tier"]:
        raise ValueError("Live JLC class differs from house-part snapshot")
    if not re.fullmatch(r"electronic_[a-z0-9_]+", observed["part_id"]):
        raise ValueError("Choose an explicit OOMP electronic part ID")
    if not isinstance(observed["evidence_notes"], list) or not all(
            isinstance(note, str) and note.strip() for note in observed["evidence_notes"]):
        raise ValueError("Provide nonempty evidence_notes as a list")
    try:
        capture_date = datetime.fromisoformat(observed["captured_on"]).date()
    except ValueError as exc:
        raise ValueError("captured_on must be YYYY-MM-DD") from exc
    if not 0 <= (datetime.now(timezone.utc).date() - capture_date).days <= 30:
        raise ValueError("Browser observation must be within the last 30 days")
    specs = observed.get("specifications") or {}
    if not isinstance(specs, dict):
        raise ValueError("specifications must be an object of observed strings")
    datasheet = str(observed.get("datasheet_url") or "").split("?", 1)[0]
    if datasheet and not datasheet.startswith("https://"):
        raise ValueError("Datasheet URL must be HTTPS")
    capture = f"parts_source/{observed['part_id']}/web_page_distributor_jlc.txt"
    lines = [f"Source URL: {observed['official_url']}",
             f"Captured: {observed['captured_on']}",
             "Method: browser-observed visible product-page text; this is a text snapshot, not an offline HTML copy.",
             "", f"{observed['mpn']} | {observed['manufacturer']} | JLCPCB",
             observed["tier_label"], f"Manufacturer: {observed['manufacturer']}",
             f"MFR.Part #: {observed['mpn']}", f"JLCPCB Part #: {row['code']}",
             f"Package: {observed['package']}", f"Description: {observed['description']}"]
    if datasheet:
        lines.append(f"Datasheet: {datasheet}")
    lines += ["", "Specifications"]
    lines += [f"{key}: {value}" for key, value in specs.items()]
    for label, key in (("In Stock", "stock_observed"), ("Minimum", "purchase_moq_observed"),
                       ("Full Reel", "full_reel_observed"), ("Available Order Qty", "available_order_qty_observed")):
        if observed.get(key) is not None:
            lines.append(f"{label}: {observed[key]}")
    record = dict(format_version=1, ledger_id=row["ledger_id"], status="researched",
                  family=observed["family"], part_id=observed["part_id"], exact_identity=True,
                  package=observed["package"], pin_count=int(observed["pin_count"]),
                  datasheet_required=True, project_references=[],
                  research=dict(manufacturer=observed["manufacturer"],
                                manufacturer_part_number=observed["mpn"],
                                lcsc_part_number=row["code"],
                                lcsc_decision=observed["compatibility_notes"],
                                product_url=observed["official_url"], datasheet_url=datasheet,
                                browser_sources=[observed["official_url"]],
                                webpage_capture=capture, evidence_notes=observed["evidence_notes"]),
                  jlc_selection=dict(verified_on=observed["captured_on"],
                                     official_url=observed["official_url"], tier=tier,
                                     tier_label_observed=observed["tier_label"],
                                     stock_observed=observed.get("stock_observed"),
                                     purchase_moq_observed=observed.get("purchase_moq_observed"),
                                     pcba_min_qty_observed=observed.get("pcba_min_qty_observed"),
                                     compatibility_notes=observed["compatibility_notes"],
                                     ratings=specs, datasheet_pages=[], pinout_checked=False,
                                     footprint_checked=False, visual_review="pending"))
    return capture, "\n".join(lines) + "\n", record


def select_task(queue, code=None, stage="intake", *, skip=(), categories=None, staged_hours=None):
    for row in queue:
        if code and row["code"] != code:
            continue
        if not code and row["code"] in skip:
            continue
        if categories is not None and row["category"] not in categories:
            continue
        if staged_hours is not None and not staged_capture_fresh(row["code"], staged_hours):
            continue
        state = progress_for(row["code"])
        if (stage == "full" and state["intake"]["status"] != "complete"):
            continue
        if code or state[stage]["status"] == "pending":
            return row
    raise ValueError("No pending candidate" if not code else "Code is not in active snapshot")


def check_intake_record(row, path, *, population_required=True):
    """Require a real OOMP purchasing identity and saved browser page; PDF optional."""
    import yaml
    record = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    research, selection = record.get("research") or {}, record.get("jlc_selection") or {}
    errors = []
    if record.get("ledger_id") != row["ledger_id"]:
        errors.append("ledger_id must match the queue item")
    if research.get("lcsc_part_number") != row["code"]:
        errors.append("research LCSC code must match the queue item")
    if research.get("manufacturer_part_number") != row["mpn"]:
        errors.append("MPN differs from snapshot; resolve source identity before intake")
    if research.get("manufacturer") != row["manufacturer"]:
        errors.append("Manufacturer differs from snapshot; resolve source identity before intake")
    if not research.get("evidence_notes") or not selection.get("compatibility_notes"):
        errors.append("Record the classification and reuse/addition decision")
    official = selection.get("official_url", "")
    if not re.match(r"https://(?:www\.)?jlcpcb\.com/partdetail/", str(official)) or not str(official).rstrip("/").endswith("/" + row["code"]):
        errors.append("Official JLCPCB detail URL must identify this C-number")
    if official not in research.get("browser_sources", []):
        errors.append("Official detail URL must be in the inspected browser sources")
    if selection.get("tier") not in ("basic", "preferred_extended"):
        errors.append("Verify Basic or Preferred house status on the official page")
    try:
        verified = datetime.fromisoformat(str(selection.get("verified_on"))).date()
        if not 0 <= (datetime.now(timezone.utc).date() - verified).days <= 30:
            errors.append("Official verification must be within the last 30 days")
    except ValueError:
        errors.append("verified_on must be YYYY-MM-DD")

    capture = str(research.get("webpage_capture") or "")
    capture_path = (ROOT / capture).resolve()
    if not capture or not capture_path.is_relative_to(ROOT) or not capture_path.is_file():
        errors.append("Save the browser-observed product webpage under this repository")
    else:
        captured = capture_path.read_text(encoding="utf-8")
        expected_page_facts = [row["code"], row["mpn"], row["manufacturer"], official]
        if row.get("package"):
            expected_page_facts.append(row["package"])
        if selection.get("tier_label_observed"):
            expected_page_facts.append(selection["tier_label_observed"])
        if any(value not in captured for value in expected_page_facts):
            errors.append("Saved webpage must contain the official URL, manufacturer, C-number, MPN, package and class")
    part_id = record.get("part_id", "")
    if not record.get("family"):
        errors.append("Record the OOMP source family")
    parts, duplicates = population()
    part = parts.get(part_id, {})
    if not part or part_id in duplicates:
        errors.append("Expected one populated OOMP component for the chosen part ID")
    if population_required:
        for field, expected in (("part_number_lcsc", row["code"]), ("part_number_jlcpcb", row["code"]),
                                ("part_number_manufacturer", row["mpn"]), ("manufacturer", row["manufacturer"])):
            if part.get(field) != expected:
                errors.append(f"Effective population {field} does not match the verified identity")
        if part.get("jlcpcb_selection") != selection:
            errors.append("Population must retain the exact recorded JLC selection")
    elif part.get("part_number_jlcpcb") not in (None, "", row["code"]):
        errors.append("This OOMP ID already has a different preferred JLC code; resolve taxonomy before promotion")
    elif not population_required and part:
        from working_oomp_populate_jlc import set_preferred_jlc
        try:
            set_preferred_jlc(deepcopy(part), code=row["code"],
                              manufacturer=row["manufacturer"], mpn=row["mpn"],
                              selection=selection)
        except ValueError as exception:
            errors.append(f"Purchasing identity cannot be applied: {exception}")
    return {"ledger_id": row["ledger_id"], "part_id": part_id,
            "stage": "intake", "status": "fail" if errors else "pass", "errors": errors}


def check_record(row, path, generated=False):
    import yaml
    from kicad_agents.component_addition_agent import validate_implementation
    record = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    result = validate_implementation(record, require_generated=generated)
    errors = result["errors"]
    research = record.get("research") or {}
    selection = record.get("jlc_selection") or {}
    if record.get("ledger_id") != row["ledger_id"]:
        errors.append("ledger_id must match the queue item")
    if research.get("lcsc_part_number") != row["code"]:
        errors.append("research LCSC code must match the queue item")
    if research.get("manufacturer_part_number") != row["mpn"]:
        errors.append("MPN differs from snapshot; resolve source identity before intake")
    if record.get("datasheet_required") is not True or int(record.get("pin_count") or 0) < 1:
        errors.append("House intake requires a datasheet and explicit positive pin count")
    for key in ("verified_on", "official_url", "tier", "compatibility_notes", "ratings", "pinout_checked", "footprint_checked", "visual_review"):
        if not selection.get(key): errors.append(f"jlc_selection.{key} is required")
    if selection.get("tier") not in ("basic", "preferred_extended"):
        errors.append("Part is no longer a verified house part; defer it instead")
    if not re.match(r"https://(?:www\.)?jlcpcb\.com/partdetail/", str(selection.get("official_url", ""))):
        errors.append("Official JLCPCB detail URL required")
    if not str(selection.get("official_url", "")).rstrip("/").endswith("/" + row["code"]):
        errors.append("Official detail URL must identify this C-number")
    if selection.get("official_url") not in research.get("browser_sources", []):
        errors.append("Official detail URL must be in the inspected browser sources")
    if not isinstance(selection.get("ratings"), dict) or not selection.get("ratings"):
        errors.append("Supply a structured dictionary of verified ratings with units")
    if generated and str(selection.get("visual_review", "")).strip().lower() in ("", "pending", "todo"):
        errors.append("Complete the rendered-artifact review before marking complete")
    if selection.get("pinout_checked") is not True or selection.get("footprint_checked") is not True:
        errors.append("Pinout and footprint checks must be true")
    try:
        verified = datetime.fromisoformat(str(selection.get("verified_on"))).date()
        if not 0 <= (datetime.now(timezone.utc).date() - verified).days <= 30:
            errors.append("Official verification must be within the last 30 days")
    except ValueError:
        errors.append("verified_on must be YYYY-MM-DD")
    parts, duplicates = population()
    part = parts.get(record.get("part_id"), {})
    if record.get("part_id") in duplicates:
        errors.append("Resolve duplicate population rows for this ID before intake")
    for field, expected in (("part_number_lcsc", row["code"]), ("part_number_jlcpcb", row["code"]),
                            ("part_number_manufacturer", research.get("manufacturer_part_number"))):
        if part.get(field) != expected: errors.append(f"Effective population {field} does not match verified choice")
    if part.get("jlcpcb_selection") != selection:
        errors.append("Family populate-extra must retain the exact jlc_selection evidence as jlcpcb_selection")
    if part.get("manufacturer") != research.get("manufacturer"):
        errors.append("Effective manufacturer must match the researched purchasing identity")
    if generated:
        generated_path = ROOT / "parts" / record["part_id"] / "working.yaml"
        actual = yaml.safe_load(generated_path.read_text(encoding="utf-8")) if generated_path.exists() else {}
        for field in ("manufacturer", "part_number_lcsc", "part_number_jlcpcb", "part_number_manufacturer", "jlcpcb_selection"):
            if actual.get(field) != part.get(field): errors.append(f"Regenerate stale {field}")
        build_report = ROOT / "kicad_agents/generated/component_additions" / (row["ledger_id"] + ".yaml")
        built = yaml.safe_load(build_report.read_text(encoding="utf-8")) if build_report.exists() else {}
        if built.get("project_output_guard") != "pass" or built.get("status") != "pass":
            errors.append("A passing component build report with project output guard is required")
        manifest_path = ROOT / "parts" / record["part_id"] / "data/kicad/manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        kinds = {x.get("kind") for x in manifest.get("assets", [])}
        if manifest.get("status") != "complete" or not {"symbol", "machine_solder"} <= kinds:
            errors.append("Complete KiCad manifest with symbol and machine-solder footprint is required")
    result["status"] = "fail" if errors else "pass"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "next", "scaffold-intake", "promote-intake", "intake-check", "intake-complete",
                                            "full-check", "full-complete", "check", "complete", "defer", "status",
                                            "claims", "release", "lock", "unlock", "plan", "stage-plan", "stage-capture"])
    parser.add_argument("--stage", choices=["intake", "full"], default="intake")
    parser.add_argument("--code")
    parser.add_argument("--record", type=Path)
    parser.add_argument("--observed", type=Path, help="JSON facts transcribed from the live browser page, with explicit OOMP decision")
    parser.add_argument("--reason")
    parser.add_argument("--claim", action="store_true", help="Atomically claim the handed-out item so other workers skip it")
    parser.add_argument("--worker", help="Worker identity used with --claim, lock and unlock")
    parser.add_argument("--categories", help="Semicolon-separated queue categories this worker may claim")
    parser.add_argument("--family", help="Populate family for lock/unlock (e.g. diode)")
    parser.add_argument("--wait-seconds", type=int, default=900, help="How long lock waits for a held lock")
    parser.add_argument("--workers", type=int, help="Worker count for plan")
    parser.add_argument("--stale", action="store_true", help="release: clear abandoned claims and locks")
    parser.add_argument("--hours", type=float, default=6.0, help="Age threshold in hours for release --stale")
    parser.add_argument("--force", action="store_true", help="unlock: release a family lock regardless of owner; stage-capture: overwrite an existing capture")
    parser.add_argument("--staged-only", action="store_true", help="next: only hand out codes with a fresh staged browser capture")
    parser.add_argument("--staged-hours", type=float, default=24.0, help="Freshness window in hours for staged browser captures")
    parser.add_argument("--from-capture", action="store_true", help="defer: compose the class-conflict reason from the staged browser capture")
    parser.add_argument("--count", type=int, default=10, help="stage-plan: how many codes to hand the reader")
    parser.add_argument("--file", type=Path, help="stage-capture: JSON capture file written by the browser reader")
    parser.add_argument("--stdin", action="store_true", help="stage-capture: read the JSON capture from stdin")
    args = parser.parse_args()
    if args.command == "prepare":
        print(json.dumps(prepare(), indent=2)); return
    queue = read_json(DATA / "queue.json")
    if args.command == "status":
        states = {stage: dict(Counter(progress_for(row["code"])[stage]["status"] for row in queue))
                  for stage in ("intake", "full")}
        claimed = {stage: len(claim_records(stage)) for stage in ("intake", "full")}
        print(json.dumps(dict(total=len(queue), stages=states, claimed=claimed), indent=2)); return
    if args.command == "plan":
        if not args.workers or args.workers < 1:
            parser.error("--workers N is required for plan")
        print(json.dumps(plan_workers(queue, args.stage, args.workers), indent=2)); return
    if args.command == "claims":
        print(json.dumps([dict(code=code, **payload) for code, payload in sorted(claim_records(args.stage).items())], indent=2)); return
    if args.command == "release":
        if args.stale:
            print(json.dumps(dict(removed=release_stale(args.hours)), indent=2)); return
        if not args.code:
            parser.error("--code or --stale is required for release")
        release_claim(args.code, args.stage)
        print(json.dumps(dict(released=args.code, stage=args.stage), indent=2)); return
    if args.command in ("lock", "unlock"):
        if not args.family or not args.worker:
            parser.error("--family and --worker are required for lock/unlock")
        if args.command == "lock":
            path = acquire_lock(f"family_{args.family}", owner=args.worker, wait_seconds=args.wait_seconds)
            print(json.dumps(dict(locked=args.family, worker=args.worker, lock=str(path)), indent=2)); return
        path = LOCKS / f"family_{args.family}.lock"
        if not args.force:
            try:
                owner = read_json(path).get("owner")
            except (OSError, ValueError):
                owner = None
            if owner != args.worker:
                raise SystemExit(f"Family lock {args.family} is owned by {owner or 'someone else'}; use --force only if that worker is gone")
        release_lock(path)
        print(json.dumps(dict(unlocked=args.family, worker=args.worker), indent=2)); return
    if args.command == "stage-plan":
        picked = [row for row in queue
                  if progress_for(row["code"])[args.stage]["status"] == "pending"
                  and not staged_capture_fresh(row["code"], args.staged_hours)][:max(1, args.count)]
        print(json.dumps([dict(code=r["code"], category=r["category"], tier=r["tier"],
                               manufacturer=r["manufacturer"], mpn=r["mpn"], package=r["package"],
                               url=r["jlcpcb_url"]) for r in picked], indent=2))
        return
    if args.command != "next" and not args.code:
        parser.error("--code is required for state changes and checks")
    stage = "full" if args.command in ("full-check", "full-complete", "check", "complete") else (
        "intake" if args.command in ("promote-intake", "intake-check", "intake-complete", "stage-capture") else args.stage)
    categories = ({x.strip() for x in args.categories.split(";") if x.strip()}
                  if args.categories else None)
    staged_hours = args.staged_hours if args.staged_only else None
    if args.command == "next" and args.claim:
        if not args.worker:
            parser.error("--worker is required with --claim")
        claimed = claim_records(stage)
        row = None
        for candidate in queue:
            if args.code and candidate["code"] != args.code:
                continue
            if candidate["code"] in claimed or (categories and candidate["category"] not in categories):
                continue
            if staged_hours is not None and not staged_capture_fresh(candidate["code"], staged_hours):
                continue
            state = progress_for(candidate["code"])
            if state[stage]["status"] != "pending" or (stage == "full" and state["intake"]["status"] != "complete"):
                continue
            if claim_code(candidate["code"], stage, args.worker):
                row = candidate
                break
            claimed[candidate["code"]] = {}
        if row is None:
            print(json.dumps(dict(task=None, stage=stage, worker=args.worker,
                                  note="No claimable pending item in scope"), indent=2))
            return
    else:
        row = select_task(queue, args.code, stage,
                          skip=() if args.code else set(claim_records(stage)),
                          categories=categories, staged_hours=staged_hours)
    if args.command == "next":
        guide = "JLC_PART_INTEGRATION_AGENT.md" if stage == "full" else "JLC_PART_INTAKE_AGENT.md"
        instructions = f"Read kicad_agents/{guide}. Follow its steps in order. Process ONLY this code; hints are not verified matches. Take time to verify evidence."
        payload = dict(task=row, stage=stage, instructions=instructions)
        if args.claim:
            payload["claimed_by"] = args.worker
            payload["staged_only"] = staged_hours is not None
            payload["instructions"] += " When done (complete or defer) the claim clears automatically; run next --claim again for the following item."
        print(json.dumps(payload, indent=2, ensure_ascii=True)); return
    if args.command == "stage-capture":
        if progress_for(row["code"])[stage]["status"] != "pending":
            raise SystemExit("Captures are staged for pending items only")
        if args.file:
            capture = read_json(args.file)
        elif args.stdin:
            capture = json.loads(sys.stdin.read())
        else:
            parser.error("--file or --stdin is required for stage-capture")
        if not isinstance(capture, dict):
            raise SystemExit("Capture must be a JSON object")
        if capture.get("code") != row["code"]:
            raise SystemExit("Capture code does not match the queue item")
        if capture.get("official_url") != row["jlcpcb_url"]:
            raise SystemExit("Capture official_url does not match the queued product URL")
        # An empty queued package means "not yet verified"; the live page adopts it.
        for key in ("manufacturer", "mpn", "package"):
            if capture.get(key) != row[key] and not (key == "package" and not row[key]):
                raise SystemExit(f"Live {key} differs from the queue; resolve identity before staging")
        if capture.get("tier_label") not in TIER_LABELS:
            raise SystemExit(f"tier_label must be the visible badge, one of: {', '.join(TIER_LABELS)}")
        if not str(capture.get("description", "")).strip():
            raise SystemExit("Description is missing")
        if not isinstance(capture.get("specifications"), dict):
            raise SystemExit("Specifications must be an object")
        if not isinstance(capture.get("visible_text"), str) or row["code"] not in capture["visible_text"]:
            raise SystemExit("Visible page text must include the C-number")
        datasheet = str(capture.get("datasheet_url") or "")
        if datasheet and (not datasheet.startswith("https://") or "?" in datasheet):
            raise SystemExit("Datasheet URL must be a query-free HTTPS URL")
        capture["captured_on"] = datetime.now(timezone.utc).date().isoformat()
        capture["capture_method"] = "zcode_inapp_browser_visible_page"
        target = staged_capture_path(row["code"])
        if target.exists() and not args.force:
            raise SystemExit("Capture already exists; recapture only with --force after review")
        write_json(target, capture)
        print(json.dumps(dict(staged=row["code"], tier_label=capture["tier_label"], path=str(target)), indent=2))
        return
    if args.command == "scaffold-intake":
        if not args.observed: parser.error("--observed is required")
        import yaml
        capture, page_text, record = build_intake_scaffold(row, read_json(args.observed))
        page_path, record_path = ROOT / capture, ROOT / "kicad_agents/component_records" / (row["ledger_id"] + ".yaml")
        if page_path.exists() or record_path.exists():
            raise ValueError("Intake page or record already exists; inspect before editing, never overwrite")
        page_path.parent.mkdir(parents=True, exist_ok=True)
        record_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(page_text, encoding="utf-8")
        record_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(json.dumps(dict(page=str(page_path), record=str(record_path),
                              next="Import browser-downloaded PDF, inspect both files, then promote-intake"), indent=2))
        return
    if args.command == "promote-intake":
        if not args.record: parser.error("--record is required")
        result = check_intake_record(row, args.record, population_required=False)
        print(json.dumps(result, indent=2))
        if result["status"] != "pass": raise SystemExit(1)
        import yaml
        record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
        # Serialise the registry read-modify-write across concurrent workers.
        lock_path = acquire_lock("reviewed_choices", owner=f"promote-{row['code']}", wait_seconds=300)
        try:
            registry_path = DATA / "reviewed_choices.json"
            choices = read_json(registry_path)
            choice = dict(code=row["code"], family=record["family"], part_id=record["part_id"],
                          manufacturer=record["research"]["manufacturer"],
                          mpn=record["research"]["manufacturer_part_number"],
                          selection=record["jlc_selection"])
            prior = next((x for x in choices if x["code"] == row["code"]), None)
            if prior and prior != choice:
                raise ValueError("Reviewed choice exists with different facts; edit the registry explicitly")
            if not prior:
                if any(x["part_id"] == choice["part_id"] for x in choices):
                    raise ValueError("Another reviewed choice already prefers this OOMP ID")
                choices.append(choice)
                choices.sort(key=lambda x: int(x["code"][1:]))
                write_json(registry_path, choices)
        finally:
            release_lock(lock_path)
        return
    if args.command in ("intake-check", "intake-complete", "full-check", "full-complete", "check", "complete"):
        if not args.record: parser.error("--record is required")
        if stage == "full" and progress_for(row["code"])["intake"]["status"] != "complete":
            parser.error("Complete first-pass intake before the full validation stage")
        result = (check_intake_record(row, args.record) if stage == "intake" else
                  check_record(row, args.record, generated=args.command in ("full-complete", "complete")))
        print(json.dumps(result, indent=2))
        if result["status"] != "pass": raise SystemExit(1)
        if args.command in ("intake-check", "full-check", "check"): return
        stage_state = dict(status="complete", record=str(args.record), part_id=result["part_id"])
    else:
        if args.from_capture:
            capture = load_staged_capture(row["code"], max_age_hours=args.staged_hours)
            if capture.get("tier_label") in HOUSE_TIER_LABELS:
                raise SystemExit("Staged capture shows a house class; run the intake flow (intake_from_capture) instead of defer --from-capture")
            reason = (f"Live JLCPCB product page on {capture['captured_on']} ({capture['official_url']}) shows house class "
                      f"{capture['tier_label']}, not Basic/Preferred/Promotional, conflicting with the queued {row['tier']} "
                      f"snapshot (last seen 2026-09-18). Identity otherwise verified: {row['manufacturer']} {row['mpn']}, "
                      f"{capture.get('description', '')}, {row['package'] or capture.get('package', '')}, "
                      f"stock {capture.get('stock_observed')}, "
                      f"MOQ {capture.get('purchase_moq_observed')}. An ordinary Extended listing is outside house-parts intake; "
                      "re-verify the class on a future snapshot or reclassify the catalogue before retrying.")
        elif not args.reason:
            parser.error("--reason is required; retain unresolved work explicitly")
        else:
            reason = args.reason
        stage_state = dict(status="deferred", reason=reason)
    state = progress_for(row["code"])
    state[stage] = dict(stage_state, updated_at=datetime.now(timezone.utc).isoformat())
    write_json(DATA / "progress" / (row["code"] + ".json"), state)
    release_claim(row["code"], stage)


if __name__ == "__main__":
    main()
