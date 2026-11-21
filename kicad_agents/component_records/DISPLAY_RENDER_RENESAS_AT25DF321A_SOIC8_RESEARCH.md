# Renesas AT25DF321A-SH-T SOIC-8 display research

Reviewed 2026-11-20. The source record identifies RENESAS and exact orderable
AT25DF321A-SH-T, SOIC-8-208mil, no KiCad footprint and generic 10 x 5 mm
dimensions. [Renesas orderable information](https://www.renesas.com/en/products/at25df321a/part-details/at25df321a-sh-t)
confirms the part and 1.27 mm pitch. Its [manufacturer-hosted datasheet](https://www.renesas.com/en/document/dst/at25df321a-datasheet)
lists that orderable as 8S2, a 0.208-inch body, not the unrelated UDFN variant.
The 8S2 table gives 5.13–5.35 mm body length, 5.18–5.40 mm body width,
7.70–8.26 mm lead span, 1.70–2.16 mm height and 1.27 mm pitch. The
catalogue's 10 x 5 mm dimensions are not these body dimensions and need
explicit disclosure.

KiCad's `SOIC-8_5.3x5.3mm_P1.27mm.step` is a candidate; inspect its bounds,
material colours and lead orientation before selecting it. No exact complete
package-top marking was located in the datasheet. `AT25DF321A` is an
illustrative partial identifier: typography, orientation, date/lot markings
and missing suffix remain unverified. No datasheet was downloaded locally.

The KiCad candidate inspection found SHA-256
`121aee742692bb7bc9ef49972786ecb89d1b2d62ab089ed278651a884c800331`,
valid 7.8 x 5.3 x 2.16 mm overall geometry and expected body, metal and
pin-indicator colours. Those values match the manufacturer span, body length
and height ranges. Preview the marking and eight leads before publication.
