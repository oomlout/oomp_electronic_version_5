# Integration review — JLC C1532 / Fenghua 0402B223K500NT (generic 0402 22 nF)

Datasheet: shared Fenghua General Series MLCC specification via
`oomp_datasheet_common_with = electronic_capacitor_0402_100_pico_farad`
(sha256 verified against the C1532 import record). Ordering code (page 4)
decodes `0402B223K500NT` = 0402 / X7R / 223 = 22 nF / K = ±10% / 500 = 50 V.
The X7R 0402 table (page 9) lists 22 nF with the CA thickness code at every
voltage including 50 V — **the full selected suffix is covered**.

- code: C1532 | OOMP ID: `electronic_capacitor_0402_22_nano_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0402B223K500NT | 0402
- official page: https://jlcpcb.com/partdetail/1884-0402B223K500NT/C1532 (Basic)
- identity reconfirmed 2026-09-26 from the saved PDF; live page verified 2026-09-24.

## Electrical evidence

| Quantity | Value | Source |
| --- | --- | --- |
| Capacitance | 22 nF (code 223) | ordering page 4; X7R 0402 table page 9 |
| Tolerance | ±10% (K) | page 4 |
| Rated voltage | 50 V (code 500; table row includes 50 V) | pages 4, 9 |
| Dielectric | X7R (Class II) | page 4 |
| Temperature range | −55 to +125 °C, ±15% | page 5 |
| Thickness | 0.50 ±0.05 mm (CA) | pages 5, 9 |
| Polarization | none | two identical terminals |

## Terminal table

Terminals 1 and 2, passive, non-polarized end metallization.

## Mechanical table — 0402 (page 5)

L 1.00 ±0.05 mm, W 0.50 ±0.05 mm, T 0.50 ±0.05 mm, WB 0.25 ±0.05 mm.

## KiCad masters

`Device:C_Small`; `Capacitor_SMD:C_0402_1005Metric` (machine);
`Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` (hand).

## Population work

Technical block added to the existing C1532 inline-choice entry in
`working_oomp_populate_capacitor_extra.py`; the inline `set_preferred_jlc`
selection is synchronized from the record per the integration doc.

## Command log

Claimed 2026-09-26; X7R 0402 coverage verified on page 9 before proceeding.

## Unresolved work

None.
