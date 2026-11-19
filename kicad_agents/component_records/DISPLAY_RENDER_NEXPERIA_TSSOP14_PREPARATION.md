# Nexperia TSSOP-14 display-render preparation

Reviewed 2026-11-19. This is preparation for the IC stage, after completing
the capacitor sequence. It does not replace an individual source, geometry,
marking and final-image review.

The two exact source records below name Nexperia and the KiCad footprint
`Package_SO:TSSOP-14_4.4x5mm_P0.65mm`:

| Catalogue part | Orderable part | Manufacturer-listed marking |
| --- | --- | --- |
| `electronic_ic_logic_quad_2_input_nand_gate_tssop_14_nexperia_74hc00pw_118` | `74HC00PW,118` | `HC00` |
| `electronic_ic_logic_hex_schmitt_trigger_inverter_tssop_14_nexperia_74hc14pw_118` | `74HC14PW,118` | `HC14` |

The [74HC00 product table](https://www.nexperia.com/products/analog-logic-ics/logic/gates/nand-gates/serie/74hc00-74hct00)
and [74HC14 product table](https://www.nexperia.com/products/analog-logic-ics/logic/buffers-inverters-transceivers/inverters/serie/74hc14-74hct14)
list those exact orderable parts, markings and SOT402-1 package. The shorter
TSSOP marking is different from the full SOIC device marking: do not reuse
the SOIC text. Typeface, layout, logos, date and lot codes are not established
by these tables and should not be invented.

The installed KiCad 10 STEP model
`Package_SO.3dshapes/TSSOP-14_4.4x5mm_P0.65mm.step` has SHA-256
`3ee5786aae56190997aa793ba3cfc003fd616782770e29719b4562f012982245`.
It has one coloured root, with body width 4.4 mm, length 5.0 mm and z span
0.1–1.0 mm; total bounds including leads are 6.4 x 5.0 x 1.0 mm. The
[manufacturer package outline](https://assets.nexperia.com/documents/package-information/SOT402-1.pdf)
supports the body dimensions and lead span and gives a 1.2 mm maximum seated
height. The model is a nominal display illustration, not an exact sample.

The single pin-indicator face is centred at model x = -1.3703, y = +1.6703 mm.
Footprint pad 1 is at PCB x = -2.8625, y = -1.95 mm; the model offset and
rotation are zero and its scale is one. These fall in the same quadrant after
the KiCad PCB Y-axis inversion. Confirm pin-one and lettering orientation in
the rendered preview; the coordinate check alone is not visual proof.

When starting IC work, revalidate the exact source identities, model hash and
evidence. Render and inspect an independent pilot before reusing material
passes for other parts; disclose approximate reflections when compositing.
No PDF or model was downloaded for this preparation.
