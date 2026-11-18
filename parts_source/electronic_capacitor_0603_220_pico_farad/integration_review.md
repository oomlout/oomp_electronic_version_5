# Integration review — JLC C1603 (CL10B221KB8NNNC, 220 pF 50 V X7R 0603)

Datasheet: Samsung Electro-Mechanics "Multilayer Ceramic Capacitors" general
catalogue (November 2015, 84 pages), stored at
`parts_source/electronic_capacitor_0402_100_nano_farad/datasheet.pdf` and
recorded via `oomp_datasheet_common_with` (C1603 provenance in
`datasheet_source.yaml`: sha256 96baebe4…, the same Samsung catalogue JLC
attaches to the CL-series parts). Page references are PDF page indices; the
key pages were rendered and read for the C1588 sibling and this part.

- code: C1603 | OOMP ID: `electronic_capacitor_0603_220_pico_farad` (generic)
- maker: Samsung Electro-Mechanics | MPN: CL10B221KB8NNNC | package 0603
- official page: https://jlcpcb.com/partdetail/1943-CL10B221KB8NNNC/C1603 (Basic)
- identity reconfirmed live 2026-10-01 in the browser: JLCPCB Part # C1603,
  MFR.Part # CL10B221KB8NNNC, Basic badge, In Stock 760,036, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579706990813036544-C1603.pdf).

## 1. Ordering-code decode (page 4) and lineup coverage (page 25)

`CL 10 B 221 K B 8 N N N C`: CL = MLCC; 10 = 0603 (1608 metric); B = X7R;
221 = 22 × 10¹ pF = 220 pF; K = ±10%; B = 50 V; 8 = 0.80 mm thickness;
N = Ni/Cu/Ni-barrier/Sn; N = normal; N = control; C = cardboard-tape 7″
reel. The X7R Product Lineup table (page 25) row 53 lists `CL10B221KB8NNN□`
= 220 pF, 50 V, ±10 %, 1.60 × 0.80 mm, thickness max 0.90 mm — the full
selected suffix is covered.

## 2. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 220 pF (code 221) | p25 row 53; decode p4 |
| Tolerance | ±10% (code K) | p25; decode p4 |
| Rated voltage | 50 V (code B) | p25; decode p4 |
| Dielectric | X7R (Class II) | p5 class table; decode p4 |
| Temperature range | −55 °C to +125 °C | X7R class definition, p5 |
| Temperature characteristic | ±15% over the operating range (X7R) | p5 |
| Thickness | code 8 = 0.80 mm; lineup table T max 0.90 | p4 + p25 |
| Capacitance measurement | 1 kHz ±10%, 1.0 ±0.2 Vrms (Class II) | family measurement section |

Polarization: none. DC-bias derating is an application-level consideration
(no curves in the catalogue). The generic ID stays unchanged; the preference
carries the ratings.

## 3. Terminal table

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | Ni-barrier termination, non-polarized |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:C_Small` — two-terminal non-polarized capacitor.

## 4. Mechanical table — 0603 (EIA 1608 metric)

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.60 mm | lineup table Size L×W, p25 |
| W | body width | 0.80 mm | same |
| T | thickness | 0.80 mm (code 8), max 0.90 mm | `dimensions_mm.height`; p4 + p25 |
| Termination | Ni barrier / Sn plating | code N | p4 |

## 5. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — generic non-polarized capacitor, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0603_1608Metric` — official 1608 metric chip pads |
| Hand footprint | `Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder` — official HandSolder master (same masters verified on the C1588 sibling) |

## 6. Population work

- `working_oomp_populate_capacitor_extra.py`: explicit 0603 220 pF X7R block
  with pins, `dimensions_mm`, `dimension_reference`, `kicad`, `electrical`,
  `research_notes`, `file_copy`.
- Registry selection synchronized from the record after the record edit.

## 7. Command log

- Claimed via `next --stage full --claim --worker solo` (2026-10-01).
- Live JLC page reconfirmed 2026-10-01 (browser).
- Shared Samsung catalogue page 25 (Product Lineup row 53) re-read from the
  already-rendered page image; decode page 4 previously read.
- Footprint masters confirmed present in the installed KiCad 10 libraries.

## 8. Unresolved work

- None.
