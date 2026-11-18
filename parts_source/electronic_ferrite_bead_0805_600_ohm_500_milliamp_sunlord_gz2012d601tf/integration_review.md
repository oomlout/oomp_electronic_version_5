# Integration review — JLC C1017 / Sunlord GZ2012D601TF

Datasheet: `parts_source/electronic_ferrite_bead_0805_600_ohm_500_milliamp_sunlord_gz2012d601tf/datasheet.pdf`
= Shenzhen Sunlord Electronics "Multilayer Chip Ferrite Bead – GZ Series"
catalogue, revision 2024/6/19, 12 pages — byte-identical (md5
f20d70a757ca7f9be3973cdeddc90ef4) to the catalogue attached to C1002's page;
JLC serves the same series catalogue PDF from every GZ-series part page.
Read in full (as page images). Product identification (page 1) decodes every
suffix element of `GZ2012D601TF`: GZ = chip ferrite bead for general use;
2012 [0805] = 2.0 × 1.25 mm body; D = material code; 601 = 600 Ω nominal
impedance; T = tape & reel; F = hazardous-substance-free. The GZ2012 TYPE
specification table (page 3) lists `GZ2012D601TF` itself, so the document
covers the full selected ordering suffix.

- code: C1017 | OOMP ID: `electronic_ferrite_bead_0805_600_ohm_500_milliamp_sunlord_gz2012d601tf`
- maker: Sunlord | full MPN: GZ2012D601TF | package: 0805 (2012 metric)
- official page: https://jlcpcb.com/partdetail/Sunlord-GZ2012D601TF/C1017 (Basic)
- identity reconfirmed live 2026-09-30 in the browser: JLCPCB Part # C1017,
  MFR.Part # GZ2012D601TF, Basic badge, In Stock 370,403, and the page's
  datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8565214663970209792-C1017.pdf).
  PDF downloaded through the interactive browser on 2026-09-30 (sha256 in
  datasheet_source.yaml).

## 1. Electrical evidence (page 3, GZ2012 TYPE table; row GZ2012D601TF)

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Impedance Z | 600 Ω ±25% | at 100 MHz test frequency (page 3) |
| Max DC resistance | 0.30 Ω | DCR column, page 3 |
| Max rated current | 500 mA | Ir column, page 3 |
| Test frequency | 100 MHz | page 3 |
| Thickness T | 0.85 ±0.2 mm | page 3 thickness column (agrees with page 1) |
| Operating temperature | −55 to +125 °C | JLC listing specifications (intake capture, reconfirmed 2026-09-30); the catalogue prints no explicit range |
| Circuits | 1 | JLC listing specifications |
| Packing | tape & reel (suffix T) | page 1 decode |
| Material code | D | page 1 decode |
| RoHS | hazardous-substance-free (suffix F) | page 1 decode |
| Impedance curve | GZ2012D601TF Z/R/X vs frequency, Z peaking near 600 Ω | page 10 |

Rated-current derating (page 5): above +85 °C derating is required only for
beads rated 1000 mA and above, so it does not apply to this 500 mA part.

Intake classification (exact GZ2012D601TF identity) holds.

## 2. Terminal table (two-terminal non-polarized chip)

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | silver printed internal electrode, non-polarized |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:FerriteBead_Small`: two `pin passive line` entries
numbered "1" and "2". Count 2 = record `pin_count` = 2.

## 3. Mechanical table — 2012 [0805] (page 1, Shape and Dimensions; unit mm [inch])

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 2.0 (+0.3/−0.1) [.079 (+.012/−.004)] | nominal used for drawing |
| W | body width | 1.25 ±0.2 [.049 ±.008] | nominal used for drawing |
| T | thickness | 0.85 ±0.2 [.033 ±.008] | `dimensions_mm.height`; page 3 agrees |
| a | terminal width | 0.5 ±0.3 [.020 ±.012] | each end |

The catalogue has no land-pattern page; PCB land geometry comes from the
official KiCad master comparison below. The standard built-in 0805 chip
renderer draws the package from `dimensions_mm` (nominals 2.0 × 1.25).

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:FerriteBead_Small` — two passive line pins "1"/"2", matches the non-polarized two-terminal chip |
| Machine footprint | `Inductor_SMD:L_0805_2012Metric` — pads 1/2 at x = ∓1.0625 mm (2.125 mm pitch), 0.875 × 1.20 mm roundrect; fab body 2.0 × 1.25 = Sunlord nominals; 1.20 mm pad width covers the 0.5 ±0.3 terminal |
| Mechanical fit | Standard 0805 chip land pattern, symmetric part, no polarity mark |
| Hand footprint | `Inductor_SMD:L_0805_2012Metric_Pad1.05x1.20mm_HandSolder` — official HandSolder master (pads 1.05 × 1.20 at ±1.15), selected unchanged |

## 5. Population work

- `working_oomp_populate_ferrite_bead.py` already has the exact GZ2012D601TF
  row — no new row.
- `working_oomp_populate_ferrite_bead_extra.py`: explicit C1017 block with
  `electrical`, `dimensions_mm` + `ferrite_bead_dimensions_mm`,
  `dimension_reference`, `pins`, `kicad`, `research_notes`, `file_copy`.
- The population's automatic datasheet deduplication folds the
  byte-identical catalogue into the shared-PDF pointer.
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim --worker solo` → C1017 (2026-09-30).
- Live JLC page reconfirmed 2026-09-30 (browser).
- Catalogue read in full (12 pages as page images; identity/decode/dimensions
  pages 1 and 3, curve page 10, derating note page 5).
- Symbol/footprint masters parsed from the installed KiCad 10 libraries.

## 7. Unresolved work

- None.
