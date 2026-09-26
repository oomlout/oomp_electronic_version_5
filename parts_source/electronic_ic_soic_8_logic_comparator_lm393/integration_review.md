# Integration review — JLC C7955 / onsemi LM393DR2G

Working checklist for Agent 2 (full stage). Datasheet:
`parts_source/electronic_ic_soic_8_logic_comparator_lm393/datasheet.pdf`
= onsemi `LM393/D` Rev. 25, April 2014 (Publication Order Number LM393/D).
Ordering table page 7 covers `LM393DR2G` = LM393, 0 °C to +70 °C, SOIC-8
Pb-free (D suffix, Case 751-07), 2500 / Tape & Reel. The PDF therefore covers
the full selected ordering suffix.

- code: C7955 | OOMP ID: `electronic_ic_soic_8_logic_comparator_lm393`
- maker: onsemi | full MPN: LM393DR2G | package: SOIC-8 NB, Case 751-07
- official page: https://jlcpcb.com/partdetail/onsemi-LM393DR2G/C7955 (Basic)
- datasheet source (browser download, provenance in `datasheet_source.yaml`):
  https://jlc-prod-smt.oss-eu-central-1.aliyuncs.com/smtDataManualFile/8579709014336602112-C7955.pdf
- identity reconfirmed against the record 2026-09-26 from the saved PDF
  (ordering page, marking diagrams and pin connections all agree with the
  intake capture; the live-page identity fields were verified 2026-09-24,
  within the 30-day window).

## 1. Electrical evidence (LM393 rows)

Absolute maximum ratings (page 2):

| Quantity | Value | Conditions |
| --- | --- | --- |
| Power supply voltage VCC | +36 V or ±18 V | absolute maximum |
| Input differential voltage VIDR | 36 V | absolute maximum |
| Input common-mode voltage VICR | −0.3 V to +36 V | for supplies below 36 V the limit equals VCC |
| Output voltage VO | 36 V | absolute maximum |
| Output sink current ISink | 20 mA | continuous short-circuit to ground permitted |
| Power dissipation PD | 570 mW | TA = 25 °C; derate 5.7 mW/°C above 25 °C |
| Operating ambient TA | 0 °C to +70 °C | LM393 suffix (LM293 −25/+85, LM2903 −40/+105) |
| ESD protection VESD | 1500 V HBM / 150 V MM | any pin |

Electrical characteristics (page 3, VCC = 5.0 V, LM293/LM393 columns):

| Quantity | Min | Typ | Max | Conditions |
| --- | --- | --- | --- | --- |
| Input offset voltage VIO | — | ±1.0 mV | ±5.0 mV | TA = 25 °C (±9.0 mV over temperature) |
| Input offset current IIO | — | ±5.0 nA | ±50 nA | TA = 25 °C |
| Input bias current IIB | — | 20 nA | 250 nA | TA = 25 °C; PNP inputs, bias flows out |
| Input common-mode range VICR | 0 V | — | VCC − 1.5 V | TA = 25 °C |
| Voltage gain AVOL | 50 V/mV | 200 V/mV | — | RL ≥ 15 k, VCC = 15 V, TA = 25 °C |
| Large-signal response | — | — | 300 ns | TTL swing, Vref = 1.4 V, RL = 5.1 k |
| Response time tTLH | — | 1.3 µs | — | 100 mV step, 5.0 mV overdrive, RL = 5.1 k |
| Output sink current ISink | 6.0 mA | 16 mA | — | VO ≤ 1.5 V, TA = 25 °C |
| Output saturation VOL | — | 150 mV | 400 mV | ISink ≤ 4.0 mA, TA = 25 °C (700 mV over temp.) |
| Output leakage IOL | — | 0.1 nA | 1.0 µA | VO = 30 V over temperature |
| Supply current ICC | — | 0.4 mA | 1.0 mA | both comparators, RL = ∞, TA = 25 °C |

Outputs are open collector (Figure 1 representative schematic; electrical
characteristics specify sink current/saturation only, no source rating), and
outputs are logic-compatible with DTL/ECL/TTL/MOS/CMOS when pulled up.

Intake classification recheck: the OOMP ID is the generic LM393 SOIC-8 dual
comparator (no taxonomy_14 maker). The onsemi facts above are a standard
LM393; nothing widens or narrows the generic identity, so the reviewed
purchase preference stands and no rated variant is required.

## 2. Pin table (datasheet page 1, PIN CONNECTIONS, top view)

| Physical pin | Function | Electrical type | Diagram side (top view) | Page |
| --- | --- | --- | --- | --- |
| 1 | Output A | open-collector output | left, top | 1 |
| 2 | Input A − | input | left | 1 |
| 3 | Input A + | input | left | 1 |
| 4 | GND (V− rail) | power (negative rail/ground) | left, bottom | 1 |
| 5 | Input B + | input | right, bottom | 1 |
| 6 | Input B − | input | right | 1 |
| 7 | Output B | open-collector output | right | 1 |
| 8 | VCC (V+ rail) | power | right, top | 1 |

No NC pins, no exposed pad, no shield (Case 751-07 has 8 gull-wing leads).
Count 8 = record `pin_count` = population pin count.

KiCad symbol `Comparator:LM393` (extends LM2903), parsed from the installed
library: unit 1 pins 1 (open_collector), 2 (− input), 3 (+ input); unit 2 pins
5 (+ input), 6 (− input), 7 (open_collector); unit 3 power pins 4 (V−,
power_in), 8 (V+, power_in). Number-for-number and function match with the
datasheet; the symbol labels pin 4 V− where onsemi prints GND — same physical
pin, correct for single-supply operation, no remapping done.

## 3. Mechanical table — SOIC-8 NB, Case 751-07, Issue AK (page 9)

Millimetres; controlling dimension millimetre.

| Dim | Meaning | Min | Max | Value used for drawing | Note |
| --- | --- | --- | --- | --- | --- |
| A | body length | 4.80 | 5.00 | 4.9 | midpoint used for illustration |
| B | body width | 3.80 | 4.00 | 3.9 | midpoint used for illustration |
| C | body height (seated) | 1.35 | 1.75 | 1.75 | max height |
| D | lead width | 0.33 | 0.51 | 0.42 | midpoint; dambar protrusion excluded |
| G | lead pitch | 1.27 BSC | — | 1.27 | basic |
| H | seat standoff | 0.10 | 0.25 | — | not drawn |
| J | lead thickness | 0.19 | 0.25 | — | not drawn |
| K | lead length | 0.40 | 1.27 | — | drawn as (S−B)/2 envelope |
| N | lead tip bend width | 0.25 | 0.50 | — | not drawn |
| S | overall lead span | 5.80 | 6.20 | 6.0 | midpoint used for illustration |

`dimensions_mm` keeps `height` at the 1.75 max; length/width/span use the
documented midpoints above (nominal values are not stated in Case 751-07).
Recommended soldering footprint (page 9): pads 0.6 × 1.52 mm, inner span
4.0 mm, outer span 7.0 mm, pitch 1.270 mm — recorded as land-pattern
reference only; the component drawing stays the physical envelope.

## 4. KiCad master comparison

Library root: `C:\Program Files\KiCad\10.0\share\kicad`.

| Comparison | Evidence |
| --- | --- |
| Symbol | `Comparator:LM393` — pin table above matches datasheet exactly; multi-unit: two comparators + shared power unit; outputs typed open_collector |
| Machine footprint | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` (JEDEC MS-012AA) — 8 SMD roundrect pads 1.95 × 0.6 mm at x = ±2.475, y = ±0.635/±1.905 (pitch 1.27); pad 1 top-left; body 3.9 × 4.9 matches Case 751-07 nominal; courtyard clears S max 6.20 |
| Mechanical fit | Pad rows straddle the 3.9 mm body; outer pad edges 6.9 mm ≥ S min 5.80 and < S max 6.20 + tolerance; no exposed pad; polarity via pin-1 dot/depth mark on package |
| Hand footprint | No `SOIC-8_3.9x4.9mm_P1.27mm:HandSolder` master exists in this install; the same verified official MS-012 master is selected unchanged for hand soldering (1.95 mm long pads already suit hand soldering; no enlargement), matching the repository convention for package-mapped ICs |

onsemi's recommended land pattern (pads 1.52 long, 4.0–7.0 mm span) is close
but not identical to KiCad's IPC-style MS-012 pattern (1.95 mm pads, 6.9 mm
outer edge); the official master is used unchanged — no automatic enlargement.

## 5. Population work

- `working_oomp_populate_ic.py` already has the single generic row
  (soic_8 / logic / comparator / lm393) — no new row needed.
- `working_oomp_populate_ic_extra.py`: new explicit block with pins,
  `ic_dimensions_mm`, `dimensions_mm`, `package_drawing`, `dimension_reference`,
  `kicad`, `electrical`, `datasheet_url`, `research_notes`, `file_copy`.
- `working_oomp_populate_unmatched_extra.py`: the older duplicate entry is
  removed so the family extra is the single source (it overwrote the family
  data in the full-detail chain).
- Registry `reviewed_choices.json` C7955 selection synchronized from the
  record after each record edit.

## 6. Command log

- `next --stage full` → C7955 (2026-09-26).
- Datasheet PDF re-read in full (10 pages); ordering, pins, ratings,
  dimensions and footprint taken from pages 7, 1, 2–3 and 9.
- Symbol/footprint masters parsed from the installed KiCad 10 libraries.
- `intake-check` / `full-check` / build — see the final report.

## 7. Ledger outcome and unresolved work

- All technical work is complete and was gate-verified: intake-check pass,
  full-check pass, component build pass (project output guard pass), KiCad
  manifest `complete` with symbol + machine + hand masters, visual review of
  the rendered PNGs, README, and s-expression masters done (see the record's
  `visual_review`).
- The ledger could not be marked full-complete: a fresh official JLC house
  crawl (2026-09-26, `sources/catalogue-browser-official-2026-09-26.json`,
  prepared at 14:32) re-curated the house category and no longer lists C7955,
  so it is `retired` and excluded from `queue.json`. `full-check`,
  `full-complete`, and `defer --stage full` all refuse codes outside the
  active snapshot ("Code is not in active snapshot"), and hand-editing the
  progress ledger is not sanctioned. The progress file still shows
  intake complete / full pending.
- Required next action (needs a browser): re-verify C7955's live JLC listing.
  If it is genuinely no longer a house part, remove or re-scope the registry
  preference (the part remains a valid generic LM393 OOMP identity with full
  technical data; only the house purchasing preference is affected). If it
  returns to the house category, rerun `prepare` and `full-complete --code
  C7955` — every gate should then pass as it did during this run.
- Environment fixes made for this run (shared venv, no pipeline changes):
  installed `pyautogui`, `clipboard`, `pyperclip`, and `cairosvg` into
  `.venv` so the roboclick file_copy/run_python and PNG-export actions work.

## 8. Unresolved work

- The browser re-verification above; no technical datasheet work remains open.
