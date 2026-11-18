# Integration review — JLC C1594 (0603B151K500NT, 150 pF 50 V X7R 0603)

Datasheet: shared Fenghua General Series MLCC specification (30 pages,
"1005～1812 TYPE"), stored at
`parts_source/electronic_capacitor_0402_100_pico_farad/datasheet.pdf` and
recorded via `oomp_datasheet_common_with` (C1594 provenance in
`datasheet_source.yaml`: sha256 705023d3…, byte-identical across the Fenghua
siblings). Page references are PDF page indices.

- code: C1594 | OOMP ID: `electronic_capacitor_0603_150_pico_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0603B151K500NT | package 0603
- official page: https://jlcpcb.com/partdetail/1902-0603B151K500NT/C1594 (Basic)
- identity reconfirmed live 2026-10-01 in the browser: JLCPCB Part # C1594,
  MFR.Part # 0603B151K500NT, Basic badge, In Stock 225,016, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987892963590144-C1594.pdf).

## 1. Ordering-code decode (page 4) and X7R 0603 coverage (page 10)

`0603 B 151 K 500 N T`: 0603 = 1.60 × 0.80 mm; B = X7R (page 4 dielectric
table); 151 = 15 × 10¹ pF = 150 pF; K = ±10%; 500 = 50 V; N = nickel-barrier
termination; T = 7-inch reel. The X7R 0603 capacitance/voltage table
(page 10, "X7R 系列" columns) lists 150 pF at 6.3–50 V with the DA thickness
code (0.80 ±0.10 mm), so the document covers the full selected suffix.

## 2. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 150 pF (code 151) | p4 decode; X7R 0603 table p10 |
| Tolerance | ±10% (code K) | p4 |
| Rated voltage | 50 V (code 500) | p4; X7R 0603 table p10 |
| Dielectric | X7R (Class II) | p4 dielectric table; p10 X7R 系列 |
| Temperature range | −55 °C to +125 °C | X7R temperature characteristic table, p5 |
| Temperature characteristic | ±15% over the operating range (X7R) | p5 |
| Thickness code | DA = 0.80 ±0.10 mm | p10 code table |
| Insulation resistance | ≥ 50 000 MΩ (C ≤ 10 nF) | family reliability test methods, p16 |

Polarization: none. DC-bias derating (Class II) is an application-level
consideration — no curves in the catalogue. The generic ID stays unchanged;
the preference carries the ratings.

## 3. Terminal table

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | nickel-barrier termination, non-polarized |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:C_Small` — two-terminal non-polarized capacitor.

## 4. Mechanical table — 0603 (EIA 1608 metric)

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.60 × 0.80 mm size code | page 10 header (1.6mm×0.8mm) |
| W | body width | 0.80 mm | same |
| T | thickness | 0.80 ±0.10 mm | DA code, p10; `dimensions_mm.height` |
| WB | terminal width | 0.25 ±0.05 mm (0603 family drawing) | family dimension table |

## 5. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — generic non-polarized capacitor, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0603_1608Metric` — official 1608 metric chip pads |
| Hand footprint | `Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder` — official HandSolder master |

## 6. Population work

- `working_oomp_populate_capacitor_extra.py`: explicit 0603 150 pF X7R block
  with pins, `dimensions_mm`, `dimension_reference`, `kicad`, `electrical`,
  `research_notes`, `file_copy` (own path; the physical PDF stays in the
  C1546 anchor folder per `oomp_datasheet_common_with`).
- Registry selection synchronized from the record after the record edit.

## 7. Command log

- Claimed via `next --stage full --claim --worker solo` (2026-10-01).
- Live JLC page reconfirmed 2026-10-01 (browser).
- Shared Fenghua PDF pages 4 (decode) and 10 (X7R 0603 table) rendered and
  read.
- Footprint masters confirmed present in the installed KiCad 10 libraries.

## 8. Unresolved work

- None.
