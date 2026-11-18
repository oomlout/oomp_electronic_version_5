"""Populate magnetic transformer identities from project source data."""


def main(**kwargs):
    options = kwargs.get("options", [])
    options.append({
        "taxonomy_2": "transformer",
        "taxonomy_3": "surface_mount",
        "taxonomy_4": "usb",
        "taxonomy_14": "coilcraft",
        "taxonomy_15": "rfcmf1220100m4t",
        "name_short": "Coilcraft RFCMF1220100M4T USB Transformer",
    })


if __name__ == "__main__":
    main()
