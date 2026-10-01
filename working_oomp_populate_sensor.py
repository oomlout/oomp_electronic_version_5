def main(**kwargs):
    options = kwargs.get("options", [])

    # Soldered/e-radionica sensor components identified from their breakouts.
    # The MQ series shares one footprint; boards carrying a specific gas
    # sensor can override to an exact MQ part later.
    options.append({
        "taxonomy_2": "sensor", "taxonomy_3": "mq", "taxonomy_4": "6_pin",
        "name_short": "MQ Gas Sensor (MQ series, 6-pin)",
    })
    options.append({
        "taxonomy_2": "sensor", "taxonomy_3": "tcrt5000", "taxonomy_4": "4_pin",
        "taxonomy_14": "vishay", "taxonomy_15": "tcrt5000l",
        "name_short": "Reflective Optical Sensor TCRT5000L",
    })
    options.append({
        "taxonomy_2": "sensor", "taxonomy_3": "pir", "taxonomy_4": "3_pin",
        "taxonomy_15": "am312",
        "name_short": "PIR Motion Sensor AM312",
    })
    options.append({
        "taxonomy_2": "sensor", "taxonomy_3": "apds_9960",
        "taxonomy_14": "broadcom", "taxonomy_15": "apds_9960",
        "name_short": "Gesture/Proximity Sensor APDS-9960",
    })
    options.append({
        "taxonomy_2": "antenna", "taxonomy_3": "3216", "taxonomy_4": "surface_mount",
        "taxonomy_5": "ceramic", "taxonomy_14": "yageo", "taxonomy_15": "ant3216ll00r2400a",
        "name_short": "Ceramic Antenna ANT3216LL00R2400A",
    })
    options.append({
        "taxonomy_2": "buzzer", "taxonomy_3": "surface_mount", "taxonomy_14": "mu_rata",
        "taxonomy_15": "mlt_8530", "name_short": "SMD Buzzer MLT-8530",
    })
    options.append({
        "taxonomy_2": "buzzer", "taxonomy_3": "surface_mount", "taxonomy_14": "hydz",
        "taxonomy_15": "hyg9605b", "name_short": "HYDZ HYG-9605B 5V SMD Magnetic Buzzer",
    })

    # First through-hole buzzers: Jiangsu Huaneng 23 mm and 30 mm active
    # piezo buzzers (built-in driving circuit) from the JLC house-parts
    # queue.  The HND-3015B page leaves Package blank; its 30 mm leaded
    # body is classified through-hole pending integration-stage datasheet
    # verification.
    options.append({
        "taxonomy_2": "buzzer", "taxonomy_3": "through_hole", "taxonomy_14": "jiangsu_huaneng_elec",
        "taxonomy_15": "hnd_2310b", "name_short": "Active Piezo Buzzer HND-2310B (23 mm)",
    })
    options.append({
        "taxonomy_2": "buzzer", "taxonomy_3": "through_hole", "taxonomy_14": "jiangsu_huaneng_elec",
        "taxonomy_15": "hnd_2319", "name_short": "Active Piezo Buzzer HND-2319 (23 mm)",
    })
    options.append({
        "taxonomy_2": "buzzer", "taxonomy_3": "through_hole", "taxonomy_14": "jiangsu_huaneng_elec",
        "taxonomy_15": "hnd_3015b", "name_short": "Active Piezo Buzzer HND-3015B (30 mm)",
    })

    # First NTC thermistor: RUILON 10D-9 inrush-current limiter (10 ohm at
    # 25 C, 1 A steady state, 7.5 mm lead pitch).
    options.append({
        "taxonomy_2": "ntc_thermistor", "taxonomy_3": "through_hole", "taxonomy_4": "10_ohm",
        "taxonomy_5": "1_a", "taxonomy_14": "ruilon", "taxonomy_15": "ntc_10d_9",
        "name_short": "NTC Inrush Limiter 10D-9 (10 ohm, 1A)",
    })
    options.append({
        "taxonomy_2": "ntc_thermistor", "taxonomy_3": "through_hole", "taxonomy_4": "5_ohm",
        "taxonomy_5": "2_a", "taxonomy_14": "ruilon", "taxonomy_15": "ntc_5d_7",
        "name_short": "NTC Inrush Limiter 5D-7 (5 ohm, 2A)",
    })

    # First optical sensors: Everlight slot photointerrupters, through-hole
    # phototransistors, a Vishay IR remote receiver and an OSRAM photodiode
    # from the JLC house-parts queue.
    options.append({
        "taxonomy_2": "photointerrupter", "taxonomy_3": "dip_4",
        "taxonomy_14": "everlight", "taxonomy_15": "itr8105",
        "name_short": "Slot Photointerrupter ITR8105",
    })
    options.append({
        "taxonomy_2": "photointerrupter", "taxonomy_3": "dip_4",
        "taxonomy_14": "everlight", "taxonomy_15": "itr8402_a",
        "name_short": "Slot Photointerrupter ITR8402-A",
    })
    options.append({
        "taxonomy_2": "phototransistor", "taxonomy_3": "through_hole", "taxonomy_4": "3_mm",
        "taxonomy_14": "everlight", "taxonomy_15": "pt204_6b",
        "name_short": "IR Phototransistor PT204-6B (3mm)",
    })
    options.append({
        "taxonomy_2": "phototransistor", "taxonomy_3": "through_hole", "taxonomy_4": "5_mm",
        "taxonomy_14": "everlight", "taxonomy_15": "pt333_3b",
        "name_short": "IR Phototransistor PT333-3B (5mm)",
    })
    options.append({
        "taxonomy_2": "ir_receiver", "taxonomy_3": "sip_3", "taxonomy_4": "36_khz",
        "taxonomy_14": "vishay_intertech", "taxonomy_15": "tsop4836",
        "name_short": "IR Remote Receiver TSOP4836 (36kHz)",
    })
    options.append({
        "taxonomy_2": "photodiode", "taxonomy_3": "surface_mount", "taxonomy_4": "3_7_x_4_5_mm",
        "taxonomy_14": "osram_opto_semiconductors", "taxonomy_15": "bpw34fs",
        "name_short": "Photodiode BPW34FS (SMD 3.7x4.5mm)",
    })

    # Sensor/module identities from the expanded unmatched-project report.
    # They are intentionally population-only placeholders until the exact
    # datasheet and mechanical records are completed from the ledger.
    unmatched_sensors = [
        ["imu", "lga_24", "st", "lsm9ds1tr", "LSM9DS1TR IMU"],
        ["air_quality", "lga_20", "ams", "ccs811b_jopr", "CCS811B-JOPR Air Quality Sensor"],
        ["light_proximity", "ch_6", "liteon", "ltr_507als_01", "LTR-507ALS-01 Light Sensor"],
        ["pressure_temperature", "lga_10", "bosch", "bmp388", "BMP388 Pressure Sensor"],
        ["gnss", "module", "quectel", "l86_m33", "Quectel L86-M33 GNSS Module"],
        ["accelerometer", "lga_14", "analog_devices", "adxl345", "ADXL345 Accelerometer"],
        ["accelerometer", "lga_14", "analog_devices", "adxl343", "ADXL343 Accelerometer"],
        ["accelerometer", "lga_16", "st", "lis3dhtr", "LIS3DHTR Accelerometer"],
        ["gnss", "module", "u_blox", "sam_m8q", "u-blox SAM-M8Q GNSS Module"],
        ["gnss", "module", "u_blox", "dan_f10n", "u-blox DAN-F10N GNSS Module"],
        ["gnss", "module", "u_blox", "neo_f10n", "u-blox NEO-F10N GNSS Module"],
        ["particulate_matter", "module", "bosch", "bmv080", "Bosch BMV080 Particulate Matter Sensor"],
    ]
    for sensor_type, package, manufacturer, part_number, name_short in unmatched_sensors:
        options.append({
            "taxonomy_2": "sensor",
            "taxonomy_3": sensor_type,
            "taxonomy_4": package,
            "taxonomy_14": manufacturer,
            "taxonomy_15": part_number,
            "name_short": name_short,
        })


if __name__ == "__main__":
    main()
