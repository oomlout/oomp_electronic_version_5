# Unmatched components — resolution plan

Source: [unmatched_components.yaml](unmatched_components.yaml) (generated
2026-09-04, 109 projects scanned, 7 with unmatched items, 103 unmatched
component instances).

## How matching works today (from `kicad_agents/oomp_matching_agent.py`)

1. `infer_kind` recognises only `led`, `resistor`, `resistor_array`,
   `capacitor`, `transistor` (plus mounting holes from PCB data). Everything
   else — connectors, switches, diodes, ICs, crystals, modules — returns an
   empty kind, so no OOMP ID can be proposed ("No supported OOMP component
   family could be inferred").
2. A proposed ID is auto-accepted only if that exact part already exists in
   `parts/`. A *new value* (e.g. 18 pF 0402) fails with "The exact normalized
   component is not present"; a *non-normalizable value* (e.g. `DNF`) fails
   with "The component value could not be normalized".
3. Escape hatches, in precedence order: per-reference `match_overrides`
   (verified exact declarations), opt-in `generic_match` rules on populated
   parts (only when the schematic carries no MPN/manufacturer), then ranked
   candidate suggestions.
4. **Consequence:** an unmatched part does not mean a new part must be added.
   Example: J4 in `oomp_project_github_hanqaqa_easyduino_stm32f103_bluepill_current`
   (`Conn_01x04`, `PinHeader_1x04_P2.54mm_Vertical`) — the part
   `electronic_connector_header_2_54_mm_pitch_through_hole_4_pin` already
   exists; only the value `Conn_01x04` is not recognised. This is a
   matching-rule / override job, not a new-component job.

Each item below is therefore labelled:

- **[match]** part exists (or a rule can cover it) — update matching, add no part
- **[populate]** new value/size in an existing family — edit a
  `working_oomp_populate_<family>.py` list, then `action_generate.bat --filter`
- **[ledger]** new exact part needing browser research — add a
  `kicad_agents/component_records/E0xxx.yaml` record, a ledger row, datasheet
  import via `browser_research_agent import-datasheet`, then
  `component_addition_agent check/build`
- **[decide]** needs a decision before work starts (see Open questions)

Legend for project short names used below:

- **BP5** = dangerousprototypes/buspirate5_hardware 5_rev10a
- **Nano** = hanqaqa/easyduino ATmega328P Arduino Nano
- **Uno** = hanqaqa/easyduino ATmega328P Arduino Uno
- **ESP32** = hanqaqa/easyduino ESP32
- **ESP32S3** = hanqaqa/easyduino ESP32S3
- **Pico** = hanqaqa/easyduino Raspberry Pi Pico 2040
- **Bluepill** = hanqaqa/easyduino STM32F103 Bluepill

## Out of scope (skipped per instructions)

| Instances | What | Why |
| --- | --- | --- |
| BP5 FID1–FID5 | `Fiducial` / `Fiducial:Fiducial_1mm_Mask2mm` | Board features, not purchased parts |
| BP5 logo1 | `fcc_logo` / `dp-logo:logo_fcc` | Silkscreen artwork |

(6 of 103 instances skipped; 97 remaining.)

## Phase 1 — DNF resistors and capacitors [decide]

| Refs | Value | Footprint |
| --- | --- | --- |
| BP5 C603 | `DNF` | `C_0402_1005Metric` |
| BP5 R102 | `DNF` | `R_0402_1005Metric` |

`DNF` (do-not-fit) has no electrical value, so it can never normalise into an
OOMP ID. Options: (a) teach the matcher to treat value `DNF`/`DNP` as a
not-fitted board item (like the existing solder-jumper/dummy-footprint
exclusions in `_is_physical_component`), or (b) record them per project with
`match_blocked`. Option (a) fixes all current and future projects in one rule
and keeps them out of `used_in_projects`. **Preferred: (a)** — pending answer
to question 1.

## Phase 2 — Extra capacitor values

| Refs | Value | Footprint | Action |
| --- | --- | --- | --- |
| Bluepill C7, C8, C10, C11 | `18p` | `C_0402_1005Metric` | **[populate]** add `18_pico_farad` to the `0402` block's `capacitance_values` in `working_oomp_populate_capacitor.py` → generates `electronic_capacitor_0402_18_pico_farad` |
| Pico C16, C17 | `27p` | `C_0402_1005Metric` | **[populate]** same block: `27_pico_farad` → `electronic_capacitor_0402_27_pico_farad` |
| Uno C10–C12; ESP32S3 C6, C7, C10 | `22u` | `CP_EIA-3216-10_Kemet-I` (tantalum) | **[match, verify first]** `electronic_capacitor_3216_avx_a_tantalum_22_micro_farad_10_volt` already exists. Package size `3216` is not in the matcher's `PACKAGE_SIZES`, so no ID was proposed. Confirm the EIA-3216-10 (Kemet-I) vs 3216 AVX-A case equivalence and voltage, then add `match_overrides` for these 6 references — or a `3216` matcher rule. See question 3. |

## Phase 3 — Missing resistor values

| Refs | Value | Footprint | Action |
| --- | --- | --- | --- |
| ESP32S3 R9 | `2.4k` | `R_0402_1005Metric` | **[populate]** 2400 is not produced by the base-value/multiplier grid (2.2k and 2.7k exist, 2.4k does not). Add `["0402", "2400_ohm"]` to `low_value_resistors` (the explicit size/value pair list) in `working_oomp_populate_resistor.py` → `electronic_resistor_0402_2400_ohm` |

## Phase 4 — The rest

### 4a. Match-rule / override only — parts already exist [match]

| Refs | Value / footprint | Existing target | Note |
| --- | --- | --- | --- |
| Bluepill J4 | `Conn_01x04`, `PinHeader_1x04_P2.54mm_Vertical` | `electronic_connector_header_2_54_mm_pitch_through_hole_4_pin` | The example case: rule/override, not a new part |
| Bluepill J2, J3; Pico J3, J4 | `Conn_01x20`, `PinHeader_1x20_P2.54mm_Vertical` | `..._through_hole_20_pin` | Same `Conn_01xNN` gap |
| Pico J5 | `Conn_01x03`, `PinHeader_1x03_P2.54mm_Vertical` | `..._through_hole_3_pin` | Same |
| Pico Y1 | `12MHz`, `Crystal_SMD_3225-4Pin` | `electronic_crystal_3225_surface_mount_4_pin_12_mhz_20_pf` | Verify load capacitance (20 pF part) before overriding — see question 6 |

Recommendation: rather than 5+ per-reference overrides, extend the matcher to
normalise `Conn_01xNN` (+ optional `PinHeader_1xNN_P2.54mm` evidence) to
`electronic_connector_header_2_54_mm_pitch_through_hole_N_pin`, mirroring the
existing resistor/capacitor value rules. The Uno already sets a precedent for
the override route (`J2` in `match_overrides`). See question 2.

### 4b. New values/sizes in existing families [populate]

| Refs | Value / footprint | Action |
| --- | --- | --- |
| Nano Y1; Uno Y1 | `16 MHz` / `16MHz`, `Crystal_SMD_3225-4Pin` | Add 16 MHz to the 3225 4-pin crystal block in `working_oomp_populate_crystal.py` |
| Bluepill Y1 | `8MHz`, `Crystal_SMD_5032-2Pin` | New package block (5032 2-pin) + 8 MHz value in the crystal populator |
| Bluepill Y2 | `32.768kHz`, `Crystal_SMD_3215-2Pin` | New package block (3215 2-pin) + 32.768 kHz value |
| Pico H1–H4 | `MountingHole_2.2mm_M2` | Add `2_2_mm` round entries (plated/unplated per board) to `working_oomp_populate_mounting_hole.py` (2.0 and 2.5 mm exist, 2.2 does not) |

### 4c. New exact parts — expansion-ledger route [ledger]

Next free ledger IDs: **E0138+** (ledger currently ends at E0137). Some are
already queued in `COMPONENT_EXPANSION_LEDGER.md`; reuse those rows rather
than duplicating.

| Refs | Identity | Status / ledger hook |
| --- | --- | --- |
| BP5 SW101 | PTS810 tactile switch | Already **E0014 `needs_input`** — footprint does not fix actuator height/force; needs fitted-BOM input |
| BP5 SW102 | GT-TC026X 4P button | Already **E0015 `needs_input`** — same |
| Nano SW1 | CK PTS636 tactile | New ledger row |
| Uno SW1 | Omron B3FS-100xP tactile | New ledger row |
| ESP32S3 SW1, SW2 | Alps SKRK tactile | New ledger row |
| Pico SW1, SW2; Bluepill SW1, SW2 | Alps Alpine SKRPACE010 | New ledger row |
| Nano D2; Uno D2, D3; ESP32S3 D2, D3; Pico D1 | `D_Schottky` 0402 / SOD-123 | No MPN in schematic → generic-family candidate or `needs_input`; see question 5 |
| Nano F1; Uno F1 | `Polyfuse` 0402 / 1206 | No fuse family exists yet — new family + generic or exact part |
| Nano J1; Uno J1; ESP32S3 J1, J2; Pico J1; Bluepill J1 | G-Switch `GT-USB-7010ASV` USB-C receptacle | New exact connector; the two existing `usb_c` parts are different MPNs — do not reuse |
| Nano J2; Uno J3 | `ICSP`, `PinHeader_2x03_P2.54mm` | No dual-row header parts exist; add `6_pin_dual_row` entries to the connector populator, then rule/override |
| Pico J6 | JST `SH BM03B-SRSS-TB` 3-pin | New exact connector |
| Uno L1 | `10uH` 0603 inductor | No inductor family exists (only ferrite beads) — new family |
| ESP32S3 Q1, Q2 | `Q_NPN_BCE`, SOT-23W | No MPN → generic NPN family or `needs_input` |
| Nano U1; Uno U2 | `ATmega328P-A`, TQFP-32 | Covered by queued **E0095** |
| Nano U2 | `XC6206P502MR` (5.0 V), SOT-23-3 | New row — E0052 covers only the 3.3 V P332 variant |
| Pico U1; Bluepill U1 | `XC6206P332MR` (3.3 V) | Covered by queued **E0052** |
| Nano U3; ESP32 U1; ESP32S3 U3 | `CP2102N-Axx-xQFN28`, QFN-28 | Row **E0084** says QFN-24 — see question 4 |
| Uno U1 | `CH340C`, SOIC-16 | Covered by queued **E0083** |
| Uno U3; Uno U4; ESP32S3 U5 | `AMS1117-5V` / `AMS1117-3.3(V)`, SOT-223 | Covered by queued **E0053/E0054** |
| Bluepill U2 | `STM32F103C8Tx`, LQFP-48 | Covered by queued **E0099** |
| Pico U2 | `RP2040`, QFN-56 | New row (not in ledger) |
| Pico U3 | `W25Q16JVUXIQ`, USON-8 | Row **E0090** covers SOIC-8 JV parts only — new row or row split |
| ESP32S3 U1 | `ESP32-S3-WROOM-1` module | Covered by queued **E0102** |
| ESP32 U4; ESP32S3 U2 | `ESP32-DevKitC` / `ESP32-S3-DevKitC` module footprints | DevKit-as-component decision needed — see question 7 |
| Nano A1; Uno A1 | `Arduino_Nano_v3.x` / `Arduino_UNO_Connects` module footprints | Same DevKit decision |

### 4d. Board features to exclude [decide]

| Refs | Value / footprint | Proposal |
| --- | --- | --- |
| Uno TP1, TP2 | `TestPoint`, `TestPoint_Pad_2.5x2.5mm` | Treat like solder jumpers: board features, not purchased parts → `not_applicable` rule |
| Pico TP1–TP14 | `~`, `rp2040_lib:TestPoint_pad` | Same rule (value `~` is the KiCad "no value" marker) |

## Execution notes

- **Order within each phase:** populate/rule edit → `action_generate.bat
  --filter <new-part-id>` for new parts → add verified `match_overrides` →
  re-run `action_generate.bat --filter <project-id>` → re-run
  `action_unmatched_component_check.py` to confirm the count drops.
- New exact parts (4c) follow the ledger checklist: browser-verified MPN,
  datasheet import through `browser_research_agent import-datasheet`,
  populate row + populate-extra block, then
  `component_addition_agent check`/`build`. Project regeneration is
  intentionally deferred until each batch is complete (ledger convention).
- Finish with `python -m unittest discover -s kicad_agents/tests -v` and
  `python -m kicad_agents.pipeline_audit_agent --fail-on-error`.

## Open questions for the owner

1. **DNF handling** — add a matcher rule treating value `DNF`/`DNP` as
   not-fitted (global, one change), or per-project `match_blocked` entries?
2. **`Conn_01xNN` headers** — extend `oomp_matching_agent` to propose the
   generic through-hole header ID (fixes J2/J3/J4/J5 across Bluepill and Pico
   at once), or keep per-reference `match_overrides` like the existing Uno J2?
3. **22 µF tantalum** — the existing part is `3216_avx_a ... 10_volt`; the
   boards use Kemet-I `CP_EIA-3216-10`. Is case-size equivalence enough for an
   override, or should a separate 3216-10 variant be added?
4. **CP2102N** — ledger E0084 says QFN-24, but all three boards use the
   QFN-28 variant (`CP2102N-Axx-xQFN28`). Correct E0084 or add a second row?
5. **Unidentified `D_Schottky` / `Q_NPN_BCE` parts** — build generic-family
   parts with `generic_match` rules, or mark `needs_input` until a fitted BOM
   supplies the exact MPN?
6. **12 MHz crystal override** — existing part specifies 20 pF load; is that
   verified against the Pico board's crystal, or research first?
7. **DevKit/module carriers** (Arduino Nano/Uno footprints, ESP32-DevKitC) —
   do these get OOMP "module" parts, or a board-feature exclusion similar to
   test points?
