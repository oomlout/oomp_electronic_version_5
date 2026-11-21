# TI TPS60110PWPR display evidence

Reviewed 2026-11-20. TI's [TPS60110 datasheet](https://www.ti.com/lit/ds/symlink/tps60110.pdf)
lists the exact orderable as 20-pin PWP (HTSSOP with exposed PowerPAD) and
specifies `TPS60110` as its marking. Font, placement and lot/date characters
are illustrative. Its mechanical drawing specifies 6.4–6.6 x 4.3–4.5 mm
body, 6.2–6.6 mm lead span, 1.2 mm maximum height and 0.65 mm pitch. The
thermal pad dimensions are 1.5–2.4 mm by 1.97–3.38 mm.

The KiCad HTSSOP-20 model has an inspected envelope 6.4 x 6.6 x 1.2 mm and
the correct 0.65 mm pitch, but its isolated underside metal pad measures
3.4 x 6.6 mm. A geometry- and SHA-guarded display-only adapter scales this
pad to 2.0 x 2.7 mm and fills the resulting underside opening; pad shape and
surface remain approximate. This is not a footprint or a mechanical model.

The source record's 10 x 5 mm dimensions are generic, with no KiCad footprint.
The compatibility note calls the device 3.3 V even though the source ratings
give 4.8–5.2 V and TI specifies 5 V. Both discrepancies must be disclosed;
the original catalogue source is not silently corrected by display generation.
