# TPS60110PWPR and UC3854DWTR display research

Reviewed 2026-11-20; neither candidate is staged or published.

## TPS60110PWPR

The catalogue gives Texas Instruments, exact orderable TPS60110PWPR, HTSSOP-20
with exposed pad, generic dimensions 10 x 5 mm and no KiCad footprint. TI's
[datasheet and orderable table](https://www.ti.com/lit/ds/symlink/tps60110.pdf)
identify 20-pin PWP and marking `TPS60110`; the
[product page](https://www.ti.com/product/TPS60110) gives package dimensions
6.5 x 6.4 mm and identifies the PowerPAD package. Its fixed output is 5 V,
consistent with the source record's 4.8–5.2 V rating but inconsistent with
its compatibility note describing 3.3 V. Preserve this discrepancy explicitly
when documenting the display and flag it for catalogue correction; do not
change electrical source data as part of rendering.

Find and inspect a KiCad 20-lead exposed-pad model against TI's actual PWP
drawing, including the pad on the underside, body dimensions, lead pitch and
pin-one orientation. Generic catalogue dimensions are not verified package
dimensions. Font, placement and lot/date markings will remain illustrative.

## UC3854DWTR

TI's [orderable information](https://www.ti.com/product/UC3854/part-details/UC3854DWTR)
specifies SOIC-16 DW, while its [quality report for the exact orderable](https://www.ti.com/quality-reliability-packaging-download/zh-tw/report?opn=UC3854DWTR)
lists marking `UC3854DW`. TI's [product page](https://www.ti.com/product/UC3854)
lists DW dimensions 10.3 x 10.3 mm; compare the manufacturer drawing to the
available 7.5 mm-body SOIC-16 model. The source record's 9.9 x 3.9 mm body and
6.04 mm overall width describe a narrower package and conflict with the DW
orderable. Preserve and disclose the conflict; do not silently change source
taxonomy or claim the catalogue's dimensions describe the selected model.

The inspected KiCad `SOIC-16W_7.5x10.3mm_P1.27mm.step` has SHA-256
`159663ceb2b4996b1b89d3111e4a355fc27de3e24d3570f50e5ed9086e0d73af`,
10.3 x 10.3 x 2.75 mm overall bounds, a valid solid and the expected body,
metal and pin-indicator colours. TI's DW0016A drawing in the
[UC3854 datasheet](https://www.ti.com/lit/ds/symlink/uc3854.pdf) limits
height to 2.65 mm; for display, scale the model height to 2.5 mm and disclose
this approximation. The source 6.04 mm overall width is inconsistent with
TI's 10.3 mm overall width. The manufacturer's `UC3854DW` marking is confirmed,
but typography, orientation and variable production codes are illustrative.
