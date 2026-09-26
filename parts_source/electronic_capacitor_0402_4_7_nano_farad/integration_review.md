# Integration review — JLC C1538 / Fenghua 0402B472K500NT (generic 0402 4.7 nF)

Datasheet: shared Fenghua General Series MLCC specification via
`oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad`
(sha256 verified against the C1538 import record). Ordering code (page 4)
decodes `0402B472K500NT` = 0402 / X7R / 472 = 4.7 nF / K = ±10% / 500 = 50 V.
The X7R 0402 table (page 9) lists 4.7 nF with the CA thickness code at every
voltage including 50 V — **the full selected suffix is covered**.

- code: C1538 | OOMP ID: `electronic_capacitor_0402_4_7_nano_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0402B472K500NT | 0402
- official page: https://jlcpcb.com/partdetail/C1538 (Basic, live-verified 2026-09-24)

## Electrical evidence

| Quantity | Value | Source |
| --- | --- | --- |
| Capacitance | 4.7 nF (code 472) | ordering page 4; X7R 0402 table page 9 |
| Tolerance | ±10% (K) | page 4 |
| Rated voltage | 50 V (code 500; table row includes 50 V) | pages 4, 9 |
| Dielectric | X7R (Class II) | page 4 |
| Temperature range | −55 to +125 °C, ±15% | page 5 |
| Thickness | 0.50 ±0.05 mm (CA) | pages 5, 9 |
| Polarization | none | two identical terminals |

## Terminals / mechanics / masters

Terminals 1 and 2, passive. 0402 (CA): L 1.00 ±0.05, W 0.50 ±0.05,
T 0.50 ±0.05, WB 0.25 ±0.05 mm (page 5). Masters: `Device:C_Small`,
`Capacitor_SMD:C_0402_1005Metric` (machine),
`Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` (hand).

## Population work

Standalone technical block added to `working_oomp_populate_capacitor_extra.py`;
registry-backed purchasing identity synchronized from the record.

## Command log

Claimed 2026-09-26; X7R 0402 coverage verified on page 9 before proceeding.

## Unresolved work

None.
