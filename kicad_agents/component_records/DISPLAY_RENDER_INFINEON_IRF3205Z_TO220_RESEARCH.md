# Infineon IRF3205ZPBF TO-220 display research

The catalogue identifies Infineon Technologies IRF3205ZPBF, 55 V and 110 A,
with the TO-220-3 vertical footprint. Its existing local International
Rectifier PDF SHA-256 is
`a9255fb228ec1d67dae67fbc7290c3bfa08e0431271c493fe337873ebbd192fc`.
Page 1 was visually reviewed and identifies IRF3205Z in TO-220AB, with 110 A
silicon-limited and 75 A package-limited. The initial impression that its
75 A headline meant a different device was incorrect. Infineon's current
[IRF3205Z listing](https://www.infineon.com/part/IRF3205Z) identifies the
IRF3205ZPBF orderable in TO-220 and gives 110 A maximum current.

The local PDF page 9 TO-220AB drawing was visually reviewed. It specifies
13.47–14.09 mm lead length; the KiCad model's approximately 13.435 mm
body-to-tip projection is 0.035 mm below the minimum. Model shape and finish
are approximate, not verified manufacturing CAD. The page 9 marking example is
for an unrelated IRF1010; `IRF3205Z` is an illustrative identifier, with
exact top marking, typeface, logo and variable production codes unverified.
The local PDF is retained unchanged; no online PDF was downloaded.
