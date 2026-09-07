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
