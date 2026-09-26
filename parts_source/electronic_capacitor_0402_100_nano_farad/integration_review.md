# Integration review — JLC C1525 / Samsung CL05B104KO5NNNC (generic 0402 100 nF)

Datasheet: Samsung MLCC catalogue (84 pages) saved at this part's
`parts_source/electronic_capacitor_0402_100_nano_farad/datasheet.pdf`
(own provenance record, sha256 verified at import). The X7R 0402 product
lineup (page 65) covers row CL05B104KO5NNN: 0402 (1.00 x 0.50 mm), 100 nF,
16 Vdc, ±10%, 0.55 mm maximum thickness. The purchased CL05B104KO5NNNC is
that same electrical row with the NNC packaging variant, defined by the
catalogue's own packaging specification section (referenced from the lineup
pages). Electrical identity covered exactly.

- code: C1525 | OOMP ID: `electronic_capacitor_0402_100_nano_farad` (generic)
- maker: Samsung Electro-Mechanics | MPN: CL05B104KO5NNNC | package 0402
- official page: https://jlcpcb.com/partdetail/1877-CL05B104KO5NNNC/C1525 (Basic)
- identity reconfirmed 2026-09-26 from the saved PDF; live page verified 2026-09-24.

## 1. Electrical evidence

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Capacitance | 100 nF (code 104) | X7R 0402 lineup, page 65 |
| Tolerance | ±10% (code K) | page 65 |
| Rated voltage | 16 Vdc (code O) | page 65 |
| Dielectric | X7R (Class II) | page 65 |
| Temperature range | −55 °C to +125 °C | X7R class definition |
| Thickness maximum | 0.55 mm | page 65 |
| Polarization | none | two identical end terminals |

DC-bias derating remains an application-level consideration (recorded in the
intake decision; no DC-bias curve in the catalogue). The generic ID keeps the
preference; the prior YAGEO C60474 alternative is preserved by the registry.

## 2. Terminal table

| Physical terminal | Function | Electrical type |
| --- | --- | --- |
| 1 | terminal 1 | passive |
| 2 | terminal 2 | passive |

## 3. Mechanical table — 0402 (page 65)

| Dim | Value | Note |
| --- | --- | --- |
| L x W | 1.00 x 0.50 mm | size row for CL05 |
| Thickness | 0.55 mm max | used as `dimensions_mm.height` |

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:C_Small` — non-polarized, two passive terminals |
| Machine footprint | `Capacitor_SMD:C_0402_1005Metric` — official 1005 metric pads |
| Hand footprint | `Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` — actual official HandSolder master |

## 5. Population work

Extended the existing LCSC-stock-research block in
`working_oomp_populate_capacitor_extra.py` with pins, `dimensions_mm`,
`dimension_reference`, `kicad`, `electrical`, `datasheet_url`, research notes
and `file_copy`. Registry selection synchronized from the record.

## 6. Command log

- Claimed via `next --stage full --claim` (2026-09-26).
- Datasheet pages read: X7R 0402 lineup (65), part numbering (23), packaging
  section (74-78, soldering/packing).
- Masters confirmed in installed KiCad 10 libraries.

## 7. Unresolved work

- None.
