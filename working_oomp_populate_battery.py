"""Populate battery identities observed in source project schematics."""


def main(**kwargs):
    options = kwargs.get("options", [])
    options.append({
        "taxonomy_2": "battery",
        "taxonomy_3": "coin_cell",
        "taxonomy_4": "6_8_mm",
        "taxonomy_14": "maxell",
        "taxonomy_15": "ml414h",
        "name_short": "ML414H 6.8 mm Rechargeable Coin Cell",
    })


if __name__ == "__main__":
    main()
