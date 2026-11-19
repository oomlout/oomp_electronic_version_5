# TI SN65LVDS32DR SO16 evidence and catalogue conflict

Reviewed 2026-11-19. [TI datasheet](https://www.ti.com/lit/ds/symlink/sn65lvds32.pdf) lists exact SN65LVDS32DR, SOIC D 16, marking LVDS32 and describes a quad differential line receiver. The local source ID and some descriptions say driver while its own supplier ratings say four receivers. This display depicts the exact manufacturer part; the function conflict remains unresolved and is disclosed on the page.

[TI D0016A outline](https://www.ti.com/lit/ml/mpds432a/mpds432a.pdf) gives 9.8–10.0 × 3.8–4.0 mm body, 1.27 mm pitch and 1.75 mm maximum height. Local source gives 9.9 × 3.9 mm but omits height and machine-solder footprint. KiCad geometry is a display approximation, not a verified PCB footprint; marking typography and layout are illustrative.

| Part ID | Manufacturer part | Marking | TI datasheet |
| --- | --- | --- | --- |
| `electronic_ic_interface_quad_lvds_line_driver_soic_16_texas_instruments_sn65lvds32dr` | SN65LVDS32DR | `LVDS32` | [TI datasheet](https://www.ti.com/lit/ds/symlink/sn65lvds32.pdf) |
