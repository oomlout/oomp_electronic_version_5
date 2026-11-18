# Integration review — JLC C1554 (0402CG200J500NT, 20 pF 50 V C0G 0402)

Datasheet: shared Fenghua General Series MLCC specification (30 pages,
"1005～1812 TYPE"), stored at
`parts_source/electronic_capacitor_0402_100_pico_farad/datasheet.pdf` and
recorded via `oomp_datasheet_common_with` (C1554 provenance in
`datasheet_source.yaml`: sha256 705023d3…, byte-identical across the C0G/X7R
siblings). Page references are PDF page indices; the same pages were rendered
and read for the C1547/C1548/C1549 siblings.

- code: C1554 | OOMP ID: `electronic_capacitor_0402_20_pico_farad` (generic)
- maker: FH (Guangdong Fenghua Advanced Tech) | MPN: 0402CG200J500NT | package 0402
- official page: https://jlcpcb.com/partdetail/1906-0402CG200J500NT/C1554 (Basic)
- identity reconfirmed live 2026-10-01 in the browser: JLCPCB Part # C1554,
  MFR.Part # 0402CG200J500NT, Basic badge, In Stock 662,756, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8770987774575165440-C1554.pdf).

## 1. Ordering-code decode (page 4, "How To Order")

`0402 C G 200 J 500 N T`: 0402 = 1.00 × 0.50 mm; CG = C0G; 200 = 20 × 10⁰ pF
= 20 pF; J = ±5%; 500 = 50 V; N = nickel-barrier termination; T = 7-inch
reel. The C0G 0402 capacitance/voltage table (page 6) lists 20 pF at 25 V and
50 V with the CA thickness code, so the document covers the full selected
suffix.

## 2. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 20 pF (code 200) | p4; C0G 0402 table p6 |
| Tolerance | ±5% (code J) | p4 tolerance table |
| Rated voltage | 50 V (code 500) | p4; C0G 0402 table p6 |
| Dielectric | C0G (Class I) | p4 dielectric table |
| Temperature range | −55 °C to +125 °C | C0G family specification (recorded in the C1546 anchor review) |
| Temperature characteristic | 0 ±30 ppm/°C referenced to 25 °C (C0G) | C0G family specification (recorded in the C1546 anchor review) |
| Thickness code | CA = 0.50 ±0.05 mm | p6 code table under the C0G 0402 columns |

Polarization: none. The generic ID stays unchanged; the preference carries
the ratings.

## 3. Terminal table

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | nickel-barrier termination, non-polarized |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:C_Small` — two-terminal non-polarized capacitor.

## 4. Mechanical table — 0402 (EIA 1005 metric, thickness code CA)

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.00 ±0.05 mm | nominal used for drawing |
| W | body width | 0.50 ±0.05 mm | nominal used for drawing |
| T | thickness | 0.50 ±0.05 mm | `dimensions_mm.height`; CA code, p6 |
| WB | terminal width | 0.25 ±0.05 mm | each end |

## 5. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — generic non-polarized capacitor, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0402_1005Metric` — official 1005 metric chip pads |
| Hand footprint | `Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` — official HandSolder master |

## 6. Population work

- `working_oomp_populate_capacitor_extra.py`: explicit 20 pF C0G block with
  pins, `dimensions_mm`, `dimension_reference`, `kicad`, `electrical`,
  `research_notes`, `file_copy` (own path; the physical PDF stays in the
  C1546 anchor folder per `oomp_datasheet_common_with`).
- Registry selection synchronized from the record after the record edit.

## 7. Command log

- Claimed via `next --stage full --claim --worker solo` (2026-10-01).
- Live JLC page reconfirmed 2026-10-01 (browser).
- Shared Fenghua PDF pages 4 and 6 rendered and read (ordering decode, C0G
  0402 coverage table).

## 8. Unresolved work

- None.
