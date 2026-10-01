def main(**kwargs):
    options = kwargs.get("options", [])

    sizes = ["0402"]
    capacitance_values = [
        "8_pico_farad",
        "15_pico_farad",
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "33_pico_farad",
        "120_pico_farad",
        "10_nano_farad",
        "22_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "2_2_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    # The Basic 0402 1 nF house part C1523 fills this missing generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "220_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_7_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "100_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "12_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "47_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "220_nano_farad",
    })
    # JLC Basic C32949 supplies this previously absent 0402 value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "10_pico_farad",
    })

    # Extended house part C1527 supplies this previously absent 0402 value
    # (FH 0402B151K500NT, 150 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "150_pico_farad",
    })

    # Extended house part C1528 supplies this previously absent 0402 value
    # (FH 0402B161K500NT, 160 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "160_pico_farad",
    })

    # Extended house part C1529 supplies this previously absent 0402 value
    # (FH 0402B201K500NT, 200 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "200_pico_farad",
    })

    # Extended house part C1531 supplies this previously absent 0402 value
    # (FH 0402B222K500NT, 2.2 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "2_2_nano_farad",
    })

    # Extended house part C1533 supplies this previously absent 0402 value
    # (FH 0402B271K500NT, 270 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "270_pico_farad",
    })

    # Extended house part C1534 supplies this previously absent 0402 value
    # (FH 0402B301K500NT, 300 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "300_pico_farad",
    })

    # Extended house part C1535 supplies this previously absent 0402 value
    # (FH 0402B331K500NT, 330 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "330_pico_farad",
    })

    # Extended house part C1537 supplies this previously absent 0402 value
    # (FH 0402B471K500NT, 470 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "470_pico_farad",
    })

    # Extended house part C1539 supplies this previously absent 0402 value
    # (FH 0402B561K500NT, 560 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "560_pico_farad",
    })

    # Extended house part C1540 supplies this previously absent 0402 value
    # (FH 0402B562K500NT, 5.6 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "5_6_nano_farad",
    })

    # Extended house part C1541 supplies this previously absent 0402 value
    # (FH 0402B681K500NT, 680 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "680_pico_farad",
    })

    # Extended house part C1542 supplies this previously absent 0402 value
    # (FH 0402B682K500NT, 6.8 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "6_8_nano_farad",
    })

    # Extended house part C1543 supplies this previously absent 0402 value
    # (FH 0402B821K500NT, 820 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "820_pico_farad",
    })

    # Extended house part C1544 supplies this previously absent 0402 value
    # (FH 0402CG0R5C500NT, 0.5 pF 50 V C0G, the first reviewed choice; a
    # SparkFun Artemis project reference already proposes this exact ID).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "0_5_pico_farad",
    })

    # Extended house part C1550 supplies this previously absent 0402 value
    # (FH 0402CG1R0C500NT, 1 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_pico_farad",
    })

    # Extended house part C1551 supplies this previously absent 0402 value
    # (FH 0402CG1R2C500NT, 1.2 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_2_pico_farad",
    })

    # Extended house part C1553 supplies this previously absent 0402 value
    # (FH 0402CG1R8C500NT, 1.8 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_8_pico_farad",
    })

    # Extended house part C1559 supplies this previously absent 0402 value
    # (FH 0402CG2R2C500NT, 2.2 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "2_2_pico_farad",
    })

    # Extended house part C1564 supplies this previously absent 0402 value
    # (FH 0402CG3R0C500NT, 3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "3_pico_farad",
    })

    # Extended house part C1565 supplies this previously absent 0402 value
    # (FH 0402CG3R3C500NT, 3.3 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "3_3_pico_farad",
    })

    # Extended house part C1566 supplies this previously absent 0402 value
    # (FH 0402CG3R9C500NT, 3.9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "3_9_pico_farad",
    })

    # Extended house part C1568 supplies this previously absent 0402 value
    # (FH 0402CG4R0C500NT, 4 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_pico_farad",
    })

    # Extended house part C1569 supplies this previously absent 0402 value
    # (FH 0402CG4R7C500NT, 4.7 pF 50 V C0G, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_7_pico_farad",
    })

    # Extended house part C1573 supplies this previously absent 0402 value
    # (FH 0402CG5R0C500NT, 5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "5_pico_farad",
    })

    # Extended house part C1574 supplies this previously absent 0402 value
    # (FH 0402CG5R6C500NT, 5.6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "5_6_pico_farad",
    })

    # Extended house part C1575 supplies this previously absent 0402 value
    # (FH 0402CG6R0C500NT, 6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "6_pico_farad",
    })

    # Extended house part C1576 supplies this previously absent 0402 value
    # (FH 0402CG6R8C500NT, 6.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 6.8 nF
    # generic supplied by C1542).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "6_8_pico_farad",
    })

    # Extended house part C1577 supplies this previously absent 0402 value
    # (FH 0402CG7R0C500NT, 7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "7_pico_farad",
    })

    # Extended house part C1579 supplies this previously absent 0402 value
    # (FH 0402CG8R2C500NT, 8.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "8_2_pico_farad",
    })

    # Extended house part C1580 supplies this previously absent 0402 value
    # (FH 0402CG9R0C500NT, 9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "9_pico_farad",
    })

    # Extended house part C1583 supplies this previously absent 0402 value
    # (FH 0402F153M500NT, 15 nF 50 V Y5V +/-20%, the first reviewed choice;
    # listing showed stock 2 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "15_nano_farad",
    })

    # Extended house part C1556 supplies this previously absent 0402 value
    # (FH 0402CG250J500NT, 25 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "25_pico_farad",
    })

    # Extended house part C1563 supplies this previously absent 0402 value
    # (FH 0402CG390J500NT, 39 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "39_pico_farad",
    })

    # Extended house part C1571 supplies this previously absent 0402 value
    # (FH 0402CG510J500NT, 51 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "51_pico_farad",
    })

    # Extended house part C1572 supplies this previously absent 0402 value
    # (FH 0402CG560J500NT, 56 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "56_pico_farad",
    })

    # Extended house part C1536 supplies this previously absent 0402 value
    # (FH 0402B332K500NT, 3.3 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "3_3_nano_farad",
    })

    # C23733 is +/-20%; retain the existing generic 0402 4.7 uF purchase
    # choice at +/-10% and add this explicit rated/tolerance variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "10_volt",
        "taxonomy_6": "20_percent",
    })

    # Keep the existing 16 V 100 nF generic preference and represent the
    # JLC Basic 50 V choice as a rated purchasing variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "50_volt",
    })

    # C1524 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0402 10 nF value (50 V, X7R, +/-10%). The reviewed
    # Samsung Basic preference C15195 keeps the plain generic ID, so this
    # exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy (as with the Samsung C1591 row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "10_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0402b103k500nt",
    })

    # C1545 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0402 10 pF value (50 V, C0G, +/-5%). The reviewed
    # Samsung Basic preference C32949 keeps the plain generic ID, so this
    # exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy (as with the Samsung C1591 and
    # C1524 rows).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "10_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0402cg100j500nt",
    })

    # C1581 is the FH (Guangdong Fenghua Advanced Tech) purchasing SKU for the
    # generic 0402 100 nF 50 V value, but with a Y5V +/-20% dielectric unlike
    # the reviewed Samsung X7R +/-10% Basic preference C307331 on the
    # _50_volt generic. This exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy (as with the
    # Samsung C1591, C1524 and C1545 rows); it must not replace the X7R
    # preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0402f104m500nt",
    })

    # C1584 is the FH (Guangdong Fenghua Advanced Tech) purchasing SKU for the
    # generic 0402 22 nF value, but with a Y5V +/-20% dielectric unlike the
    # verified Basic X7R +/-10% preference C1532 on the plain generic. This
    # exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy; it must not replace the X7R
    # preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "22_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0402f223m500nt",
    })

    # Extended house part C1552 supplies this previously absent 0402 value
    # (FH 0402CG1R5C500NT, 1.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_5_pico_farad",
    })

    # Extended house part C1558 supplies this previously absent 0402 value
    # (FH 0402CG2R0C500NT, 2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "2_pico_farad",
    })

    # Extended house part C1560 supplies this previously absent 0402 value
    # (FH 0402CG2R5C500NT, 2.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "2_5_pico_farad",
    })

    # Extended house part C1561 supplies this previously absent 0402 value
    # (FH 0402CG2R7C500NT, 2.7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "2_7_pico_farad",
    })

    # Extended house part C1570 supplies this previously absent 0402 value
    # (FH 0402CG300J500NT, 30 pF 50 V C0G +/-5%, the first reviewed choice;
    # 30 pF previously existed only as a 0603 generic).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "30_pico_farad",
    })

    sizes = ["0603"]
    capacitance_values = [
        "10_pico_farad",
        "18_pico_farad",
        "22_pico_farad",
        "27_pico_farad",
        "33_pico_farad",
        "47_pico_farad",
        "470_pico_farad",
        "2_2_nano_farad",
        "10_nano_farad",
        "100_nano_farad",
        "1_micro_farad",
        "2_2_micro_farad",
        "4_7_micro_farad",
        "10_micro_farad",
        "22_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    # Keep the generic C14663 preference intact while giving the exact Samsung
    # C1591 purchasing identity its own linked OOMP record.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10b104kb8nnnc",
    })

    # C1589 is the Samsung equivalent-spec SKU for the generic 0603 10 nF
    # value (50 V, X7R, +/-10%). The reviewed Basic preference C57112
    # (FH 0603B103K500NT) keeps the plain generic ID, so this exact
    # purchasing identity gets its own linked row following the established
    # maker/mpn variant taxonomy (as with the Samsung C1591 row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "10_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10b103kb8nnnc",
    })

    # Keep the reviewed 50 V generic 0603 1 uF choice intact and represent
    # Samsung C1592's lower 16 V rating as an explicit linked variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # C1607 is Samsung's 10 V 0603 2.2 uF X5R +/-10% SKU. The generic 0603
    # 2.2 uF preference (C23630, 16 V) stays intact; this lower-voltage
    # purchasing identity is an explicit linked rated variant following the
    # C1592 16 V and C1590 25 V precedents.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_2_micro_farad",
        "taxonomy_5": "10_volt",
    })

    # Extended house part C1608 supplies this previously absent 0603 value
    # (FH 0603B271K500NT, 270 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "270_pico_farad",
    })

    # Extended house part C1609 supplies this previously absent 0603 value
    # (FH 0603B272K500NT, 2.7 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 2.7 pF C0G generic supplied by C1561).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_7_nano_farad",
    })

    # Extended house part C1656 (Samsung CL10C270JB8NNNC) verified as the
    # first reviewed preferred extended purchasing choice for the in-grid
    # generic 0603 27 pF value; the pre-existing YAGEO C107045 LCSC-only
    # supply is preserved as a prior alternative.

    # C1657 is the Samsung C0G +/-5% SKU for the generic 0603 270 pF value.
    # The X7R +/-10% preference C1608 on the plain generic ID keeps it, so
    # this exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy; the C0G option must not
    # silently replace the X7R preference either.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "270_pico_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10c271jb8nnnc",
    })

    # C1688 is the Samsung Y5V -20/+80% SKU for the generic 0603 100 nF
    # value. The reviewed 50 V X7R +/-10% preference C14663 (and the Samsung
    # X7R C1591 variant) on the plain generic ID keep it, so this exact
    # purchasing identity gets its own linked row following the established
    # maker/mpn variant taxonomy; the Y5V option must not silently replace
    # the X7R preferences.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10f104zb8nnnc",
    })

    # C1691 is Samsung's 6.3 V +/-20% 0603 10 uF X5R SKU. The reviewed Basic
    # 10 V +/-10% preference C19702 on the plain generic ID (and the 25 V
    # +/-20% rated variant C96446) keep their IDs, so this exact purchasing
    # identity gets its own linked rated row following the established
    # 25_volt_20_percent taxonomy; the 6.3 V option must not silently
    # replace the higher-voltage choices.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "6_3_volt_20_percent",
    })

    # C1692 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 12 nF value. The X7R +/-10% preference C1593 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "12_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f123m500nt",
    })

    # C1694 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 150 nF value. The X7R +/-10% preference C1597 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "150_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f154m500nt",
    })

    # C1696 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 20 nF value. The X7R +/-10% preference C1602 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "20_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f203m500nt",
    })

    # C1697 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 22 nF value. The X7R +/-10% preference C1532 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "22_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f223m500nt",
    })

    # C1698 is the Samsung Y5V -20/+80% SKU for the generic 0603 220 nF
    # value. The reviewed Basic X7R +/-10% 25 V preference C21120 (and the
    # FH X7R variant C1606) keep their IDs, so this exact purchasing
    # identity gets its own linked row following the established maker/mpn
    # variant taxonomy; the Y5V option must not silently replace the X7R
    # preferences.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "220_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10f224zb8nnnc",
    })

    # C1711 is the Samsung equivalent-spec 50 V SKU for the generic 0805
    # 100 nF 50 V value. The reviewed Basic preference C49678 (YAGEO
    # CC0805KRX7R9BB104) keeps the plain 50_volt generic ID, so this exact
    # purchasing identity gets its own linked row following the established
    # maker/mpn variant taxonomy (as with the Samsung C1591 row on 0603).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl21b104kbcnnnc",
    })

    # C1712 is the Samsung 25 V SKU for the generic 0805 1 uF value. The
    # reviewed Basic 50 V preference C28323 (CL21B105KBFNNNE) keeps the
    # plain generic ID, so this lower-voltage purchasing identity gets its
    # own linked rated row following the established rated variant taxonomy
    # (16_volt/25_volt precedent).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_micro_farad",
        "taxonomy_5": "25_volt",
    })

    # C1713 is Samsung's 16 V 0805 10 uF X5R +/-10% SKU. The reviewed Basic
    # 25 V preference C15850 (CL21A106KAYNNNE) on the plain generic ID and
    # the 50 V rated variant keep their IDs, so this lower-voltage
    # purchasing identity gets its own linked rated row following the
    # established rated variant taxonomy; the 16 V option must not silently
    # replace the higher-voltage choices.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # Extended house part C1714 supplies this previously absent 0805 value
    # (FH 0805B122K500NT, 1.2 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 1.2 nF generic supplied by C1551).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_2_nano_farad",
    })

    # Extended house part C1715 supplies this previously absent 0805 value
    # (FH 0805B123K500NT, 12 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 12 nF generic supplied by C1593).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "12_nano_farad",
    })

    # Extended house part C1716 supplies this previously absent 0805 value
    # (FH 0805B151K500NT, 150 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "150_pico_farad",
    })

    # C1795 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 150 pF value (50 V). The reviewed X7R +/-10%
    # preference C1716 (FH 0805B151K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "150_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg151j500nt",
    })

    # Extended house part C1796 supplies this previously absent 0805 value
    # (FH 0805CG160J500NT, 16 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 16 pF generic supplied by C1646).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "16_pico_farad",
    })

    # Extended house part C1797 supplies this previously absent 0805 value
    # (FH 0805CG180J500NT, 18 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the in-grid 0402 18 pF generic and the 0603 18 pF
    # generic supplied by C1647).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "18_pico_farad",
    })

    # C1799 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 200 pF value (50 V). The reviewed X7R +/-10%
    # preference C1724 (FH 0805B201K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "200_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg201j500nt",
    })

    # Extended house part C1800 supplies this previously absent 0805 value
    # (FH 0805CG2R0C500NT, 2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 2 pF generics supplied by C1558 and C1650).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_pico_farad",
    })

    # Extended house part C1801 supplies this previously absent 0805 value
    # (FH 0805CG2R2C500NT, 2.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 2.2 pF generics supplied by C1559 and C1651).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_2_pico_farad",
    })

    # Extended house part C1802 supplies this previously absent 0805 value
    # (FH 0805CG2R5C500NT, 2.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 2.5 pF generics supplied by C1560 and C1652).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_5_pico_farad",
    })

    # Extended house part C1803 supplies this previously absent 0805 value
    # (FH 0805CG2R7C500NT, 2.7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 2.7 pF
    # generic supplied by C1561).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_7_pico_farad",
    })

    # C1805 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 220 pF value (50 V). The reviewed Yageo X7R +/-10%
    # preference C107145 (CC0805KRX7R9BB221) on the plain generic ID keeps
    # it and the FH X7R variant C1727 (0805B221K500NT) already exists, so
    # this exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg221j500nt",
    })

    # Extended house part C1806 supplies this previously absent 0805 value
    # (FH 0805CG240J500NT, 24 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 24 pF generic supplied by C1654).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "24_pico_farad",
    })

    # Extended house part C1807 supplies this previously absent 0805 value
    # (FH 0805CG250J500NT, 25 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 25 pF generics supplied by C1556 and
    # C1655).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "25_pico_farad",
    })

    # Extended house part C1808 supplies this previously absent 0805 value
    # (FH 0805CG270J500NT, 27 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the in-grid 0402 27 pF generic and the 0603 27 pF
    # generic supplied by C1656).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "27_pico_farad",
    })

    # Extended house part C1810 supplies this previously absent 0805 value
    # (FH 0805CG3R0C500NT, 3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 3 pF generic
    # supplied by C1564).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_pico_farad",
    })

    # Extended house part C1811 supplies this previously absent 0805 value
    # (FH 0805CG3R3C500NT, 3.3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 3.3 pF generics supplied by C1565 and C1660).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_3_pico_farad",
    })

    # Extended house part C1812 supplies this previously absent 0805 value
    # (FH 0805CG3R6C500NT, 3.6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0603 3.6 pF
    # generic supplied by C1661).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_6_pico_farad",
    })

    # Extended house part C1813 supplies this previously absent 0805 value
    # (FH 0805CG3R9C500NT, 3.9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 3.9 pF generics supplied by C1566 and C1662).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_9_pico_farad",
    })

    # C1815 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 330 pF value (50 V). The reviewed X7R +/-10%
    # preference C1737 (FH 0805B331K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "330_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg331j500nt",
    })

    # Extended house part C1816 supplies this previously absent 0805 value
    # (FH 0805CG360J500NT, 36 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 36 pF generic supplied by C1665).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "36_pico_farad",
    })

    # Extended house part C1817 supplies this previously absent 0805 value
    # (FH 0805CG390J500NT, 39 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 39 pF generics supplied by C1563 and
    # C1666).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "39_pico_farad",
    })

    # C1818 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 390 pF value (50 V). The reviewed X7R +/-10%
    # preference C1741 (FH 0805B391K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "390_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg391j500nt",
    })

    # Extended house part C1819 supplies this previously absent 0805 value
    # (FH 0805CG4R0C500NT, 4 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 4 pF generics supplied by C1568 and C1668).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "4_pico_farad",
    })

    # Extended house part C1820 supplies this previously absent 0805 value
    # (FH 0805CG4R7C500NT, 4.7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 4.7 pF generics supplied by C1569 and C1669).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "4_7_pico_farad",
    })

    # C1822 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 470 pF value (50 V). The reviewed X7R +/-10%
    # preference C1743 (FH 0805B471K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg471j500nt",
    })

    # Extended house part C1823 supplies this previously absent 0805 value
    # (FH 0805CG500J500NT, 50 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 50 pF generic supplied by C1672).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "50_pico_farad",
    })

    # Extended house part C1824 supplies this previously absent 0805 value
    # (FH 0805CG5R0C500NT, 5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 5 pF generics supplied by C1573 and C1673).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "5_pico_farad",
    })

    # Extended house part C1825 supplies this previously absent 0805 value
    # (FH 0805CG5R1C500NT, 5.1 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; no 5.1 pF generic exists in any
    # other package).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "5_1_pico_farad",
    })

    # Extended house part C1826 supplies this previously absent 0805 value
    # (FH 0805CG5R6C500NT, 5.6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 5.6 pF generics supplied by C1574 and C1674).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "5_6_pico_farad",
    })

    # Extended house part C1827 supplies this previously absent 0805 value
    # (FH 0805CG510J500NT, 51 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 51 pF generics supplied by C1571 and
    # C1675).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "51_pico_farad",
    })

    # Extended house part C1828 supplies this previously absent 0805 value
    # (FH 0805CG560J500NT, 56 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 56 pF generics supplied by C1572 and
    # C1676).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "56_pico_farad",
    })

    # C1829 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 560 pF value (50 V). The reviewed X7R +/-10%
    # preference C1751 (FH 0805B561K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "560_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg561j500nt",
    })

    # Extended house part C1831 supplies this previously absent 0805 value
    # (FH 0805CG6R2C500NT, 6.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0603 6.2 pF
    # generic supplied by C1678).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "6_2_pico_farad",
    })

    # Extended house part C1832 supplies this previously absent 0805 value
    # (FH 0805CG6R8C500NT, 6.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 6.8 pF generics supplied by C1576 and C1679).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "6_8_pico_farad",
    })

    # Extended house part C1833 supplies this previously absent 0805 value
    # (FH 0805CG620J500NT, 62 pF 50 V C0G +/-5%, the first reviewed choice;
    # no 62 pF generic exists in any other package).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "62_pico_farad",
    })

    # Extended house part C1834 supplies this previously absent 0805 value
    # (FH 0805CG680J500NT, 68 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 68 pF generic supplied by C1680).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "68_pico_farad",
    })

    # C1835 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 680 pF value (50 V). The reviewed X7R +/-10%
    # preference C1754 (FH 0805B681K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "680_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg681j500nt",
    })

    # Extended house part C1836 supplies this previously absent 0805 value
    # (FH 0805CG7R0C500NT, 7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 7 pF generics supplied by C1577 and C1682).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "7_pico_farad",
    })

    # Extended house part C1837 supplies this previously absent 0805 value
    # (FH 0805CG7R5C500NT, 7.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; no 7.5 pF generic exists in any
    # other package).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "7_5_pico_farad",
    })

    # Extended house part C1838 supplies this previously absent 0805 value
    # (FH 0805CG750J500NT, 75 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 75 pF generic supplied by C1681).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "75_pico_farad",
    })

    # Extended house part C1839 supplies this previously absent 0805 value
    # (FH 0805CG8R0C500NT, 8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the in-grid 0402 8 pF
    # generic supplied by C1578).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "8_pico_farad",
    })

    # Extended house part C1840 supplies this previously absent 0805 value
    # (FH 0805CG8R2C500NT, 8.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 8.2 pF generics supplied by C1579 and C1685).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "8_2_pico_farad",
    })

    # Extended house part C1841 supplies this previously absent 0805 value
    # (FH 0805CG820J500NT, 82 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 82 pF generic supplied by C1683).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "82_pico_farad",
    })

    # C1842 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 0805 820 pF value (50 V). The reviewed X7R +/-10%
    # preference C1757 (FH 0805B821K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "820_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805cg821j500nt",
    })

    # Extended house part C1843 supplies this previously absent 0805 value
    # (FH 0805CG910J500NT, 91 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 91 pF generic supplied by C1686).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "91_pico_farad",
    })

    # Extended house part C1844 supplies this previously absent 0805 value
    # (FH 0805CG9R0C500NT, 9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 9 pF generic
    # supplied by C1580).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "9_pico_farad",
    })

    # Extended house part C1845 supplies this previously absent plain 1206
    # value (FH 1206B102K500NT, 1 nF 50 V X7R +/-10%, the first reviewed
    # choice; distinct from the 1206 1 nF 2000 V variant supplied by
    # C9196).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
    })

    # C1849 is Samsung's 16 V 1206 10 uF X5R +/-10% SKU. The generic 1206
    # 10 uF preference (C13585, 50 V) stays intact; this lower-voltage
    # purchasing identity is an explicit linked rated variant following the
    # established rated-variant taxonomy (as with the C1592 16 V row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # Extended house part C1850 supplies this previously absent 1206 value
    # (FH 1206B151K500NT, 150 pF 50 V X7R +/-10%, the first reviewed choice;
    # listing showed stock 9 at capture time, which does not change
    # identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "150_pico_farad",
    })

    # Extended house part C1851 supplies this previously absent 1206 value
    # (FH 1206B152K500NT, 1.5 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402/0603 1.5 nF generics supplied by C1552/C1595
    # and the 0805 1.5 nF generic supplied by C1717).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_5_nano_farad",
    })

    # Extended house part C1853 supplies this previously absent 1206 value
    # (FH 1206B203K500NT, 20 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0805 20 nF generic supplied by C1726).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "20_nano_farad",
    })

    # Extended house part C1854 supplies this previously absent 1206 value
    # (FH 1206B221K500NT, 220 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 and 0603 220 pF generics supplied by C1530 and
    # C1603 and the 0805 220 pF generic supplied by C107145).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "220_pico_farad",
    })

    # Extended house part C1855 supplies this previously absent 1206 value
    # (FH 1206B222K500NT, 2.2 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 2.2 nF generics supplied by
    # C1531, C1604 and C28260).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_2_nano_farad",
    })

    # Extended house part C1856 supplies this previously absent 1206 value
    # (FH 1206B223K500NT, 22 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 22 nF generics supplied by
    # C1532, C21122 and C1729).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_nano_farad",
    })

    # Extended house part C1857 supplies this previously absent 1206 value
    # (FH 1206B224K500NT, 220 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 220 nF generics supplied by
    # C16772, C21120 and C5378).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "220_nano_farad",
    })

    # C1859 is FH's 10 V 1206 22 uF X5R +/-10% SKU. The generic 1206 22 uF
    # preference (C12891, 25 V) stays intact; this lower-voltage purchasing
    # identity is an explicit linked rated variant following the established
    # rated-variant taxonomy (as with the C1592 16 V row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_micro_farad",
        "taxonomy_5": "10_volt",
    })

    # Extended house part C1860 supplies this previously absent 1206 value
    # (FH 1206B272K500NT, 2.7 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 2.7 nF generics supplied by C1609 and
    # C1733).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_7_nano_farad",
    })

    # Extended house part C1862 supplies this previously absent 1206 value
    # (FH 1206B331K500NT, 330 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 330 pF generics supplied by
    # C1535, C1664 and C1737).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "330_pico_farad",
    })

    # Extended house part C1863 supplies this previously absent 1206 value
    # (FH 1206B332K500NT, 3.3 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 3.3 nF generics supplied by
    # C1536, C1613 and C1738).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "3_3_nano_farad",
    })

    # Extended house part C1864 supplies this previously absent 1206 value
    # (FH 1206B333K500NT, 33 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 33 nF generics supplied by C21117 and
    # C1739).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "33_nano_farad",
    })

    # Extended house part C1865 supplies this previously absent 1206 value
    # (FH 1206B334K500NT, 330 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 330 nF generics supplied by C1615 and
    # C1740).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "330_nano_farad",
    })

    # Extended house part C1866 supplies this previously absent 1206 value
    # (FH 1206B391K500NT, 390 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 390 pF generics supplied by C1617 and
    # C1741).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "390_pico_farad",
    })

    # Extended house part C1867 supplies this previously absent 1206 value
    # (FH 1206B392K500NT, 3.9 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 3.9 nF generics supplied by C1618 and
    # C1742).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "3_9_nano_farad",
    })

    # Extended house part C1868 supplies this previously absent 1206 value
    # (FH 1206B471K500NT, 470 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 470 pF generics supplied by
    # C1537, C1620 and C1743).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "470_pico_farad",
    })

    # Extended house part C1869 supplies this previously absent 1206 value
    # (FH 1206B472K500NT, 4.7 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 4.7 nF generics supplied by
    # C1538, C53987 and C1744).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_nano_farad",
    })

    # Extended house part C1870 supplies this previously absent 1206 value
    # (FH 1206B473K500NT, 47 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 47 nF generics supplied by C1622 and
    # C53134).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "47_nano_farad",
    })

    # Extended house part C1871 supplies this previously absent 1206 value
    # (FH 1206B474K500NT, 470 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 470 nF generics supplied by C1623 and
    # C13967).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "470_nano_farad",
    })

    # C1872 is Samsung's 25 V 1206 4.7 uF X7R +/-10% SKU. The generic 1206
    # 4.7 uF preference (C29823, 50 V) stays intact; this lower-voltage
    # purchasing identity is an explicit linked rated variant following the
    # established rated-variant taxonomy (as with the C1592 16 V row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "25_volt",
    })

    # Extended house part C1873 supplies this previously absent 1206 value
    # (FH 1206B501K500NT, 500 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 500 pF generics supplied by C1624 and
    # C1747).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "500_pico_farad",
    })

    # Extended house part C1874 supplies this previously absent 1206 value
    # (FH 1206B511K500NT, 510 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 510 pF generics supplied by C1626 and
    # C1749; listing showed stock 9 at capture time, which does not change
    # identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "510_pico_farad",
    })

    # Extended house part C1875 supplies this previously absent 1206 value
    # (FH 1206B561K500NT, 560 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 560 pF generics supplied by
    # C1539, C1627 and C1751).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "560_pico_farad",
    })

    # Extended house part C1876 supplies this previously absent 1206 value
    # (FH 1206B562K500NT, 5.6 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 and 0603 5.6 nF generics supplied by C1540 and
    # C1628; listing showed stock 4 at capture time, which does not change
    # identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "5_6_nano_farad",
    })

    # Extended house part C1877 supplies this previously absent 1206 value
    # (FH 1206B563K500NT, 56 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 56 nF generics supplied by C1629 and
    # C1753).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "56_nano_farad",
    })

    # Extended house part C1878 supplies this previously absent 1206 value
    # (FH 1206B681K500NT, 680 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 680 pF generics supplied by
    # C1541, C1630 and C1754).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "680_pico_farad",
    })

    # Extended house part C1879 supplies this previously absent 1206 value
    # (FH 1206B682K500NT, 6.8 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 6.8 nF generics supplied by
    # C1542, C1631 and C1755).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "6_8_nano_farad",
    })

    # Extended house part C1880 supplies this previously absent 1206 value
    # (FH 1206B683K500NT, 68 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0805 68 nF generic supplied by C1756).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "68_nano_farad",
    })

    # Extended house part C1881 supplies this previously absent 1206 value
    # (FH 1206B684K500NT, 680 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0805 680 nF generic supplied by C1783).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "680_nano_farad",
    })

    # Extended house part C1882 supplies this previously absent 1206 value
    # (FH 1206CG0R5C500NT, 0.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 0.5 pF generics supplied by C1544, C1633 and C1784).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "0_5_pico_farad",
    })

    # Extended house part C1883 supplies this previously absent 1206 value
    # (FH 1206CG100J500NT, 10 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 10 pF generics supplied by C32949 and
    # C1634).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "10_pico_farad",
    })

    # Extended house part C1884 supplies this previously absent 1206 value
    # (FH 1206CG101J500NT, 100 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 100 pF generics supplied by
    # C1546, C14858 and C1790).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_pico_farad",
    })

    # C1885 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 1 nF value (50 V). The reviewed X7R +/-10%
    # preference C1845 (FH 1206B102K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg102j500nt",
    })

    # Extended house part C1886 supplies this previously absent 1206 value
    # (FH 1206CG120J500NT, 12 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 12 pF generics supplied by
    # C1547, C38523 and C1792).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "12_pico_farad",
    })

    # Extended house part C1887 supplies this previously absent 1206 value
    # (FH 1206CG150J500NT, 15 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the in-grid 0402 15 pF generic and the 0603 15 pF
    # generic supplied by C1644).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "15_pico_farad",
    })

    # C1888 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 150 pF value (50 V). The reviewed X7R +/-10%
    # preference C1850 (FH 1206B151K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "150_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg151j500nt",
    })

    # Extended house part C1889 supplies this previously absent 1206 value
    # (FH 1206CG180J500NT, 18 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 and 0805 18 pF generics supplied by C1647 and
    # C1797).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "18_pico_farad",
    })

    # Extended house part C1890 supplies this previously absent 1206 value
    # (FH 1206B181K500NT, 180 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 and 0805 180 pF generics supplied by C1598 and
    # C1721; listing showed stock 2 at capture time, which does not change
    # identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "180_pico_farad",
    })

    # Extended house part C1891 supplies this previously absent 1206 value
    # (FH 1206CG1R0C500NT, 1 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0805
    # 1 pF generics supplied by C1550 and C1786).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_pico_farad",
    })

    # Extended house part C1892 supplies this previously absent 1206 value
    # (FH 1206CG1R5C500NT, 1.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 1.5 pF generics supplied by C1552, C1639 and C1788).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_5_pico_farad",
    })

    # Extended house part C1893 supplies this previously absent 1206 value
    # (FH 1206CG1R8C500NT, 1.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 1.8 pF generics supplied by C1553, C1640 and C1789).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_8_pico_farad",
    })

    # Extended house part C1894 supplies this previously absent 1206 value
    # (FH 1206CG200J500NT, 20 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 20 pF generics supplied by
    # C1554, C1648 and C1798).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "20_pico_farad",
    })

    # Extended house part C1895 supplies this previously absent 1206 value
    # (FH 1206CG201J500NT, 200 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 200 pF generics supplied by
    # C1529, C1600 and C1724).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "200_pico_farad",
    })

    # Extended house part C1896 supplies this previously absent 1206 value
    # (FH 1206CG220J500NT, 22 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 22 pF generics supplied by
    # C1555, C1653 and C1804).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_pico_farad",
    })

    # C1897 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 220 pF value (50 V). The reviewed X7R +/-10%
    # preference C1854 (FH 1206B221K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "220_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg221j500nt",
    })

    # Extended house part C1898 supplies this previously absent 1206 value
    # (FH 1206CG250J500NT, 25 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 25 pF generics supplied by
    # C1556, C1655 and C1807).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "25_pico_farad",
    })

    # Extended house part C1899 supplies this previously absent 1206 value
    # (FH 1206CG270J500NT, 27 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 27 pF generics supplied by
    # C1557, C1656 and C1808).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "27_pico_farad",
    })

    # Extended house part C1900 supplies this previously absent 1206 value
    # (FH 1206CG271J500NT, 270 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 270 pF generics supplied by
    # C1533, C1608 and C1732).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "270_pico_farad",
    })

    # Extended house part C1901 supplies this previously absent 1206 value
    # (FH 1206CG2R0C500NT, 2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 2 pF generics supplied by C1558, C1650 and C1800).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_pico_farad",
    })

    # Extended house part C1902 supplies this previously absent 1206 value
    # (FH 1206CG2R2C500NT, 2.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 2.2 pF generics supplied by C1559, C1651 and C1801).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_2_pico_farad",
    })

    # Extended house part C1903 supplies this previously absent 1206 value
    # (FH 1206CG2R5C500NT, 2.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 2.5 pF generics supplied by C1560, C1652 and C1802).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_5_pico_farad",
    })

    # Extended house part C1904 supplies this previously absent 1206 value
    # (FH 1206CG2R7C500NT, 2.7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0805
    # 2.7 pF generics supplied by C1561 and C1803).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_7_pico_farad",
    })

    # Extended house part C1905 supplies this previously absent 1206 value
    # (FH 1206CG300J500NT, 30 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 30 pF generics supplied by C1570 and
    # C1658).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "30_pico_farad",
    })

    # Extended house part C1906 supplies this previously absent 1206 value
    # (FH 1206CG330J500NT, 33 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 33 pF generics supplied by C1562 and
    # C1663).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "33_pico_farad",
    })

    # C1907 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 330 pF value (50 V). The reviewed X7R +/-10%
    # preference C1862 (FH 1206B331K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "330_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg331j500nt",
    })

    # Extended house part C1908 supplies this previously absent 1206 value
    # (FH 1206CG360J500NT, 36 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 36 pF generic supplied by C1665).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "36_pico_farad",
    })

    # Extended house part C1909 supplies this previously absent 1206 value
    # (FH 1206CG390J500NT, 39 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 39 pF generics supplied by C1563 and
    # C1666).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "39_pico_farad",
    })

    # Extended house part C1911 supplies this previously absent 1206 value
    # (FH 1206CG3R0C500NT, 3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0805
    # 3 pF generics supplied by C1564 and C1810).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "3_pico_farad",
    })

    # Extended house part C1912 supplies this previously absent 1206 value
    # (FH 1206CG3R3C500NT, 3.3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 3.3 pF generics supplied by C1565, C1660 and C1811).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "3_3_pico_farad",
    })

    # Extended house part C1913 supplies this previously absent 1206 value
    # (FH 1206CG3R9C500NT, 3.9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 3.9 pF generics supplied by C1566, C1662 and C1813).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "3_9_pico_farad",
    })

    # Extended house part C1914 supplies this previously absent 1206 value
    # (FH 1206CG4R0C500NT, 4 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402, 0603 and
    # 0805 4 pF generics supplied by C1568, C1668 and C1819).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_pico_farad",
    })

    # Extended house part C1916 supplies this previously absent 1206 value
    # (FH 1206CG470J500NT, 47 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 47 pF generics supplied by
    # C1567, C1671 and C14857).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "47_pico_farad",
    })

    # C1917 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 470 pF value (50 V). The reviewed X7R +/-10%
    # preference C1868 (FH 1206B471K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "470_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg471j500nt",
    })

    # Extended house part C1918 supplies this previously absent 1206 value
    # (FH 1206CG510J500NT, 51 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 51 pF generics supplied by
    # C1571, C1675 and C1827).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "51_pico_farad",
    })

    # Extended house part C1919 supplies this previously absent 1206 value
    # (FH 1206CG560J500NT, 56 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 56 pF generics supplied by
    # C1572, C1676 and C1828).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "56_pico_farad",
    })

    # Extended house part C1920 supplies this previously absent 1206 value
    # (FH 1206CG6R0C500NT, 6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 6 pF generic
    # supplied by C1575).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "6_pico_farad",
    })

    # Extended house part C1921 supplies this previously absent 1206 value
    # (FH 1206CG620J500NT, 62 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0805 62 pF generic supplied by C1833).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "62_pico_farad",
    })

    # Extended house part C1922 supplies this previously absent 1206 value
    # (FH 1206CG680J500NT, 68 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 and 0805 68 pF generics supplied by C1680 and
    # C1834).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "68_pico_farad",
    })

    # C1923 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for
    # the generic 1206 680 pF value (50 V). The reviewed X7R +/-10%
    # preference C1878 (FH 1206B681K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "680_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206cg681j500nt",
    })

    # Extended house part C1924 supplies this previously absent 1206 value
    # (FH 1206CG820J500NT, 82 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 and 0805 82 pF generics supplied by C1683 and
    # C1841).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "82_pico_farad",
    })

    # C1926 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 1206 1 uF value (50 V). The reviewed X7R +/-10%
    # preference C1848 (Samsung CL31B105KBHNNNE) on the plain generic ID
    # keeps it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_micro_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f105m500nt",
    })

    # Extended house part C1928 supplies this previously absent 1206 value
    # (FH 1206F153M500NT, 15 nF 50 V Y5V +/-20%, the first reviewed choice;
    # distinct from the 0402, 0603 and 0805 15 nF generics supplied by
    # C1583, C1596 and C1718; listing showed stock 4 at capture time, which
    # does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "15_nano_farad",
    })

    # Extended house part C1929 supplies this previously absent 1206 value
    # (FH 1206F154M500NT, 150 nF 50 V Y5V +/-20%, the first reviewed choice;
    # distinct from the 0603 and 0805 150 nF generics supplied by C1597 and
    # C1719).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "150_nano_farad",
    })

    # C1930 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 1206 20 nF value (50 V). The reviewed X7R +/-10%
    # preference C1853 (FH 1206B203K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "20_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f203m500nt",
    })

    # C1931 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 1206 22 nF value (50 V). The reviewed X7R +/-10%
    # preference C1856 (FH 1206B223K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f223m500nt",
    })

    # C1933 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% 25 V SKU
    # for the generic 1206 2.2 uF value. The reviewed X7R +/-10% 50 V
    # preference C1855 (FH 1206B222K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_2_micro_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f225m250nt",
    })

    # C1935 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 1206 33 nF value (50 V). The reviewed X7R +/-10%
    # preference C1864 (FH 1206B333K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "33_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f333m500nt",
    })

    # C1939 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% 25 V SKU
    # for the generic 1206 4.7 uF value. The reviewed X7R +/-10% 50 V
    # preference C29823 (FH 1206B475K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f475m250nt",
    })

    # C1940 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 1206 68 nF value (50 V). The reviewed X7R +/-10%
    # preference C1880 (FH 1206B683K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "68_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "1206f683m500nt",
    })

    # C1941 is FH's 1 kV 1206 1 nF X7R +/-10% SKU. The generic 1206 1 nF
    # preference (C1845, 50 V) stays intact; this higher-voltage purchasing
    # identity is an explicit linked rated variant following the established
    # rated-variant taxonomy (as with the 2000 V variant C9196).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "1000_volt",
    })

    # C1942 is FH's 500 V 1206 1 nF X7R +/-10% SKU. The generic 1206 1 nF
    # preference (C1845, 50 V) stays intact; this higher-voltage purchasing
    # identity is an explicit linked rated variant following the established
    # rated-variant taxonomy (as with the 1 kV variant C1941).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "500_volt",
    })

    # C1945 is Samsung's 100 V 1206 100 nF X7R +/-10% SKU. The generic 1206
    # 100 nF preference (C24497, 50 V) stays intact; this higher-voltage
    # purchasing identity is an explicit linked rated variant following the
    # established rated-variant taxonomy (as with the C1592 16 V row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "100_volt",
    })

    # Extended house part C1950 supplies this previously absent 1210 value
    # (FH 1210B225K500NT, 2.2 uF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 1210 68 uF tantal generic already in the grid).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1210",
        "taxonomy_4": "2_2_micro_farad",
    })

    # Extended house part C2029 supplies this previously absent leaded
    # electrolytic value (CX KM106M100E11RR0VH2FP0, 10 uF 100 V, D6.3 x
    # 11 mm radial, the first reviewed choice; size follows the existing
    # diameter_tall electrolytic naming).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_11_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "10_micro_farad",
        "taxonomy_6": "100_volt",
    })

    # Extended house part C2033 supplies this previously absent leaded
    # electrolytic value (CX GR477M010F12RR0VL4FP0, 470 uF 10 V, D8 x 12 mm
    # radial, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "10_volt",
    })

    # Extended house part C2036 supplies this previously absent leaded
    # electrolytic value (CX GR227M010E11RR0VH4FP0, 220 uF 10 V, D6.3 x
    # 11 mm radial, the first reviewed choice; shares the C2029 can size).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_11_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "10_volt",
    })

    # Extended house part C2051 supplies this previously absent leaded
    # electrolytic value (CX KM337M025F12RR0VH2FP0, 330 uF 25 V, D8 x 12 mm
    # radial, the first reviewed choice; shares the C2033 can size).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "330_micro_farad",
        "taxonomy_6": "25_volt",
    })

    # Extended house part C2063 supplies this previously absent leaded
    # electrolytic value (CX KM227M035F12RR0VH2FP0, 220 uF 35 V, D8 x 12 mm
    # radial, the first reviewed choice; shares the C2033 can size).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "35_volt",
    })

    # Extended house part C2064 supplies this previously absent leaded
    # electrolytic value (CX KM477M035G17RR0VH2FP0, 470 uF 35 V, D10 x
    # 17 mm radial, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_17_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "35_volt",
    })

    # Extended house part C2065 supplies this previously absent leaded
    # electrolytic value (CX KS225M050C07RR0VH2FP0, 2.2 uF 50 V, D4 x 7 mm
    # radial, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "2_2_micro_farad",
        "taxonomy_6": "50_volt",
    })

    # Extended house parts C2746-C2775 supply previously absent leaded
    # electrolytic values from the CX KM/KS series (all first reviewed
    # choices; sizes follow the existing diameter_tall naming).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "16_mm_diameter_25_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "47_micro_farad",
        "taxonomy_6": "450_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "18_mm_diameter_30_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "6800_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "1_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "16_mm_diameter_25_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "2200_micro_farad",
        "taxonomy_6": "35_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "18_mm_diameter_30_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "400_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "63_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "4_7_micro_farad",
        "taxonomy_6": "250_volt",
    })

    # Extended house parts C3299-C3314 supply more leaded electrolytic
    # values (CX GR/KS series; all first reviewed choices, including the
    # first 10 mm x 20 mm can).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_12_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "1000_micro_farad",
        "taxonomy_6": "10_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_20_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "1500_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_20_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "33_micro_farad",
        "taxonomy_6": "16_volt",
    })

    # Extended house parts C3328-C3347: more leaded values plus the first
    # SMD aluminum electrolytic cans (Honor RVT series; the registry's
    # 6.3 mm cans already use the same diameter_tall naming).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_20_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "2200_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_17_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "100_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "5_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "47_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "5_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "10_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_7_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_7_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "35_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "35_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_7_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "10_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "47_micro_farad",
        "taxonomy_6": "35_volt",
    })

    # Extended house parts C3348-C3359: more Honor RVT SMD electrolytic
    # values, adding the 10x10.2 mm and 8x10.5 mm cans.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "1_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_7_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "47_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "35_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "100_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_10_5_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "6_3_mm_diameter_7_7_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "6_3_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "4_7_micro_farad",
        "taxonomy_6": "35_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "22_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "4_mm_diameter_5_4_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "10_micro_farad",
        "taxonomy_6": "16_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "220_micro_farad",
        "taxonomy_6": "50_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_10_2_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "1000_micro_farad",
        "taxonomy_6": "16_volt",
    })

    # C1951 is the FH (Guangdong Fenghua Advanced Tech) X7R +/-10% SKU for
    # the generic 0603 82 nF value (50 V). The reviewed Y5V +/-20%
    # preference C1708 (FH 0603F823M500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; this X7R SKU is
    # the more stable dielectric and projects requiring X7R stability should
    # pick it explicitly.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "82_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603b823k500nt",
    })

    # Extended house part C1717 supplies this previously absent 0805 value
    # (FH 0805B152K500NT, 1.5 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402/0603 1.5 nF generics supplied by C1552/C1595).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_5_nano_farad",
    })

    # Extended house part C1718 supplies this previously absent 0805 value
    # (FH 0805B153K500NT, 15 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 15 nF generic supplied by C1596).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "15_nano_farad",
    })

    # Extended house part C1719 supplies this previously absent 0805 value
    # (FH 0805B154K500NT, 150 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 150 nF generic supplied by C1597).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "150_nano_farad",
    })

    # Extended house part C1720 supplies this previously absent 0805 value
    # (FH 0805B161K500NT, 160 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "160_pico_farad",
    })

    # Extended house part C1721 supplies this previously absent 0805 value
    # (FH 0805B181K500NT, 180 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 180 pF generic supplied by C1598).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "180_pico_farad",
    })

    # Extended house part C1722 supplies this previously absent 0805 value
    # (FH 0805B182K500NT, 1.8 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 1.8 nF generic supplied by C1599).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_8_nano_farad",
    })

    # Extended house part C1723 (FH 0805B183K500NT, 18 nF 50 V X7R +/-10%)
    # is the first reviewed choice for the in-grid 0805 18 nF generic; the
    # grid entry already exists, so no populate row is added here.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "18_nano_farad",
    })

    # Extended house part C1724 supplies this previously absent 0805 value
    # (FH 0805B201K500NT, 200 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 200 pF generic supplied by C1529 and the 0603
    # 200 pF generic supplied by C1600).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "200_pico_farad",
    })

    # Extended house part C1725 supplies this previously absent 0805 value
    # (FH 0805B202K500NT, 2 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 2 nF generic supplied by C1601).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_nano_farad",
    })

    # Extended house part C1726 supplies this previously absent 0805 value
    # (FH 0805B203K500NT, 20 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 20 nF generic supplied by C1602).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "20_nano_farad",
    })

    # C1727 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0805 220 pF value. The reviewed Basic preference
    # C107145 (YAGEO CC0805KRX7R9BB221) keeps the plain generic ID, so this
    # exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805b221k500nt",
    })

    # C1728 is the Samsung X7R +/-10% SKU for the generic 0805 2.2 nF value.
    # The reviewed Basic C0G +/-5% preference C28260 (same maker) keeps the
    # plain generic ID, so this exact purchasing identity gets its own
    # linked row following the established maker/mpn variant taxonomy; the
    # X7R option must not silently replace the C0G preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_2_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl21b222kbannnc",
    })

    # C1731 is Samsung's 16 V 0805 2.2 uF X5R +/-10% SKU. The reviewed Basic
    # 50 V preference C377773 (CL21A225KBQNNNE) on the plain generic ID
    # keeps it, so this lower-voltage purchasing identity gets its own
    # linked rated row following the established rated variant taxonomy;
    # the 16 V option must not silently replace the 50 V choice.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_2_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # Extended house part C1732 supplies this previously absent 0805 value
    # (FH 0805B271K500NT, 270 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 270 pF generic supplied by C1608).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "270_pico_farad",
    })

    # Extended house part C1733 supplies this previously absent 0805 value
    # (FH 0805B272K500NT, 2.7 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 2.7 nF generic supplied by C1609).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "2_7_nano_farad",
    })

    # Extended house part C1734 supplies this previously absent 0805 value
    # (FH 0805B273K500NT, 27 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 27 nF generic supplied by C1700).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "27_nano_farad",
    })

    # Extended house part C1735 supplies this previously absent 0805 value
    # (FH 0805B301K500NT, 300 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 300 pF generic supplied by C1610).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "300_pico_farad",
    })

    # Extended house part C1736 supplies this previously absent 0805 value
    # (FH 0805B302K500NT, 3 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 3 nF generic supplied by C1611).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_nano_farad",
    })

    # Extended house part C1737 supplies this previously absent 0805 value
    # (FH 0805B331K500NT, 330 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 330 pF generic supplied by C1612).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "330_pico_farad",
    })

    # Extended house part C1738 supplies this previously absent 0805 value
    # (FH 0805B332K500NT, 3.3 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 3.3 nF generic supplied by C1576).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_3_nano_farad",
    })

    # Extended house part C1740 supplies this previously absent 0805 value
    # (FH 0805B334K500NT, 330 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 330 nF generic supplied by C1615).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "330_nano_farad",
    })

    # Extended house part C1741 supplies this previously absent 0805 value
    # (FH 0805B391K500NT, 390 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 390 pF generic supplied by C1617).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "390_pico_farad",
    })

    # Extended house part C1742 supplies this previously absent 0805 value
    # (FH 0805B392K500NT, 3.9 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 3.9 nF generic supplied by C1618).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "3_9_nano_farad",
    })

    # Extended house part C1700 supplies this previously absent 0603 value
    # (FH 0603F273M500NT, 27 nF 50 V Y5V +/-20%, the first reviewed choice;
    # listing showed stock 8 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "27_nano_farad",
    })

    # C1745 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0805 47 nF value. The reviewed Basic preference
    # C53134 (Samsung CL21B473KBCNNNC) keeps the plain generic ID, so this
    # exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "47_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805b473k500nt",
    })

    # C1746 is Samsung's 16 V 0805 4.7 uF X5R +/-10% SKU. The reviewed Basic
    # 25 V preference C1779 (CL21A475KAQNNNE) on the plain generic ID keeps
    # it, so this lower-voltage purchasing identity gets its own linked
    # rated row following the established rated variant taxonomy; the 16 V
    # option must not silently replace the 25 V choice.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # Extended house part C1747 supplies this previously absent 0805 value
    # (FH 0805B501K500NT, 500 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 500 pF generic supplied by C1624).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "500_pico_farad",
    })

    # Extended house part C1748 supplies this previously absent 0805 value
    # (FH 0805B502K500NT, 5 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 5 nF generic supplied by C1625).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "5_nano_farad",
    })

    # Extended house part C1749 supplies this previously absent 0805 value
    # (FH 0805B511K500NT, 510 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 510 pF generic supplied by C1626).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "510_pico_farad",
    })

    # Extended house part C1750 supplies this previously absent 0805 value
    # (FH 0805B512K500NT, 5.1 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 5.1 nF generic supplied by C1587).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "5_1_nano_farad",
    })

    # Extended house part C1751 supplies this previously absent 0805 value
    # (FH 0805B561K500NT, 560 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 560 pF generic supplied by C1627).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "560_pico_farad",
    })

    # Extended house part C1753 supplies this previously absent 0805 value
    # (FH 0805B563K500NT, 56 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 56 nF generic supplied by C1629; listing showed
    # stock 60 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "56_nano_farad",
    })

    # Extended house part C1754 supplies this previously absent 0805 value
    # (FH 0805B681K500NT, 680 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 680 pF generic supplied by C1630).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "680_pico_farad",
    })

    # Extended house part C1755 supplies this previously absent 0805 value
    # (FH 0805B682K500NT, 6.8 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 6.8 nF generic supplied by C1633).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "6_8_nano_farad",
    })

    # Extended house part C1756 supplies this previously absent 0805 value
    # (FH 0805B683K500NT, 68 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "68_nano_farad",
    })

    # Extended house part C1757 supplies this previously absent 0805 value
    # (FH 0805B821K500NT, 820 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 820 pF generic supplied by C1632).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "820_pico_farad",
    })

    # Extended house part C1758 supplies this previously absent 0805 value
    # (FH 0805B822K500NT, 8.2 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0603 8.2 nF generic supplied by C1634).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "8_2_nano_farad",
    })

    # C1701 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 33 nF value. The Samsung X7R Basic preference C21117
    # and the FH X7R variant C1614 keep their IDs, so this exact purchasing
    # identity gets its own linked row following the established maker/mpn
    # variant taxonomy; the Y5V option must not silently replace the X7R
    # preferences.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "33_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f333m500nt",
    })

    # C1761 is the Samsung Y5V -20/+80% SKU for the generic 0805 1 uF value.
    # The reviewed Basic X7R +/-10% 50 V preference C28323 (and the 25 V
    # X7R rated variant C1712) keep their IDs, so this exact purchasing
    # identity gets its own linked row following the established maker/mpn
    # variant taxonomy; the Y5V option must not silently replace the X7R
    # preferences.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_micro_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl21f105zafnnne",
    })

    # C1763 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 12 nF value. The X7R +/-10% preference C1715 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "12_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f123m500nt",
    })

    # Extended house part C1764 supplies this previously absent 0805 value
    # (FH 0805F124M500NT, 120 nF 50 V Y5V +/-20%, the first reviewed choice;
    # listing showed stock 17 at capture time, which does not change
    # identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "120_nano_farad",
    })

    # C1767 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 18 nF value. The X7R +/-10% preference C1723 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "18_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f183m500nt",
    })

    # C1768 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 20 nF value. The X7R +/-10% preference C1726 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "20_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f203m500nt",
    })

    # C1770 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 220 nF value. The X7R +/-10% Basic preference C5378
    # on the plain generic ID keeps it, so this exact purchasing identity
    # gets its own linked row following the established maker/mpn variant
    # taxonomy; the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f224m500nt",
    })

    # C1773 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 27 nF value. The X7R +/-10% preference C1734 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "27_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f273m500nt",
    })

    # C1774 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 33 nF value. The X7R +/-10% preference C1739 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "33_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f333m500nt",
    })

    # Extended house part C1776 supplies this previously absent 0805 value
    # (FH 0805F393M500NT, 39 nF 50 V Y5V +/-20%, the first reviewed choice;
    # listing showed stock 5 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "39_nano_farad",
    })

    # C1778 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 470 nF value (50 V). The reviewed Basic X7R +/-10%
    # preference C13967 (Samsung CL21B474KBFNNNE) on the plain generic ID
    # keeps it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f474m500nt",
    })

    # C1781 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0805 68 nF value (50 V). The reviewed X7R +/-10%
    # preference C1756 (FH 0805B683K500NT) on the plain generic ID keeps
    # it, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy; the Y5V option
    # must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "68_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0805f683m500nt",
    })

    # Extended house part C1782 supplies this previously absent 0805 value
    # (FH 0805F823M500NT, 82 nF 50 V Y5V +/-20%, the first reviewed choice;
    # distinct from the 0805 820 pF X7R generic supplied by C1757).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "82_nano_farad",
    })

    # Extended house part C1783 supplies this previously absent 0805 value
    # (FH 0805F684M500NT, 680 nF 50 V Y5V +/-20%, the first reviewed choice;
    # listing showed stock 5 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "680_nano_farad",
    })

    # Extended house part C1784 supplies this previously absent 0805 value
    # (FH 0805CG0R5C500NT, 0.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 0.5 pF generics supplied by C1544 and C1633).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "0_5_pico_farad",
    })

    # Extended house part C1786 supplies this previously absent 0805 value
    # (FH 0805CG1R0C500NT, 1 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 1 pF generic
    # supplied by C1550).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_pico_farad",
    })

    # Extended house part C1787 supplies this previously absent 0805 value
    # (FH 0805CG1R2C500NT, 1.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 1.2 pF generics supplied by C1551 and C1638).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_2_pico_farad",
    })

    # Extended house part C1788 supplies this previously absent 0805 value
    # (FH 0805CG1R5C500NT, 1.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 1.5 pF generics supplied by C1552 and C1639).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_5_pico_farad",
    })

    # Extended house part C1789 supplies this previously absent 0805 value
    # (FH 0805CG1R8C500NT, 1.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 and 0603
    # 1.8 pF generics supplied by C1553 and C1640).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_8_pico_farad",
    })

    # C1791 is the Samsung Electro-Mechanics C0G +/-5% SKU for the generic
    # 0805 1 nF value (50 V). The reviewed Basic X7R +/-10% preference
    # C46653 (Samsung CL21B102KBCNNNC) on the plain generic ID keeps it, so
    # this exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl21c102jbcnnnc",
    })

    # Extended house part C1792 supplies this previously absent 0805 value
    # (FH 0805CG120J500NT, 12 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 and 0603 12 pF generics supplied by C1547 and
    # C38523).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "12_pico_farad",
    })

    # Extended house part C1793 supplies this previously absent 0805 value
    # (FH 0805CG121J500NT, 120 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the in-grid 0402 120 pF generic and the 0603 120 pF
    # generic supplied by C1643).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "120_pico_farad",
    })

    # C1702 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 330 nF value. The X7R +/-10% preference C1615 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "330_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f334m250nt",
    })

    # C1703 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 47 nF value. The X7R +/-10% preference on the plain
    # generic ID keeps it, so this exact purchasing identity gets its own
    # linked row following the established maker/mpn variant taxonomy; the
    # Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "47_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f473m500nt",
    })

    # C1705 is Samsung's 10 V 0603 4.7 uF X5R +/-10% SKU. The 16 V rated
    # variant C78 on the generic 0603 4.7 uF family keeps its ID, so this
    # exact purchasing identity gets its own linked rated row following the
    # established 16_volt taxonomy; the 10 V option must not silently
    # replace the 16 V choice.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "10_volt",
    })

    # C1706 is the FH (Guangdong Fenghua Advanced Tech) Y5V +/-20% SKU for
    # the generic 0603 56 nF value. The X7R +/-10% preference C1629 on the
    # plain generic ID keeps it, so this exact purchasing identity gets its
    # own linked row following the established maker/mpn variant taxonomy;
    # the Y5V option must not silently replace the X7R preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "56_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603f563m500nt",
    })

    # Extended house part C1708 supplies this previously absent 0603 value
    # (FH 0603F823M500NT, 82 nF 50 V Y5V +/-20%, the first reviewed choice;
    # distinct from the 0603 820 pF X7R generic supplied by C1632).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "82_nano_farad",
    })

    # Extended house part C1660 supplies this previously absent 0603 value
    # (FH 0603CG3R3C500NT, 3.3 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0603 3.3 nF
    # generic and the 0402 3.3 pF generic supplied by C1565).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_3_pico_farad",
    })

    # Extended house part C1661 supplies this previously absent 0603 value
    # (FH 0603CG3R6C500NT, 3.6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_6_pico_farad",
    })

    # Extended house part C1662 supplies this previously absent 0603 value
    # (FH 0603CG3R9C500NT, 3.9 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0603 3.9 nF
    # generic and the 0402 3.9 pF generic supplied by C1566).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_9_pico_farad",
    })

    # Extended house part C1665 supplies this previously absent 0603 value
    # (FH 0603CG360J500NT, 36 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "36_pico_farad",
    })

    # Extended house part C1666 supplies this previously absent 0603 value
    # (FH 0603CG390J500NT, 39 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0603 39 nF generic supplied by C1619).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "39_pico_farad",
    })

    # C1667 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for the
    # generic 0603 390 pF value. The X7R +/-10% preference C1617 on the plain
    # generic ID keeps it, so this exact purchasing identity gets its own
    # linked row following the established maker/mpn variant taxonomy; the
    # C0G option must not silently replace the X7R preference either.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "390_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg391j500nt",
    })

    # Extended house part C1668 supplies this previously absent 0603 value
    # (FH 0603CG4R0C500NT, 4 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 4 pF
    # generic supplied by C1568).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_pico_farad",
    })

    # Extended house part C1669 supplies this previously absent 0603 value
    # (FH 0603CG4R7C500NT, 4.7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 4.7 pF
    # generic supplied by C1569).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_7_pico_farad",
    })

    # Extended house part C1670 supplies this previously absent 0603 value
    # (FH 0603CG430J500NT, 43 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "43_pico_farad",
    })

    # Extended house part C1672 supplies this previously absent 0603 value
    # (FH 0603CG500J500NT, 50 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "50_pico_farad",
    })

    # Extended house part C1673 supplies this previously absent 0603 value
    # (FH 0603CG5R0C500NT, 5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 5 pF
    # generic supplied by C1573).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "5_pico_farad",
    })

    # Extended house part C1674 supplies this previously absent 0603 value
    # (FH 0603CG5R6C500NT, 5.6 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 5.6 pF
    # generic supplied by C1574).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "5_6_pico_farad",
    })

    # Extended house part C1675 supplies this previously absent 0603 value
    # (FH 0603CG510J500NT, 51 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 51 pF generic supplied by C1571).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "51_pico_farad",
    })

    # Extended house part C1676 supplies this previously absent 0603 value
    # (FH 0603CG560J500NT, 56 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 56 pF generic supplied by C1572).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "56_pico_farad",
    })

    # Extended house part C1678 supplies this previously absent 0603 value
    # (FH 0603CG6R2C500NT, 6.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "6_2_pico_farad",
    })

    # Extended house part C1679 supplies this previously absent 0603 value
    # (FH 0603CG6R8C500NT, 6.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 6.8 pF
    # generic supplied by C1576).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "6_8_pico_farad",
    })

    # Extended house part C1610 supplies this previously absent 0603 value
    # (FH 0603B301K500NT, 300 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "300_pico_farad",
    })

    # Extended house part C1611 supplies this previously absent 0603 value
    # (FH 0603B302K500NT, 3 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 3 nF generic supplied by C1564).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_nano_farad",
    })

    # C1612 is the FH (Guangdong Fenghua Advanced Tech) purchasing SKU for the
    # generic 0603 330 pF value, but with an X7R +/-10% dielectric unlike the
    # reviewed Basic C0G +/-5% preference C1664 (Samsung CL10C331JB8NNNC).
    # This exact purchasing identity gets its own linked row following the
    # established maker/mpn variant taxonomy (as with the Samsung C1591,
    # C1524 and C1581 rows); it must not replace the C0G preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "330_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603b331k500nt",
    })

    # C1614 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0603 33 nF value (50 V, X7R, +/-10%). The reviewed
    # Basic preference C21117 (Samsung CL10B333KB8NNNC) keeps the plain
    # generic ID, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "33_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603b333k500nt",
    })

    # Extended house part C1615 supplies this previously absent 0603 value
    # (FH 0603B334K250NT, 330 nF 25 V X7R +/-10%, the first reviewed choice;
    # the generic ID stays plain since no higher-voltage sibling exists yet).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "330_nano_farad",
    })

    # Extended house part C1616 supplies this previously absent 0603 value
    # (FH 0603B361K500NT, 360 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "360_pico_farad",
    })

    # Extended house part C1617 supplies this previously absent 0603 value
    # (FH 0603B391K500NT, 390 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "390_pico_farad",
    })

    # Extended house part C1618 supplies this previously absent 0603 value
    # (FH 0603B392K500NT, 3.9 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 3.9 pF C0G generic supplied by C1566).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_9_nano_farad",
    })

    # Extended house part C1619 supplies this previously absent 0603 value
    # (FH 0603B393K500NT, 39 nF 50 V X7R +/-10%, the first reviewed choice;
    # listing showed stock 321 at capture time, which does not change identity).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "39_nano_farad",
    })

    # C1621 is the Samsung equivalent-spec SKU for the generic 0603 4.7 nF
    # value (50 V, X7R, +/-10%). The reviewed Basic preference C53987
    # (FH 0603B472K500NT) keeps the plain generic ID, so this exact
    # purchasing identity gets its own linked row following the established
    # maker/mpn variant taxonomy (as with the Samsung C1591 and C1589 rows).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_7_nano_farad",
        "taxonomy_5": "samsung_electro_mechanics",
        "taxonomy_6": "cl10b472kb8nnnc",
    })

    # Extended house part C1624 supplies this previously absent 0603 value
    # (FH 0603B501K500NT, 500 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "500_pico_farad",
    })

    # Extended house part C1625 supplies this previously absent 0603 value
    # (FH 0603B502K500NT, 5 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 5 pF C0G generic supplied by C1573).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "5_nano_farad",
    })

    # Extended house part C1626 supplies this previously absent 0603 value
    # (FH 0603B511K500NT, 510 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "510_pico_farad",
    })

    # Extended house part C1627 supplies this previously absent 0603 value
    # (FH 0603B561K500NT, 560 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 560 pF C0G generic supplied by C1539).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "560_pico_farad",
    })

    # Extended house part C1628 supplies this previously absent 0603 value
    # (FH 0603B562K500NT, 5.6 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 5.6 nF generic supplied by C1542).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "5_6_nano_farad",
    })

    # Extended house part C1629 supplies this previously absent 0603 value
    # (FH 0603B563K500NT, 56 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "56_nano_farad",
    })

    # Extended house part C1630 supplies this previously absent 0603 value
    # (FH 0603B681K500NT, 680 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 680 pF C0G generic supplied by C1541).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "680_pico_farad",
    })

    # Extended house part C1632 supplies this previously absent 0603 value
    # (FH 0603B821K500NT, 820 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 820 pF C0G generic supplied by C1543).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "820_pico_farad",
    })

    # Extended house part C1633 supplies this previously absent 0603 value
    # (FH 0603CG0R5C500NT, 0.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 0.5 pF
    # generic supplied by C1544).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "0_5_pico_farad",
    })

    # C1635 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0603 100 pF value (50 V, C0G, +/-5%). The reviewed
    # Basic preference C14858 (Samsung CL10C101JB8NNNC) keeps the plain
    # generic ID, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg101j500nt",
    })

    # C1636 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for the
    # generic 0603 1 nF value. The reviewed Basic preference C1588 (Samsung
    # CL10B102KB8NNNC, X7R +/-10%) keeps the plain generic ID, so this exact
    # purchasing identity gets its own linked row following the established
    # maker/mpn variant taxonomy; the C0G option must not silently replace
    # the X7R preference either.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg102j500nt",
    })

    # Extended house part C1638 supplies this previously absent 0603 value
    # (FH 0603CG1R2C500NT, 1.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 1.2 pF
    # generic supplied by C1551).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_2_pico_farad",
    })

    # Extended house part C1639 supplies this previously absent 0603 value
    # (FH 0603CG1R5C500NT, 1.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 1.5 pF
    # generic supplied by C1552).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_5_pico_farad",
    })

    # Extended house part C1640 supplies this previously absent 0603 value
    # (FH 0603CG1R8C500NT, 1.8 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 1.8 pF
    # generic supplied by C1553).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_8_pico_farad",
    })

    # Extended house part C1641 supplies this previously absent 0603 value
    # (FH 0603CG110J500NT, 11 pF 50 V C0G +/-5%, the first reviewed choice;
    # 110 = 11 x 10^0 pF, distinct from the in-grid 10 pF generic).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "11_pico_farad",
    })

    # C1642 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0603 12 pF value (50 V, C0G, +/-5%). The reviewed
    # Basic preference C38523 (Samsung CL10C120JB8NNNC) keeps the plain
    # generic ID, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "12_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg120j500nt",
    })

    # Extended house part C1643 supplies this previously absent 0603 value
    # (FH 0603CG121J500NT, 120 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "120_pico_farad",
    })

    # Extended house part C1646 supplies this previously absent 0603 value
    # (FH 0603CG160J500NT, 16 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "16_pico_farad",
    })

    # C1649 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for the
    # generic 0603 200 pF value. The X7R +/-10% preference C1600 on the plain
    # generic ID keeps it, so this exact purchasing identity gets its own
    # linked row following the established maker/mpn variant taxonomy; the
    # C0G option must not silently replace the X7R preference either.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "200_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg201j500nt",
    })

    # Extended house part C1680 supplies this previously absent 0603 value
    # (FH 0603CG680J500NT, 68 pF 50 V C0G +/-5%, the first reviewed choice;
    # 680 = 68 x 10^0 pF, distinct from the 0603 680 pF X7R generic
    # supplied by C1630).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "68_pico_farad",
    })

    # Extended house part C1681 supplies this previously absent 0603 value
    # (FH 0603CG750J500NT, 75 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "75_pico_farad",
    })

    # Extended house part C1682 supplies this previously absent 0603 value
    # (FH 0603CG7R0C500NT, 7 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 7 pF
    # generic supplied by C1577).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "7_pico_farad",
    })

    # Extended house part C1683 supplies this previously absent 0603 value
    # (FH 0603CG820J500NT, 82 pF 50 V C0G +/-5%, the first reviewed choice;
    # 820 = 82 x 10^0 pF, distinct from the 0603 820 pF X7R generic
    # supplied by C1632).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "82_pico_farad",
    })

    # Extended house part C1685 supplies this previously absent 0603 value
    # (FH 0603CG8R2C500NT, 8.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 8.2 pF
    # generic supplied by C1579).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "8_2_pico_farad",
    })

    # Extended house part C1686 supplies this previously absent 0603 value
    # (FH 0603CG910J500NT, 91 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "91_pico_farad",
    })

    # Extended house part C1650 supplies this previously absent 0603 value
    # (FH 0603CG2R0C500NT, 2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 2 pF
    # generic supplied by C1558).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_pico_farad",
    })

    # Extended house part C1651 supplies this previously absent 0603 value
    # (FH 0603CG2R2C500NT, 2.2 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 2.2 pF
    # generic supplied by C1559).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_2_pico_farad",
    })

    # Extended house part C1652 supplies this previously absent 0603 value
    # (FH 0603CG2R5C500NT, 2.5 pF 50 V C0G, the first reviewed choice; the
    # live page lists no tolerance row; distinct from the 0402 2.5 pF
    # generic supplied by C1560).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_5_pico_farad",
    })

    # Extended house part C1654 supplies this previously absent 0603 value
    # (FH 0603CG240J500NT, 24 pF 50 V C0G +/-5%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "24_pico_farad",
    })

    # Extended house part C1655 supplies this previously absent 0603 value
    # (FH 0603CG250J500NT, 25 pF 50 V C0G +/-5%, the first reviewed choice;
    # distinct from the 0402 25 pF generic supplied by C1556).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "25_pico_farad",
    })

    # C1645 is the FH (Guangdong Fenghua Advanced Tech) C0G +/-5% SKU for the
    # generic 0603 150 pF value. The reviewed Basic preference C1594 (same
    # maker, X7R +/-10%) keeps the plain generic ID, so this exact purchasing
    # identity gets its own linked row following the established maker/mpn
    # variant taxonomy; the C0G option must not silently replace the X7R
    # preference either.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "150_pico_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603cg151j500nt",
    })

    # C1590 is Samsung's 25 V 0603 100 nF X7R +/-10% SKU. The generic 0603
    # 100 nF preference (C14663, 50 V) stays intact; this lower-voltage
    # purchasing identity is an explicit linked rated variant following the
    # C1592 16 V precedent.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "25_volt",
    })

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "150_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "220_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "3_3_nano_farad",
    })

    # Extended house part C1587 supplies this previously absent 0603 value
    # (FH 0603B512K500NT, 5.1 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "5_1_nano_farad",
    })

    # Extended house part C1593 supplies this previously absent 0603 value
    # (FH 0603B123K500NT, 12 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "12_nano_farad",
    })

    # Extended house part C1595 supplies this previously absent 0603 value
    # (FH 0603B152K500NT, 1.5 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_5_nano_farad",
    })

    # Extended house part C1596 supplies this previously absent 0603 value
    # (FH 0603B153K500NT, 15 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 15 nF Y5V generic supplied by C1583).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "15_nano_farad",
    })

    # Extended house part C1597 supplies this previously absent 0603 value
    # (FH 0603B154K500NT, 150 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "150_nano_farad",
    })

    # Extended house part C1598 supplies this previously absent 0603 value
    # (FH 0603B181K500NT, 180 pF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "180_pico_farad",
    })

    # Extended house part C1599 supplies this previously absent 0603 value
    # (FH 0603B182K500NT, 1.8 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "1_8_nano_farad",
    })

    # Extended house part C1600 supplies this previously absent 0603 value
    # (FH 0603B201K500NT, 200 pF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 200 pF generic supplied by C1529).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "200_pico_farad",
    })

    # Extended house part C1601 supplies this previously absent 0603 value
    # (FH 0603B202K500NT, 2 nF 50 V X7R +/-10%, the first reviewed choice;
    # distinct from the 0402 2.2 nF generic supplied by C1531).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2_nano_farad",
    })

    # Extended house part C1602 supplies this previously absent 0603 value
    # (FH 0603B203K500NT, 20 nF 50 V X7R +/-10%, the first reviewed choice).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "20_nano_farad",
    })

    # C1606 is the FH (Guangdong Fenghua Advanced Tech) equivalent-spec SKU
    # for the generic 0603 220 nF value (25 V, X7R, +/-10%). The reviewed
    # Basic preference C21120 (Samsung CL10B224KA8NNNC) keeps the plain
    # generic ID, so this exact purchasing identity gets its own linked row
    # following the established maker/mpn variant taxonomy (as with the
    # Samsung C1591 and C1524 rows).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "220_nano_farad",
        "taxonomy_5": "fenghua_adv_tech",
        "taxonomy_6": "0603b224k250nt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "47_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "470_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "6_8_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "15_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "30_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "330_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "100_pico_farad",
    })
    # Missing generic values supplied by Basic C21117, C21120 and C21122.
    for value in ("33_nano_farad", "220_nano_farad", "22_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0603",
            "taxonomy_4": value,
        })
    # Basic C53987 and C1322360 fill these 0603 values.
    for value in ("4_7_nano_farad", "8_2_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0603",
            "taxonomy_4": value,
        })
    # JLC Basic C38523 supplies this previously absent 0603 value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "12_pico_farad",
    })

    # C19666 is a 16 V Basic choice. Keep the existing generic 0603 4.7 uF
    # purchase preference at 25 V and represent this lower-rated SKU explicitly.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_5": "16_volt",
    })

    # C96446 is rated 25 V but has +/-20% tolerance. Keep the generic
    # 0603 10 uF preference at +/-10% and expose this SKU explicitly.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "25_volt",
        "taxonomy_6": "20_percent",
    })

    sizes = ["0805"]
    capacitance_values = [
        "4_7_micro_farad",
        "10_micro_farad",
        "22_micro_farad",
        "47_micro_farad",
    ]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "10_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "22_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "33_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "4_7_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "100_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "20_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "22_pico_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "470_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "47_pico_farad",
    })
    # New compatible generic values supplied by Basic C28233, C28260,
    # C28323 and C46653.
    for value in ("100_nano_farad", "2_2_nano_farad", "1_micro_farad", "1_nano_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0805",
            "taxonomy_4": value,
        })
    # Basic C53134, C107145 and C377773 fill these 0805 values.
    for value in ("47_nano_farad", "220_pico_farad", "2_2_micro_farad"):
        options.append({
            "taxonomy_2": "capacitor",
            "taxonomy_3": "0805",
            "taxonomy_4": value,
        })
    # Keep the 100 V C28233 generic preference; C49678 is the 50 V variant.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "100_nano_farad",
        "taxonomy_5": "50_volt",
    })

    # C440198 is a 50 V Basic option alongside the generic 25 V preference.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "10_micro_farad",
        "taxonomy_5": "50_volt",
    })

    sizes = ["1206"]
    capacitance_values = ["10_micro_farad", "47_micro_farad"]
    for size in sizes:
        for capacitance_value in capacitance_values:
            option = {}
            option["taxonomy_2"] = "capacitor"
            option["taxonomy_3"] = size
            option["taxonomy_4"] = capacitance_value
            options.append(option)

    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "10_nano_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "1_nano_farad",
        "taxonomy_5": "2000_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_nano_farad",
    })
    # Basic C29823 supplies the new 1206 4.7 uF generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_micro_farad",
    })
    # Basic C50254 supplies the previously absent 1206 2.2 uF generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "2_2_micro_farad",
    })
    # The 100 uF 1206 house SKU is only 6.3 V and +/-20%; keep both ratings
    # explicit rather than assigning it to an unrated generic value.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "100_micro_farad",
        "taxonomy_5": "6_3_volt",
        "taxonomy_6": "20_percent",
    })

    sizes = ["3216_avx_a"]
    capacitor_styles = ["tantalum"]
    capacitance_values = ["4_7_micro_farad"]
    voltages = ["16_volt"]
    for size in sizes:
        for capacitor_style in capacitor_styles:
            for capacitance_value in capacitance_values:
                for voltage in voltages:
                    option = {}
                    option["taxonomy_2"] = "capacitor"
                    option["taxonomy_3"] = size
                    option["taxonomy_4"] = capacitor_style
                    option["taxonomy_5"] = capacitance_value
                    option["taxonomy_6"] = voltage
                    options.append(option)

    # Tranche-98: the AVX TAJ CASE-A tantalum ladder (the queue lists the
    # maker as "--"; TAJ is Kyocera AVX's molded tantalum series). Exact
    # purchasing identities ride the tantalum grid taxonomy.
    for capacitance_value, voltage, mpn, size in [
        ("100_nano_farad", "35_volt", "taja104k035rnej", "3216_avx_a"),
        ("1_micro_farad", "16_volt", "taja105k016rnej", "3216_avx_a"),
        ("1_micro_farad", "25_volt", "taja105k025rnej", "3216_avx_a"),
        ("1_micro_farad", "35_volt", "taja105k035rnej", "3216_avx_a"),
        ("10_micro_farad", "10_volt", "taja106k010rnej", "3216_avx_a"),
        # Tranche-99: the rest of the TAJA ladder. TAJA226M is the 20-percent
        # (M) tolerance sibling of the 22uF/10V K part.
        ("1_5_micro_farad", "16_volt", "taja155k016rnej", "3216_avx_a"),
        ("2_2_micro_farad", "16_volt", "taja225k016rnej", "3216_avx_a"),
        ("2_2_micro_farad", "25_volt", "taja225k025rnej", "3216_avx_a"),
        ("22_micro_farad", "6_3_volt", "taja226k006rnej", "3216_avx_a"),
        ("22_micro_farad", "10_volt", "taja226m010rnej", "3216_avx_a"),
        ("3_3_micro_farad", "16_volt", "taja335k016rnej", "3216_avx_a"),
        ("33_micro_farad", "6_3_volt", "taja336k006rnej", "3216_avx_a"),
        ("33_micro_farad", "10_volt", "taja336k010rnej", "3216_avx_a"),
        ("4_7_micro_farad", "16_volt", "taja475k016rnej", "3216_avx_a"),
        ("4_7_micro_farad", "20_volt", "taja475k020rnej", "3216_avx_a"),
        ("4_7_micro_farad", "25_volt", "taja475k025rnej", "3216_avx_a"),
        ("47_micro_farad", "6_3_volt", "taja476k006rnej", "3216_avx_a"),
        # Tranche-100: the TAJA 6.8uF rail and the bigger TAJB CASE-B
        # (3528-21) ladder; the 004 voltage code is 4V. 3528_avx_b is a new
        # size token.
        ("6_8_micro_farad", "16_volt", "taja685k016rnej", "3216_avx_a"),
        ("1_micro_farad", "35_volt", "tajb105k035rnej", "3528_avx_b"),
        ("10_micro_farad", "16_volt", "tajb106k016rnej", "3528_avx_b"),
        ("10_micro_farad", "25_volt", "tajb106k025rnej", "3528_avx_b"),
        ("100_micro_farad", "6_3_volt", "tajb107m006rnej", "3528_avx_b"),
        ("100_micro_farad", "10_volt", "tajb107m010rnej", "3528_avx_b"),
        ("22_micro_farad", "10_volt", "tajb226k010rnej", "3528_avx_b"),
        ("22_micro_farad", "20_volt", "tajb226k020rnej", "3528_avx_b"),
        ("220_micro_farad", "4_volt", "tajb227m004rnej", "3528_avx_b"),
        ("3_3_micro_farad", "35_volt", "tajb335k035rnej", "3528_avx_b"),
        ("33_micro_farad", "10_volt", "tajb336k010rnej", "3528_avx_b"),
        ("33_micro_farad", "16_volt", "tajb336k016rnej", "3528_avx_b"),
        # Tranche-101: the TAJB 475/476 rails and the TAJC CASE-C (6032-28)
        # ladder; 6032_avx_c is a new size token.
        ("4_7_micro_farad", "16_volt", "tajb475k016rnej", "3528_avx_b"),
        ("4_7_micro_farad", "25_volt", "tajb475k025rnej", "3528_avx_b"),
        ("4_7_micro_farad", "35_volt", "tajb475k035rnej", "3528_avx_b"),
        ("47_micro_farad", "6_3_volt", "tajb476k006rnej", "3528_avx_b"),
        ("47_micro_farad", "6_3_volt", "tajb476m006rnej", "3528_avx_b"),
        ("10_micro_farad", "16_volt", "tajc106k016rnej", "6032_avx_c"),
        ("10_micro_farad", "25_volt", "tajc106k025rnej", "6032_avx_c"),
        ("10_micro_farad", "35_volt", "tajc106k035rnej", "6032_avx_c"),
        ("22_micro_farad", "25_volt", "tajc226k025rnej", "6032_avx_c"),
        ("220_micro_farad", "6_3_volt", "tajc227k006rnej", "6032_avx_c"),
        ("33_micro_farad", "16_volt", "tajc336k016rnej", "6032_avx_c"),
        ("47_micro_farad", "16_volt", "tajc476k016rnej", "6032_avx_c"),
        # Tranche-102: the TAJC 68uF rail, the big TAJD CASE-D (7343-31)
        # ladder and two TAJE CASE-E (7343-43) parts; 7343_avx_d and
        # 7343_avx_e are new size tokens.
        ("68_micro_farad", "16_volt", "tajc686k016rnej", "6032_avx_c"),
        ("10_micro_farad", "35_volt", "tajd106k035rnej", "7343_avx_d"),
        ("100_micro_farad", "10_volt", "tajd107k010rnej", "7343_avx_d"),
        ("100_micro_farad", "16_volt", "tajd107k016rnej", "7343_avx_d"),
        ("100_micro_farad", "20_volt", "tajd107k020rnej", "7343_avx_d"),
        ("22_micro_farad", "35_volt", "tajd226k035rnej", "7343_avx_d"),
        ("330_micro_farad", "10_volt", "tajd337k010rnej", "7343_avx_d"),
        ("47_micro_farad", "16_volt", "tajd476k016rnej", "7343_avx_d"),
        ("47_micro_farad", "25_volt", "tajd476k025rnej", "7343_avx_d"),
        ("470_micro_farad", "6_3_volt", "tajd477k006rnej", "7343_avx_d"),
        ("100_micro_farad", "25_volt", "taje107m025rnej", "7343_avx_e"),
        ("220_micro_farad", "16_volt", "taje227k016rnej", "7343_avx_e"),
        # Tranche-103: the TAJE 330uF/47uF/470uF rails and one TAJR low-ESR
        # 10uF in the small CASE-R (2012-12) body; 2012_avx_r is a new size
        # token.
        ("330_micro_farad", "10_volt", "taje337k010rnej", "7343_avx_e"),
        ("47_micro_farad", "35_volt", "taje476k035rnej", "7343_avx_e"),
        ("470_micro_farad", "10_volt", "taje477k010rnej", "7343_avx_e"),
        ("10_micro_farad", "6_3_volt", "tajr106m006rnej", "2012_avx_r"),
    ]:
        option = {
            "taxonomy_2": "capacitor",
            "taxonomy_3": size,
            "taxonomy_4": "tantalum",
            "taxonomy_5": capacitance_value,
            "taxonomy_6": voltage,
            "taxonomy_14": "avx",
            "taxonomy_15": mpn,
        }
        options.append(option)
        if capacitance_value == "1_micro_farad" and voltage == "16_volt":
            option["name_short"] = "1uF 16V Tantalum CASE-A (AVX TAJA105K016RNJ)"

    # Tranche-103 also brings the Samsung 1206 4.7uF X5R MLCC exact row.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "4_7_micro_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl31a475kohnnne",
        "name_short": "4.7uF 16V X5R 1206 (Samsung CL31A475KOHNNNE)",
    })

    sizes = [
        "6_3_mm_diameter_5_4_mm_tall",
        "6_3_mm_diameter_7_7_mm_tall",
        "8_mm_diameter_6_5_mm_tall",
    ]
    capacitor_styles = ["electrolytic"]
    capacitance_values = ["220_micro_farad"]
    voltages = ["10_volt"]
    for size in sizes:
        for capacitor_style in capacitor_styles:
            for capacitance_value in capacitance_values:
                for voltage in voltages:
                    option = {}
                    option["taxonomy_2"] = "capacitor"
                    option["taxonomy_3"] = size
                    option["taxonomy_4"] = capacitor_style
                    option["taxonomy_5"] = capacitance_value
                    option["taxonomy_6"] = voltage
                    options.append(option)

    # Easyduino ESP32: keep the value/voltage pair explicit, not a cross-product.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "3216_avx_a",
        "taxonomy_4": "tantalum",
        "taxonomy_5": "22_micro_farad",
        "taxonomy_6": "10_volt",
    })

    # Soldered 1210C_tantal 68uF and the 8 mm radial electrolytic (the fitted
    # MPN's "681" code is 68x10 = 680 uF at 16 V).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1210",
        "taxonomy_4": "68_micro_farad",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_14_5_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "680_micro_farad",
        "taxonomy_6": "16_volt",
    })

    # Extended house part C5154 supplies the 8x14 mm can (CX GR477M025F14,
    # 470 uF 25 V, the first reviewed choice).  C5153's 0805 220 nF X7R 25 V
    # is a second source on an already-populated generic whose preferred code
    # is taken, so it gets its own Samsung exact row below.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "8_mm_diameter_14_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "470_micro_farad",
        "taxonomy_6": "25_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "220_nano_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl21b224kafnnne",
        "name_short": "220nF 25V X7R 0805 (Samsung CL21B224KAFNNNE)",
    })

    # Extended house parts C5296/C5300: the 0402 1.8nF X7R (Samsung, first
    # reviewed choice) and the 10x17 mm 15 uF 400 V can (CX).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0402",
        "taxonomy_4": "1_8_nano_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl05b182kb5nnnc",
        "name_short": "1.8nF 50V X7R 0402 (Samsung CL05B182KB5NNNC)",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "10_mm_diameter_17_mm_tall",
        "taxonomy_4": "electrolytic",
        "taxonomy_5": "15_micro_farad",
        "taxonomy_6": "400_volt",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0603",
        "taxonomy_4": "2200_pico_farad",
    })
    # C5422: Samsung Y5V 1 uF 50 V 0805 exact purchasing identity (first
    # reviewed preferred choice; the Y5V dielectric rides only in the record).
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "1_micro_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl21f105zbfnnne",
        "name_short": "1uF 50V Y5V 0805 (Samsung CL21F105ZBFNNNE)",
    })
    # C5672/C5674: the 22 uF X5R pair in 1206 (10 V) and 0805 (6.3 V) bodies.
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "1206",
        "taxonomy_4": "22_micro_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl31a226kphnnne",
        "name_short": "22uF 10V X5R 1206 (Samsung CL31A226KPHNNNE)",
    })
    options.append({
        "taxonomy_2": "capacitor",
        "taxonomy_3": "0805",
        "taxonomy_4": "22_micro_farad",
        "taxonomy_14": "samsung_electro_mechanics",
        "taxonomy_15": "cl21a226mqqnnne",
        "name_short": "22uF 6.3V X5R 0805 (Samsung CL21A226MQQNNNE)",
    })


if __name__ == "__main__":
    main()
