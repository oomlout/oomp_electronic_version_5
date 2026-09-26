def main(**kwargs):
    options = kwargs.get("options", [])

    # Keep exact diode definitions as a plain array.  Diode families do not
    # share every package/manufacturer combination, so a cross-product of four
    # separate lists would create invalid parts that do not exist.
    diodes = [
        {
            "diode_type": "rectifier",
            "package": "sma",
            "manufacturer": "",
            "part_number": "m4",
            "name_short": "Rectifier Diode M4 (SMA)",
        },
        {
            "diode_type": "bridge_rectifier",
            "package": "mbs",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "mb10s_50mil",
            "name_short": "Single-Phase Bridge Rectifier MB10S-50MIL (MBS)",
        },
        {
            "diode_type": "rectifier",
            "package": "sod_123fl",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "sm4007pl",
            "name_short": "Rectifier Diode SM4007PL (SOD-123FL)",
        },
        {
            "diode_type": "rectifier",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "m7",
            "name_short": "Rectifier Diode M7 (SMA)",
        },
        {
            "diode_type": "fast_recovery",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "us1m",
            "name_short": "Fast-Recovery Diode US1M (SMA)",
        },
        {
            "diode_type": "schottky",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "ss14",
            "name_short": "Schottky Diode SS14 (SMA)",
        },
        {
            "diode_type": "schottky",
            "package": "sod_123",
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "b5819w_sl",
            "name_short": "Schottky Diode B5819W SL (SOD-123)",
        },
        {
            "diode_type": "schottky",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "ss34",
            "name_short": "Schottky Diode SS34 (SMA)",
        },
        {
            "diode_type": "schottky",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "ss210",
            "name_short": "Schottky Diode SS210 (SMA)",
        },
        {
            "diode_type": "schottky",
            "package": "sma",
            "manufacturer": "mdd_microdiode_semiconductor",
            "part_number": "ss54",
            "name_short": "Schottky Diode SS54 (SMA)",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "manufacturer": "guangdong_hottech",
            "part_number": "1n5819ws",
            "name_short": "Schottky Diode 1N5819WS (SOD-323)",
        },
        {
            "diode_type": "schottky",
            "package": "0402",
            "manufacturer": "",
            "part_number": "",
            "name_short": "Schottky Diode 0402 (generic)",
        },
        {"diode_type": "tvs_array", "package": "sot_143", "manufacturer": "littelfuse",
         "part_number": "sp0503bahtg", "name_short": "ESD Array SP0503BAHTG"},
        {
            "diode_type": "tvs_array",
            "package": "sot_23_6",
            "manufacturer": "protek",
            "part_number": "srv054pt7",
        },
        {
            "diode_type": "tvs_array",
            "package": "sot_23",
            "manufacturer": "protek",
            "part_number": "psm712_lf_t7",
            "name_short": "RS-485 TVS Array PSM712-LF-T7",
        },
        {
            "diode_type": "switching",
            "package": "sod_523f",
            "manufacturer": "onsemi",
            "part_number": "1n4148wt",
            "name_short": "Switching Diode 1N4148WT",
        },
        {
            "diode_type": "switching",
            "package": "sod_323",
            "manufacturer": "onsemi",
            "part_number": "1n4148ws",
            "name_short": "Switching Diode 1N4148WS",
        },
        {
            "diode_type": "switching",
            "package": "sod_123",
            "manufacturer": "onsemi",
            "part_number": "1n4148w",
            "name_short": "Switching Diode 1N4148W",
        },
        {
            "diode_type": "switching",
            "package": "sod_123",
            "manufacturer": "st_semtech",
            "part_number": "1n4148w",
            "name_short": "Switching Diode 1N4148W",
        },
        {
            "diode_type": "switching_dual_series",
            "package": "sot_23",
            "manufacturer": "nexperia",
            "part_number": "bav99_215",
            "name_short": "Dual Switching Diode BAV99,215 (SOT-23)",
        },
        {
            "diode_type": "switching_dual_common_cathode",
            "package": "sot_23",
            "manufacturer": "jiangsu_changjing_electronics_technology_co_ltd",
            "part_number": "bav70",
            "name_short": "Dual Switching Diode BAV70 (SOT-23)",
        },
        {
            "diode_type": "schottky_dual_common_cathode",
            "package": "sot_523",
            "manufacturer": "diodes_incorporated",
            "part_number": "bas40t_05",
            "name_short": "Dual Schottky Diode BAS40T-05",
        },
        {
            "diode_type": "schottky",
            "package": "sod_123",
            "part_number": "ss14",
            "name_short": "Schottky Diode SOD-123",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "part_number": "bat54w",
            "name_short": "Schottky Diode SOD-323",
        },
        {
            "diode_type": "schottky",
            "package": "sod_523",
            "part_number": "1ss400",
            "name_short": "Schottky Diode SOD-523",
        },
        # SparkFun-specific diodes/protection
        {
            "diode_type": "tvs",
            "package": "sot_353",
            "manufacturer": "toshiba",
            "part_number": "df5a5_6lfu",
            "name_short": "TVS Diode DF5A5.6LFU",
        },
        {
            "diode_type": "tvs",
            "package": "smb",
            "manufacturer": "brightking",
            "part_number": "p6smb6_8ca_tr13",
            "name_short": "Bidirectional TVS Diode P6SMB6.8CA/TR13",
        },
        {
            "diode_type": "tvs",
            "package": "smb",
            "manufacturer": "hongjiacheng",
            "part_number": "smbj6_5ca",
            "name_short": "Bidirectional TVS Diode SMBJ6.5CA",
        },
        {
            "diode_type": "esd",
            "package": "0402",
            "manufacturer": "littelfuse",
            "part_number": "pesd0402",
            "name_short": "ESD Suppressor PESD0402",
        },
        {
            "diode_type": "esd_array",
            "package": "sot_353",
            "manufacturer": "nexperia",
            "part_number": "pesd3v3l4ug",
            "name_short": "ESD Array PESD3V3L4UG",
        },
        {
            "diode_type": "tvs_array",
            "package": "sot_26",
            "manufacturer": "diodes_incorporated",
            "part_number": "dt1042_04so",
            "name_short": "TVS Array DT1042-04SO",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "manufacturer": "infineon",
            "part_number": "bat60a",
            "name_short": "Schottky Diode BAT60A",
        },
        {
            "diode_type": "tvs_array",
            "package": "sot_143",
            "manufacturer": "nxp",
            "part_number": "prtr5v0u2x",
            "name_short": "USB ESD Protection PRTR5V0U2X",
        },
        {
            "diode_type": "schottky",
            "package": "sod_323",
            "manufacturer": "infineon",
            "part_number": "bat20j",
            "name_short": "Schottky Diode BAT20J",
        },
    ]

    for diode in diodes:
        option = {}
        option["taxonomy_2"] = "diode"
        option["taxonomy_3"] = diode["diode_type"]
        option["taxonomy_4"] = diode["package"]
        option["taxonomy_14"] = diode.get("manufacturer", "")
        option["taxonomy_15"] = diode["part_number"]
        if "name_short" in diode:
            option["name_short"] = diode["name_short"]
        options.append(option)


if __name__ == "__main__":
    main()
