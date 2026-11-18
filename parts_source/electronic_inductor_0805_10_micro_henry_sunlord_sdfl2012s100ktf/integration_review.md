# Integration review — JLC C1046 / Sunlord SDFL2012S100KTF

Datasheet: `parts_source/electronic_inductor_0805_10_micro_henry_sunlord_sdfl2012s100ktf/datasheet.pdf`
= Shenzhen Sunlord Electronics "Multilayer Chip Ferrite Inductor – SDFL
Series" catalogue, revised 2025/5/23, 6 pages — byte-identical (md5
821d20058dd7d3996389689c2d5e8686) to the catalogue attached to C1035's page;
JLC serves the same series catalogue PDF from every SDFL-series part page.
Read in full (as page images). Product identification (page 1) decodes every
suffix element of `SDFL2012S100KTF`: SDFL = chip ferrite inductor; 2012
[0805] = 2.0 × 1.25 mm body; S = material code (L/P/Q/S/T); S100 = nominal
inductance 10 µH (code table: R is the decimal point, N = nH; 100 in the µH
code = 10 × 10⁰ µH); K = ±10% tolerance; T = tape & reel; F =
hazardous-substance-free. The SDFL2012 Series specification table (page 4)
lists `SDFL2012S100 □ TF` itself, so the document covers the full selected
ordering suffix.

- code: C1046 | OOMP ID: `electronic_inductor_0805_10_micro_henry_sunlord_sdfl2012s100ktf`
- maker: Sunlord | full MPN: SDFL2012S100KTF | package: 0805 (2012 metric)
- official page: https://jlcpcb.com/partdetail/Sunlord-SDFL2012S100KTF/C1046 (Basic)
- identity reconfirmed live 2026-10-01 in the browser: JLCPCB Part # C1046,
  MFR.Part # SDFL2012S100KTF, Basic badge, In Stock 121,617, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8755216271270907904-C1046.pdf).
  PDF downloaded through the interactive browser on 2026-10-01 (sha256 in
  datasheet_source.yaml).

## 1. Electrical evidence (page 4, SDFL2012 Series table; row SDFL2012S100 □ TF)

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Inductance L | 10 µH | page 4 |
| Tolerance | ±10% (code K) | page 1 decode |
| Min Q | 50 | at the 2 MHz L,Q test frequency, page 4 |
| L, Q test frequency | 2 MHz | page 4 |
| Min self-resonant frequency | 24 MHz | S.R.F. column, page 4 |
| Max DC resistance | 1.15 Ω | DCR column, page 4 |
| Max rated current | 15 mA | Ir column, page 4 |
| Thickness T | 0.85 ±0.2 mm [0.033 ±.008 in] | page 4 thickness column (agrees with page 1) |
| Operating temperature | −40 °C to +85 °C | page 1 "Operating Temp" |
| Packing | tape & reel (suffix T) | page 1 decode |
| RoHS | hazardous-substance-free (suffix F) | page 1 decode |

Monolithic ferrite chip inductor with magnetic shielding (no cross-coupling),
suitable for reflow or wave soldering (page 1 features). Intake classification
(exact SDFL2012S100KTF identity, distinct from the generic 0805 10 µH row)
holds; the 15 mA / 1.15 Ω ratings stay attached to this exact purchasing
choice, not to the generic.

## 2. Terminal table (two-terminal non-polarized chip)

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | non-polarized chip inductor termination |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:L`: two passive pins "1"/"2". Count 2 = record
`pin_count` = 2.

## 3. Mechanical table — SDFL2012 [0805] (page 1, Shape and Dimensions; unit mm [inch])

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 2.0 (+0.3/−0.1) [.079 (+.012/−.004)] | nominal used for drawing |
| W | body width | 1.25 ±0.2 [.049 ±.008] | nominal used for drawing |
| T | thickness | 0.85 ±0.2 [.033 ±.008] | `dimensions_mm.height`; page 4 agrees |
| a | terminal width | 0.5 ±0.3 [.020 ±.012] | each end |

The catalogue has no land-pattern page; PCB land geometry comes from the
official KiCad master comparison below. The standard built-in 0805 chip
renderer draws the package from `dimensions_mm` (nominals 2.0 × 1.25).

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:L` — generic two-terminal inductor, pins 1/2 passive |
| Machine footprint | `Inductor_SMD:L_0805_2012Metric` — pads 1/2 at x = ∓1.0625 mm (2.125 mm pitch), 0.875 × 1.20 mm roundrect; fab body 2.0 × 1.25 = Sunlord nominals; 1.20 mm pad width covers the 0.5 ±0.3 terminal |
| Mechanical fit | Standard 0805 chip land pattern, symmetric part, no polarity mark |
| Hand footprint | `Inductor_SMD:L_0805_2012Metric_Pad1.05x1.20mm_HandSolder` — official HandSolder master (pads 1.05 × 1.20 at ±1.15), selected unchanged |

## 5. Population work

- `working_oomp_populate_inductor.py` already has the exact SDFL2012S100KTF
  row — no new row.
- `working_oomp_populate_inductor_extra.py`: explicit C1046 block with
  `electrical`, `dimensions_mm`, `dimension_reference`, `pins`, `kicad`,
  `research_notes`, `file_copy`.
- The population's automatic datasheet deduplication folds the
  byte-identical catalogue into the shared-PDF pointer.
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim --worker solo` → C1046 (2026-10-01).
- Live JLC page reconfirmed 2026-10-01 (browser).
- Catalogue read in full (6 pages as page images; decode/dimensions/operating
  temperature page 1, SDFL2012 spec table page 4).
- Symbol/footprint masters parsed from the installed KiCad 10 libraries
  (same 0805 masters already verified for C1015's ferrite bead work).

## 7. Unresolved work

- None.
