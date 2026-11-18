# Three-family display render evidence

This record documents an existing resistor pilot and two display-only extensions.
The renders show nominal KiCad package geometry, not manufacturing models.

## Samsung CL10B104KB8NNNC

- Existing part: `electronic_capacitor_0603_100_nano_farad_samsung_electro_mechanics_cl10b104kb8nnnc`.
- Samsung's [reference specification, hosted by DigiKey](https://media.digikey.com/pdf/Data%20Sheets/Samsung%20PDFs/CL10B104KB8NNNC_Spec.pdf), identifies the exact part as 100 nF, 50 V, X7R, 0603, and its dimensional table gives 1.60 x 0.80 x 0.80 mm nominal. Viewed online 2026-11-17; this is a link to the source, not a claimed local PDF download.
- The specification diagram depicts the component but does not explicitly establish a no-marking policy. The blank body is therefore an **illustrative unmarked appearance**, not a verified statement that all production units are unmarked. Body colour and plated-end finish are also illustrative.
- KiCad `C_0603_1608Metric.step` nominal bounds agree with the specification. The model's two reviewed colours represent termination and ceramic. The STEP license header and model hash are recorded in the render manifest.

## Texas Instruments NE555DR

- Existing part: `electronic_ic_timer_555_timer_soic_8_texas_instruments_ne555dr`.
- TI's [xx555 datasheet, Rev. K](https://www.ti.com/lit/ds/symlink/ne555.pdf), package option addendum page 1, lists `NE555DR`, SOIC (D), 8 pins, with device marking `NE555`. TI's [quality report](https://www.ti.com/quality-reliability-packaging-download/ko-kr/report?opn=NE555DR) independently lists the same marking. Viewed online 2026-11-17; no local PDF capture is claimed.
- The render uses the device marking only. Typeface, ink, placement and body material are illustrative; no logo, date or lot code is claimed. The light pin-one feature comes from KiCad's geometry and is not a verified image of a specific TI production lot.
- KiCad `SOIC-8_3.9x4.9mm_P1.27mm.step` matches the existing part's specified footprint. Its reviewed colours distinguish moulded body, pins and the pin-one feature. The exact source header and hash are preserved in the manifest.

## Resistor pilot

`electronic_resistor_0603_10000_ohm` and its UNI-ROYAL `01C` marking are documented in `DISPLAY_RENDER_AGENT.md` and the recipe/manifest. When the shared renderer changes, refresh and inspect its render so metadata validation remains current.
