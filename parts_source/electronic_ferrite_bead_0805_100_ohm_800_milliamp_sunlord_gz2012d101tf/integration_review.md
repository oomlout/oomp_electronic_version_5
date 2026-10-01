# Integration review — JLC C1015 / Sunlord GZ2012D101TF

Datasheet: `parts_source/electronic_ferrite_bead_0805_100_ohm_800_milliamp_sunlord_gz2012d101tf/datasheet.pdf`
= Sunlord "Specifications for Multi-layer Chip Ferrite Bead", SPEC No.
GZ10190000, Rev. 01, 10 pages, with a text layer. Section 1 (Scope, page 4)
states "This specification applies to GZ2012D101TF of multi-layer ferrite chip
bead", so the document covers the exact selected part (not merely the series).

- code: C1015 | OOMP ID: `electronic_ferrite_bead_0805_100_ohm_800_milliamp_sunlord_gz2012d101tf`
- maker: Sunlord | full MPN: GZ2012D101TF | package: 0805 (2012 metric)
- official page: https://jlcpcb.com/partdetail/Sunlord-GZ2012D101TF/C1015 (Basic)
- identity reconfirmed live 2026-09-30 in the browser: JLCPCB Part # C1015,
  MFR.Part # GZ2012D101TF, Basic badge, In Stock 2,343,664, and the page's
  signed datasheet link resolves to the stable URL recorded at intake
  (https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8756360797033779200-C1015.pdf).
  PDF downloaded through the interactive browser on 2026-09-30 (sha256 in
  datasheet_source.yaml).

## 1. Electrical evidence (page 4, Section 3 Electrical Characteristics)

| Quantity | Value | Conditions / page |
| --- | --- | --- |
| Impedance Z | 100 Ω ±25% | at 100 MHz test frequency (page 4) |
| Max DC resistance | 0.15 Ω | DCR column, page 4 |
| Max rated current | 800 mA | Ir column, page 4 |
| Test frequency | 100 MHz | page 4 |
| Operating & storage temperature | −55 °C to +125 °C (individual chip) | note 1 under Section 3, page 4 |
| Storage (packaged) | −10 to +40 °C, RH ≤70% | note 2, page 4 |
| Rated-current definition | current raising chip surface 20 °C above Ta | Fig. 5.3.3-2, page 6 |
| Derating | above +85 °C only for beads rated over 1000 mA | page 6 — not applicable to this 800 mA part |
| Packing | tape carrier (T), 4 K pieces, paper tape | page 8 |
| Impedance curve | GZ2012D101TF Z/R/X vs frequency, Z peaking near 100 MHz | page 4 figure |

Intake classification (exact GZ2012D101TF identity) holds.

## 2. Terminal table (two-terminal non-polarized chip)

| Physical terminal | Function | Electrical type | Note |
| --- | --- | --- | --- |
| 1 | terminal 1 | passive | internal Ag electrode, Ni/Sn plated termination (Fig. 4-4) |
| 2 | terminal 2 | passive | non-polarized |

KiCad symbol `Device:FerriteBead_Small`: two `pin passive line` entries
numbered "1" and "2". Count 2 = record `pin_count` = 2.

## 3. Mechanical table — 2012 [0805] (page 5, Table 4-1; unit mm [inch])

| Dim | Meaning | Value | Note |
| --- | --- | --- | --- |
| L | body length | 2.0 (+0.3/−0.1) [.079 (+.012/−.004)] | nominal used for drawing |
| W | body width | 1.25 ±0.2 [.049 ±.008] | nominal used for drawing |
| T | thickness | 0.85 ±0.2 [.033 ±.008] | `dimensions_mm.height`; page 8 taping table agrees |
| a | terminal width | 0.5 ±0.3 [.020 ±.012] | each end |
| A | recommended land gap | 0.80–1.20 | reflow PCB pattern, Fig. 4-2 |
| B | recommended land length (each side) | 0.80–1.20 | Fig. 4-2 |
| C | recommended land width | 0.90–1.60 | Fig. 4-2 |

The recommended_pad_* values in the extra block use the midpoints of the
Table 4-1 A/B/C ranges (1.0 / 1.0 / 1.25 mm), documented as midpoints of the
stated ranges, not guaranteed limits.

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Device:FerriteBead_Small` — two passive line pins "1"/"2", matches the non-polarized two-terminal chip |
| Machine footprint | `Inductor_SMD:L_0805_2012Metric` — pads 1/2 at x = ∓1.0625 mm (2.125 mm pitch), 0.875 × 1.20 mm roundrect; fab body 2.0 × 1.25 = Sunlord nominals; 1.20 mm pad width covers the 0.5 ±0.3 terminal; land extent 3.0 mm matches the recommended A+2B midpoint span |
| Mechanical fit | Standard 0805 chip land pattern, symmetric part, no polarity mark |
| Hand footprint | `Inductor_SMD:L_0805_2012Metric_Pad1.05x1.20mm_HandSolder` — official HandSolder master (pads 1.05 × 1.20 at ±1.15), selected unchanged |

## 5. Population work

- `working_oomp_populate_ferrite_bead.py` already has the exact GZ2012D101TF
  row — no new row.
- `working_oomp_populate_ferrite_bead_extra.py`: explicit C1015 block with
  `electrical`, `dimensions_mm` + `ferrite_bead_dimensions_mm`,
  `dimension_reference`, `pins`, `kicad`, `research_notes`, `file_copy`.
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim --worker solo` → C1015 (2026-09-30).
- Live JLC page reconfirmed 2026-09-30 (browser).
- SPEC read in full (10 pages; text layer plus rendered page 5 for Table 4-1).
- Symbol/footprint masters parsed from the installed KiCad 10 libraries.

## 7. Unresolved work

- None.
