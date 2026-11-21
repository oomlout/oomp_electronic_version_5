# Vishay IRFL9014TRPBF SOT-223 display evidence

Reviewed 2026-11-21 against the existing local `parts_source/electronic_transistor_sot_223_mosfet_p_channel_enhancement_mode_60_volt_1_8_amp_vishay_intertech_irfl9014trpbf/datasheet.pdf`, SHA-256 `0e2847953fed483654671ca47aa940332e5eee0763051df08d3d0b784b98b46f`.

Page 1 identifies Vishay IRFL9014TRPbF in SOT-223, a -60 V, -1.8 A
P-channel MOSFET, and explicitly gives the marking code **FE**. Page 7's
SOT-223 drawing was visually reviewed: three narrow leads and an opposite
tab, body length 6.30–6.70 mm, total width 6.71–7.29 mm, and height
1.55–1.80 mm. The existing KiCad SOT-223 model has overall bounds 7.0 x
6.5 x 1.7 mm and the same lead/tab arrangement; fine shape and finish are
approximate. The source catalogue's 10 x 5 mm values differ from the
manufacturer drawing and are not changed here.

The FE code is documented; its exact location, typeface, production codes
and the model's small pin indicator are illustrative. This is a display model,
not a footprint or verified manufacturing geometry.
