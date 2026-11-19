# Nexperia SO20W follow-on research

Manufacturer tables checked 2026-11-19; these are research leads only. Validate exact local source, footprint and dimensions individually and do not stage before the independent SO20W pilot is reviewed and published.

- [74HC244 / 74HCT244](https://www.nexperia.com/products/analog-logic-ics/logic/buffers-inverters-transceivers/buffers/serie/74hc244-74hct244): `74HCT244D,653` has marking `74HCT244D`, package SOT163-1.
- [74HC241 / 74HCT241](https://www.nexperia.com/products/analog-logic-ics/logic/buffers-inverters-transceivers/buffers/serie/74hc241-74hct241): `74HC241D,653` has marking `74HC241D`, package SOT163-1.
- [74HC374 / 74HCT374](https://www.nexperia.com/products/analog-logic-ics/logic/flip-flops-latches-registers-counters-dividers/d-type-flip-flops/series/74HC374-74HCT374.html): `74HC374D,653` has marking `74HC374D`, package SOT163-1.
- [74HC245 / 74HCT245](https://www.nexperia.com/products/analog-logic-ics/logic/buffers-inverters-transceivers/transceivers/series/74HC245-74HCT245.html): `74HC245D,653` has marking `74HC245D`, package SOT163-1.

All must inherit the pilot's explicit display-only KiCad model vertical correction and marking limitation. A shared-pass master requires its own comparison against the independent pilot before use.

Local source validation 2026-11-19: exact Nexperia manufacturer, MPN, 12.8 x 7.5 x 2.65 mm dimensions and SOIC-20W footprint confirmed for 74HCT244D,653, 74HC374D,653 and 74HC245D,653. No local record for 74HC241D,653 was found; do not stage it without rechecking the catalogue.
