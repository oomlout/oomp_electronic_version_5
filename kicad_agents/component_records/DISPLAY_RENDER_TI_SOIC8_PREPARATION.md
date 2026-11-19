# Texas Instruments SOIC-8 amplifier preparation

Reviewed 2026-11-19. These are candidates, not rendered or published parts.
The linked TI package-option addenda identify the exact orderable part, package
and device marking. Layout, typeface, logos and lot/date information are not
established by the table and must remain illustrative.

| Catalogue ID | Orderable part | TI marking | Manufacturer evidence |
| --- | --- | --- | --- |
| `electronic_ic_amplifier_operational_amplifier_dual_low_noise_soic_8_texas_instruments_ne5532dr` | NE5532DR | `N5532` | [TI NE5532 datasheet and package addendum](https://www.ti.com/lit/ds/symlink/ne5532.pdf) |
| `electronic_ic_amplifier_operational_amplifier_dual_soic_8_texas_instruments_lm358dr` | LM358DR | `LM358` | [TI LM258 package option addendum](https://www.ti.com/ods/sysadd/oa/symlink/lm258_oa.pdf) |

Both current source records name Texas Instruments and machine footprint
`Package_SO:SOIC-8_3.9x4.9mm_P1.27mm`. The NE5532 source gives a 3.9 x
4.9 x 1.75 mm body. The LM358 source only specifies 3.9 x 4.9 mm; do not
silently add a source height. Check the individual package drawing and selected
model height, pin-one position and pin count before creating its recipe. A
previous NE555 example uses the same general SOIC-8 footprint, but its exact
model, material and marking configuration must be rechecked before reuse.

The `N5532` marking is shorter than the NE5532DR orderable part number; never
substitute the MPN as a package marking. Manufacturer documents were inspected
online; no local PDF or model was downloaded for this note. Inspect a preview
and independent final before relying on shared material passes. Individual
sources and final outputs require normal provenance and disclosure checks.

Geometry review: the installed KiCad SOIC-8 STEP matches the previously
published NE555 manifest SHA-256
`07f46cff378d30e6c27dfd5a03092c795323f86d91c71fc7e743f4f418dc553a`;
its recorded overall bounds are 6.0 x 4.9 x 1.75 mm. TI's D0008A outline in
[NE5532 datasheet](https://www.ti.com/lit/ds/symlink/ne5532.pdf) page 18 and
[LM358 datasheet](https://www.ti.com/lit/ds/symlink/lm358.pdf) page 63 gives
body length 4.81–5.00 mm, width 3.81–3.98 mm, lead span 5.80–6.19 mm and
seated height 1.75 mm maximum. Thus the nominal model is within those published
limits; this does not establish actual production appearance. The LM358 source
still has no explicit height: the manufacturer maximum is distinct from a
measured or nominal source value. Verify the final pin-one representation.

Additional individual TI top-marking reports, checked 2026-11-19; these are
research candidates only, pending exact source-record, package drawing and
model review:

| Catalogue ID | Orderable part | TI top marking | Source |
| --- | --- | --- | --- |
| `electronic_ic_amplifier_operational_amplifier_dual_cmos_soic_8_texas_instruments_tlc27m2cdr` | TLC27M2CDR | `27M2C` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/de-de/report?opn=TLC27M2CDR) |
| `electronic_ic_amplifier_operational_amplifier_dual_jfet_input_soic_8_texas_instruments_tl072idr` | TL072IDR | `TL072I` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/es-mx/report?opn=TL072IDR) |
| `electronic_ic_amplifier_operational_amplifier_dual_jfet_input_soic_8_texas_instruments_tl082idr` | TL082IDR | `TL082I` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/de-de/report?opn=TL082IDR) |

Each exact source record was found with the TI manufacturer and the same
SOIC-8 machine footprint. These reports support the strings, not their layout,
logo, date code or typography. Check manufacturer drawings separately before
selecting a model or staging each recipe.

The D0008A package outline was subsequently checked in each manufacturer
 datasheet: [TLC27M2](https://www.ti.com/lit/ds/symlink/tlc27m2.pdf), page 40;
[TL072](https://www.ti.com/lit/ds/symlink/tl072.pdf), page 76; and
[TL082](https://www.ti.com/lit/ds/symlink/tl082.pdf), page 53. Each gives the
same body width/length ranges and 1.75 mm maximum as the D0008A geometry above.
The KiCad model's nominal overall bounds fit those limits. Confirm each source
record's dimensions and pin-one convention again when staging its exact recipe.

Two further TI-listed markings, with catalogue IDs checked against the source
manufacturer and SOIC-8 machine footprint:

| Catalogue ID | Orderable part | TI top marking | Source |
| --- | --- | --- | --- |
| `electronic_ic_amplifier_operational_amplifier_dual_rail_to_rail_soic_8_texas_instruments_tlc2272cdr` | TLC2272CDR | `2272C` | [TI quality report](https://www.ti.com/quality-reliability-packaging-download/es-mx/report?opn=TLC2272CDR) |
| `electronic_ic_amplifier_operational_amplifier_precision_soic_8_texas_instruments_op07cdr` | OP07CDR | `OP07C` | [TI OP07C datasheet addendum](https://www.ti.com/lit/ds/symlink/op07.pdf) |

These are research candidates only. Check their individual package drawings and
actual source dimensions before staging. Do not infer TI markings for TL062IDR or
TLC27L2CDR from similar part numbers; their marking evidence is not established
here.

The additional D0008A drawings appear in [TLC2272](https://www.ti.com/lit/ds/symlink/tlc2272.pdf)
page 48 and [OP07](https://www.ti.com/lit/ds/symlink/op07.pdf) page 17. Both
show the same body and lead-span ranges and 1.75 mm maximum height as above.
The earlier OP07C symlink no longer resolved; the current OP07 datasheet
includes the exact OP07CDR marking and package addendum. Individual source
dimensions and pin-one still need review at recipe staging.
