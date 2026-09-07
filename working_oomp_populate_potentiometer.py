def main(**kwargs):
    options = kwargs.get("options", [])
    options.append({
        "taxonomy_2": "potentiometer", "taxonomy_3": "trimmer", "taxonomy_4": "through_hole",
        "taxonomy_5": "10_kilo_ohm",
        "taxonomy_14": "bourns", "taxonomy_15": "tc33x_2_103e",
        "name_short": "Trimmer Potentiometer TC33X-2-103E 10k",
    })
    # Soldered PIR movement sensor R1: same TC33X trimmer, 1 megaohm ("105E").
    options.append({
        "taxonomy_2": "potentiometer", "taxonomy_3": "trimmer", "taxonomy_4": "through_hole",
        "taxonomy_5": "1_mega_ohm",
        "taxonomy_14": "bourns", "taxonomy_15": "tc33x_2_105e",
        "name_short": "Trimmer Potentiometer TC33X-2-105E 1M",
    })


if __name__ == "__main__":
    main()
