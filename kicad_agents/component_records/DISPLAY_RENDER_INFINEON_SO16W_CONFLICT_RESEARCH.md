# Infineon SOIC-16 wide-body package conflicts

Reviewed 2026-11-19. The three catalogue source records below contain `dimensions_mm: {length: 9.9, width: 3.9}` and no machine-solder footprint. Infineon identifies each exact orderable as SOIC 16W. Their manufacturer drawings specify 16-lead wide-body MS-013AA, with 10.00–10.65 mm body length, 7.40–7.60 mm body width, and 1.27 mm pitch. Both stored body dimensions conflict with the drawing, especially the width. Do not reuse a 3.9 mm narrow-SOIC render. A display of the exact MPN could use a validated wide-body model only with this discrepancy disclosed; the catalogue dimensions should be reconciled separately. Full top-marking evidence needs individual review; no recipe has been staged.

| Source ID | Manufacturer product evidence | Package drawing |
| --- | --- | --- |
| `electronic_ic_driver_half_bridge_gate_driver_soic_16_infineon_ir2110strpbf` | [IR2110STRPBF](https://www.infineon.com/part/IR2110S) | [IR2110/IR2113 datasheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-ir2110-datasheet-en.pdf) |
| `electronic_ic_driver_half_bridge_gate_driver_soic_16_infineon_ir2112spbf` | [IR2112SPBF](https://www.infineon.com/part/IR2112S) | [IR2112 datasheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-ir2112-ds-en.pdf) |
| `electronic_ic_driver_half_bridge_gate_driver_soic_16_infineon_ir2113strpbf` | [IR2113STRPBF](https://www.infineon.com/part/IR2113S) | [IR2110/IR2113 datasheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-ir2110-datasheet-en.pdf) |

The 2017 [Infineon information note](https://www.mouser.com/PCN/Infineon_1324_DISTI42_C4009659_Infonote.pdf) also lists IR2112SPBF as SOIC 16W. It concerns a lot-code change and does not establish an exact device identifier; do not treat its product table as a top-marking table.
