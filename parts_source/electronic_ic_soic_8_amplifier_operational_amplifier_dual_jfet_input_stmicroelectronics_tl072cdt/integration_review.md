# Integration review — JLC C6961 / STMicroelectronics TL072CDT

Datasheet: `parts_source/electronic_ic_soic_8_amplifier_operational_amplifier_dual_jfet_input_stmicroelectronics_tl072cdt/datasheet.pdf`
= ST `TL072, TL072A, TL072B`, Doc ID 2298 Rev 7 (July 2012). Ordering table
(page 14) covers `TL072CDT` = TL072C, 0 °C to +70 °C, SO-8, tube or tape & reel,
marking 072C. The PDF therefore covers the full selected ordering suffix.

- code: C6961 | OOMP ID: `electronic_ic_soic_8_amplifier_operational_amplifier_dual_jfet_input_stmicroelectronics_tl072cdt`
- maker: STMicroelectronics | full MPN: TL072CDT | package: SO-8 (= SOIC-8, JEDEC MS-012)
- official page: https://jlcpcb.com/partdetail/STMicroelectronics-TL072CDT/C6961 (Basic)
- identity reconfirmed 2026-09-26 from the saved PDF (ordering, marking, pins,
  package all agree with the intake capture; live page verified 2026-09-24).

## 1. Electrical evidence (TL072C grade rows)

Absolute maximum (page 3, Table 1): VCC ±18 V; input voltage ±15 V (never more
than supply or 15 V, whichever is less); differential input ±30 V; Rthja 125 °C/W
(SO-8); output short-circuit duration infinite; ESD 1 kV HBM / 200 V MM / 1.5 kV CDM.

Operating conditions (page 3, Table 2): supply 6 to 36 V; TL072C 0 to +70 °C.

Electrical characteristics (pages 4–5, Table 3, VCC = ±15 V, TA = 25 °C, TL072C column):

| Quantity | Min | Typ | Max | Conditions |
| --- | --- | --- | --- | --- |
| Input offset voltage Vio | — | 3 mV | 10 mV | RS = 50 Ω (13 mV over temperature) |
| Offset voltage drift DVio | — | 10 µV/°C | — | |
| Input offset current Iio | — | 5 pA | 100 pA | 25 °C (10 nA over temperature) |
| Input bias current Iib | — | 20 pA | 200 pA | 25 °C (20 nA over temperature); junction leakage |
| Large-signal gain Avd | 25 V/mV | 200 V/mV | — | RL = 2 kΩ, Vo = ±10 V |
| Supply rejection SVR | 70 dB | 86 dB | — | RS = 50 Ω |
| Supply current ICC | — | 1.4 mA | 2.5 mA | no load, both amplifiers |
| Input common-mode range Vicm | ±11 V | — | — | −12 to +15 V limit noted |
| Common-mode rejection CMR | 70 dB | 86 dB | — | RS = 50 Ω |
| Output short-circuit current Ios | 10 mA | 40 mA | 60 mA | 25 °C |
| Output swing ±Vopp | 10 V | 12 V | — | RL = 2 kΩ; 12/13.5 V at RL = 10 kΩ |
| Slew rate SR | 8 V/µs | 16 V/µs | — | Vin = 10 V, RL = 2 kΩ, CL = 100 pF, unity gain |
| Gain bandwidth product GBP | 2.5 MHz | 4 MHz | — | Vin = 10 mV, RL = 2 kΩ, CL = 100 pF, F = 100 kHz |
| Input resistance Ri | — | 10^12 Ω | — | JFET input stage |
| Equivalent input noise en | — | 15 nV/√Hz | — | RS = 100 Ω, F = 1 kHz |
| THD | — | 0.01 % | — | F = 1 kHz, RL = 2 kΩ, CL = 100 pF, AV = 20 dB |
| Channel separation | — | 120 dB | — | AV = 100 |

JFET-input dual op-amp, push-pull output stage (source and sink specified);
short-circuit protected. Intake classification (exact TL072CDT identity) holds.

## 2. Pin table (datasheet page 1, pin connections, top view)

| Physical pin | Function | Electrical type | Diagram side (top view) | Page |
| --- | --- | --- | --- | --- |
| 1 | Output 1 | output | left, top | 1 |
| 2 | Inverting input 1 | input | left | 1 |
| 3 | Non-inverting input 1 | input | left | 1 |
| 4 | VCC− (negative rail) | power | left, bottom | 1 |
| 5 | Non-inverting input 2 | input | right, bottom | 1 |
| 6 | Inverting input 2 | input | right | 1 |
| 7 | Output 2 | output | right | 1 |
| 8 | VCC+ (positive rail) | power | right, top | 1 |

No NC pins, no exposed pad. Count 8 = record `pin_count` = population pin count.

KiCad symbol `Amplifier_Operational:TL072` (extends LM2903-family LM2904),
parsed from the installed library: unit 1 pins 1 (output), 2 (− input), 3
(+ input); unit 2 pins 5 (+ input), 6 (− input), 7 (output); unit 3 power pins
4 (V−, power_in), 8 (V+, power_in). Number-for-number match; no remapping.

## 3. Mechanical table — SO-8 (datasheet page 13, Table 5)

| Dim | Meaning | Min | Typ | Max | Value used for drawing | Note |
| --- | --- | --- | --- | --- | --- | --- |
| D | body length | 4.80 | 4.90 | 5.00 | 4.9 | typ stated |
| E1 | body width | 3.80 | 3.90 | 4.00 | 3.9 | typ stated |
| A | body height | — | — | 1.75 | 1.75 | max |
| E | overall lead span | 5.80 | 6.00 | 6.20 | 6.0 | typ stated |
| e | lead pitch | — | 1.27 | — | 1.27 | |
| b | lead width | 0.28 | — | 0.48 | 0.38 | midpoint for drawing |
| L | lead length | 0.40 | — | 1.27 | — | drawn as (E−E1)/2 envelope |
| A1 | seat standoff | 0.10 | — | 0.25 | — | not drawn |

ST gives typ values here, so the drawing uses them directly (no invented
midpoints). Same JEDEC MS-012 geometry as the LM393 package work.

## 4. KiCad master comparison

| Comparison | Evidence |
| --- | --- |
| Symbol | `Amplifier_Operational:TL072` — pin table above matches exactly; two amplifier units + shared power unit |
| Machine footprint | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` (JEDEC MS-012AA) — 8 SMD roundrect pads 1.95 × 0.6 mm at x = ±2.475, y = ±0.635/±1.905, pitch 1.27; body 3.9 × 4.9 = ST SO-8 typ; courtyard clears E max 6.20 |
| Mechanical fit | Same package family as onsemi Case 751-07; pin 1 top-left; no exposed pad |
| Hand footprint | Same verified official master selected unchanged (1.95 mm long pads; no enlargement), matching the repo convention |

## 5. Population work

- `working_oomp_populate_ic.py` already has the exact TL072CDT row — no new row.
- `working_oomp_populate_ic_extra.py`: explicit block with pins, `ic_dimensions_mm`,
  `dimensions_mm`, `package_drawing`, `dimension_reference`, `kicad`, `electrical`,
  `datasheet_url`, `research_notes`, `file_copy`.
- Registry selection synchronized from the record after each record edit.

## 6. Command log

- `next --stage full --claim` → C6961 (2026-09-26).
- Datasheet read in full (16 pages); ordering/pins/ratings/dimensions from
  pages 14, 1, 3–5, 13.
- Symbol/footprint masters parsed from installed KiCad 10 libraries.
- Gates and build results recorded in the build report.

## 7. Unresolved work

- None.
