# Integration review — JLC C1002 / Sunlord GZ1608D601TF

Datasheet: `parts_source/electronic_ferrite_bead_0603_600_ohm_200_milliamp_sunlord_gz1608d601tf/datasheet.pdf`
= Shenzhen Sunlord Electronics "Multilayer Chip Ferrite Bead – GZ Series"
catalogue, revision 2024/6/19, 12 pages (scanned images, no text layer; read
page by page as rendered images). The product-identification section
(page 1) decodes every suffix element of `GZ1608D601TF`: GZ = chip ferrite
bead for general use; 1608 [0603] = 1.6 × 0.8 mm body; D = material code
(D/E/U); 601 = 600 Ω nominal impedance (code table: 300 = 30 Ω, 121 =
120 Ω, 102 = 1000 Ω); T = tape & reel; F = hazardous-substance-free. The
GZ1608 TYPE specification table (page 3) lists `GZ1608D601TF` itself, so the
document covers the full selected ordering suffix.

- code: C1002 | OOMP ID: `electronic_ferrite_bead_0603_600_ohm_200_milliamp_sunlord_gz1608d601tf`
- maker: Sunlord (Shenzhen Sunlord Electronics Co., Ltd) | full MPN: GZ1608D601TF | package: 0603 (1608 metric)
- official page: https://jlcpcb.com/partdetail/Sunlord-GZ1608D601TF/C1002 (Basic)
- identity reconfirmed live 2026-09-30 in the browser: JLCPCB Part # C1002,
  MFR.Part # GZ1608D601TF, Basic badge, In Stock 657,869, Minimum 1, and the
  page's datasheet link resolves to the same stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709915062976512-C1002.pdf).
  PDF downloaded through the interactive browser on 2026-09-30 (sha256
  recorded in datasheet_source.yaml).

## 1. Electrical evidence (page 3, GZ1608 TYPE table; row GZ1608D601TF)

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Impedance Z | 600 Ω ±25% | at 100 MHz test frequency (page 3) |
| Max DC resistance | 0.45 Ω | DCR column, page 3 |
| Max rated current | 200 mA | Ir column, page 3 |
| Test frequency | 100 MHz | Z test frequency column, page 3 |
| Thickness T | 0.8 ±0.15 mm [0.031 ±.006 in] | page 3 (agrees with page 1) |
| Operating temperature | −55 to +125 °C | JLC listing specifications (intake capture, reconfirmed 2026-09-30); the catalogue itself prints no explicit range |
| Circuits | 1 | JLC listing specifications |
| Packing | tape & reel (suffix T) | page 1 decode |
| Material code | D | page 1 decode |
| RoHS | hazardous-substance-free (suffix F) | page 1 decode |

Rated-current derating (page 5, "Rated Current"): above +85 °C derating is
required only for beads rated 1000 mA and above, so it does not apply to this
200 mA part. The GZ1608 D/E/U material comparison and the per-part R/X/Z
impedance curve for GZ1608D601TF (page 8) show Z peaking near the 600 Ω
region around the rated 100 MHz point — consistent with the table.

Intake classification (exact Sunlord GZ1608D601TF identity, distinct from the
generic unrated 0603 600 Ω 500 mA bead) holds against the datasheet.

## 2. Terminal table (page 1 outline drawing; two-terminal non-polarized chip)

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | silver printed internal electrode, non-polarized |
| 2 | terminal 2 | passive | silver printed internal electrode, non-polarized |

KiCad symbol `Device:FerriteBead_Small` is a two-terminal passive bead with
pins numbered "1" and "2" (parsed from the installed Device library: two
`pin passive line` entries, empty names). Count 2 = record `pin_count` = 2.

## 3. Mechanical table — GZ1608 [0603] (page 1, Shape and Dimensions; unit mm [inch])

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 1.6 ±0.15 [.063 ±.006] | nominal used for drawing |
| W | body width | 0.8 ±0.15 [.031 ±.006] | nominal used for drawing |
| T | thickness | 0.8 ±0.15 [.031 ±.006] | `dimensions_mm.height`; page 3 thickness column agrees |
| a | terminal width | 0.3 ±0.2 [.012 ±.008] | metallization at each end |

The catalogue has no land-pattern page; PCB land geometry comes from the
official KiCad master comparison below. The standard built-in 0603 chip
renderer draws the package from `dimensions_mm` (renderer default for the
0603 token is 1.6 × 0.8 — the verified nominals), so no custom
`package_drawing` is required.

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:FerriteBead_Small` — two passive line pins "1"/"2", matches the non-polarized two-terminal chip |
| Machine footprint | `Inductor_SMD:L_0603_1608Metric` (generator "SMD_2terminal_chip_molded") — pads 1/2 at x = ∓0.7875 mm (1.575 mm pitch), 0.875 × 0.95 mm roundrect; fab body 1.6 × 0.8 = Sunlord nominals; 0.95 mm pad width covers the 0.3 ±0.2 terminal; land extent 2.45 mm clears the 1.9 mm max body |
| Mechanical fit | Standard 0603 chip land pattern, no polarity mark needed (symmetric part) |
| Hand footprint | `Inductor_SMD:L_0603_1608Metric_Pad1.05x0.95mm_HandSolder` — actual official HandSolder master for this package (pads 1.05 × 0.95 at ±0.875), selected unchanged |

## 5. Population work

- `working_oomp_populate_ferrite_bead.py` already has the exact Sunlord row —
  no new row.
- `working_oomp_populate_ferrite_bead_extra.py`: explicit C1002 block with
  `part_number_manufacturer`-consistent identity fields, `electrical`,
  `dimensions_mm` + `ferrite_bead_dimensions_mm`, `dimension_reference`,
  `pins`, `kicad`, `research_notes`, `file_copy` (datasheet.pdf copy).
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim --code C1002 --worker solo` → C1002 (2026-09-30).
- Live JLC page reconfirmed 2026-09-30 (browser).
- Datasheet read in full (12 pages) as page images; identity/decode/dimensions
  from pages 1, 3; electrical limits page 3; curves pages 5 and 8.
- Symbol/footprint masters parsed from the installed KiCad 10 libraries.

## 7. Unresolved work

- None.
