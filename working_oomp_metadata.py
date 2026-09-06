"""Shared, deterministic display names, distributor links, and navigation data."""

import re
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
        ["_pf", "pF"],
        ["_volt", "V"],
        ["_amp", "A"],
    ]
    for suffix, unit in unit_rows:
        if value_text.endswith(suffix):
            number_text = value_text[: -len(suffix)]
            return f"{_format_number(number_text)} {unit}"
    return _pretty_token(value_text)


def _connector_detail(value):
    if value.endswith("_mm_pitch"):
        return f"{_format_number(value[:-len('_mm_pitch')])} mm pitch"
    replacements = {
        "through_hole": "through-hole",
        "surface_mount": "surface-mount",
        "right_angle": "right-angle",
    }
    if value in replacements:
        return replacements[value]
    if value.endswith("_pin") or value.endswith("_pin_dual_row"):
        return value.replace("_", " ")
    return _pretty_token(value)


def readable_name(part):
    override = str(part.get("name_readable_override", "")).strip()
    if override:
        return override
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
        board = str(part.get("project_board_name", "")).strip()
        if board:
            return f"Project {owner}/{repository} {board} {version}".strip()
        return f"Project {owner}/{repository} {version}".strip()

    if component_type == "capacitor":
        details = []
        for taxonomy_value in taxonomy[3:]:
            if taxonomy_value.endswith("_farad") or taxonomy_value.endswith("_volt"):
                details.append(_format_value(taxonomy_value))
        if value in ["electrolytic", "tantalum"]:
            details.append(_pretty_token(value))
        if "_mm_diameter_" in package:
            diameter, height = package.split("_mm_diameter_", 1)
            height = height.replace("_mm_tall", "")
            details.append(f"{_format_number(diameter)} mm diameter x {_format_number(height)} mm tall")
        else:
            details.append(package.replace("_", " ").upper())
        return "Capacitor " + " ".join(details)
    if component_type == "resistor":
        return f"Resistor {_format_value(value)} {package.upper()}".strip()
    if component_type == "resistor_array":
        return f"Resistor array {_format_value(value)} {_pretty_token(package)}".strip()
    if component_type == "connector":
        connector_type = _pretty_token(package)
        if manufacturer_part_number != "":
            return f"Connector {connector_type} {manufacturer_part_number}".strip()
        details = []
        for taxonomy_value in taxonomy[3:7]:
            details.append(_connector_detail(taxonomy_value))
        return f"Connector {connector_type} {' '.join(details)}".strip()
    if component_type == "ic":
        if manufacturer_part_number != "":
            return f"IC {manufacturer_part_number} {package.replace('_', ' ').upper()}".strip()
        details = [_pretty_token(value_text) for value_text in taxonomy[3:6]]
        return f"IC {' '.join(details)} {package.upper()}".strip()
    if component_type == "led":
        if manufacturer_part_number != "":
            return f"LED {manufacturer_part_number} {package.replace('_', ' ').upper()}"
        details = [_pretty_token(value_text) for value_text in taxonomy[3:6]]
        return f"LED {' '.join(details)} {package.upper()}".strip()
    if component_type == "diode":
        diode_package = value.replace("_", "-").upper()
        identity = manufacturer_part_number or _pretty_token(package)
        return f"Diode {identity} {diode_package}".strip()
    if component_type == "crystal":
        details = []
        for taxonomy_value in taxonomy[3:]:
            if taxonomy_value.endswith(("_hz", "_mhz", "_khz", "_pf")):
                details.append(_format_value(taxonomy_value))
        details.append(package.upper())
        for taxonomy_value in taxonomy[3:]:
            if taxonomy_value.endswith("_pin"):
                details.append(taxonomy_value.replace("_", "-"))
        return "Crystal " + " ".join(details)
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
        for taxonomy_value in taxonomy[3:]:
            details.append(_pretty_token(taxonomy_value))
    if package != "":
        details.append(package.replace("_", " ").upper())
    return f"{title} {' '.join(details)}".strip()


def add_distributor_links(part):
    """Add an editable list of distributor identities and URLs.

    A part can carry several purchasable options per distributor: the singular
    ``part_number_lcsc`` stays the primary catalogue number, while
    ``part_numbers_lcsc`` holds extra options, each with an optional product
    name and URL.  Manufacturer identities work the same way: the singular
    ``manufacturer`` / ``part_number_manufacturer`` pair is primary and
    ``part_numbers_manufacturer`` lists further name/number pairs.
    """
    distributor_definitions = [
        ["lcsc", "LCSC", "part_number_lcsc", "part_numbers_lcsc", "https://www.lcsc.com/product-detail/{part_number}.html"],
        ["digikey", "DigiKey", "part_number_digikey", "part_numbers_digikey", "https://www.digikey.com/en/products/result?keywords={part_number}"],
        ["mouser", "Mouser", "part_number_mouser", "part_numbers_mouser", "https://www.mouser.com/c/?q={part_number}"],
        ["farnell", "Farnell", "part_number_farnell", "part_numbers_farnell", "https://uk.farnell.com/search?st={part_number}"],
    ]
    distributors = []
    seen = set()

    def add_distributor(key, title, part_number, url, product_name=""):
        part_number = str(part_number or "").strip()
        if part_number == "":
            return
        if part_number.isascii() and part_number.isdigit():
            part_number = "C" + part_number
        identity = (key, part_number.upper())
        product_name = str(product_name or "").strip()
        if identity in seen:
            # A repeated number that names the product enriches the first
            # entry instead of creating a look-alike second option.
            if product_name:
                for entry in distributors:
                    if (entry["key"], entry["part_number"].upper()) == identity and not entry.get("product_name"):
                        entry["product_name"] = product_name
            return
        seen.add(identity)
        entry = {
            "key": key,
            "title": title,
            "part_number": part_number,
            "url": url,
        }
        if product_name:
            entry["product_name"] = product_name
        distributors.append(entry)

    for distributor_key, distributor_title, field_name, options_field, url_template in distributor_definitions:
        part_number = str(part.get(field_name, "")).strip()
        if part_number != "":
            explicit_url = str(part.get(f"{field_name}_url", "")).strip()
            if explicit_url == "":
                explicit_url = url_template.format(part_number=part_number)
            add_distributor(distributor_key, distributor_title, part_number, explicit_url)
        for option in part.get(options_field) or []:
            if not isinstance(option, dict):
                continue
            option_number = str(option.get("part_number", "")).strip()
            if option_number == "":
                continue
            option_url = str(option.get("url", "")).strip()
            if option_url == "":
                option_url = url_template.format(part_number=option_number)
            add_distributor(distributor_key, distributor_title, option_number, option_url,
                            option.get("product_name", ""))
    part["distributors"] = distributors

    manufacturers = []
    seen_manufacturers = set()

    def add_manufacturer(name, part_number):
        name = str(name or "").strip()
        part_number = str(part_number or "").strip()
        if name == "" and part_number == "":
            return
        identity = (name.lower(), part_number.upper())
        if identity in seen_manufacturers:
            return
        seen_manufacturers.add(identity)
        manufacturers.append({"manufacturer": name, "part_number": part_number})

    for option in part.get("part_numbers_manufacturer") or []:
        if isinstance(option, dict):
            add_manufacturer(option.get("manufacturer", ""), option.get("part_number", ""))
    add_manufacturer(part.get("manufacturer", ""), part.get("part_number_manufacturer", ""))
    part["manufacturers"] = manufacturers
    return part


_LCSC_UNIT_SUFFIXES = [
    ("_pico_farad", "pF"),
    ("_nano_farad", "nF"),
    ("_micro_farad", "uF"),
    ("_milli_farad", "mF"),
    ("_farad", "F"),
    ("_micro_henry", "uH"),
    ("_milli_henry", "mH"),
    ("_henry", "H"),
    ("_mega_ohm", "MΩ"),
    ("_kilo_ohm", "kΩ"),
    ("_milliohm", "mΩ"),
    ("_ohm", "Ω"),
    ("_mhz", "MHz"),
    ("_khz", "kHz"),
    ("_hz", "Hz"),
    ("_volt", "V"),
    ("_amp", "A"),
    ("_watt", "W"),
]


def _trim_number(number):
    return f"{number:g}"


def _lcsc_value_text(value_token):
    """Compact LCSC-style value: "10000_ohm" reads "10kΩ", "47_micro_farad" "47uF"."""
    value_text = str(value_token or "").strip().lower()
    if value_text == "":
        return ""
    for suffix, unit in _LCSC_UNIT_SUFFIXES:
        if value_text.endswith(suffix):
            number_text = value_text[: -len(suffix)].replace("_", ".")
            try:
                number = float(number_text)
            except ValueError:
                return number_text + unit
            if unit == "Ω" and number >= 1000:
                for factor, prefix in ((1e9, "G"), (1e6, "M"), (1e3, "k")):
                    if number >= factor:
                        return f"{_trim_number(number / factor)}{prefix}{unit}"
            return f"{_trim_number(number)}{unit}"
    return _pretty_token(str(value_token))


def _lcsc_search_for_part(part):
    """Derive the string to type into LCSC search to find this part.

    Package plus value for passives (the same words a human would search),
    manufacturer part number for everything catalogued by number.
    """
    taxonomy = taxonomy_values(part)
    component_type = taxonomy[1] if len(taxonomy) > 1 else ""
    package = taxonomy[2] if len(taxonomy) > 2 else ""
    values = taxonomy[3:]
    manufacturer_part_number = str(part.get("part_number_manufacturer", "")).strip()

    def value_with(suffixes):
        for value_token in values:
            if value_token.endswith(suffixes):
                return _lcsc_value_text(value_token)
        return ""

    if component_type == "resistor":
        value = value_with(("_ohm",))
        if re.fullmatch(r"(0201|0402|0603|0805|1206|1210|2010|2512)", package):
            return f"{package} {value}".strip()
        return f"{value} through hole".strip()
    if component_type == "resistor_array":
        array_match = re.search(r"(0201|0402|0603|0805|1206)", package + " " + " ".join(values))
        array_size = array_match.group(1) if array_match else package
        return f"{array_size} {value_with(('_ohm',))} resistor array".strip()
    if component_type == "capacitor":
        if re.fullmatch(r"(0201|0402|0603|0805|1206|1210|2010|2512)", package):
            return f"{package} {value_with(('_farad',))}".strip()
        if values and values[0] in ("electrolytic", "tantalum"):
            return " ".join(part for part in [
                value_with(("_farad",)), value_with(("_volt",)), values[0]] if part)
        return value_with(("_farad",))
    if component_type in ("ferrite_bead", "inductor"):
        return f"{package} {value_with(('_ohm', '_henry'))}".strip()
    if component_type == "fuse":
        return f"{package} {' '.join(v.replace('_', ' ') for v in values)} fuse".strip()
    if component_type == "led":
        return f"{package.replace('_mm', 'mm')} led"
    if component_type == "crystal":
        return f"{package} {value_with(('_hz', '_mhz', '_khz'))}".strip()
    if component_type == "wire":
        return f"{_pretty_token(package)} wire"
    if component_type == "connector" and manufacturer_part_number == "":
        pitch_token = next((v for v in values if v.endswith("_mm_pitch")), "")
        pitch = pitch_token[: -len("_mm_pitch")].replace("_", ".") + "mm" if pitch_token else ""
        mount = "smd" if "surface_mount" in values else ("through hole" if "through_hole" in values else "")
        pins = next((v.replace("_pin_dual_row", " pin dual row").replace("_pin", " pin")
                     for v in values if v.endswith(("_pin", "_pin_dual_row"))), "")
        return " ".join(part for part in [pitch, "header", pins, mount] if part)
    if manufacturer_part_number != "":
        return manufacturer_part_number
    if component_type in ("", "project", "mounting_hole", "navigation"):
        return ""
    tokens = [v.replace("_", " ") for v in values if v not in ("surface_mount", "through_hole")]
    words = [package.replace("_", " ")] + tokens
    if component_type not in ("prototyping",) and package != component_type:
        words.append(component_type)
    return " ".join(word for word in words if word).strip()


def add_lcsc_search(part):
    """Declare each part's ``lcsc_search`` value; explicit settings win.

    Only purchasable electronic parts get a derived value — navigation,
    project and mechanical records stay clean.
    """
    search = str(part.get("lcsc_search", "") or "").strip()
    if search == "" and str(part.get("taxonomy_1", "")) == "electronic":
        search = _lcsc_search_for_part(part)
    if search != "":
        part["lcsc_search"] = search
    return part


def add_readable_metadata(parts):
    for part in parts:
        part["name_readable"] = readable_name(part)
        part["name_short"] = part["name_readable"]
        part["name_proper"] = part["name_readable"]
        add_distributor_links(part)
        add_lcsc_search(part)


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
