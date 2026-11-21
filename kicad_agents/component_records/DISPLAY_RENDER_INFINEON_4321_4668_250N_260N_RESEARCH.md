# Infineon TO-247 device drawing review

Four local International Rectifier PDF page 8 drawings were visually reviewed.
Their SHA-256 values and relevant lead lengths are:

| Device | PDF SHA-256 | Drawing lead length |
| --- | --- | --- |
| IRFP4321PBF | `e8c9d54b1f9766fa6ea0820a5a6600eefd1fd5579aabf92c40516e0732c8c206` | 14.20–16.10 mm |
| IRFP4668PBF | `cdc3a5738f45a546511c3a7850678fe771413900485aebc701cfc3e5aab04910` | 14.20–16.10 mm |
| IRFP250NPBF | `7f80b137e3c0e635f2367884710ef0db8417c896dd6e77c26f16447b05904fd2` | 14.20–14.80 mm |
| IRFP260NPBF | `941dd0b0cec05f54e5fa60dbadba156bd7491d1064ebdd6ac1f762485c9bbb9d` | 14.20–14.80 mm |

The reviewed 15.15 mm adjusted KiCad TO-247 model is suitable only for the
first two drawings. The last two require the independently reviewed 14.50 mm
adjustment; do not reuse the 15.15 mm shared material master for them. For
IRFP4321 and IRFP4668 the 20.95 x 15.9 mm model body slightly exceeds the
drawings' 19.71–20.70 x 15.29–15.87 mm range. For IRFP250N and IRFP260N the
drawings specify 19.70–20.30 x 15.30–15.90 mm, so its body height is similarly
oversized. Shape and finish are approximate; none is manufacturing CAD.

Each drawing's marking example shows an unrelated IRFPE30. The device names
may be used as illustrative partial identifiers, with exact top markings,
typeface, logo, placement and production codes disclosed as unverified.
