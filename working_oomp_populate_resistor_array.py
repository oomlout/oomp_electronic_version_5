def main(**kwargs):
    options = kwargs.get("options", [])

    packages = ["4_x_0402_convex", "4_x_0603_convex"]
    resistance_values = [330, 510, 10000, 100000, 1000000]
    for package in packages:
        for resistance_value in resistance_values:
            option = {}
            option["taxonomy_2"] = "resistor_array"
            option["taxonomy_3"] = package
            option["taxonomy_4"] = f"{resistance_value}_ohm"
            option["taxonomy_5"] = "8_pin"
            options.append(option)

    # JLC house-part array: UNI-ROYAL 4D03 convex 0603x4 network, 4.7 kohm.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "4700_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # JLC house-part array: UNI-ROYAL 4D03 convex 0603x4 network, 1 kohm.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "1000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1952: UNI-ROYAL 4D03 convex 0603x4 network,
    # 0 ohm (4 isolated jumpers, 62.5 mW per element), the first reviewed
    # choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "0_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1959: FH convex 0603x4 network, 30 ohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "30_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1966: FH convex 0603x4 network, 270 ohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "270_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1973: FH convex 0603x4 network, 1.5 kohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "1500_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1983: FH convex 0603x4 network, 6.8 kohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "6800_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1990: RALEC convex 0603x4 network, 30 kohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "30000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C1992: FH convex 0603x4 network, 36 kohm, the
    # first reviewed choice for this previously absent 0603x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0603_convex"
    option["taxonomy_4"] = "36000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2001: FH convex 0402x4 network, 0 ohm jumpers,
    # the first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "0_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2002: FH convex 0402x4 network, 3 ohm, the first
    # reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "3_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2004: FH convex 0402x4 network, 20 ohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "20_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2006: FH convex 0402x4 network, 27 ohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "27_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2007: FH convex 0402x4 network, 30 ohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "30_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2011: FH convex 0402x4 network, 200 ohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "200_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2017: FH convex 0402x4 network, 2.2 kohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "2200_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2018: FH convex 0402x4 network, 3.3 kohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "3300_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2021: FH convex 0402x4 network, 5.1 kohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "5100_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2022: FH convex 0402x4 network, 20 kohm, the
    # first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "20000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)

    # Extended house part C2028: UNI-ROYAL convex 0402x4 network, 47 kohm,
    # the first reviewed choice for this previously absent 0402x4 value.
    option = {}
    option["taxonomy_2"] = "resistor_array"
    option["taxonomy_3"] = "4_x_0402_convex"
    option["taxonomy_4"] = "47000_ohm"
    option["taxonomy_5"] = "8_pin"
    options.append(option)


if __name__ == "__main__":
    main()
