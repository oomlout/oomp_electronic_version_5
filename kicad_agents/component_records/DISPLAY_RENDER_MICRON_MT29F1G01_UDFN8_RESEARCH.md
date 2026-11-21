# Micron MT29F1G01ABAFDWB U-PDFN display research

Reviewed 2026-11-20. The source names MT29F1G01ABAFDWB, leaves manufacturer
blank, provides no footprint, and lists 6 x 5 mm. The orderable suffix is not
present, so infer Micron and the WB package family, but do not silently claim
a complete orderable or populate the manufacturer field.

The already-present local manufacturer datasheet
`parts_source/electronic_ic_memory_spi_nand_flash_1_gbit_updfn_8_micron_mt29f1g01abafdwb/datasheet.pdf`
has SHA-256 `f42985953dcba2647c9d7825f69de19f5a76f10d81b6bbb1095d2a5e72d41ac7`.
Page 59 was visually inspected: package WB is an 8-pin U-PDFN body
8 ±0.1 x 6 ±0.1 mm, 1.27 mm typical pitch, 0.4 ±0.05 mm terminal features,
and height 0.55 ±0.1 mm. The figure header calls it 0.65 mm high. The
manufacturer's [product page](https://www.micron.com/products/storage/nand-flash/slc-nand/part-catalog/part-detail/mt29f1g01abafdwb-it-f)
also lists 8 x 6 x 0.65 mm for a related complete orderable. The source's
6 x 5 mm dimensions conflict and must be disclosed. The eight terminals are
arranged four on each short edge; the drawing indicates a pin-one index and
a Micron logo, not an exact full production marking.

No suitable KiCad 8 x 6 mm eight-terminal model was found in the initial
package search. Inspect the full library and, if none matches, make a small
procedural display model based on the drawing, keeping terminal appearance,
marking and any unverified lot code explicitly illustrative. A partial family
identifier can aid identification but is not a verified physical marking.
No local source PDF was downloaded or changed.
