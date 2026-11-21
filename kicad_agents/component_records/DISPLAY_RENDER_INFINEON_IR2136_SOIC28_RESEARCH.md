# Infineon IR2136STRPBF SOIC-28 display research

Reviewed 2026-11-20. The catalogue record identifies Infineon Technologies,
exact orderable IR2136STRPBF, SOIC-28, and generic 10 x 5 mm dimensions; it
has no KiCad footprint. Infineon's [product page](https://www.infineon.com/part/IR2136S)
confirms this orderable is 28-lead SOIC wide-body. The manufacturer-authored
[IR2136 family datasheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-ir213-datasheet-en.pdf)
shows the 28-pin wide-body outline with 17.7–18.1 mm body length,
7.4–7.6 mm body width, 10.0–10.65 mm lead span, 2.35–2.65 mm height and
1.27 mm adjacent lead pitch. Its extracted generic marking diagram does not
establish an exact complete package-top inscription for this orderable.

KiCad has a candidate `SOIC-28W_7.5x17.9mm_P1.27mm.step`; its bounds,
colours and geometry were checked: SHA-256
`b889a13dbe9ec59e79fa9f1b5118b00bfa54f9582392335ff3365b64afc264b1`,
valid geometry, expected body/metal/pin-indicator colours and overall bounds
10.3 x 17.9 x 2.75 mm. Scale height to 2.65 mm for display, within the
manufacturer's 2.35–2.65 mm range, and disclose that approximation. The
catalogue's 10 x 5 mm dimensions
do not describe this manufacturer package and must be explicitly disclosed.
`IR2136` can be an illustrative partial identifier only; font, orientation,
placement, suffix, brand and variable date/lot codes are unverified. No
manufacturer PDF has been downloaded into the repository for this research.
