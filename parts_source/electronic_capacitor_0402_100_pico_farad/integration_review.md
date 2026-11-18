# Integration review — JLC C1546 (0402CG101J500NT, 100 pF 50 V C0G 0402)

Stage-two (full) integration pass for generic part
`electronic_capacitor_0402_100_pico_farad`, per
`kicad_agents/JLC_PART_INTEGRATION_AGENT.md`. Claimed 2026-09-26 by
`oomp-stage2-batch`.

## 1. Identity

| Field | Value | Evidence |
| --- | --- | --- |
| JLC code | C1546 | record; live JLC page (stage-one capture) |
| Tier | Basic | stage-one capture, 2026-09-24 |
| Manufacturer | FH (Guangdong Fenghua Advanced Tech) | JLC page |
| MPN | 0402CG101J500NT | JLC page; decoded below |
| Package | 0402 (metric 1005) | ordering decode |
| Value | 100 pF | stage-one capture; ordering decode |
| Ratings | 50 V, C0G, ±5% | stage-one capture; ordering decode |
| Datasheet | `datasheet.pdf` (this folder; original C1546.pdf, sha256 705023d3…) | provenance yaml |

The saved PDF is the Fenghua **General Series MLCC** product specification
(30 pages, "1005～1812 TYPE"). It is this part's own datasheet (downloaded from
the record's `datasheet_url`); the 1 nF / 22 nF / 4.7 nF X7R parts in this
family share it via `oomp_datasheet_common_with`.

## 2. Ordering-code decode (datasheet page 4, "How To Order")

`0402 C G 101 J 500 N T`

| Field | Code | Meaning |
| --- | --- | --- |
| Size | 0402 | 1.00 × 0.50 mm |
| Dielectric | CG | C0G |
| Capacitance | 101 | 10 × 10¹ pF = 100 pF |
| Tolerance | J | ±5% |
| Rated voltage | 500 | 50 × 10⁰ = 50 V |
| Termination | N | nickel-barrier (three-layer plating) |
| Packing | T | 7-inch braided disc |

The decode matches the JLC page's advertised ratings (100 pF, 50 V, C0G, ±5%)
exactly.

## 3. Electrical verification

C0G 0402 capacitance/voltage table (datasheet page 6): the 100 pF row shows
`CA` at both 25 V and 50 V — the exact ordering suffix is a catalogue row.

Temperature characteristics (page 5): C0G = 0 ± 30 ppm/°C referenced to 25 °C,
operating range −55 °C to +125 °C.

## 4. Terminals

Two-terminal non-polarized chip: pin 1 and pin 2, both passive, named "1"/"2"
(consistent with the other 0402 chip capacitors integrated this batch).

## 5. Mechanical (datasheet page 5)

Size code CA: L 1.00 ± 0.05 mm, W 0.50 ± 0.05 mm, T 0.50 ± 0.05 mm, terminal
width WB 0.25 ± 0.05 mm. The capacitance table gives thickness code CA for
100 pF @ 50 V, consistent with the dimension table's note that T comes from the
capacitance/voltage table.

`dimensions_mm` = {length: 1.0, width: 0.5, height: 0.5}.

## 6. KiCad masters (verified against installed KiCad 10 libraries)

| Role | Master |
| --- | --- |
| Symbol | `Device:C_Small` |
| Machine solder | `Capacitor_SMD:C_0402_1005Metric` |
| Hand solder | `Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder` |

Same set already parsed and confirmed present for the earlier 0402 parts of
this batch.

## 7. Population work

Added a technical block for `electronic_capacitor_0402_100_pico_farad` to
`working_oomp_populate_capacitor_extra.py` (before the final
`apply_reviewed_jlc_choices` call): package name, datasheet URL, electrical
dict, dimensions + reference, pins, kicad masters, research notes, own-path
file_copy. C1546 is registry-backed, so the selection was synced through
`reviewed_choices.json` (no inline `set_preferred_jlc` call for this part).

## 8. Commands

- `python -m kicad_agents.jlc_house_parts_agent next --stage full --claim --worker oomp-stage2-batch` → C1546
- `python tmp/stage2_record_update.py C1546` → record + registry updated
- `python -m kicad_agents.jlc_house_parts_agent full-check --code C1546 --record kicad_agents/component_records/JLC_C1546.yaml`
- `python -m kicad_agents.component_addition_agent build kicad_agents/component_records/JLC_C1546.yaml --regenerate-pngs`
- visual inspection of regenerated assets (hero `working_svg_square_pins_300.png`)
- `python tmp/stage2_record_visual.py C1546`, rebuild, `full-complete --code C1546`
