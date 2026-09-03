# OOMP KiCad integration

## Normal workflow

1. Run the normal `working_oomp_populate` and `working_oomp` steps. Master selections are defined in `working_oomp_populate_kicad.py`; exact family overrides belong in the corresponding populate-extra file.
2. Each component's Roboclick actions run `kicad_library_agent.py`. Files go into `parts/<id>/data/kicad/`: a symbol library containing the full OOMP ID, `machine_solder/<id>.kicad_mod`, `hand_solder/<id>.kicad_mod`, and a JSON/YAML availability manifest. Missing masters or unavailable hand-solder variants are reported, never fabricated.
3. Project actions preserve original inputs in `data/original/`, then create a separate editable copy in `data/oomp_design/`. The converted copy retains the upstream basename, hierarchical sheet filenames, and local library tables. The original inputs remain untouched.
4. Run `action_build_kicad_libraries.bat` to build all available part libraries and collect them into `kicad_libraries/`. `action_regenerate_all.bat` also packages them after its actions. Neither step opens a browser or uses an LLM.

## Master selections

Defaults use the installed KiCad masters. Set `OOMP_KICAD_ROOT` if KiCad isn't in the normal Windows installation directory. Generation requires KiCad's bundled Python/pcbnew and `kicad-cli`, plus the repository's normal Python dependencies.

An exact populate-extra override looks like:

```python
extra['kicad'] = {
    'symbol': 'Device:R_Small',
    'machine_solder': 'Resistor_SMD:R_0603_1608Metric',
    'hand_solder': 'Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder',
}
```

Editable arrays cover standard passive sizes and headers. An otherwise unspecified part may use a unique official library ID already present in a project with an approved OOMP match. Multiple alternatives require an explicit selection. No manufacturer identity or pin geometry is inferred from an unapproved match. Through-hole parts can use the same official geometry for both soldering methods. SMD parts require an actual hand-solder master; the code never grows pads automatically.

Symbols are self-contained: inherited library symbols are flattened, unit names are renamed along with the main symbol, and footprint properties point to the available OOMP variant. Footprints retain original pad geometry and add the existing uppercase MD5 alpha code (for example `1X0XV`) beside the package on silkscreen. Library provenance and licensing travel with every exported set.

## Replacement safety

`kicad_project_action.py` is an always-run Roboclick Python action. It re-extracts current inputs and uses current approved part matches. For each item it checks both the original source master and the selected OOMP master.

- KiCad normalises temporary footprint copies into the same coordinate frame, including underside mirroring. KiCad's symbol format upgrader normalises temporary symbol copies before comparison.
- Pin geometry, pin types, drawing geometry, pads, models and electrical overrides must agree. Unrecognised fields remain in the comparison: differences fail closed.
- Library names, UUIDs, nets, reference/value properties and other listed placement metadata are excluded from comparison. They are preserved in the design. The automatic reference/value text's 180-degree keep-upright convention is normalised, not treated as a physical modification.
- Replacement never changes soldering style. A design using a hand-solder master stays hand-solder. Its pads are not replaced by machine-solder pads.
- Only the verified library ID and added silkscreen annotation change in a PCB footprint. Pad trees, nets, placement and existing UUIDs are preserved. Schematic symbol instance fields/wires remain intact; footprint fields change only when the corresponding PCB instances were verified too.
- Custom imports, modified defaults, missing masters, incompatible canonical symbols and unmatched parts stay unchanged and receive a reason in `data/oomp_design/conversion_report.yaml` and `.json`.
- Original snapshots retain source checksums. New upstream revisions archive previous snapshots. Edited snapshots, generated designs or library tables are not silently overwritten. Copy `oomp_design` elsewhere before editing it.
- Every project conversion runs `kicad_validation_agent.py`: KiCad exports both netlists and verifies that component values/UUIDs and named-net pin memberships match. A structural PCB check allows only the approved library IDs and appended annotations to change. Results are saved in `validation.yaml` / `.json`; a failed check fails the action.
- Obsolete generated library entries are moved under `previous_generated/<sha256>/`, so removed entries aren't accidentally offered as active library items and their contents remain recoverable.

The generated copy is not a claim that the upstream design has passed ERC/DRC. Keep the existing design review and fabrication checks. Dense boards may need silkscreen label repositioning in an editable project copy.

## Installation and commands

Add `kicad_libraries/OOMP.kicad_sym` in KiCad's **Manage Symbol Libraries**, using nickname **OOMP**. Add both `.pretty` folders in **Manage Footprint Libraries**, using **OOMP_MachineSolder** and **OOMP_HandSolder**. Each converted project also carries a local subset and library tables; no global settings are changed automatically.

```powershell
# One part; no diagram/PNG regeneration
python -m kicad_agents.kicad_library_agent --part parts/electronic_resistor_0603_2200_ohm

# Collect already-generated part files
python -m kicad_agents.kicad_library_agent --package-only

# Full tests, including real KiCad front/back conversion fixtures
python -m unittest discover -s kicad_agents/tests -v
```

Online research/downloads for new exact master selections must use the available browser. The build and conversion agents are entirely local and deterministic. Library format reference: [KiCad S-expression documentation](https://dev-docs.kicad.org/en/file-formats/sexpr-intro/). License: [official KiCad library license](https://www.kicad.org/libraries/license/).
