# onsemi TO-204 / TO-3 transistor render evidence

Reviewed 2026-11-21 using the existing local manufacturer PDFs. Page 1 of
each was visually checked for the package and fixed marking, and page 4 for
the package drawing. Production location and date codes are intentionally
omitted from the display marking.

| Orderable | Datasheet SHA-256 | Drawing | Fixed device marking |
| --- | --- | --- | --- |
| MJ15024G | `7b46afbdd8de68c25d2bca66cb5009a9396c5e460d5037da246b58605b51d1f6` | case 1-07 | MJ15024G |
| MJ15025G | `b7045e15a4b295363b37f0b3eaa01802ceac322d6c70a52c74c0a5f31baab46f` | case 1-07 | MJ15025G |
| MJ15004G | `2139768db1f29730d031c4aa29eb942345c0c7c97fc85990a49dd40ac5d20f38` | case 1-07 | MJ15004G |
| MJ11032G | `3ae0782cde581a2000e515ec20b033c4c3da00a8d4ca725b071f6e327da1b6ff` | case 197A-05 | MJ11032G |

Each PDF is at `parts_source/<exact part ID>/datasheet.pdf`. The drawings show
a circular metal can on a two-hole flange and two pins. The three case 1-07
drawings give flange length 39.37 mm reference, width up to 26.67 mm and
above-flange height 6.35–8.51 mm; the case 197A-05 drawing gives 38.86 mm
reference, 25.15–26.67 mm width and 6.35–8.51 mm height. The KiCad `TO-3.step`
has a 40.2 x 27.2 mm flange and 9.0 mm height above the seating plane, so it
is an approximate visual representation with a somewhat oversized envelope,
not manufacturing geometry. Its total source bounds include 10 mm pins below
the flange. The catalogue's 26 x 20 x 10.5 mm dimensions use a different
envelope and remain unchanged.

The fixed codes and G suffix follow the respective marking diagrams; actual
typeface, ink, exact placement, finish, logos and variable production codes
are not established by those diagrams. The model is for display only.
