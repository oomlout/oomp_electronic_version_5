"""Build the LCSC research queue for every part missing supplier details."""
import glob, json, os, re

ROOT = r"C:/gh/oomp_electronic_version_5"

CATEGORY = {
    "chip_resistor": 1199,   # Chip Resistor - Surface Mount (verified 2026-09)
    "capacitor": 1142,       # Ceramic Capacitors (MLCC)
    "tht_resistor": 1203,    # Through Hole Resistors
    "resistor_array": 1200,  # Resistor Networks, Arrays
    "led": 412,              # LED Indication - Discrete
}

# Hand-written queries for one-off families (kind "other" / special capacitors)
SPECIAL_QUERIES = {
    "electronic_capacitor_3216_avx_a_tantalum_4_7_micro_farad_16_volt": "T491B476K016AT",
    "electronic_capacitor_6_3_mm_diameter_5_4_mm_tall_electrolytic_220_micro_farad_10_volt": "220uF 10V 6.3x5.4 electrolytic",
    "electronic_capacitor_6_3_mm_diameter_7_7_mm_tall_electrolytic_220_micro_farad_10_volt": "220uF 10V 6.3x7.7 electrolytic",
    "electronic_capacitor_8_mm_diameter_6_5_mm_tall_electrolytic_220_micro_farad_10_volt": "220uF 10V 8x6.5 electrolytic",
    "electronic_crystal_3215_surface_mount_2_pin_32_768_khz_12_5_pf": "32.768kHz 3215 12.5pF",
    "electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf": "12MHz 3225 20pF",
    "electronic_crystal_3225_surface_mount_4_pin_16_mhz_20_pf": "16MHz 3225 20pF",
    "electronic_crystal_5032_surface_mount_2_pin_8_mhz_20_pf": "8MHz 5032 20pF",
    "electronic_diode_esd_0402_littelfuse_pesd0402": "PESD0402",
    "electronic_diode_schottky_dual_common_cathode_sot_523_diodes_incorporated_bas40t_05": " BAS40T-05",
    "electronic_diode_schottky_sod_123_ss14": "SS14 SOD-123",
    "electronic_diode_schottky_sod_323_bat54w": "BAT54W",
    "electronic_diode_schottky_sod_523_1ss400": "1SS400",
    "electronic_display_lcd_character_16_by_2_backlight_yellow": "16x2 LCD yellow backlight",
    "electronic_display_tft_2_inch_240_x_320_pixel_ips_spi_12_pin_szhtc_qt200h1201": "QT200H1201",
    "electronic_fuse_0402_resettable": "0402 resettable fuse",
    "electronic_fuse_1206_resettable": "1206 resettable fuse",
    "electronic_ic_tssop_24_logic_16_channel_analog_multiplexer_nexperia_74hct4067pw118": "74HCT4067PW,118",
    "electronic_inductor_0603_10_micro_henry": "0603 10uH inductor",
    "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_bss138": "BSS138",
    "electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_60_volt_2n7002": "2N7002 SOT-23",
    "electronic_transistor_sot_523_mosfet_p_channel_enhancement_mode_20_volt_2_8_amp_cbi_bc2301t_2_8a": "BC2301T-2.8A",
    "electronic_led_1010_rgb_ws2812b_xinglight_1010rgbc": "1010RGBC",
    "electronic_led_5050_rgb_ws2812b_worldsemi_ws2812b_b_w": "WS2812B-B/W",
}

LED_COLOURS = {"red", "green", "blue", "yellow", "white"}

def yaml_data(path):
    import yaml
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}

def resistor_value(part_id):
    match = re.search(r"^electronic_resistor(?:_array)?_[a-z0-9_]+?_(\d+(?:_\d+)*)_ohm", part_id)
    if not match:
        return None
    return int(match.group(1).replace("_", ""))

def ohm_query(value):
    if value is None:
        return None
    if value == 0:
        return "0Ω"
    if value >= 1_000_000 and value % 1_000_000 == 0:
        return f"{value // 1_000_000}MΩ"
    if value >= 1_000 and value % 1_000 == 0:
        return f"{value // 1_000}KΩ"
    return f"{value}Ω"

def farad_query(part_id):
    match = re.search(r"^electronic_capacitor_[a-z0-9_]+?_(\d+(?:_\d+)*)_(pico|nano|micro)_farad$", part_id)
    if not match:
        return None
    number = float(match.group(1).replace("_", "."))
    suffix = {"pico": "pF", "nano": "nF", "micro": "uF"}[match.group(2)]
    return f"{number:g}{suffix}"

def jst_mpn(part_id):
    match = re.search(r"_jst_([a-z0-9_]+)$", part_id)
    if not match:
        return None
    return match.group(1).replace("_", "-").upper()

def led_entry(part_id):
    tokens = part_id.replace("electronic_led_", "").split("_")
    if "ws2812b" in tokens:
        return None  # handled by SPECIAL_QUERIES
    size = tokens[0]
    if len(tokens) > 1 and tokens[1] == "mm":
        size = f"{tokens[0]}mm"
    colour = tokens[1] if len(tokens) > 1 and tokens[1] in LED_COLOURS else ""
    lens = "clear" if "clear" in tokens else ("tint" if "tint" in tokens else "")
    query = f"{size} {colour} LED".strip()
    hints = [h for h in (colour, lens) if h]
    return {"kind": "led", "category": CATEGORY["led"], "query": query, "hints": hints}

def build_entry(part_id):
    if part_id in SPECIAL_QUERIES:
        return {"kind": "mpn", "category": None, "query": SPECIAL_QUERIES[part_id].strip()}
    if part_id.startswith("electronic_resistor_quarter_watt"):
        return {"kind": "tht_resistor", "category": CATEGORY["tht_resistor"], "query": ohm_query(resistor_value(part_id))}
    if part_id.startswith("electronic_resistor_array"):
        value = ohm_query(resistor_value(part_id))
        return {"kind": "resistor_array", "category": CATEGORY["resistor_array"], "query": f"0402 {value}"}
    if part_id.startswith("electronic_resistor_"):
        size = part_id.split("_")[2]
        return {"kind": "chip_resistor", "category": CATEGORY["chip_resistor"], "query": f"{size} {ohm_query(resistor_value(part_id))}"}
    if part_id.startswith("electronic_led_"):
        return led_entry(part_id)
    if part_id.startswith(("electronic_connector_jst_ph_", "electronic_connector_jst_sh_", "electronic_connector_jst_xh_")):
        return {"kind": "mpn", "category": None, "query": jst_mpn(part_id)}
    if part_id.startswith("electronic_capacitor_"):
        value = farad_query(part_id)
        if value:
            size = part_id.split("_")[2]
            return {"kind": "capacitor", "category": CATEGORY["capacitor"], "query": f"{size} {value}"}
    return None

def main():
    queue = []
    for wy in sorted(glob.glob(os.path.join(ROOT, "parts/*/working.yaml"))):
        part_id = os.path.basename(os.path.dirname(wy))
        if part_id.startswith(("mechanical_mounting_hole", "oomp_project")):
            continue
        d = yaml_data(wy)
        has_lcsc = bool(d.get("part_number_lcsc") or d.get("part_numbers_lcsc"))
        has_mpn = bool(d.get("part_number_manufacturer") or d.get("part_numbers_manufacturer") or d.get("manufacturers"))
        if has_lcsc and has_mpn:
            continue
        entry = build_entry(part_id)
        if not entry or not entry.get("query"):
            print("NO QUERY:", part_id)
            continue
        entry["part_id"] = part_id
        entry["missing"] = [n for n, ok in (("lcsc", has_lcsc), ("mpn", has_mpn)) if not ok]
        queue.append(entry)
    out = os.path.join(ROOT, "tmp", "lcsc_queue.json")
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(queue, handle, indent=1)
    kinds = {}
    for entry in queue:
        kinds[entry.get("kind", "?")] = kinds.get(entry.get("kind", "?"), 0) + 1
    print("queue size:", len(queue))
    print("kinds:", json.dumps(kinds))

if __name__ == "__main__":
    main()
