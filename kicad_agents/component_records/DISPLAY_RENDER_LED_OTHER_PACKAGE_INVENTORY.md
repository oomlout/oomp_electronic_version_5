# Additional KiCad LED package inventory

The installed KiCad 10 STEP models were inspected with OpenCascade on 2026-11-21. All four shapes are valid single roots. Bounds below are overall millimetres, with source colour roles checked by face. These are generic models and their geometry is not evidence that any exact manufacturer's product has the same package height or unlit appearance.

| KiCad STEP model | SHA-256 | Overall X × Y × Z | Green region Z bounds |
| --- | --- | --- | --- |
| `LED_0402_1005Metric.step` | `401a17c0a337a26edbde24f58dabfc1560d6cb1bfb8c8fc5c31b8692e321eb12` | 1.00 × 0.50 × 0.50 | 0.0075–0.015 |
| `LED_0603_1608Metric.step` | `98343205ec260ec165026ba2d44329a23096779ac36c553ea84aa7b370242e6d` | 1.60 × 0.80 × 1.10 | 0.015–0.030 |
| `LED_0805_2012Metric.step` | `0aa8b791804f5d72a2fc7d1bf231dd9959207d83df8ad801176fbc459f575b98` | 2.00 × 1.25 × 1.10 | 0.0175–0.035 |
| `LED_1206_3216Metric.step` | `9de47a5de5d40bcdc5dcc40d5b9d41fc41af90bbd37d25c17d211285e1c63a6e` | 3.20 × 1.60 × 1.10 | 0.030–0.060 |

Each model has 12 pale body faces, 34 metallic contact faces and four green orientation faces. In these models the green region is at the bottom of the package, not an illuminated top lens. Do not substitute the emitted colour for that orientation marker. Check per-part dimensions and evidence before staging; named or visibly tinted lenses require separate evidence and materials. Render and validate an independent example for each size before any image reuse.

The generic `electronic_led_0402`, `electronic_led_0603`, `electronic_led_0805` and `electronic_led_1206` source records each have unspecified emission colour, manufacturer, part number and lens treatment. Their listed X/Y sizes match the four model bounds above and they select the corresponding KiCad footprint. They have no identified production marking. The 1.10 mm model height for the last three is a generic model property, not a measured exact-part specification; disclose it and show each unlit and unmarked.

Installed through-hole `LED_D3.0mm.step`, `LED_D3.0mm_Clear.step`, `LED_D5.0mm.step`, `LED_D5.0mm_Clear.step` and `LED_D10.0mm.step` contain authored body/contact colours but no STEP transparency attribute was found by text inspection. In particular, the name `Clear` alone does not provide a transparent material or establish internal LED geometry. Inspect the complete model and create a physically plausible display material before rendering a clear or tinted lens; avoid asserting an exact lens colour from an emission-colour token.
