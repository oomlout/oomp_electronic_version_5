# TI TPS5430DDAR SO PowerPAD display research

The catalogue identifies Texas Instruments `TPS5430DDAR`, with generic 10 × 5 mm dimensions and no selected KiCad footprint. TI's [TPS5430 data sheet](https://www.ti.com/lit/ds/symlink/tps5430.pdf) identifies this exact orderable in the 8-pin DDA SO PowerPAD package and lists the fixed part marking `5430`. Production date/lot, logo, typeface and layout have not been established; omit variable characters and disclose an illustrative appearance.

The same manufacturer's DDA0008J and DDA0008B drawings specify a 4.8–5.0 × 3.8–4.0 mm body, 5.8–6.2 mm lead span, 1.27 mm lead pitch and 1.7 mm maximum height. They depict different allowable exposed-pad dimensions. The catalogue's generic dimensions do not identify a reference and should not be presented as package measurements.

The inspected KiCad `Package_SO.3dshapes/SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm.step` has SHA-256 `2d6f7e774e8143e3320cbd59eb5be9f3b7864614644e3b072006e1eb05fb7fa6`, valid geometry, expected coating/termination/pin-indicator colours, and 6.0 × 4.9 × 1.55 mm overall bounds. Its nominal 2.29 × 3.0 mm exposed pad falls within both drawings' pad ranges; this is a visual approximation, not a verified mechanical model or footprint.
