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


if __name__ == "__main__":
    main()
