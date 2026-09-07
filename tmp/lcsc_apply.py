"""Convert tmp/lcsc_results.jsonl into working_oomp_populate_lcsc_research_data.py.

Selection: prefer JLCPCB-basic tagged rows, then stock, filtered by kind-specific
value/size checks against the LCSC description.
"""
import json, re, sys
from collections import Counter

ROOT = r"C:/gh/oomp_electronic_version_5"

def resistor_value(part_id):
    match = re.search(r"^electronic_resistor(?:_array)?_[a-z0-9_]+?_(\d+(?:_\d+)*)_ohm", part_id)
    return int(match.group(1).replace("_", "")) if match else None

def ohm_tokens(value):
    """Acceptable LCSC description spellings for a resistance."""
    if value == 0:
        return ["0Ω", "0 ohm", "0r", "jumper"]
    tokens = []
    for divisor, unit in ((1_000_000, "MΩ"), (1_000, "KΩ"), (1, "Ω")):
        if value >= divisor:
            number = value / divisor
            text = f"{number:g}"
            if not text.endswith(".0"):
                tokens.append(text + unit)
            elif value % divisor == 0:
                tokens.append(f"{int(number)}{unit}")
    if value >= 1000 and value % 1000:
        # 4.7K style
        tokens.append(f"{value / 1000:g}KΩ")
    return tokens

def cap_tokens(part_id):
    match = re.search(r"^electronic_capacitor_[a-z0-9_]+?_(\d+(?:_\d+)*)_(pico|nano|micro)_farad$", part_id)
    if not match:
        return []
    number = float(match.group(1).replace("_", "."))
    unit = {"pico": "pF", "nano": "nF", "micro": "uF"}[match.group(2)]
    text = f"{number:g}{unit}"
    return [text, text.replace("uF", "µF")]

def pick_row(rows, kind, part_id, hints):
    scored = []
    for row in rows:
        description = row.get("description", "")
        description_lower = description.lower()
        mpn = (row.get("mpn") or "").lower()
        tags = row.get("tags", [])
        ok = True
        if kind == "chip_resistor":
            size = part_id.split("_")[2]
            tokens = ohm_tokens(resistor_value(part_id))
            ok = size in description_lower.replace(" ", "") and any(
                token.lower() in description_lower or token.lower() in mpn for token in tokens
            )
        elif kind == "tht_resistor":
            tokens = ohm_tokens(resistor_value(part_id))
            ok = any(token.lower() in description_lower or token.lower() in mpn for token in tokens)
        elif kind == "resistor_array":
            tokens = ohm_tokens(resistor_value(part_id))
            ok = any(token.lower() in description_lower for token in tokens) and "0402" in description_lower
        elif kind == "capacitor":
            tokens = cap_tokens(part_id)
            size = part_id.split("_")[2]
            ok = any(token.lower() in description_lower for token in tokens)
        elif kind == "led":
            size = part_id.replace("electronic_led_", "").split("_")[0]
            colour = hints[0] if hints and hints[0] in ("red", "green", "blue", "yellow", "white") else ""
            lens = hints[1] if len(hints) > 1 else ""
            # Word boundaries keep "emerald" from matching "red".
            ok = re.search(rf"{re.escape(size)}(?:mm)?", description_lower) is not None
            if ok and colour and re.search(rf"{colour}", description_lower) is None:
                ok = False
            if ok and lens == "clear" and re.search(r"(transparent|clear|water)", description_lower) is None:
                ok = False
            if ok and lens == "tint" and re.search(r"(transparent|water clear)", description_lower) is not None:
                ok = False
        elif kind == "mpn":
            # Series queries carry an MPN-prefix hint ("B4B-") in hints.
            prefix = hints[0] if hints else ""
            ok = True
            if prefix and prefix.lower() not in (row.get("mpn", "").lower() + " " + description_lower):
                ok = False
        elif kind == "header_ra":
            count_token, variant = hints[0], hints[1]
            text = row.get("mpn", "").lower() + " " + description_lower
            count_ok = any(token in text for token in (f"{count_token}p", f"1x{count_token}", f"{count_token}pin", f"{count_token} pin"))
            angle_ok = "right angle" in text or "bent" in text or "angled" in text or "ra" in text.split()
            ok = count_ok and angle_ok
            if ok and variant == "long":
                ok = "long" in text
        elif kind == "dual_row":
            text = row.get("mpn", "").lower() + " " + description_lower
            ok = "2x3" in text and "header" in text and "right angle" not in text
        elif kind == "info":
            ok = False
        if ok:
            score = row.get("stock", 0) + (10**12 if "basic" in tags else 0)
            scored.append((score, row))
    if not scored:
        return None
    scored.sort(key=lambda item: -item[0])
    return scored[0][1]

def main():
    queue = {entry["part_id"]: entry for entry in json.load(open(f"{ROOT}/tmp/lcsc_queue.json", encoding="utf-8"))}
    results = {}
    for line in open(f"{ROOT}/tmp/lcsc_results.jsonl", encoding="utf-8"):
        if not line.strip():
            continue
        record = json.loads(line)
        results[record["key"]] = record
    applied = {}
    no_pick = []
    for part_id, record in results.items():
        entry = queue.get(part_id)
        if not entry or not record.get("rows"):
            if entry and not record.get("rows"):
                no_pick.append((part_id, record.get("status", "empty")))
            continue
        row = pick_row(record["rows"], entry["kind"], part_id, entry.get("hints", []))
        if not row:
            no_pick.append((part_id, "filtered-out"))
            continue
        applied[part_id] = {
            "manufacturer": row.get("manufacturer", ""),
            "part_number_manufacturer": row.get("mpn", ""),
            "part_number_lcsc": row.get("code", ""),
            "product_url": f"https://www.lcsc.com/product-detail/{row.get('code', '')}.html",
            "lcsc_stock_at_capture": row.get("stock", 0),
            "lcsc_description": row.get("description", ""),
            "lcsc_query": record.get("query", ""),
        }
    # summarise manufacturer coverage per family
    families = Counter("_".join(p.split("_")[:3]) for p in applied)
    print("applied:", len(applied))
    for family, count in families.most_common():
        print(f"  {family}: {count}")
    print("no pick:", len(no_pick))
    for part_id, reason in no_pick[:25]:
        print("   ", part_id, reason)
    json.dump(applied, open(f"{ROOT}/tmp/lcsc_applied.json", "w", encoding="utf-8"), indent=1)

if __name__ == "__main__":
    main()
