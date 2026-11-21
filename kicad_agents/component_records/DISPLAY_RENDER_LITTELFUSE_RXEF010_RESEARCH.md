# Littelfuse RXEF010 display research

The existing local `parts_source/electronic_fuse_radial_5_08_mm_pitch_resettable_littelfuse_rxef010/datasheet.pdf`
is a one-page Tyco Electronics specification SCD25213 revision G (2011),
SHA-256 `e6ddfc474ba47e8cc9ebaeb418a1082e58612288a7de7ddd0bb97f4446874ee0`.
It was visually inspected. It identifies RXEF010 and marking `X10`, with an
additional manufacturer's mark and lot identification. It specifies cured
flame-retardant epoxy insulation and 24 AWG tin-plated nickel-copper alloy
leads. The drawing gives maximum width 7.4 mm, maximum thickness 3.0 mm, lead
spacing 4.3–5.8 mm, and lead length at least 7.6 mm. The source uses 5.08 mm
pitch and labels its body dimensions 7.4 × 6.6 × 3.0 mm, though the drawing
sets maxima for several dimensions rather than nominal values. Source notes
elsewhere say 1 A, but the drawing states 0.10 A hold; do not repeat the 1 A
claim in display evidence.

KiCad's installed Fuse library includes other manufacturers' radial PTC models
but no exact RXEF010 model. A drawing-inspired display model may show the part
lying face-up to make `X10` legible. Body curvature, yellow colour, lead bends,
inking, lot code and omitted manufacturer logo are illustrative; exact nominal
body dimensions are not established. Do not treat the render as CAD or a
footprint, and preserve the source's electrical and dimensional fields.
