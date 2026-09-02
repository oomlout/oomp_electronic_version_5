"""Shared, deterministic display names, distributor links, and navigation data."""

from pathlib import PurePosixPath


REPOSITORY_PARTS_URL = "https://github.com/oomlout/oomp_electronic_version_5/tree/main/parts"
REPOSITORY_NAVIGATION_URL = "https://github.com/oomlout/oomp_electronic_version_5/tree/main/navigation"


def taxonomy_values(part):
    values = []
    for taxonomy_number in range(1, 16):
        value = str(part.get(f"taxonomy_{taxonomy_number}", "")).strip()
        if value != "":
            values.append(value)
    return values


def _pretty_token(value):
    replacements = {
        "ic": "IC",
        "led": "LED",
        "pcb": "PCB",
        "rgb": "RGB",
        "tft": "TFT",
        "usb_a": "USB-A",
        "usb_b": "USB-B",
        "usb_c": "USB-C",
        "jst": "JST",
        "smd": "SMD",
        "smt": "SMT",
        "spi": "SPI",
        "i2c": "I2C",
    }
    value_text = str(value).strip().lower()
    if value_text in replacements:
        return replacements[value_text]
    words = value_text.replace("_", " ").split()
    pretty_words = []
    for word in words:
        if word in replacements:
            pretty_words.append(replacements[word])
        elif any(character.isdigit() for character in word):
            pretty_words.append(word.upper())
        else:
            pretty_words.append(word.capitalize())
    return " ".join(pretty_words)


def _format_number(value_text):
    try:
        number = float(value_text.replace("_", "."))
    except ValueError:
        return value_text.replace("_", ".")
    return f"{number:g}"


def _format_value(value_token):
    value_text = str(value_token).lower()
    unit_rows = [
        ["_pico_farad", "pF"],
        ["_nano_farad", "nF"],
        ["_micro_farad", "uF"],
        ["_milli_farad", "mF"],
        ["_farad", "F"],
        ["_milliohm", "mOhm"],
        ["_kilo_ohm", "kOhm"],
        ["_mega_ohm", "MOhm"],
        ["_ohm", "Ohm"],
        ["_mhz", "MHz"],
        ["_khz", "kHz"],
        ["_hz", "Hz"],
    ]
    for suffix, unit in unit_rows:
        if value_text.endswith(suffix):
            number_text = value_text[: -len(suffix)]
            return f"{_format_number(number_text)} {unit}"
    return _pretty_token(value_text)


def readable_name(part):
    taxonomy = taxonomy_values(part)
    if taxonomy == []:
        return "OOMP part"
    if taxonomy[0] == "navigation":
        if len(taxonomy) == 1:
            return "OOMP navigation"
        return f"OOMP navigation: {' / '.join(_pretty_token(value) for value in taxonomy[1:])}"

    family = taxonomy[0]
    component_type = taxonomy[1] if len(taxonomy) > 1 else family
    package = taxonomy[2] if len(taxonomy) > 2 else ""
    value = taxonomy[3] if len(taxonomy) > 3 else ""
    manufacturer_part_number = str(part.get("part_number_manufacturer", "")).strip()

    if family == "oomp" and component_type == "project":
        owner = str(part.get("project_github_user", "")).strip()
        repository = str(part.get("project_github_repository", "")).strip()
        version = str(part.get("project_version", "current")).strip()
        return f"Project {owner}/{repository} {version}".strip()

    if component_type == "capacitor":
        return f"Capacitor {_format_value(value)} {package.upper()}".strip()
    if component_type == "resistor":
        return f"Resistor {_format_value(value)} {package.upper()}".strip()
    if component_type == "resistor_array":
        return f"Resistor array {_format_value(value)} {package.upper()}".strip()
    if component_type == "connector":
        connector_type = _pretty_token(package)
        if manufacturer_part_number != "":
            return f"Connector {connector_type} {manufacturer_part_number}".strip()
        details = []
        for taxonomy_value in taxonomy[3:7]:
            details.append(_pretty_token(taxonomy_value))
        return f"Connector {connector_type} {' '.join(details)}".strip()
    if component_type == "ic":
        if manufacturer_part_number != "":
            return f"IC {manufacturer_part_number} {package.upper()}".strip()
        details = [_pretty_token(value_text) for value_text in taxonomy[3:6]]
        return f"IC {' '.join(details)} {package.upper()}".strip()
    if component_type == "led":
        details = [_pretty_token(value_text) for value_text in taxonomy[3:6]]
        return f"LED {' '.join(details)} {package.upper()}".strip()
    if component_type == "mounting_hole":
        size_text = package.replace("_mm_x_", " mm x ")
        size_text = size_text.replace("_mm", " mm")
        size_text = size_text.replace("_", ".")
        style_text = _pretty_token(value)
        plating_text = _pretty_token(taxonomy[4]) if len(taxonomy) > 4 else ""
        return f"Mounting Hole {size_text} {style_text} {plating_text}".strip()

    title = _pretty_token(component_type)
    details = []
    if manufacturer_part_number != "":
        details.append(manufacturer_part_number)
    else:
        for taxonomy_value in taxonomy[3:6]:
            details.append(_pretty_token(taxonomy_value))
    if package != "":
        details.append(package.upper())
    return f"{title} {' '.join(details)}".strip()


def add_distributor_links(part):
    """Add an editable list of distributor identities and URLs."""
    distributor_definitions = [
        ["lcsc", "LCSC", "part_number_lcsc", "https://www.lcsc.com/product-detail/{part_number}.html"],
        ["digikey", "DigiKey", "part_number_digikey", "https://www.digikey.com/en/products/result?keywords={part_number}"],
        ["mouser", "Mouser", "part_number_mouser", "https://www.mouser.com/c/?q={part_number}"],
        ["farnell", "Farnell", "part_number_farnell", "https://uk.farnell.com/search?st={part_number}"],
    ]
    distributors = []
    for distributor_key, distributor_title, field_name, url_template in distributor_definitions:
        part_number = str(part.get(field_name, "")).strip()
        if part_number == "":
            continue
        explicit_url = str(part.get(f"{field_name}_url", "")).strip()
        if explicit_url == "":
            explicit_url = url_template.format(part_number=part_number)
        distributors.append(
            {
                "key": distributor_key,
                "title": distributor_title,
                "part_number": part_number,
                "url": explicit_url,
            }
        )
    part["distributors"] = distributors
    return part


def add_readable_metadata(parts):
    for part in parts:
        part["name_readable"] = readable_name(part)
        part["name_short"] = part["name_readable"]
        part["name_proper"] = part["name_readable"]
        add_distributor_links(part)


def _navigation_file_path(category_path):
    if category_path == []:
        return "navigation/README.md"
    return str(PurePosixPath("navigation", *category_path, "README.md"))


def add_navigation_parts(parts):
    """Append one OOMP part for each populated taxonomy category."""
    source_parts = []
    for part in parts:
        if str(part.get("taxonomy_1", "")) != "navigation":
            source_parts.append(part)

    category_paths = [[]]
    part_rows = []
    for part in source_parts:
        taxonomy = taxonomy_values(part)
        if taxonomy == []:
            continue
        part_id = "_".join(taxonomy)
        part_rows.append(
            {
                "id": part_id,
                "name": part.get("name_readable", readable_name(part)),
                "taxonomy": taxonomy,
                "url": f"{REPOSITORY_PARTS_URL}/{part_id}",
            }
        )
        for prefix_length in range(1, len(taxonomy)):
            category_path = taxonomy[:prefix_length]
            if category_path not in category_paths:
                category_paths.append(category_path)

    category_paths.sort(key=lambda path: (len(path), path))
    navigation_parts = []
    for category_path in category_paths:
        option = {"taxonomy_1": "navigation"}
        for category_index in range(len(category_path)):
            option[f"taxonomy_{category_index + 2}"] = category_path[category_index]

        child_categories = []
        for possible_child in category_paths:
            if len(possible_child) != len(category_path) + 1:
                continue
            if possible_child[: len(category_path)] != category_path:
                continue
            child_categories.append(
                {
                    "name": _pretty_token(possible_child[-1]),
                    "path": possible_child[-1] + "/README.md",
                    "url": f"{REPOSITORY_NAVIGATION_URL}/{'/'.join(possible_child)}",
                }
            )

        direct_parts = []
        descendant_count = 0
        for part_row in part_rows:
            taxonomy = part_row["taxonomy"]
            if taxonomy[: len(category_path)] == category_path:
                descendant_count += 1
            if taxonomy[:-1] == category_path:
                direct_parts.append(
                    {
                        "name": part_row["name"],
                        "id": part_row["id"],
                        "url": part_row["url"],
                    }
                )

        child_categories.sort(key=lambda row: row["name"])
        direct_parts.sort(key=lambda row: row["name"])
        if category_path == []:
            title = "OOMP navigation"
            parent_path = ""
            parent_url = ""
        else:
            title = " / ".join(_pretty_token(value) for value in category_path)
            parent_path = "../README.md"
            parent_url = REPOSITORY_NAVIGATION_URL
            if len(category_path) > 1:
                parent_url += "/" + "/".join(category_path[:-1])

        option["navigation"] = {
            "title": title,
            "category_path": list(category_path),
            "parent_path": parent_path,
            "parent_url": parent_url,
            "child_categories": child_categories,
            "parts": direct_parts,
            "descendant_part_count": descendant_count,
            "canonical_file": _navigation_file_path(category_path),
            "canonical_output_from_part": "../../" + _navigation_file_path(category_path),
            "canonical_url": REPOSITORY_NAVIGATION_URL + ("/" + "/".join(category_path) if category_path else ""),
        }
        option["name_readable"] = title
        option["name_short"] = title
        navigation_parts.append(option)

    parts.extend(navigation_parts)
    return navigation_parts


def navigation_link_for_part(part):
    taxonomy = taxonomy_values(part)
    if taxonomy == [] or taxonomy[0] == "navigation":
        return ""
    category_path = taxonomy[:-1]
    if category_path == []:
        return "../../navigation/README.md"
    return "../../" + _navigation_file_path(category_path)
