# Samsung CL31B104KBCNNNC display evidence

Reviewed 2026-11-18. [Samsung's product page](https://product.samsungsem.com/mlcc/CL31B104KBCNNN.do) lists the exact C suffix, 100 nF, X7R, 50 V, ±10%, and nominal 3.20 × 1.60 × 0.85 mm. The source record selects that part and LCSC C24497 but omits height and electrical fields; ratings were checked against Samsung.

KiCad's generic `C_1206_3216Metric.step` has 3.2 × 1.6 × 1.6 mm nominal bounds. The display mesh is scaled vertically by 0.53125 to approximate the selected part's 0.85 mm nominal height. Detailed shape, ceramic colour, terminal finish and blank surface are illustrative; exact selected-part finish and marking remain unverified. No PDF was captured.
