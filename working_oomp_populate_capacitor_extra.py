def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})
    current = "electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt"
    if current in extras_dict:
        part = extras_dict[current]
        part["part_number_manufacturer"] = "TAJA226K010RNJ"
        part["part_number_manufacturer_kyocera_avx"] = "TAJA226K010RNJ"
        part["manufacturer"] = "Kyocera AVX"
        part["part_number_lcsc"] = "C11366"
        part["product_url"] = "https://www.lcsc.com/product-detail/C11366.html"
        part["category"] = "capacitor"
        part["electrical"] = {"capacitance": "22 uF", "voltage": "10 V", "tolerance": "10%"}
        part["pins"] = {
            "pin_1": {"number": "1", "name": "positive", "type": "passive"},
            "pin_2": {"number": "2", "name": "negative", "type": "passive"},
        }
        part["kicad"] = {
            "symbol": "Device:C_Polarized",
            "machine_solder": "Capacitor_Tantalum_SMD:CP_EIA-3216-18_Kemet-A",
            "hand_solder": "",
        }
        part["research_notes"] = [
            "LCSC verifies AVX A case 3.2 x 1.6 x 1.8 mm. The project uses a Kemet-I height-1.0 footprint; review physical height clearance.",
        ]
