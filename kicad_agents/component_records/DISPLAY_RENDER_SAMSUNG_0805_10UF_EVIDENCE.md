# Samsung CL21A106KOQNNNE display evidence

Reviewed 2026-11-18: [Samsung's product page](https://product.samsungsem.com/mlcc/CL21A106KOQNNN.do) explicitly lists the E packaging code and specifies 0805 (2012), 2.00 × 1.25 × 1.25 mm nominal, X5R, 10 µF, 16 V and ±10%. The selected source record identifies the same manufacturer part and LCSC C1713. Its existing dimensions omit height; Samsung supplies the nominal height.

KiCad's `Capacitor_SMD.3dshapes/C_0805_2012Metric.step` has matching nominal overall bounds, and separate ceramic and termination colours. It is a generic package model, not a Samsung model. The ceramic colour, terminal finish and blank surface are illustrative: the exact part's surface appearance and absence of printing have not been established. The manufacturer page was inspected online; no local PDF was captured.
