# Integration review — JLC C1588 (CL10B102KB8NNNC, 1 nF 50 V X7R 0603)

Datasheet: Samsung Electro-Mechanics "Multilayer Ceramic Capacitors" general
catalogue (November 2015, 84 pages), stored at
`parts_source/electronic_capacitor_0402_100_nano_farad/datasheet.pdf` and
recorded via `oomp_datasheet_common_with` (C1588 provenance in
`datasheet_source.yaml`: sha256 96baebe4…, the same Samsung catalogue JLC
attaches to the CL-series parts). Page references are PDF page indices.

- code: C1588 | OOMP ID: `electronic_capacitor_0603_1_nano_farad` (generic)
- maker: Samsung Electro-Mechanics | MPN: CL10B102KB8NNNC | package 0603
- official page: https://jlcpcb.com/partdetail/1940-CL10B102KB8NNNC/C1588 (Basic)
- identity reconfirmed live 2026-10-01 in the browser: JLCPCB Part # C1588,
  MFR.Part # CL10B102KB8NNNC, Basic badge, In Stock 7,814,954, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706978444034048-C1588.pdf).

## 1. Ordering-code decode (page 4) and lineup coverage (page 25)

`CL 10 B 102 K B 8 N N N C` (page 4 numbering system): CL = multilayer
ceramic capacitor; 10 = 0603 (1608 metric); B = X7R; 102 = 10 × 10² pF =
1 nF; K = ±10%; B = 50 V; 8 = 0.80 mm thickness; N = Ni/Cu/Ni-barrier/Sn
termination; N = normal product; N = control code; C = cardboard-tape 7″
reel.

The "Product Lineup (Standard & High Capacitors-X7R, X7S)" table (page 25)
row 51 lists `CL10B102KB8NNN□` = 1 nF, 50 V, ±10 %, 1.60 × 0.80 mm, thickness
max 0.90 mm; the □ is the packaging code filled by the last character
(page 74 table), so `CL10B102KB8NNNC` itself is covered. Note the X7R
range-bar chart (page 11) only reaches down to 0.1 µF — the per-part lineup
table on page 25 is the ordering-coverage evidence for the nF-range values.

## 2. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 1 nF (code 102) | p25 row 51; decode p4 |
| Tolerance | ±10% (code K) | p25; decode p4 |
| Rated voltage | 50 V (code B) | p25; decode p4 |
| Dielectric | X7R (Class II) | p5 class table; decode p4 |
| Temperature range | −55 °C to +125 °C | X7R class definition, p5 |
| Temperature characteristic | ±15% over the operating range (X7R) | p5 |
| Thickness | code 8 = 0.80 mm; lineup table T max 0.90 | p4; p25 |
| Capacitance measurement | 1 kHz ±10%, 1.0 ±0.2 Vrms (Class II) | family reliability/measurement section |
| Insulation resistance | ≥ 10 000 MΩ family requirement | family reliability section |

Polarization: none. DC-bias derating (Class II capacitance drops with applied
voltage) is an application-level consideration — the catalogue carries no
DC-bias curves; recorded as a note, not a rating. The generic ID stays
unchanged; the preference carries the ratings.

## 3. Terminal table

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | Ni-barrier termination, non-polarized |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:C_Small` — two-terminal non-polarized capacitor.

## 4. Mechanical table — 0603 (EIA 1608 metric)

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.60 × 0.80 mm size code | lineup table Size L×W, p25 |
| W | body width | 0.80 mm | same |
| T | thickness | 0.80 mm code 8, max 0.90 mm | `dimensions_mm.height`; p4 + p25 |
| Termination | Ni barrier / Sn plating | code N | p4 |

## 5. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — generic non-polarized capacitor, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0603_1608Metric` — official 1608 metric chip pads |
| Hand footprint | `Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder` — official HandSolder master (confirmed present in the installed KiCad 10 libraries) |

## 6. Population work

- `working_oomp_populate_capacitor_extra.py`: explicit 0603 1 nF X7R block
  with pins, `dimensions_mm`, `dimension_reference`, `kicad`, `electrical`,
  `research_notes`, `file_copy`.
- Registry selection synchronized from the record after the record edit.

## 7. Command log

- Claimed via `next --stage full --claim --code C1588 --worker solo` (2026-10-01).
- Live JLC page reconfirmed 2026-10-01 (browser).
- Shared Samsung catalogue: pages 4 (decode), 5 (X7R class), 11 (range chart
  — noted as NOT covering nF values), and 25 (Product Lineup row 51 =
  ordering coverage) rendered and read.
- Footprint masters confirmed present in the installed KiCad 10 libraries.

## 8. Unresolved work

- None.
