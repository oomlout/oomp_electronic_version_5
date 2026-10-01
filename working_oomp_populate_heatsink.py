def main(**kwargs):
    options = kwargs.get("options", [])

    # First heat sinks in the population: XSD through-hole TO-220 style
    # extruded aluminium coolers from the JLC house-parts queue.  taxonomy_3
    # carries the body dimensions in millimetres as printed on the page
    # (MPN is the same dimension string).
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "50_18_21",
        "taxonomy_14": "xsd", "taxonomy_15": "50_18_21",
        "name_short": "Heat Sink 50x18x21 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "15_5_10_5_21",
        "taxonomy_14": "xsd", "taxonomy_15": "15_5_10_5_21",
        "name_short": "Heat Sink 15.5x10.5x21 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "22_10_25",
        "taxonomy_14": "xsd", "taxonomy_15": "22_10_25",
        "name_short": "Heat Sink 22x10x25 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "32_7_22",
        "taxonomy_14": "xsd", "taxonomy_15": "32_7_22",
        "name_short": "Heat Sink 32x7x22 mm (XSD)",
    })

    # Second batch of XSD heat sinks.  C4663's page lists a through-hole
    # package; the other pages leave Package blank like the first batch.
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "23_5_16_25",
        "taxonomy_14": "xsd", "taxonomy_15": "23_5_16_25",
        "name_short": "Heat Sink 23.5x16x25 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "35_12_25",
        "taxonomy_14": "xsd", "taxonomy_15": "35_12_25",
        "name_short": "Heat Sink 35x12x25 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "23_16_20",
        "taxonomy_14": "xsd", "taxonomy_15": "23_16_20",
        "name_short": "Heat Sink 23x16x20 mm (XSD)",
    })

    # Third batch of XSD heat sinks.
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "35_15_35",
        "taxonomy_14": "xsd", "taxonomy_15": "35_15_35",
        "name_short": "Heat Sink 35x15x35 mm (XSD)",
    })
    options.append({
        "taxonomy_2": "heatsink", "taxonomy_3": "30_25_25",
        "taxonomy_14": "xsd", "taxonomy_15": "30_25_25",
        "name_short": "Heat Sink 30x25x25 mm (XSD)",
    })


if __name__ == "__main__":
    main()
