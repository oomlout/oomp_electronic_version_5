# Integration review — JLC C1035 / Sunlord SDFL1608S100KTF

Datasheet: `parts_source/electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf/datasheet.pdf`
= Shenzhen Sunlord Electronics "Multilayer Chip Ferrite Inductor – SDFL
Series" catalogue, revised 2025/5/23, 6 pages (scanned images; read page by
page as rendered images). Product identification (page 1) decodes every
suffix element of `SDFL1608S100KTF`: SDFL = chip ferrite inductor; 1608
[0603] = 1.6 × 0.8 mm body; Q = material code (L/P/Q/S/T); S100 = nominal
inductance 10 µH (code table: R is the decimal point, N = nH; 100 in the µH
code = 10 × 10⁰ µH); K = ±10% tolerance; T = tape & reel; F =
hazardous-substance-free. The SDFL1608 Series specification table (page 3)
lists `SDFL1608S100 □ TF` itself, so the document covers the full selected
ordering suffix.

- code: C1035 | OOMP ID: `electronic_inductor_0603_10_micro_henry_sunlord_sdfl1608s100ktf`
- maker: Sunlord | full MPN: SDFL1608S100KTF | package: 0603 (1608 metric)
- official page: https://jlcpcb.com/partdetail/Sunlord-SDFL1608S100KTF/C1035 (Basic)
- identity reconfirmed live 2026-09-30 in the browser: JLCPCB Part # C1035,
  MFR.Part # SDFL1608S100KTF, Basic badge, In Stock 794,898, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8755215265330278400-C1035.pdf).
  PDF downloaded through the interactive browser on 2026-09-30 (sha256 in
  datasheet_source.yaml).

## 1. Electrical evidence (page 3, SDFL1608 Series table; row SDFL1608S100 □ TF)

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Inductance L | 10 µH | page 3 |
| Tolerance | ±10% (code K) | page 1 decode |
| Min Q | 30 | at the 2 MHz L,Q test frequency, page 3 |
| L, Q test frequency | 2 MHz | page 3 |
| Min self-resonant frequency | 17 MHz | S.R.F. column, page 3 |
| Max DC resistance | 1.85 Ω | DCR column, page 3 |
| Max rated current | 3 mA | Ir column, page 3 |
| Thickness T | 0.8 ±0.15 mm | page 3 (agrees with page 1) |
| Operating temperature | −40 °C to +85 °C | page 1 "Operating Temp" |
| Packing | tape & reel (suffix T) | page 1 decode |
| RoHS | hazardous-substance-free (suffix F) | page 1 decode |

Monolithic ferrite chip inductor with magnetic shielding (no cross-coupling),
suitable for reflow or wave soldering (page 1 features). Intake classification
(exact SDFL1608S100KTF identity, distinct from the generic 0603 10 µH row)
holds; the 3 mA / 1.85 Ω ratings stay attached to this exact purchasing
choice, not to the generic.

## 2. Terminal table (two-terminal non-polarized chip)

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | non-polarized chip inductor termination |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:L`: two passive pins "1"/"2". Count 2 = record
`pin_count` = 2.

## 3. Mechanical table — SDFL1608 [0603] (page 1, Shape and Dimensions; unit mm [inch])

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.6 ±0.15 [.063 ±.006] | nominal used for drawing |
| W | body width | 0.8 ±0.15 [.031 ±.006] | nominal used for drawing |
| T | thickness | 0.8 ±0.15 [.031 ±.006] | `dimensions_mm.height`; page 3 agrees |
| a | terminal width | 0.3 ±0.2 [.012 ±.008] | each end |

The catalogue has no land-pattern page; PCB land geometry comes from the
official KiCad master comparison below. The standard built-in 0603 chip
renderer draws the package from `dimensions_mm` (nominals 1.6 × 0.8).

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:L` — generic two-terminal inductor, pins 1/2 passive |
| Machine footprint | `Inductor_SMD:L_0603_1608Metric` — pads 1/2 at x = ∓0.7875 mm (1.575 mm pitch), 0.875 × 0.95 mm roundrect; fab body 1.6 × 0.8 = Sunlord nominals; 0.95 mm pad width covers the 0.3 ±0.2 terminal |
| Mechanical fit | Standard 0603 chip land pattern, symmetric part, no polarity mark |
| Hand footprint | `Inductor_SMD:L_0603_1608Metric_Pad1.05x0.95mm_HandSolder` — official HandSolder master (pads 1.05 × 0.95 at ±0.875), selected unchanged |

## 5. Population work

- `working_oomp_populate_inductor.py` already has the exact Sunlord row — no
  new row.
- `working_oomp_populate_inductor_extra.py`: explicit C1035 block with
  `electrical`, `dimensions_mm`, `dimension_reference`, `pins`, `kicad`,
  `research_notes`, `file_copy`.
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim --worker solo` → C1035 (2026-09-30).
- Live JLC page reconfirmed 2026-09-30 (browser).
- Catalogue read in full (6 pages as page images; decode/dimensions/operating
  temperature page 1, SDFL1608 spec table page 3).
- Symbol/footprint masters parsed from the installed KiCad 10 libraries.

## 7. Unresolved work

- None.
