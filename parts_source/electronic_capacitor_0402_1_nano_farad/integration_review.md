# Integration review — JLC C1523 / Fenghua 0402B102K500NT (generic 0402 1 nF)

Datasheet: shared Fenghua General Series MLCC specification (30 pages), stored
at `parts_source/electronic_capacitor_0402_100_pico_farad/datasheet.pdf` and
recorded via `oomp_datasheet_common_with`; provenance sha256 matches the
C1523 import record. Ordering code section (page 4) decodes
`0402B102K500NT` = 0402 / B = X7R / 102 = 10×10² pF = 1 nF / K = ±10% /
500 = 50 V / NT packing. The X7R 0402 table (page 9) lists 1 nF at 50 V, so
the document covers the full selected suffix.

- code: C1523 | OOMP ID: `electronic_capacitor_0402_1_nano_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0402B102K500NT | package 0402
- official page: https://jlcpcb.com/partdetail/1875-0402B102K500NT/C1523 (Basic)
- identity reconfirmed 2026-09-26 from the saved PDF (ordering decode, X7R
  0402 1 nF/50 V coverage); live page verified 2026-09-24.

## 1. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 1 nF (code 102) | ordering code page 4; X7R 0402 table page 9 |
| Tolerance | ±10% (code K) | page 4 |
| Rated voltage | 50 V (code 500) | page 4; X7R 0402 table page 9 |
| Dielectric | X7R, Class II | page 4 |
| Temperature range | −55 °C to +125 °C | temperature characteristic table, page 5 |
| Temperature characteristic | ±15% over the operating range | page 5 |
| Insulation resistance | ≥ 50 000 MΩ (C ≤ 10 nF) | reliability test methods, page 16 |
| Capacitance measurement | 1 kHz ±10%, 1.0 ±0.2 Vrms (Class II, C ≤ 10 µF) | page 16 |

Polarization: none (monolithic Class II ceramic, two identical terminals).
DC-bias derating: the X7R capacitance drops with applied DC voltage; the
datasheet carries no DC-bias curves — recorded as an application-level
consideration, not a rating. The generic ID stays unchanged: the preference
carries the ratings, no rated variant needed.

## 2. Terminal table

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | end metallization, non-polarized |
| 2 | terminal 2 | passive | end metallization, non-polarized |

KiCad symbol `Device:C_Small` is a two-terminal non-polarized capacitor —
terminal numbering is arbitrary and consistent.

## 3. Mechanical table — 0402 (EIA 1005 metric, thickness code CA, page 5)

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.00 ±0.05 mm | nominal used for drawing |
| W | body width | 0.50 ±0.05 mm | nominal used for drawing |
| T | thickness | 0.50 ±0.05 mm | `dimensions_mm.height` |
| WB | terminal width | 0.25 ±0.05 mm | each end |

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — generic non-polarized capacitor, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0402_1005Metric` — official 1005 metric chip pads, fits the 1.00 × 0.50 body |
| Hand footprint | `Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` — actual official HandSolder master for this package |

## 5. Population work

- `working_oomp_populate_capacitor_extra.py`: explicit block with pins,
  `dimensions_mm`, `dimension_reference`, `kicad`, `electrical`, `research_notes`,
  `file_copy` (shared-PDF source resolved automatically by the pipeline).
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- Claimed via `next --stage full --claim` (2026-09-26).
- Datasheet sections read: ordering (4), dimensions (5), X7R characteristics (5),
  X7R 0402 coverage (9), reliability/measurement (16).
- Footprint masters confirmed present in the installed KiCad 10 libraries.

## 7. Unresolved work

- None.
