def main(**kwargs):
    extras_dict = kwargs.get("extras_dict", {})

    # Apply explicitly promoted browser-reviewed JLC identities (manufacturer,
    # MPN, LCSC code) to the relay family, matching the other families'
    # reviewed-choice enrichment.
    from working_oomp_populate_jlc import apply_reviewed_jlc_choices
    apply_reviewed_jlc_choices(extras_dict, family="relay")

    # === BEGIN generated relay batch (tmp/relay_batch.py) — regenerated, do not hand-edit ===
    # JLC C3638 / HF(Xiamen Hongfa Electroacoustic) JQC-3FF/24VDC-1HS(551) - relay family batch 2026-10-06
    current = "electronic_relay_through_hole_24_volt_coil_spst_no_hongfa_jqc_3ff_24vdc_1hs_551"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Hongfa JQC-3FF (Songle SRD form) SPST-NO power relay, 19.0 x 15.5 x 15.5 mm, 24 VDC coil"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8757064350995755008-C3638.pdf"
        part["dimensions_mm"] = {"length": 19.0, "width": 15.5, "height": 15.5}
        part["dimension_reference"] = {
            "document": "JQC-3FF/24VDC-1HS(551) datasheet (C3638 provenance)",
            "pages": [1],
            "notes": "Hongfa JQC-3FF (Songle SRD form) SPST-NO power relay, 19.0 x 15.5 x 15.5 mm, 24 VDC coil; pad layout per the official Relay_THT Hongfa JQC-3FF master.",
        }
        part["electrical"] = {
            "coil_voltage": "24V",
            "coil_resistance": "1.6k ohm",
            "coil_power": "360mW",
            "contact_form": "1 Set Normally Open: 1A (SPST NO)",
            "contact_rating": "10A@277VAC、10A@28VDC",
            "contact_material": "AgCdO",
            "device_type": "electromechanical power relay, SPST-NO (1 form A)"
        }
        part["pins"] = {
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_A1": {"number": "A1", "name": "A1", "type": "passive"},
            "pin_A2": {"number": "A2", "name": "A2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Relay:Relay_SPST-NO",
            "machine_solder": "Relay_THT:Relay_SPST_Hongfa_JQC-3FF_0XX-1H",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HF(Xiamen Hongfa Electroacoustic) JQC-3FF/24VDC-1HS(551) (C3638); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Relay:Relay_SPST-NO master and the Relay_THT:Relay_SPST_Hongfa_JQC-3FF_0XX-1H footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # JLC C3640 / HF(Xiamen Hongfa Electroacoustic) JQC-3FF/12-1HS(551) - relay family batch 2026-10-06
    current = "electronic_relay_through_hole_12_volt_coil_spst_no_hongfa_jqc_3ff_12_1hs_551"
    if current in extras_dict:
        part = extras_dict[current]
        part["package_name_manufacturer"] = "Hongfa JQC-3FF (Songle SRD form) SPST-NO power relay, 19.0 x 15.5 x 15.5 mm, 12 VDC coil"
        part["datasheet_url"] = "https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8588886941894500352-C3640.pdf"
        part["dimensions_mm"] = {"length": 19.0, "width": 15.5, "height": 15.5}
        part["dimension_reference"] = {
            "document": "JQC-3FF/12-1HS(551) datasheet (C3640 provenance)",
            "pages": [1],
            "notes": "Hongfa JQC-3FF (Songle SRD form) SPST-NO power relay, 19.0 x 15.5 x 15.5 mm, 12 VDC coil; pad layout per the official Relay_THT Hongfa JQC-3FF master.",
        }
        part["electrical"] = {
            "coil_voltage": "12V",
            "coil_resistance": "400 ohm",
            "coil_power": "360mW",
            "contact_form": "1 Set Normally Open: 1A (SPST NO)",
            "contact_rating": "10A@277VAC、10A@28VDC",
            "contact_material": "AgCdO",
            "device_type": "electromechanical power relay, SPST-NO (1 form A)"
        }
        part["pins"] = {
            "pin_13": {"number": "13", "name": "13", "type": "passive"},
            "pin_14": {"number": "14", "name": "14", "type": "passive"},
            "pin_A1": {"number": "A1", "name": "A1", "type": "passive"},
            "pin_A2": {"number": "A2", "name": "A2", "type": "passive"}
        }
        part["kicad"] = {
            "symbol": "Relay:Relay_SPST-NO",
            "machine_solder": "Relay_THT:Relay_SPST_Hongfa_JQC-3FF_0XX-1H",
            "hand_solder": "",
            "allow_project_fallback": False,
        }
        part["research_notes"] = [
            "The official JLC page lists HF(Xiamen Hongfa Electroacoustic) JQC-3FF/12-1HS(551) (C3640); identity and ratings observed live at intake 2026-09-30.",
            "Mapped to the KiCad Relay:Relay_SPST-NO master and the Relay_THT:Relay_SPST_Hongfa_JQC-3FF_0XX-1H footprint master in the 2026-10-06 family batch.",
        ]
        part["file_copy"] = [
            {
                "file_source": f"parts_source/{current}/datasheet.pdf",
                "file_destination": "datasheet.pdf",
            }
        ]
    # === END generated relay batch (tmp/relay_batch.py) ===