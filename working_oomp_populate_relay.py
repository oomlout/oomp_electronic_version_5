def main(**kwargs):
    options = kwargs.get("options", [])

    # First relays in the population: Hongfa 12 V through-hole power relays
    # from the JLC house-parts queue.  taxonomy_5 carries the contact form
    # (spst_no / spdt); coil voltage rides in taxonomy_4.
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "jqx_105f_1_012d_1hs",
        "name_short": "Power Relay JQX-105F-1/012D-1HS (SPST-NO 40A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "jzc_32f_012_hs3_555",
        "name_short": "Power Relay JZC-32F/012-HS3(555) (SPST-NO 10A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spdt", "taxonomy_14": "hongfa", "taxonomy_15": "hf32f_012_zs3",
        "name_short": "Power Relay HF32F/012-ZS3 (SPDT 3A)",
    })

    # Second batch of Hongfa relays from the JLC house-parts queue (a 24 V
    # coil, a signal-relay DIP body, and more 12 V SPST parts).
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "jzc_33f_012_hs3_555",
        "name_short": "Power Relay JZC-33F/012-HS3(555) (SPST-NO 10A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "24_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "jqc_3ff_24vdc_1hs_551",
        "name_short": "Power Relay JQC-3FF/24VDC-1HS(551) (SPST-NO 15A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "hf49fd_012_1h11",
        "name_short": "Power Relay HF49FD/012-1H11 (SIP, SPST-NO 5A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spst_no", "taxonomy_14": "hongfa", "taxonomy_15": "jqc_3ff_12_1hs_551",
        "name_short": "Power Relay JQC-3FF/12-1HS(551) (SPST-NO 15A)",
    })
    options.append({
        "taxonomy_2": "relay", "taxonomy_3": "through_hole", "taxonomy_4": "12_volt_coil",
        "taxonomy_5": "spdt", "taxonomy_14": "hongfa", "taxonomy_15": "hfd23_012_1zs",
        "name_short": "Signal Relay HFD23/012-1ZS (DIP, SPDT 2A)",
    })


if __name__ == "__main__":
    main()
