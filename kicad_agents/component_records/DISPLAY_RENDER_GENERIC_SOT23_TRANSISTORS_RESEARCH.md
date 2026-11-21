# Generic BSS138 and onsemi-labelled MMBT4403 display evidence

Reviewed 2026-11-21. Both target records lack their own local datasheet PDF;
no PDF was downloaded or copied.

* The generic `BSS138` record does not specify a manufacturer or exact
  orderable. The existing sibling onsemi BSS138 PDF at
  `parts_source/electronic_transistor_sot_23_mosfet_n_channel_enhancement_mode_50_volt_220_milliamp_onsemi_bss138/datasheet.pdf`
  has SHA-256 `d7ef8509e41f2def9147c14a68a0578155f7400c58e3b9514aad07524d6dd4dd`.
  Its first-page marking diagram supports `SS` for onsemi's SOT-23 BSS138.
  For the generic record this is an **illustrative onsemi example**, not a
  verified marking or manufacturer.
* The MMBT4403 record names onsemi only in its ID; its manufacturer and MPN
  fields are empty and the exact orderable is not specified. The online
  [onsemi MMBT4403 family datasheet](https://www.onsemi.com/pdf/datasheet/mmbt4403-d.pdf)
  identifies SOT-23 and a `2T` device code. The display uses `2T` as a family
  example, with the inferred manufacturer and unspecified orderable disclosed.

Both use the reviewed KiCad SOT-23 display model, 2.5 x 3.0 x 1.2 mm overall,
vertically scaled to 1.1 mm. The source dimensions are approximate, and
typeface, placement, finish and variable production codes are illustrative or
omitted. These renders are display-only, not manufacturing models or
footprints.
