# OOMP electronics

[Browse the component catalogue by category](navigation/README.md)

Electronic components, mounting holes, and KiCad projects are defined in the
`working_oomp_populate_*.py` files. Python and Roboclick generate their records,
diagrams, previews, and documentation.

- [Component and project workflow](kicad_agents/AGENT_GUIDE.md)
- [Add a board or component by editing populate data](ADDING_BOARDS_AND_COMPONENTS.md)
- [Navigation, file layout, and build commands](kicad_agents/README.md)
- [Component expansion list](kicad_agents/COMPONENT_EXPANSION_LEDGER.md)
- [OOMP KiCad libraries and guarded design conversion](kicad_agents/KICAD_LIBRARY_GUIDE.md)
- [Installable symbol and footprint libraries](kicad_libraries/README.md)

Each generated part keeps `README.md` and `working.yaml` at its root; supporting
files live in `data/`. Project pages include top/bottom board drawings, mounting
hole tables, an offline board explorer, and InteractiveHtmlBom.

Run `action_generate.bat --filter <oomp-id>` for a normal populate/action build
and navigation refresh, retaining existing PNGs. Run `action_regenerate_all.bat` for a complete rebuild, including existing PNGs
and 300-pixel previews. Browser-driven actions are skipped. Normal runs preserve
existing PNGs; forcing a rebuild does not change that default.

The project HTML links target GitHub Pages. After publishing, enable Pages for
the `main` branch and `/ (root)` folder. The generated HTML also opens locally
without external scripts or stylesheets.
