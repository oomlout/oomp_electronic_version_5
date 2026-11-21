# Vishay D2PAK IRF840AS, IRF840S and IRF9640S display research

All three catalogue records identify Vishay Intertech and their locally stored Vishay family PDFs list the exact Pb-free tape-and-reel orderables on page 1. The files were already present locally.

| Orderable | Local PDF SHA-256 | Package evidence |
| --- | --- | --- |
| IRF840ASTRLPBF | `0d0d47cb473c1842d5a68b2ada3b84c59f610561462831ccc532c06a1dd7019a` | Page 8, TO-263AB high-voltage outline 91364. |
| IRF840STRLPBF | `a3bca7fa7e16110f20ace074d0b377c0b2104babe96115e9cdc633397e391783` | Local family sheet omits a package outline; Vishay's [IRF840S product page](https://www.vishay.com/en/product/91071/) links [outline 91364](https://www.vishay.com/docs/91364/to263ab.pdf), also visually reviewed in the other local PDFs. |
| IRF9640STRLPBF | `31f381baf2926f90533e23b67d6fcf2141e59209dc84ce7dc576d2306d2f803c` | Page 8, TO-263AB high-voltage outline 91364. |

The IRF9640 catalogue name contains 6.8 A; the local datasheet specifies 11 A at 25 °C and 6.8 A at 100 °C. This render work does not change that catalogue value. The 840A and 840 parts are distinct variants and remain distinct.

The drawings show two full leads and a clipped centre connection. The KiCad TO-263 model is adapted for display by trimming its centre lead to an approximate 0.5 mm external stub. Its approximately 9.25 × 10 × 4.4 mm body and 15 × 10 × 4.42 mm overall bounds fit the principal outline ranges; fine details, stub, finish and materials remain approximate. It is not manufacturing CAD.

IRF840AS, IRF840S and IRF9640S are illustrative identifiers. The local family sheets do not establish their exact top markings, typography, logo or production codes. No replacement PDF was saved from the web.
