# OOMP KiCad libraries

In KiCad **Preferences → Manage Symbol Libraries**, add `OOMP.kicad_sym` as **OOMP**. In **Manage Footprint Libraries**, add `OOMP_MachineSolder.pretty` and `OOMP_HandSolder.pretty` using those exact nicknames.

For a portable project, place these files beside its `.kicad_pro` and use the included `sym-lib-table` / `fp-lib-table`. Merge entries if tables already exist; do not overwrite them.

Missing assets are listed in [NEEDS_REVIEW.md](NEEDS_REVIEW.md) and [manifest.yaml](manifest.yaml); pads are never guessed. Individual part sources live in `parts/<oomp_id>/data/kicad/`.

These derivatives retain the official KiCad library licensing, including its design exception. See the [KiCad library license](https://www.kicad.org/libraries/license/). Master source identifiers and checksums are recorded per part.
