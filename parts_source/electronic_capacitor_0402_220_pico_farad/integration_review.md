# Integration review — JLC C1530 / Fenghua 0402B221K500NT (generic 0402 220 pF)

Datasheet: shared Fenghua General Series MLCC specification via
`oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad`
(sha256 matches the C1530 import record). Ordering code (page 4) decodes
`0402B221K500NT` = 0402 / B = X7R / 221 = 220 pF / K = ±10% / 500 = 50 V.

**Coverage gap found 2026-09-26:** the X7R 0402 table in this document
revision starts at 330 pF (page 9). The 220 pF rows that exist are the C0G
table (page 6) and the 01005 X7R table (page 8) — neither is the selected
0402 X7R row. The ordering table therefore does NOT cover the full selected
suffix, which the integration doc requires for full completion.

- code: C1530 | OOMP ID: `electronic_capacitor_0402_220_pico_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0402B221K500NT | 0402
- official page: https://jlcpcb.com/partdetail/C1530 (Basic, live-verified 2026-09-24)

## Verified facts (series-generic)

| Item | Value | Source |
| --- | --- | --- |
| Ordering decode | 0402 / X7R / 220 pF / ±10% / 50 V | page 4 |
| Body L x W | 1.00 ±0.05 x 0.50 ±0.05 mm | page 5 (CA code) |
| Thickness T | 0.50 ±0.05 mm | page 5 |
| Terminal width WB | 0.25 ±0.05 mm | page 5 |
| X7R range/characteristic | −55 to +125 °C, ±15% | page 5 |
| Terminals | 2, non-polarized, passive | page 4 product structure |

## Population work

Explicit block added to `working_oomp_populate_capacitor_extra.py` (pins,
`dimensions_mm`, `dimension_reference`, `kicad` with Device:C_Small +
C_0402_1005Metric + official HandSolder master, `electrical`, `research_notes`,
`file_copy`).

## Remaining task (recorded as the deferral reason)

Obtain a current Fenghua 0402 X7R datasheet (or the manufacturer product page)
whose ordering table lists the 0402 X7R 221 (220 pF) row at 50 V, then re-run
the full-stage gates and complete. Everything else is verified and in place.
