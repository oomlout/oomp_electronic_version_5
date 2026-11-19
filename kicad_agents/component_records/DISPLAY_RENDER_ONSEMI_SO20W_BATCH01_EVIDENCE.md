# onsemi SOIC-20W batch 01 evidence

Reviewed 2026-11-19. Onsemi identifies all three orderables as 20-pin SOIC, and their manufacturer drawings include case 751BJ, a 300-mil package with 12.8 x 7.5 mm nominal body, 1.27 mm pitch and 2.64 mm maximum seated height. Local records list 12.8 x 7.5 x 2.65 mm and the wide SOIC footprint. The KiCad model is vertically scaled from 2.75 to 2.65 mm; it is a display approximation 0.01 mm above the 751BJ maximum, not a verified mechanical model. Typeface, position, logo, pin-one indicator and variable codes are illustrative.

The AC240 and AC245 ordering tables specify their listed device codes. For MM74HC244WMX, the datasheet's SOIC marking diagram depicts `HC244A`, but the accompanying legend says `HC240A` and the ordering table does not explicitly associate a marking with the exact orderable; show HC244A only as a diagram-derived illustrative example and preserve the conflict on its page.

| Source record | Manufacturer part | Top marking | Manufacturer evidence |
|---|---|---|---|
| `electronic_ic_logic_octal_bus_buffer_tri_state_inverting_soic_20_300mil_onsemi_74ac240scx` | 74AC240SCX | `AC240` | [onsemi datasheet](https://www.onsemi.com/download/data-sheet/pdf/74ac240-d.pdf) |
| `electronic_ic_logic_octal_bus_buffer_tri_state_soic_20_300mil_onsemi_mm74hc244wmx` | MM74HC244WMX | `HC244A` | [onsemi datasheet](https://www.onsemi.com/download/data-sheet/pdf/mm74hc244-d.pdf) |
| `electronic_ic_logic_octal_bus_transceiver_tri_state_soic_20_300mil_onsemi_74ac245scx` | 74AC245SCX | `AC245` | [onsemi datasheet](https://www.onsemi.com/download/data-sheet/pdf/74act245-d.pdf) |
