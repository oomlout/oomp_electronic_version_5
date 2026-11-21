# Intel/Altera EPM1270T144C5N TQFP-144 display research

Reviewed 2026-11-20. Source identifies exact EPM1270T144C5N, Intel/Altera,
TQFP-144 and a generic 10 x 5 mm placeholder, with no selected KiCad footprint.
[Altera's MAX II package information](https://cdrdv2-public.intel.com/654716/max2_mii51007.pdf)
describes a TQFP-144 body 20 x 20 mm, overall 22 x 22 mm, 0.5 mm pitch,
1.6 mm maximum total height and 1.4 mm nominal body thickness. The generic
source dimensions are not the package and must be disclosed. Figure was
text-extracted rather than visually reviewed.

The exact physical top marking has not been verified. `EPM1270T144C5N` can
only be an illustrative catalogue identifier; font, logo, orientation and
production fields are illustrative or omitted. The KiCad
`Package_QFP.3dshapes/TQFP-144_20x20mm_P0.5mm.step` is a candidate; inspect
its geometry, colours, height and hash before staging. Render only for display,
not as a verified mechanical model or footprint. No manufacturer PDF was
downloaded in this research.

Inspected KiCad `Package_QFP.3dshapes/TQFP-144_20x20mm_P0.5mm.step`:
valid single root, SHA-256
`04375074474c94e835558669f44d0989e234e983d3964161956a27bc675357d1`,
22 x 22 x 1.10 mm overall bounds, with separate coating, metal and index
colours. The source model is thinner than the maker's body-thickness and
seating-plane combination; inspect body and lead vertical geometry before
choosing a representative display scale. No candidate is staged.

Source face-colour inspection measured the KiCad coating from z=0.10 to
1.10 mm (1.00 mm body thickness), and metal from z=0 to 0.65 mm. Scaling
all display geometry vertically by 1.4 yields approximately 1.40 mm body
thickness, 0.14 mm clearance and 1.54 mm overall height: within the maker's
1.35-1.45 mm body, 0.05-0.15 mm clearance and 1.60 mm maximum. This is an
illustrative display adjustment and must be disclosed; review leads and index
in preview and final. It does not establish manufacturing accuracy.
