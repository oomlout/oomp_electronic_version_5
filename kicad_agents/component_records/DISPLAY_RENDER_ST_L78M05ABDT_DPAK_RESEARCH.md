# ST L78M05ABDT-TR DPAK display research

Reviewed 2026-11-20. Candidate only: no recipe has been staged or published.

The source record identifies STMicroelectronics L78M05ABDT-TR, 5 V, DPAK
(TO-252-2), and two external leads plus the metal tab, but has no KiCad
footprint and generic 10 x 5 mm dimensions. ST's
[L78M datasheet, order-code table](https://www.st.com/resource/en/datasheet/cd00000447.pdf)
confirms this exact orderable as a 5 V DPAK device. Section 8.4 presents
several DPAK mechanical variants; confirm the correct source geometry against
the drawings rather than assuming the generic catalogue dimensions are a body
measurement. The type A table lists 2.20–2.40 mm height; package variant and
type selection still need visual review.

KiCad includes `TO-252-2.step`, which needs geometry, colours, dimensions,
lead and tab orientation inspection before use. ST's datasheet establishes
the family identity but no exact package-top legend was located during this
review. `L78M05AB` can only be used as an illustrative partial identifier,
with typeface, placement, layout and lot/date text explicitly unverified.
Do not infer a pin-one dot, brand logo or a mechanical footprint from the
display. Manufacturer PDF has not been downloaded into the repository.

Initial inspection of KiCad `TO-252-2.step` found SHA-256
`3eb4c99603a4fe837c2fe9308bc174769ded87a785a0df48d2dc441432ee8b4c`,
valid overall geometry 9.9 x 6.5 x 2.32 mm and **no face colours** on all
83 faces. The height is within ST's type A range. A dedicated, reviewed
material adapter is required; inspect its constituent solids and verify body,
two leads and tab before staging or rendering. The 9.9 mm measurement is the
overall envelope, not a verified body-only length.

The source contains five valid solids: a 6.22 x 6.5 mm moulded body, a rear
tab, two outer full leads and a short central stub. A geometry-based adapter
can assign body and metal materials while preserving the stub. Review a render
for placement, lead and tab orientation; the drawing variant is not yet
visually matched and the central stub should not be described as a full lead.
