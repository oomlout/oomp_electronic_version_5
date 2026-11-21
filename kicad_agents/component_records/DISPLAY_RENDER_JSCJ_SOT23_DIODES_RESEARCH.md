# JSCJ BAW56 and BAV70 SOT-23 diode display evidence

Existing local manufacturer PDFs reviewed 2026-11-21:

* `parts_source/electronic_diode_switching_dual_common_anode_sot_23_jiangsu_changjing_electronics_technology_co_ltd_baw56/datasheet.pdf`, SHA-256 `7ea39b2c8229c3bffebb55dd96f0a07d99b18caf316f92293f4287e31e1d7737`. Page 1 identifies BAW56 and marking **A1**; page 3 shows the SOT-23 outline: length 2.80–3.00 mm, lead span 2.25–2.55 mm and height 0.90–1.15 mm.
* `parts_source/electronic_diode_switching_dual_common_cathode_sot_23_jiangsu_changjing_electronics_technology_co_ltd_bav70/datasheet.pdf`, SHA-256 `2688a2ac8f7576e7ffa8b58c76f9ff025cd61a80053774b2a07b9cbee540b07d`. Page 1 identifies BAV70 and marking **A4**. Its page 3 did not display its drawing reliably in the local PDF renderer, so the BAW56 family PDF's individually reviewed SOT-23 outline is used as package-family evidence.

Both sources show an optional solid dot indicating green moulding; it is
omitted because the catalogue does not specify that variant. The KiCad
SOT-23 model has 2.5 x 3.0 x 1.2 mm overall source bounds and is vertically
scaled to 1.1 mm for display. Codes are supported by their local sources;
typeface, placement, finish and variable production details are illustrative.
This display model is not manufacturing CAD or a PCB footprint.
