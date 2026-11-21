# TI TPS62067DSGR WSON-8 display research

TI's [TPS6206x data sheet](https://www.ti.com/lit/ds/symlink/tps62067.pdf) lists exact orderable `TPS62067DSGR` in eight-pin DSG WSON with fixed top marking `ODH`. Variable production codes, typeface and placement must not be invented; the display should disclose them as illustrative.

The same data sheet's DSG0008A drawing gives a 1.9–2.1 mm square body, 0.7–0.8 mm height, 0.5 mm pitch and an exposed thermal pad nominally 0.9 × 1.6 mm. The catalogue record identifies the exact orderable, has no machine-solder footprint selected, and gives generic 10 × 5 mm dimensions, which lack a documented measurement reference.

KiCad's `Package_DFN_QFN.3dshapes/VDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.7mm.step` is valid and has SHA-256 `1bd0639f406461ef59516cc8d6dd8d149ea04d7d69464ca6da929b7539ea3033`, bounds 2.0 × 1.98 × 0.77 mm and coating, metal and pin-indicator colours. Its nominal 0.9 × 1.7 mm exposed pad is at the upper end of TI's 1.5–1.7 mm length range. Rendering must be visually inspected for the pin indicator and eight terminals; the approximation is for display and is not a verified mechanical model or footprint.
