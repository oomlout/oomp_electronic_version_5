"""Explainable OOMP component matcher intended for use by an AI agent or pipeline."""

import argparse
import json
import math
import re
from difflib import SequenceMatcher
from pathlib import Path

import yaml


PACKAGE_SIZES = ["0201", "0402", "0603", "0805", "1206", "1205", "1210", "2512", "3216", "1010", "5050"]
LED_COLORS = ["warm_white", "white", "yellow", "green", "blue", "pink", "red", "rgb"]

# Value/MPN fragments that identify an exact OOMP part already in the
# catalogue. Consulted before candidate ranking so generic values ("SS14")
# resolve without per-project override files. A proposal is only accepted if
# the target part exists, so stale rows stay inert.
KNOWN_PART_ALIASES = {
    # Soldered/e-radionica breakout parts identified by exact value/MPN.
    "attiny404_ssnr": "electronic_ic_soic_14_microcontroller_8_bit_avr_microchip_attiny404_ssnr",
    "tps613222a": "electronic_ic_sot_23_5_power_management_boost_converter_texas_instruments_tps613222a",
    "lm393": "electronic_ic_soic_8_logic_comparator_lm393",
    "rt9080_3_3": "electronic_ic_sot_23_5_power_management_linear_voltage_regulator_3_3_volt_richtek_rt9080_33",
    "opa344": "electronic_ic_sot_23_5_amplifier_operational_amplifier_texas_instruments_opa344",
    "si7211_b_00_iv": "electronic_ic_sot_23_5_sensor_hall_effect_silicon_labs_si7211_b_00_iv",
    "si7201_b_06_iv": "electronic_ic_sot_23_sensor_hall_effect_silicon_labs_si7201_b_06_iv",
    "hx711": "electronic_ic_sop_16_converter_load_cell_amplifier_avia_semiconductor_hx711",
    "df5a5_6lfu": "electronic_diode_tvs_sot_353_toshiba_df5a5_6lfu",
    "pesd3v3l4ug": "electronic_diode_esd_array_sot_353_nexperia_pesd3v3l4ug",
    "dt1042_04so": "electronic_diode_tvs_array_sot_26_diodes_incorporated_dt1042_04so",
    "m4_dioda": "electronic_diode_rectifier_sma_m4",
    "mmbt4403": "electronic_transistor_sot_23_bipolar_pnp_40_volt_600_milliamp_onsemi_mmbt4403",
    "nmos_dual": "electronic_transistor_sot_363_6_mosfet_n_channel_dual",
    "q_npn_bce": "electronic_transistor_sot_23_bipolar_npn",
    # Soldered boards draw bare "NPN"/"PNP"/"NMOS" values on SOT-23-3
    # footprints with no MPN; the underscore suffix defeats the word-boundary
    # match, so the spelled-out schematic values get their own rows.
    "npn": "electronic_transistor_sot_23_bipolar_npn",
    "npn_sot_23_3": "electronic_transistor_sot_23_bipolar_npn",
    "pnp": "electronic_transistor_sot_23_bipolar_pnp",
    "nmos": "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode",
    "dfe201612e_2r2m_p2": "electronic_inductor_0806_2_2_micro_henry",
    "dshp03ts_s": "electronic_switch_slide_surface_mount_dpdt_ck_dshp03ts_s",
    "tc33x_2_103e": "electronic_potentiometer_trimmer_through_hole_10_kilo_ohm_bourns_tc33x_2_103e",
    "mq_x": "electronic_sensor_mq_6_pin",
    "tcrt5000l": "electronic_sensor_tcrt5000_4_pin_vishay_tcrt5000l",
    "am312": "electronic_sensor_pir_3_pin_am312",
    "apds_9960": "electronic_sensor_apds_9960_broadcom_apds_9960",
    "easyc_smd": "electronic_connector_easyc_1_25_mm_pitch_surface_mount_right_angle_4_pin_jst_sm04b_gh_tf",
    "u_fl": "electronic_connector_u_fl_surface_mount_i_pex_u_fl_r_smt_1",
    "sma_edge": "electronic_connector_sma_edge_mount",
    "kf235_5_0_2p": "electronic_connector_terminal_block_5_mm_pitch_through_hole_2_pin_kf235_5_0_2p",
    "cr1220_holder": "electronic_connector_coin_cell_holder_through_hole_cr1220",
    "cp2102n": "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r",
    # The full schematic value "CP2102N-Axx-xQFN28" -- the bare "cp2102n" alias
    # above cannot match it because the word-boundary rule stops at the
    # following underscore.
    "cp2102n_axx_xqfn28": "electronic_ic_qfn_28_5_mm_x_5_mm_converter_usb_to_serial_converter_silicon_labs_cp2102n_a01_gqfn28r",
    "xc6206p332mr": "electronic_ic_sot_23_power_management_linear_voltage_regulator_3_3_volt_torex_xc6206p332mr",
    "xc6206p502mr": "electronic_ic_sot_23_power_management_linear_voltage_regulator_5_volt_torex_xc6206p502mr",
    "atmega328p_a": "electronic_ic_tqfp_32_7_mm_x_7_mm_microcontroller_8_bit_avr_microchip_atmega328p_au",
    # The Uno schematic writes the AMS1117 suffix with a trailing V.
    "ams1117_3_3": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
    "ams1117_3_3v": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_3_3_volt_advanced_monolithic_systems_ams1117_3_3",
    "ams1117_5v": "electronic_ic_sot_223_3_power_management_linear_voltage_regulator_5_volt_advanced_monolithic_systems_ams1117_5",
    "ch340c": "electronic_ic_sop_16_converter_usb_to_serial_converter_wch_ch340c",
    # Pico board MCU: same RP2040 the Bus Pirate 5 uses.
    "rp2040": "electronic_ic_qfn_56_7_mm_x_7_mm_microcontroller_dual_core_arm_cortex_m0_plus_raspberry_pi_rp2040",
    # BSS138 on SparkFun boards: the part's generic_match rules list KiCad's
    # symbol/footprint names, but SparkFun ships its own symbol and footprint,
    # so the value itself (which is the bare MPN there) aliases straight to the
    # stocked onsemi variant.
    "bss138": "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138",
    "jst_sh_2pin_1mm_c145954": "electronic_connector_jst_sh_1_mm_pitch_surface_mount_right_angle_2_pin_jst_sm02b_srss_tb",
    "pesd0402": "electronic_diode_esd_0402_littelfuse_pesd0402",
    "ss14": "electronic_diode_schottky_sod_123_ss14",
    "bat54w": "electronic_diode_schottky_sod_323_bat54w",
    "1ss400": "electronic_diode_schottky_sod_523_1ss400",
    # Schematic values that are really MPNs of catalogue capacitors.
    "cl10a226mpcnube": "electronic_capacitor_0603_22_micro_farad",
    # Soldered radial electrolytic (16 V, 681 code = 680 uF, 8 mm x 14.5 mm).
    "emzr160ara681mha0g": "electronic_capacitor_8_mm_diameter_14_5_mm_tall_electrolytic_680_micro_farad_16_volt",
    "c1608x7s1a475k080ac": "electronic_capacitor_0603_4_7_micro_farad",
    # 2N7002 carries an opt-in generic_match rule in its populate data, so it
    # is intentionally not aliased here (BSS138 above needs the alias because
    # SparkFun boards use their own symbol/footprint names).
}


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
    # "15mR"/"15mΩ" is fifteen milliohms; KiCad's lowercase m before the unit
    # marker means milli on shunt resistors (the bare-letter path below keeps
    # its historic mega reading for plain "15m").
    milli_text = str(value or "").strip().lower().replace("ω", "r").replace("Ω", "r")
    milli_match = re.fullmatch(r"(\d+(?:\.\d+)?)\s*mr", milli_text)
    if milli_match:
        parsed = float(milli_match.group(1)) / 1000
        if abs(parsed - round(parsed)) < 1e-9:
            return int(round(parsed))
        return round(parsed, 6)
    parsed = _engineering_number(value, {"": 1, "r": 1, "k": 1000, "m": 1000000})
    if parsed is None:
        return None
    if abs(parsed - round(parsed)) < 1e-9:
        return int(round(parsed))
    return round(parsed, 6)


def resistance_taxonomy(value):
    resistance = parse_resistance_ohms(value)
    if resistance is None:
        return ""
    if isinstance(resistance, int):
        return str(resistance)
    return ("%.6f" % resistance).rstrip("0").rstrip(".").replace(".", "_")


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


def parse_inductance_henries(value):
    """Only values with an explicit inductance unit ("33nH", "10uH", "4.7uH")."""
    match = re.fullmatch(
        r"(\d+(?:\.\d+)?)\s*(nh|uh|µh|μh|mh|h)",
        str(value or "").strip().lower().replace("henry", "h").replace("henries", "h"),
    )
    if not match:
        return None
    suffix = {"nh": 1e-9, "uh": 1e-6, "µh": 1e-6, "μh": 1e-6, "mh": 1e-3, "h": 1.0}
    return float(match.group(1)) * suffix[match.group(2)]


def inductance_taxonomy(value):
    henries = parse_inductance_henries(value)
    if henries is None:
        return ""
    units = [
        (1e-9, "nano_henry"),
        (1e-6, "micro_henry"),
        (1e-3, "milli_henry"),
        (1.0, "henry"),
    ]
    selected_multiplier, selected_name = units[0]
    for multiplier, unit_name in units:
        scaled = henries / multiplier
        if scaled >= 1 and abs(scaled - round(scaled, 6)) < 1e-6:
            selected_multiplier = multiplier
            selected_name = unit_name
    scaled = henries / selected_multiplier
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
        "manufacturer": properties.get("Manufacturer") or properties.get("Manufacturer Name") or "",
    }


def infer_kind(fields):
    reference = fields["reference"].upper()
    evidence = " ".join(
        normalize_text(fields[field_name])
        for field_name in ["value", "footprint", "library_id"]
    )
    if reference.startswith("LED") or "led" in evidence or "ws2812" in evidence:
        return "led"
    if "r_array" in evidence or reference.startswith("RN"):
        return "resistor_array"
    if reference.startswith("R") and not reference.startswith("REF"):
        return "resistor"
    # Inductors first: an explicit inductance unit beats any footprint or
    # reference hint (SparkFun draws fitted inductors with capacitor symbols).
    if parse_inductance_henries(fields["value"]) is not None:
        return "inductor"
    if "ferrite" in evidence:
        return "ferrite_bead"
    # A resistance written on a capacitor-referenced symbol means the board
    # fitted a resistor there (SparkFun USB current limiters say "470Ohm" on
    # C-prefixed references).
    if reference.startswith("C") and not reference.startswith("CON"):
        value_text = str(fields["value"] or "")
        if "ohm" in normalize_text(value_text) or (
            parse_resistance_ohms(value_text) is not None
            and parse_capacitance_farads(value_text) is None
        ):
            return "resistor"
        return "capacitor"
    if reference.startswith("Q") or "transistor" in evidence or "mosfet" in evidence:
        return "transistor"
    # Diodes: D-prefixed references, or schottky/tvs/rectifier/zener in evidence
    if reference.startswith("D") and not reference.startswith("DN"):
        return "diode"
    if any(d in evidence for d in ["d_schottky", "d_tvs", "d_rectifier", "d_zener", "d_zener_sod"]):
        return "diode"
    # Resettable PTC fuses (SparkFun draws them on F references with a fuse
    # symbol; the value is a voltage/hold/trip rating triplet, not an MPN).
    if reference.startswith("F") and not reference.startswith("FID") and "fuse" in evidence:
        return "fuse"
    # Generic through-hole 2.54 mm pin headers: KiCad's Conn_01xNN symbols on
    # PinHeader_1xNN_P2.54mm footprints, and SparkFun's 1xNN footprints (2.54 mm
    # with or without an explicit _P2.54mm suffix). A SparkFun 1xNN footprint is
    # a 2.54 mm header whatever symbol sits on it -- SparkFun also uses
    # I2C_01xNN and friends on the same footprints -- so the footprint alone is
    # sufficient there. JST and other finer-pitch Conn_01xNN symbols stay
    # excluded from the symbol-driven branch.
    sparkfun_header_footprint = bool(
        re.fullmatch(r"sparkfun_connector_1x\d+(_p2_54mm)?", normalize_text(fields["footprint"]))
    )
    # e-radionica (Soldered) boards use their own header footprints:
    # HEADER_MALE_NX1 is the plain 2.54 mm header row; HEADER-UPDI is the
    # 1x03 UPDI programming header.
    erad_header_footprint = bool(
        re.search(r"header_male_\d+x\d+", normalize_text(fields["footprint"]))
    ) or "header_updi" in normalize_text(fields["footprint"])
    dual_row_header_footprint = bool(re.search(r"pinheader_2x\d+_p2_54mm", normalize_text(fields["footprint"])))
    if sparkfun_header_footprint or erad_header_footprint or dual_row_header_footprint or (
        "conn_01x" in evidence
        and "jst" not in evidence
        and "pinheader" in evidence
        and "2_54mm" in evidence
    ):
        return "connector_header"
    if reference.startswith("Y") and "crystal" in evidence:
        return "crystal"
    # USB-C and other connectors
    if "usb_c_receptacle" in evidence or "usb_c" in evidence:
        return "connector"
    if reference.startswith("J") and ("conn_" in evidence or "header" in evidence or "receptacle" in evidence):
        return "connector"
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

    pcb = component.get("pcb") or {}
    mounting_holes = pcb.get("mounting_holes") or []
    if pcb.get("is_mounting_hole", False) and len(mounting_holes) > 0:
        return str(mounting_holes[0].get("oomp_id", ""))

    # Known value/MPN aliases point straight at an exact catalogue part.
    # A bare value may only alias when the schematic carries no MPN -- a
    # specific MPN ("BSS138-13-F") means the exact identity is known and needs
    # its own part. An MPN alias requires the normalized MPN to be exact.
    value_normalized = normalize_text(fields["value"])
    mpn_normalized = normalize_text(fields["mpn"])
    if mpn_normalized:
        if mpn_normalized in KNOWN_PART_ALIASES:
            return KNOWN_PART_ALIASES[mpn_normalized]
    else:
        for alias, oomp_id in KNOWN_PART_ALIASES.items():
            # \b keeps "2N7002" from matching the "2N7002K" variant.
            if re.search(rf"\b{re.escape(alias)}\b", value_normalized):
                return oomp_id

    if kind == "resistor":
        resistance = resistance_taxonomy(fields["value"])
        if package_size and resistance != "":
            return f"electronic_resistor_{package_size}_{resistance}_ohm"

    if kind == "resistor_array":
        resistance = resistance_taxonomy(fields["value"])
        if resistance != "":
            return f"electronic_resistor_array_4_x_0402_convex_{resistance}_ohm_8_pin"

    if kind == "capacitor":
        capacitance = capacitance_taxonomy(fields["value"])
        if package_size and capacitance:
            evidence = normalize_text(
                " ".join([fields["footprint"], fields["library_id"], fields["value"]])
            )
            if "tantal" in evidence or "kemet" in evidence or "eia" in evidence:
                if package_size == "3216":
                    # AVX-A / Kemet-I tantalum family: nominal voltage per value.
                    voltage = "10_volt" if capacitance.startswith("22_") else "16_volt"
                    return f"electronic_capacitor_{package_size}_avx_a_tantalum_{capacitance}_{voltage}"
            return f"electronic_capacitor_{package_size}_{capacitance}"

    if kind == "inductor":
        inductance = inductance_taxonomy(fields["value"])
        if package_size and inductance:
            return f"electronic_inductor_{package_size}_{inductance}"

    if kind == "ferrite_bead":
        # The generic catalogue bead (created for the Soldered "0603L" boards);
        # specific MPNs keep coming through aliases and overrides.
        if package_size == "0603":
            return "electronic_ferrite_bead_0603_600_ohm_500_milliamp"

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

    if kind == "connector_header":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        dual_row = False
        pin_count = None
        m = re.search(r"conn_01x(\d+)", value_text)
        if m:
            pin_count = int(m.group(1))
        else:
            m = re.search(r"pinheader_1x(\d+)_p2_54mm", footprint_text) or re.fullmatch(
                r"sparkfun_connector_1x(\d+)(?:_p2_54mm)?", footprint_text
            )
            if m:
                pin_count = int(m.group(1))
        if not pin_count:
            # Dual-row headers (ICSP and friends): PinHeader_2x03_P2.54mm.
            m = re.search(r"pinheader_2x(\d+)_p2_54mm", footprint_text)
            if m:
                pin_count = 2 * int(m.group(1))
                dual_row = True
        if not pin_count:
            # e-radionica HEADER_MALE_NX1 and the 1x03 UPDI header.
            m = re.search(r"header_male_(\d+)x(\d+)", footprint_text)
            if m:
                pin_count = int(m.group(1)) * int(m.group(2))
            elif "header_updi" in footprint_text or "header_updi" in value_text:
                pin_count = 3
        if pin_count:
            if dual_row:
                return f"electronic_connector_header_2_54_mm_pitch_through_hole_dual_row_{pin_count}_pin"
            return f"electronic_connector_header_2_54_mm_pitch_through_hole_{pin_count}_pin"

    if kind == "crystal":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])

        # Parse frequency
        freq_match = re.search(r"(\d+(?:_\d+)?)[_\s]*(mhz|khz)", value_text)
        if not freq_match:
            return ""
        freq_num = freq_match.group(1).replace("_", ".")
        freq_unit = freq_match.group(2)
        if freq_unit == "mhz":
            freq_taxonomy = freq_num.replace(".", "_") + "_mhz"
        else:
            freq_taxonomy = freq_num.replace(".", "_") + "_khz"

        # Parse package and pin count from footprint
        pkg_match = re.search(r"crystal_smd_(\d+)_(\d)pin", footprint_text)
        if not pkg_match:
            # Size-styled footprints ("Crystal_SMD_3.2x2.5mm") name the body;
            # a 3225 body is the standard 4-pad ceramic resonator can.
            size_match = re.search(r"crystal_smd_(\d+)_(\d)x(\d+)_(\d+)mm", footprint_text)
            if not size_match:
                return ""
            package = f"{size_match.group(1)}{size_match.group(2)}{size_match.group(3)}{size_match.group(4)}"
            pin_count = "4_pin" if package in ("3225", "2520") else "2_pin"
        else:
            package = pkg_match.group(1)
            pin_count = pkg_match.group(2) + "_pin"

        # Default load capacitance by frequency
        if "32_768" in freq_taxonomy:
            load_cap = "12_5_pf"
        else:
            load_cap = "20_pf"

        return f"electronic_crystal_{package}_surface_mount_{pin_count}_{freq_taxonomy}_{load_cap}"

    if kind == "diode":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # Determine diode type
        diode_type = ""
        if "schottky" in value_text or "schottky" in library_text:
            diode_type = "schottky"
        elif "tvs" in value_text or "tvs" in library_text or "esd" in value_text or "pesd" in value_text:
            diode_type = "tvs"
        elif "zener" in value_text or "zener" in library_text:
            diode_type = "zener"
        elif "switching" in value_text or "switching" in library_text:
            diode_type = "switching"
        elif "rectifier" in value_text or "rectifier" in library_text:
            diode_type = "rectifier"
        else:
            # Default for generic D_Schottky and similar
            diode_type = "schottky"

        # Determine package from footprint
        package = ""
        for pkg_token in ["sod_123", "sod_323", "sod_523f", "sod_523", "sot_23", "sot_143", "sot_523", "d_0402", "d_0603"]:
            if pkg_token in footprint_text or pkg_token in library_text:
                if pkg_token.startswith("d_"):
                    package = pkg_token[2:]
                else:
                    package = pkg_token
                break

        if diode_type and package:
            return f"electronic_diode_{diode_type}_{package}"

    if kind == "fuse" and package_size:
        return f"electronic_fuse_{package_size}_resettable"

    if kind == "connector":
        value_text = normalize_text(fields["value"])
        footprint_text = normalize_text(fields["footprint"])
        library_text = normalize_text(fields["library_id"])

        # USB-C receptacle
        if "usb_c" in value_text or "usb_c" in library_text or "usb_c" in footprint_text:
            return "electronic_connector_usb_c_surface_mount_16_pin"

    return ""


class OompPartIndex:
    def __init__(self, parts_directory):
        self.parts_directory = Path(parts_directory).resolve()
        self.parts = []
        self.by_id = {}
        self.generic_parts = []
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
            # Generic family matching is opt-in population data, never a guess
            # from a similar suffix. The C loader keeps the metadata pass small.
            if part_directory.name.startswith("electronic_"):
                loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
                metadata = yaml.load(working_yaml.read_text(encoding="utf-8"), Loader=loader) or {}
                rules = metadata.get("generic_match") or {}
                if rules:
                    self.generic_parts.append({
                        "oomp_id": part_directory.name,
                        "kind": metadata.get("taxonomy_2", ""),
                        "package": metadata.get("taxonomy_3", ""),
                        "rules": rules,
                    })

    def generic_matches(self, fields):
        if fields.get("mpn") or fields.get("manufacturer"):
            return []
        matches = []
        for part in self.generic_parts:
            rules = part["rules"]
            checks = [
                ["value", "values"],
                ["library_id", "symbols"],
                ["footprint", "footprints"],
            ]
            agrees = True
            for field_name, rule_name in checks:
                accepted_values = []
                for accepted_value in rules.get(rule_name, []):
                    accepted_values.append(normalize_text(accepted_value))
                if normalize_text(fields.get(field_name, "")) not in accepted_values:
                    agrees = False
            if agrees:
                matches.append(part)
        return matches

    def candidate_parts(self, kind):
        if kind:
            prefix = f"electronic_{kind}_"
            if kind == "mounting_hole":
                prefix = "mechanical_mounting_hole_"
            return [part for part in self.parts if part["oomp_id"].startswith(prefix)]
        return []


def _is_board_feature(fields):
    """Silkscreen art, fiducials, test points, standoffs and solder-jumper
    traces live on the board but are never purchased, like DNF parts."""
    footprint = normalize_text(fields["footprint"])
    library_id = normalize_text(fields["library_id"])
    value = normalize_text(fields["value"])
    reference_upper = str(fields.get("reference", "")).upper()
    board_feature_evidence = " ".join([footprint, library_id, value])
    if "buzzard" in board_feature_evidence or "kibuzzard" in board_feature_evidence:
        return True
    if "fiducial" in board_feature_evidence or reference_upper.startswith("FID") or reference_upper.startswith("FD"):
        return True
    if "standoff" in board_feature_evidence:
        return True
    if "testpoint" in board_feature_evidence or "test_point" in board_feature_evidence or (
        reference_upper.startswith("TP") and "test" in board_feature_evidence
    ):
        return True
    if "logo" in board_feature_evidence or "oshw" in board_feature_evidence:
        return True
    if "soldered_graphics" in board_feature_evidence or "sparkfun_aesthetic" in board_feature_evidence:
        return True
    if "smd_jumper" in board_feature_evidence or "jumper_2_nc" in board_feature_evidence or (
        value.startswith("smd_jumper")
    ):
        return True
    # Jumper_2_NC_Trace / Jumper_3_NC-2_Trace and friends: NC solder-blob
    # traces, not purchased parts.
    if "jumper" in board_feature_evidence and ("_trace" in board_feature_evidence or "_nc" in board_feature_evidence or "nc_" in board_feature_evidence):
        return True
    # Jumper_2_NO / Jumper_3_NO: unpopulated solder-blob option pads.
    if re.search(r"jumper_\d+_no", board_feature_evidence):
        return True
    # Soldered "PAD_2x1.5": exposed probe/sensing pads etched in the board copper.
    if value.startswith("pad_") and reference_upper.startswith("PAD"):
        return True
    # Footprint-only outline graphics (SparkFun "BMV080_Outline" on REF**).
    if "outline" in board_feature_evidence:
        return True
    if value in ("measure",) and "jumper" in board_feature_evidence:
        return True
    return False


def _is_physical_component(component):
    reference = component.get("reference", "")
    reference_upper = reference.upper()
    fields = component_fields(component)
    footprint = normalize_text(fields["footprint"])

    pcb = component.get("pcb") or {}
    if pcb.get("is_mounting_hole", False):
        return True

    if reference_upper.startswith("SJ"):
        return False
    if reference_upper.startswith("UNK_HOLE"):
        return False
    if footprint.startswith("dummyfp"):
        return False
    if reference.startswith("#"):
        return False
    value_upper = str(fields.get("value", "")).strip().upper()
    if value_upper in ("DNF", "DNP"):
        return False
    if _is_board_feature(fields):
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
            match = re.search(r"_([0-9]+(?:_[0-9]+)?)_ohm$", part_id)
            return float(match.group(1).replace("_", ".")) if match else None
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


def match_component(index, component, overrides=None, blocked=None):
    overrides = overrides or {}
    reference = component.get("reference", "")
    fields = component_fields(component)
    kind = infer_kind(fields)
    pcb = component.get("pcb") or {}
    if pcb.get("is_mounting_hole", False):
        kind = "mounting_hole"
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
        value_upper = str(fields.get("value", "")).strip().upper()
        if value_upper in ("DNF", "DNP"):
            result["reasons"].append("Component is marked do-not-fit / do-not-populate and has no purchased OOMP part requirement.")
        elif _is_board_feature(fields):
            result["reasons"].append("Fiducials, logos, test points, standoffs and solder-jumper traces are board features, not purchased OOMP parts.")
        elif reference_upper.startswith("SJ"):
            result["reasons"].append("PCB solder jumpers are board features, not purchased OOMP parts.")
        elif reference_upper.startswith("UNK_HOLE") or footprint.startswith("dummyfp"):
            result["reasons"].append("Mechanical or dummy mounting holes do not require OOMP parts.")
        else:
            result["reasons"].append("The symbol has no physical PCB/OOMP part requirement.")
        return result

    if reference in (blocked or {}):
        # A blocked reference is a documented decision, not an unexplained
        # failure: it keeps the reason text and leaves the unmatched report
        # to genuinely unexplained components.
        result["status"] = "blocked"
        result["reasons"].append(str(blocked[reference]))
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

    explicit_ids = []
    for library_id in [fields.get("footprint", ""), fields.get("library_id", "")]:
        if ":" not in library_id:
            continue
        nickname, entry = library_id.split(":", 1)
        if nickname in ["OOMP", "OOMP_MachineSolder", "OOMP_HandSolder"] and entry not in explicit_ids:
            explicit_ids.append(entry)
    if explicit_ids:
        if len(explicit_ids) == 1 and explicit_ids[0] in index.by_id:
            result.update(status="matched", accepted=True, oomp_id=explicit_ids[0], confidence=1.0,
                          reasons=["Explicit OOMP KiCad library identifier."])
        else:
            result.update(status="ambiguous", reasons=["Conflicting or unavailable explicit OOMP library identifiers."])
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

    generic_matches = index.generic_matches(fields)
    if len(generic_matches) == 1:
        generic_part = generic_matches[0]
        result.update(
            status="matched",
            accepted=True,
            oomp_id=generic_part["oomp_id"],
            confidence=1.0,
            identity_scope="generic_family",
            reasons=["Generic value, symbol and footprint agree with the populated matching rule; no manufacturer or MPN was supplied."],
        )
        result["inferred"]["kind"] = generic_part["kind"]
        result["inferred"]["package_size"] = generic_part["package"]
        return result
    if len(generic_matches) > 1:
        result.update(status="ambiguous", reasons=["More than one populated generic family rule matches this component."])
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
