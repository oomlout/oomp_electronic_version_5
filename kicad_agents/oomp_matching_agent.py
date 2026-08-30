"""Explainable OOMP component matcher intended for use by an AI agent or pipeline."""

import argparse
import json
import math
import re
from difflib import SequenceMatcher
from pathlib import Path

import yaml


PACKAGE_SIZES = ["0201", "0402", "0603", "0805", "1206", "1010", "5050"]
LED_COLORS = ["warm_white", "white", "yellow", "green", "blue", "pink", "red", "rgb"]


def normalize_text(value):
    value = str(value or "").strip().lower()
    value = value.replace("µ", "u").replace("μ", "u").replace("ω", "ohm").replace("Ω", "ohm")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def _engineering_number(value, suffixes):
    normalized = str(value or "").strip().lower().replace("µ", "u").replace("μ", "u")
    normalized = normalized.replace("ohms", "").replace("ohm", "").replace("Ω", "")
    normalized = normalized.replace("farads", "").replace("farad", "").replace("f", "")
    normalized = normalized.replace(" ", "")

    middle_match = re.fullmatch(r"(\d+)([a-z])(\d+)", normalized)
    if middle_match and middle_match.group(2) in suffixes:
        whole = float(middle_match.group(1))
        decimal = float("0." + middle_match.group(3))
        return (whole + decimal) * suffixes[middle_match.group(2)]

    normal_match = re.fullmatch(r"(\d+(?:\.\d+)?)([a-z]?)", normalized)
    if normal_match and normal_match.group(2) in suffixes:
        return float(normal_match.group(1)) * suffixes[normal_match.group(2)]
    return None


def parse_resistance_ohms(value):
    parsed = _engineering_number(value, {"": 1, "r": 1, "k": 1000, "m": 1000000})
    if parsed is None:
        return None
    return int(round(parsed))


def parse_capacitance_farads(value):
    return _engineering_number(
        value,
        {"": 1, "p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3},
    )


def capacitance_taxonomy(value):
    farads = parse_capacitance_farads(value)
    if farads is None:
        return ""
    units = [
        (1e-12, "pico_farad"),
        (1e-9, "nano_farad"),
        (1e-6, "micro_farad"),
        (1e-3, "milli_farad"),
        (1, "farad"),
    ]
    selected_multiplier, selected_name = units[0]
    for multiplier, unit_name in units:
        scaled = farads / multiplier
        if scaled >= 1 and abs(scaled - round(scaled, 6)) < 1e-6:
            selected_multiplier = multiplier
            selected_name = unit_name
    scaled = farads / selected_multiplier
    if abs(scaled - round(scaled)) < 1e-7:
        number = str(int(round(scaled)))
    else:
        number = ("%.6f" % scaled).rstrip("0").rstrip(".").replace(".", "_")
    return f"{number}_{selected_name}"


def _first_schematic_unit(component):
    schematic = component.get("schematic") or {}
    units = schematic.get("units") or []
    return units[0] if units else {}


def component_fields(component):
    unit = _first_schematic_unit(component)
    properties = unit.get("properties") or {}
    pcb = component.get("pcb") or {}
    return {
        "reference": component.get("reference", ""),
        "value": properties.get("Value") or pcb.get("value") or "",
        "footprint": properties.get("Footprint") or pcb.get("library_id") or "",
        "library_id": unit.get("library_id", ""),
        "mpn": properties.get("MPN") or properties.get("Manufacturer Part Number") or "",
    }


def infer_kind(fields):
    reference = fields["reference"].upper()
    evidence = " ".join(
        normalize_text(fields[field_name])
        for field_name in ["value", "footprint", "library_id"]
    )
    if reference.startswith("LED") or "led" in evidence or "ws2812" in evidence:
        return "led"
    if reference.startswith("R") and not reference.startswith("REF"):
        return "resistor"
    if reference.startswith("C") and not reference.startswith("CON"):
        return "capacitor"
    return ""


def infer_package_size(fields):
    evidence = " ".join([fields["footprint"], fields["library_id"], fields["value"]]).lower()
    for package_size in PACKAGE_SIZES:
        if re.search(rf"(?<!\d){re.escape(package_size)}(?!\d)", evidence):
            return package_size
    if any(token in evidence for token in ["din0207", "quarter_watt", "axial_6", "axial-din0207"]):
        return "quarter_watt_through_hole"
    return ""


def infer_led_color(fields):
    evidence = normalize_text(" ".join([fields["value"], fields["library_id"]]))
    for color in LED_COLORS:
        if color in evidence:
            return color
    return ""


def proposed_oomp_id(component):
    fields = component_fields(component)
    kind = infer_kind(fields)
    package_size = infer_package_size(fields)

    if kind == "resistor":
        resistance = parse_resistance_ohms(fields["value"])
        if package_size and resistance is not None:
            return f"electronic_resistor_{package_size}_{resistance}_ohm"

    if kind == "capacitor":
        capacitance = capacitance_taxonomy(fields["value"])
        if package_size and capacitance:
            return f"electronic_capacitor_{package_size}_{capacitance}"

    if kind == "led" and package_size:
        value_text = normalize_text(fields["value"])
        library_text = normalize_text(fields["library_id"])
        color = infer_led_color(fields)
        if "ws2812" in value_text or "ws2812" in library_text:
            if package_size == "1010":
                return "electronic_led_1010_rgb_ws2812b_xinglight_1010rgbc"
            if package_size == "5050":
                return "electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w"
        if color:
            return f"electronic_led_{package_size}_{color}"
        return f"electronic_led_{package_size}"

    return ""


class OompPartIndex:
    def __init__(self, parts_directory):
        self.parts_directory = Path(parts_directory).resolve()
        self.parts = []
        self.by_id = {}
        self._load()

    def _load(self):
        if not self.parts_directory.is_dir():
            raise FileNotFoundError(f"OOMP parts directory does not exist: {self.parts_directory}")
        for part_directory in sorted(self.parts_directory.iterdir()):
            working_yaml = part_directory / "working.yaml"
            if not part_directory.is_dir() or not working_yaml.is_file():
                continue
            part = {
                "oomp_id": part_directory.name,
                "directory": str(part_directory),
                "working_yaml": str(working_yaml),
                "tokens": set(part_directory.name.lower().split("_")),
            }
            self.parts.append(part)
            self.by_id[part["oomp_id"]] = part

    def candidate_parts(self, kind):
        if kind:
            prefix = f"electronic_{kind}_"
            return [part for part in self.parts if part["oomp_id"].startswith(prefix)]
        return []


def _is_physical_component(component):
    reference = component.get("reference", "")
    reference_upper = reference.upper()
    fields = component_fields(component)
    footprint = normalize_text(fields["footprint"])

    if reference_upper.startswith("SJ"):
        return False
    if reference_upper.startswith("UNK_HOLE"):
        return False
    if footprint.startswith("dummyfp"):
        return False
    if reference.startswith("#"):
        return False
    if component.get("pcb"):
        return True
    for unit in (component.get("schematic") or {}).get("units", []):
        if unit.get("on_board") and (unit.get("properties") or {}).get("Footprint"):
            return True
    return False


def _rank_candidates(index, component, proposed_id, kind, maximum=5):
    fields = component_fields(component)
    package_size = infer_package_size(fields)
    query_tokens = set(
        normalize_text(
            " ".join(
                [kind, infer_package_size(fields), fields["value"], fields["footprint"], fields["library_id"]]
            )
        ).split("_")
    )
    query_numeric_value = None
    if kind == "resistor":
        query_numeric_value = parse_resistance_ohms(fields["value"])
    elif kind == "capacitor":
        query_numeric_value = parse_capacitance_farads(fields["value"])

    def candidate_numeric_value(part_id):
        if kind == "resistor":
            match = re.search(r"_([0-9]+)_ohm$", part_id)
            return float(match.group(1)) if match else None
        if kind == "capacitor":
            match = re.search(r"_([0-9]+(?:_[0-9]+)?)_(pico|nano|micro|milli)_farad(?:_|$)", part_id)
            if not match:
                return None
            number = float(match.group(1).replace("_", "."))
            multipliers = {"pico": 1e-12, "nano": 1e-9, "micro": 1e-6, "milli": 1e-3}
            return number * multipliers[match.group(2)]
        return None

    candidates = []
    for part in index.candidate_parts(kind):
        part_tokens = part["tokens"]
        union = query_tokens | part_tokens
        token_score = len(query_tokens & part_tokens) / len(union) if union else 0
        text_score = SequenceMatcher(None, proposed_id or normalize_text(fields["value"]), part["oomp_id"]).ratio()
        candidate_value = candidate_numeric_value(part["oomp_id"])
        same_package = bool(package_size and f"_{package_size}_" in part["oomp_id"])
        reasons = ["same component family"]
        if same_package:
            reasons.append("same package size")
        if query_numeric_value is not None and candidate_value is not None:
            if query_numeric_value == candidate_value:
                numeric_score = 1.0
                reasons.append("same normalized value")
            elif query_numeric_value > 0 and candidate_value > 0:
                numeric_score = max(0.0, 1.0 - abs(math.log10(candidate_value / query_numeric_value)))
                reasons.append("nearby normalized value")
            else:
                numeric_score = 0.0
            score = round(numeric_score * 0.7 + float(same_package) * 0.25 + text_score * 0.05, 4)
        else:
            score = round(token_score * 0.65 + text_score * 0.35, 4)
        candidates.append({"oomp_id": part["oomp_id"], "score": score, "reasons": reasons})
    candidates.sort(key=lambda candidate: (-candidate["score"], candidate["oomp_id"]))
    return candidates[:maximum]


def match_component(index, component, overrides=None):
    overrides = overrides or {}
    reference = component.get("reference", "")
    fields = component_fields(component)
    kind = infer_kind(fields)
    package_size = infer_package_size(fields)
    proposed_id = proposed_oomp_id(component)

    result = {
        "status": "unmatched",
        "accepted": False,
        "oomp_id": None,
        "confidence": 0.0,
        "proposed_oomp_id": proposed_id or None,
        "inferred": {
            "kind": kind or None,
            "package_size": package_size or None,
            "value": fields["value"] or None,
            "mpn": fields["mpn"] or None,
        },
        "reasons": [],
        "candidates": [],
    }

    if not _is_physical_component(component):
        result["status"] = "not_applicable"
        reference_upper = reference.upper()
        footprint = normalize_text(fields["footprint"])
        if reference_upper.startswith("SJ"):
            result["reasons"].append("PCB solder jumpers are board features, not purchased OOMP parts.")
        elif reference_upper.startswith("UNK_HOLE") or footprint.startswith("dummyfp"):
            result["reasons"].append("Mechanical or dummy mounting holes do not require OOMP parts.")
        else:
            result["reasons"].append("The symbol has no physical PCB/OOMP part requirement.")
        return result

    override_id = overrides.get(reference)
    if override_id:
        if override_id in index.by_id:
            result.update(
                {
                    "status": "matched",
                    "accepted": True,
                    "oomp_id": override_id,
                    "confidence": 1.0,
                    "reasons": ["Accepted from the AI/human match override file."],
                }
            )
        else:
            result["reasons"].append(f"Override refers to missing OOMP part: {override_id}")
        return result

    if proposed_id and proposed_id in index.by_id:
        result.update(
            {
                "status": "matched",
                "accepted": True,
                "oomp_id": proposed_id,
                "confidence": 1.0,
                "reasons": [
                    "Exact OOMP ID constructed from component type, package size, and normalized value."
                ],
            }
        )
        return result

    result["candidates"] = _rank_candidates(index, component, proposed_id, kind)
    if not kind:
        result["reasons"].append("No supported OOMP component family could be inferred.")
    elif not package_size:
        result["reasons"].append("Component family was inferred, but package size was not.")
    elif proposed_id:
        result["reasons"].append("The exact normalized component is not present in the OOMP parts directory.")
    else:
        result["reasons"].append("The component value could not be normalized into an OOMP ID.")
    return result


def load_overrides(path):
    if path is None or not Path(path).is_file():
        return {}
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if "matches" in data:
        data = data["matches"] or {}
    return {str(reference): str(oomp_id) for reference, oomp_id in data.items()}


def main():
    parser = argparse.ArgumentParser(description="Match extracted KiCad components to OOMP parts.")
    parser.add_argument("component_file", help="JSON file containing one component or a components list")
    parser.add_argument("--parts-dir", default="parts", help="OOMP parts directory")
    parser.add_argument("--overrides", help="Optional YAML reference-to-OOMP override file")
    parser.add_argument("--output", help="Optional JSON output file; stdout is used when omitted")
    arguments = parser.parse_args()

    source_data = json.loads(Path(arguments.component_file).read_text(encoding="utf-8"))
    components = source_data.get("components", source_data) if isinstance(source_data, dict) else source_data
    one_component = isinstance(components, dict)
    if one_component:
        components = [components]

    index = OompPartIndex(arguments.parts_dir)
    overrides = load_overrides(arguments.overrides)
    results = [
        {
            "reference": component.get("reference", ""),
            "match": match_component(index, component, overrides=overrides),
        }
        for component in components
    ]
    output_data = results[0] if one_component else {"matches": results}
    rendered = json.dumps(output_data, indent=2, ensure_ascii=False) + "\n"
    if arguments.output:
        output_path = Path(arguments.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
