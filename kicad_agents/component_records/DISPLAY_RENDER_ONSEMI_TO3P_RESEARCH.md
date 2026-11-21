# onsemi / Fairchild TO-3P transistor display research

Reviewed 2026-11-21 against existing local Fairchild datasheets, with their
onsemi ownership context confirmed by [onsemi's company history](https://www.onsemi.com/company/about-onsemi/company-history).

* `FQA28N50`: local `parts_source/electronic_transistor_to_3p_3_mosfet_n_channel_enhancement_mode_500_volt_28_4_amp_onsemi_fqa28n50/datasheet.pdf`, SHA-256 `9a86516a93ff64580fd3f4d2e81d7c3f464b752d96e1d5e90ee245f201a72a45`. Pages 1 and 7 were visually reviewed; the 2000 Fairchild drawing labels TO-3P and gives 16.50 ± 0.30 mm lead length below the body. The [later online onsemi/Fairchild sheet](https://www.onsemi.com/download/data-sheet/pdf/fqa28n50-d.pdf) labels the family TO-3PN, so the actual revision represented by the catalogue record is uncertain. The display follows the local historical TO-3P drawing.
* `FQA9N90C-F109`: local `parts_source/electronic_transistor_to_3pn_mosfet_n_channel_enhancement_mode_900_volt_9_amp_onsemi_fqa9n90c_f109/datasheet.pdf`, SHA-256 `382ad37b21678d0b1c1c8cfb0eb1f3c2bda741d9dc5562501118d871d36e3b63`. Pages 1 and 7 were visually reviewed; the TO-3PN drawing gives 19.70–20.30 mm lead length below the body.

The KiCad TO-3P-3 model has 15.51 x 4.51 x 40.7 mm source bounds and leads
extending about 20.7 mm below the body base. Display-only mesh adjustments
shorten the leads to 16.5 mm and 20.0 mm respectively; the body and pad
geometry are approximate, and the catalogue's generic 15.9 x 5.5 x 15.6 mm
dimensions are unchanged. These are not manufacturing models or footprints.
The local sheets do not prove exact top-surface markings. Rendered `FQA28N50`
and `FQA9N90C` are illustrative partial identifiers; typeface, logo,
placement, omitted `-F109` suffix and production codes are unverified.
