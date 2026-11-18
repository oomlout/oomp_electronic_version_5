# Fenghua 1206 C0G local datasheet review

An existing local file, `parts/electronic_capacitor_1206_22_nano_farad_fenghua_adv_tech_1206f223m500nt/data/datasheet.pdf`, SHA-256 `705023d3be0454148a96fc2715d249a32d8ff442e70b64d1116d3490ed1d8136`, contains Fenghua General Type MLCC tables. No file was downloaded.

PDF page 7 (printed page 5) lists 1206 C0G at 25 V and 50 V with code FA for listed values from 0.1 pF to 8.2 nF; FA is 0.80 ± 0.20 mm thick. The table lists FA/FB for 10 nF and FA/FC for 12–33 nF. Values not explicitly listed should not be assumed to match.

The following existing C0G recipes use the unscaled 1.6 mm KiCad 1206 body. Some prior evidence relies on secondary listings, and not all values below are explicitly in the manufacturer table. Check the exact value, voltage and MPN against manufacturer documentation and resolve the discrepancy before changing renders. The general series table alone does not prove the thickness of every historical or special MPN. Do not silently overwrite earlier evidence or claim precise part-specific dimensions.

- `electronic_capacitor_1206_200_pico_farad`: 200 pF; represented MPN `1206CG201J500NT`.
- `electronic_capacitor_1206_22_pico_farad`: 22 pF; represented MPN `1206CG220J500NT`.
- `electronic_capacitor_1206_27_pico_farad`: 27 pF; represented MPN `1206CG270J500NT`.
- `electronic_capacitor_1206_30_pico_farad`: 30 pF; represented MPN `1206CG300J500NT`.
- `electronic_capacitor_1206_51_pico_farad`: 51 pF; represented MPN `1206CG510J500NT`.
- `electronic_capacitor_1206_62_pico_farad`: 62 pF; represented MPN `1206CG620J500NT`.
- `electronic_capacitor_1206_0_5_pico_farad`: 0.5 pF; represented MPN `1206CG0R5C500NT`.
- `electronic_capacitor_1206_1_5_pico_farad`: 1.5 pF; represented MPN `1206CG1R5C500NT`.
- `electronic_capacitor_1206_2_5_pico_farad`: 2.5 pF; represented MPN `1206CG2R5C500NT`.
- `electronic_capacitor_1206_2_7_pico_farad`: 2.7 pF; represented MPN `1206CG2R7C500NT`.
- `electronic_capacitor_1206_3_3_pico_farad`: 3.3 pF; represented MPN `1206CG3R3C500NT`.
- `electronic_capacitor_1206_6_pico_farad`: 6 pF; represented MPN `1206CG6R0C500NT`.
- `electronic_capacitor_1206_20_pico_farad`: 20 pF; represented MPN `1206CG200J500NT`.
