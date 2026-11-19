# Nexperia SO20W pilot research — 74HC244D,653

Reviewed 2026-11-19. This is research, not an approved render recipe.

- [Nexperia exact orderable product table](https://www.nexperia.com/products/analog-logic-ics/logic/buffers-inverters-transceivers/buffers/serie/74hc244-74hct244) lists marking `74HC244D` and SO20 package SOT163-1 for `74HC244D,653`.
- [Nexperia SOT163-1 drawing](https://assets.nexperia.com/documents/package-information/SOT163-1.pdf) specifies 12.6–13.0 mm body length, 7.4–7.6 mm width, 1.27 mm pitch and 2.65 mm maximum seated height.
- Local source `parts_source/electronic_ic_logic_octal_bus_buffer_tri_state_soic_20_300mil_nexperia_74hc244d_653/working.yaml` identifies that orderable part, KiCad SOIC-20W 7.5 × 12.8 mm footprint, and 2.65 mm height.
- Installed KiCad model `Package_SO.3dshapes/SOIC-20W_7.5x12.8mm_P1.27mm.step`, SHA-256 `59a10b341e6972b31d81802a048060326da627d8b92dcf4263064f4f62ec808e`, measured 10.3 × 12.8000002 × 2.7500001 mm overall, z range approximately 0 to 2.75 mm. The model exceeds Nexperia's stated maximum height by 0.10 mm, so it must not be represented as dimensionally exact. Investigate whether the manufacturer-provided SOT163-1 model or a documented height correction produces a better display model before staging. Do not silently alter or assert the model height. The KiCad model remains a possible disclosed display approximation.
- Manufacturer page links a 3D model for SOT163-1. Inspect availability and license before relying on it; preserve source and provenance. No manufacturer model has been downloaded or assessed yet.

Next: assess the manufacturer model or a transparent correction, establish role colors and dimensions, prepare a guarded pilot, inspect preview and independent final, and only then consider shared passes and additional SO20W parts.
