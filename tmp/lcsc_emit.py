"""Emit working_oomp_populate_lcsc_research_data.py from applied LCSC picks."""
import json, re
from collections import Counter

ROOT = r"C:/gh/oomp_electronic_version_5"
import sys
sys.path.insert(0, ROOT + "/tmp")
from lcsc_apply import pick_row
import json as _json

def load_queue():
    return {e["part_id"]: e for e in _json.load(open(f"{ROOT}/tmp/lcsc_queue.json", encoding="utf-8"))}

def build_applied():
    queue = load_queue()
    results = {}
    for line in open(f"{ROOT}/tmp/lcsc_results.jsonl", encoding="utf-8"):
        if not line.strip():
            continue
        record = _json.loads(line)
        results[record["key"]] = record
    applied = {}
    missing = []
    for part_id, record in results.items():
        entry = queue.get(part_id)
        if not entry or entry["kind"] == "info":
            continue
        rows = record.get("rows") or []
        if not rows:
            missing.append((part_id, record.get("status", "empty")))
            continue
        row = pick_row(rows, entry["kind"], part_id, entry.get("hints", []))
        if not row or not row.get("code"):
            missing.append((part_id, "filtered-out"))
            continue
        applied[part_id] = {
            "manufacturer": row.get("manufacturer", ""),
            "part_number_manufacturer": row.get("mpn", ""),
            "part_number_lcsc": row.get("code", ""),
            "lcsc_description": row.get("description", ""),
            "lcsc_stock": row.get("stock", 0),
            "lcsc_query": record.get("query", ""),
        }
    return applied, missing

def emit():
    applied, missing = build_applied()
    lines = [
        '"""LCSC stock research applied to the catalogue (browser captures parsed',
        'with kicad_agents/lcsc_capture_parser.py conventions).',
        '',
        'One literal row per part: highest-stock in-stock listing that matches the',
        "part's kind-specific description filter. Regenerate with tmp/lcsc_emit.py.",
        '"""',
        '',
        'LCSC_RESEARCH = {',
    ]
    for part_id in sorted(applied):
        data = applied[part_id]
        lines.append(f'    "{part_id}": {{')
        for key in ("manufacturer", "part_number_manufacturer", "part_number_lcsc", "lcsc_description", "lcsc_stock", "lcsc_query"):
            value = data[key]
            if isinstance(value, str):
                value = value.replace("\\", " ").replace('"', "'")
                lines.append(f'        "{key}": "{value}",')
            else:
                lines.append(f'        "{key}": {value},')
        lines.append("    },")
    lines.append("}")
    lines.append("")
    open(f"{ROOT}/working_oomp_populate_lcsc_research_data.py", "w", encoding="utf-8").write("\n".join(lines))
    families = Counter("_".join(p.split("_")[:3]) for p in applied)
    print("applied:", len(applied))
    for family, count in families.most_common(12):
        print(f"  {family}: {count}")
    print("missing/filtered:", len(missing))
    for part_id, reason in missing[:20]:
        print("   ", part_id, reason)

if __name__ == "__main__":
    emit()
