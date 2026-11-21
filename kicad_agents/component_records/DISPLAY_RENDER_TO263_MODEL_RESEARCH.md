# TO-263 / D2PAK display model investigation

The catalogue's remaining TO-263 transistors specify the KiCad footprint `Package_TO_SOT_SMD:TO-263-3_TabPin2`. The installed matching STEP `Package_TO_SOT_SMD.3dshapes/TO-263-3_TabPin2.step` has SHA-256 `f8d7f00ad233d49496cf0b53aca1891fcbc2d8d007dfe42465186627fedd54d0` and five solids. Its body bounds are 9.25 × 10.0 × 4.4 mm, and complete bounds are 15.0 × 10.0 × 4.42 mm. Geometry inspection found a body, a tab, and **three full-length leads**.

The following local PDFs were independently identified and their page 8 package drawings visually reviewed:

| Catalogue part | Local PDF SHA-256 | Review |
| --- | --- | --- |
| Infineon IRF3205STRLPBF | `65ae69363cbeb25c807523218c9667ddda9657b3692fdb9c1661d17a470ae7b5` | International Rectifier IRF3205S/LPbF D2PAK; marking example is a different IRF530S. [Infineon product page](https://www.infineon.com/part/IRF3205S) confirms the exact orderable; exact physical marking remains unverified. |
| Infineon IRF3710STRLPBF | `28c3c50b0aab99deb1d00b37bfc44a2337795a5011315f085db9e4f74937e23c` | International Rectifier IRF3710S/L D2PAK; example is IRF530S. [Infineon product page](https://www.infineon.com/part/IRF3710S) confirms the exact orderable; exact physical marking remains unverified. |
| Vishay IRF840ASTRLPBF | `0d0d47cb473c1842d5a68b2ada3b84c59f610561462831ccc532c06a1dd7019a` | Vishay IRF840AS family, TO-263AB high-voltage drawing 91364. Exact orderable suffix and top marking still need checking. |
| Vishay IRF9640STRLPBF | `31f381baf2926f90533e23b67d6fcf2141e59209dc84ce7dc576d2306d2f803c` | Vishay IRF9640S family, visually identical drawing 91364. Exact orderable suffix and top marking still need checking. |

These drawings show two full leads and a clipped centre connection. Do not render the unmodified three-full-lead STEP as an exact representation. A display-only adapter must classify the five pinned solids, trim the centre lead to the illustrated short stub while preserving the tab, document that the trim is approximate, and verify orientation, material regions, output bounds and a preview. Dimensions and terminal shapes must be checked against each part's own drawing before reuse.

For the IRF3205S pilot, the display adapter trims the centre lead to an approximate 0.5 mm stub outside the model body; this is a visual approximation rather than a measured manufacturing dimension. The KiCad body and overall bounds fit the drawing's principal dimensions, but the exact moulding and finish remain approximate. IRF3205S is an illustrative partial identifier: the drawing's IRF530S marking example cannot verify its exact marking, typeface, logo or production codes.
