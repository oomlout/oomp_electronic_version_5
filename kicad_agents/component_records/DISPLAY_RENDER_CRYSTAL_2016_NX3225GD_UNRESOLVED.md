# Crystal 2016 / NX3225GD identity conflict

Record: `parts_source/electronic_crystal_2016_surface_mount_4_pin_26_mhz_20_pf_txc_nx3225gd/working.yaml`.

The catalogue ID names TXC and NX3225GD; the source asserts a four-pad 2.0 × 1.6 mm, 26 MHz package and cites a “TXC NX3225GD package drawing”, but has no populated manufacturer, distributor, or KiCad footprint. The [NDK manufacturer page for NX3225GD](https://www.ndk.com/en/products/lineup/crystal-unit/NX3225GD.html) identifies NX3225GD as an NDK product in a 3.2 × 2.5 × 0.80 mm package. Its listed standard frequency range is 7.98–12 MHz, though the manufacturer also says other specifications can be requested. [NDK’s application listing](https://www.ndk.com/en/products/application/automotive/block_diagram_electric.html) describes NX3225GD as two-pad. These are multiple conflicts; the standard frequency range alone does not rule out a special specification.

No exact manufacturer identity, drawing, or markings for this record have been established. Do not label a 2016 four-pad render as NX3225GD or silently replace the source geometry with NDK geometry. Obtain the actual part identity or correct the catalogue record before producing a manufacturer-specific render. The source record has not been changed.
