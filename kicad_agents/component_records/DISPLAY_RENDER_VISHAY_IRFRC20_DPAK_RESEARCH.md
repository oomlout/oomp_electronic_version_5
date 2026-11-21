# Vishay IRFRC20TRLPBF DPAK display research

The source record identifies Vishay Intertech IRFRC20TRLPBF, 600 V and 2 A,
with the TO-252-3_TabPin2 PCB footprint. The existing local Vishay Siliconix
IRFRC20 family PDF has SHA-256
`9cae01c92506ebc134ebcd9a34df27431e471b51ddb6f33fcc605856ef8347c4`.
Page 1 identifies the IRFRC20 surface-mount family and page 8's extracted text
identifies Vishay outline 71197. Its page 8 could not be rendered by Poppler
because of a damaged cross-reference, so that local drawing was not visually
accepted.

Vishay's [official product page](https://www.vishay.com/en/product/91285/)
links [TO-252AA outline 71197](https://www.vishay.com/docs/71197/to252aa.pdf).
The related Vishay IRFR320 local PDF contains an earlier copy of the same
outline document, visually reviewed in
`DISPLAY_RENDER_VISHAY_IRFR320_9220_DPAK_RESEARCH.md`; it shows two full outer
leads, a short centre stub and a metal tab. Vishay's
[family datasheet](https://www.vishay.com/docs/91285/sihfrc20.pdf) lists the
IRFRC20TRLPbF orderable as DPAK. These online references were inspected without
downloading a replacement PDF.

The KiCad TO-252-2 model approximates this shape more closely than the
three-full-lead model associated with the unchanged footprint. Its 9.9 x 6.5
x 2.32 mm overall bounds and centre stub are approximate, not manufacturing
CAD. `IRFRC20` is an illustrative partial identifier; the exact device
marking, typeface, placement, logo and production codes are unverified.
