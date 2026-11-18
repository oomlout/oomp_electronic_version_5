# OOMP Electronics

**A component catalogue that connects the part in your drawer to the part in your design.**

OOMP brings component identities, datasheets, pinouts, dimensions, drawer labels,
and KiCad assets together in one place. Browse a part, check its details, and use
the same identity across purchasing records, physical storage, and electronic projects.

**[Browse components](navigation/README.md)** · **[KiCad libraries](kicad_libraries/README.md)** · **[Add a component](ADDING_COMPONENTS.md)** · **[Electronic projects](https://github.com/oomlout/oomp_electronic_project_version_5)**

| Identify the pins | Check the dimensions |
| :---: | :---: |
| [![LMV321-TR pinout with its short code and three-word label][pinout]][example] | [![LMV321-TR package dimensions][dimensions]][example] |

*An example from the catalogue: [Gainsil LMV321-TR in SOT-23-5][example]. Its page
connects these drawings to the datasheet, component record, labels, and KiCad assets.*

## Find what you need

| I want to… | Start here |
| --- | --- |
| Find a component by family or package | [Component catalogue](navigation/README.md) |
| Search locally by name, supplier code, or short name | [Parts Explorer](webserver/README.md) |
| Use OOMP symbols and footprints in KiCad | [Installable libraries](kicad_libraries/README.md) and [library guide](kicad_agents/KICAD_LIBRARY_GUIDE.md) |
| Add a part or improve its data | [Adding components](ADDING_COMPONENTS.md) |
| Make studio renders with package markings | [Display-render pipeline and agent guide](kicad_agents/DISPLAY_RENDER_AGENT.md) · [GPT-6.1 Terra launch prompt](kicad_agents/DISPLAY_RENDER_TERRA_PROMPT.md) |
| Research and integrate supplier parts | [Intake guide](kicad_agents/JLC_PART_INTAKE_AGENT.md) → [integration guide](kicad_agents/JLC_PART_INTEGRATION_AGENT.md) |
| Explore boards that use these components | [OOMP Electronic Projects](https://github.com/oomlout/oomp_electronic_project_version_5) |

## What is in a component record?

- **Identity and purchasing:** a canonical OOMP ID, manufacturer and part number,
  supplier references, and recorded research evidence.
- **Electrical and mechanical details:** documented pins, ratings, dimensions,
  and datasheets where available.
- **Drawings and labels:** SVG diagrams, PNG previews, short codes, and drawer labels.
- **KiCad assets:** symbols and footprints with source provenance and explicit
  reports for assets that still need review.

Each component lives in `parts/<oomp-id>/`. Its `README.md`, `working.yaml`, and
`web.yaml` are at the root; drawings, datasheets, and KiCad files live under `data/`.
Available detail varies by component: check the record and its supporting evidence.

## Browse locally

The checked-in pages and assets can be browsed directly on GitHub. For local
search and image galleries, run the Flask-based Parts Explorer from the repository root
using the project's Python environment:

```powershell
python -X utf8 -m webserver.app
```

Open the `/explore` address for the configured port. Host, port, component sources,
and display options are explained in the [Parts Explorer guide](webserver/README.md).

## Update a component

Edit the appropriate `working_oomp_populate_<family>.py` definition and its
`_extra.py` metadata, then generate the selected part. For example:

```powershell
$partId = 'electronic_resistor_0603_10000_ohm'
python action_generate.py --filter $partId
```

Normal generation retains existing PNGs. To deliberately refresh them for the
same selection:

```powershell
python action_regenerate_all.py --filter $partId
```

Component generation uses Python, the Oomlout component-generation framework,
Roboclick, Inkscape, and KiCad. Drawer-label rendering also needs **Arial Narrow
Bold**; both system and per-user Windows font installations are supported.
Use an environment where the framework modules are importable before running
generation. See the [component workflow](kicad_agents/AGENT_GUIDE.md) for the
research, validation, and generation steps.

### IC naming

ICs use **function → subtype → package → manufacturer → part number**:

```text
electronic_ic_<function>_<subtype>_<package>_<manufacturer>_<mpn>
```

These occupy taxonomy levels **3, 4, 5, 14, and 15**. Levels 6–13 are empty, so
the package is the final regular taxonomy field. Short codes and BIP39 labels
are computed from the current canonical ID. See the [naming migration](migrations/README.md)
and [old-to-new ID map](migrations/ic_package_last_ids.json).

## Two repositories, connected by component IDs

| Repository | Owns |
| --- | --- |
| **OOMP Electronics — this repository** | Component definitions, datasheets, drawings, labels, mounting-hole definitions, and installable KiCad libraries. |
| **[OOMP Electronic Projects](https://github.com/oomlout/oomp_electronic_project_version_5)** | Board definitions, source imports, component matching, board explorers, and manufacturing outputs. |

Both run independently. Projects use a committed component snapshot and update
it explicitly. Public project and usage links are configured in
[`repository_config.json`](repository_config.json); component generation does
not need a project checkout.

## Maintainer reference

- [Component tooling](kicad_agents/README.md) and [workflow](kicad_agents/AGENT_GUIDE.md)
- [Component expansion ledger](kicad_agents/COMPONENT_EXPANSION_LEDGER.md)
- [Research record format](kicad_agents/component_records/README.md)
- [KiCad fallback evidence](source_file/kicad_library/project_fallback_candidates.json)
  retains previous candidate choices and ambiguity checks. New verified selections
  belong in component population data.

[example]: parts/electronic_ic_amplifier_operational_single_rail_to_rail_input_output_sot_23_5_gainsil_lmv321_tr/README.md
[pinout]: parts/electronic_ic_amplifier_operational_single_rail_to_rail_input_output_sot_23_5_gainsil_lmv321_tr/data/working_svg_square_pins_300.png
[dimensions]: parts/electronic_ic_amplifier_operational_single_rail_to_rail_input_output_sot_23_5_gainsil_lmv321_tr/data/working_svg_dimensioned_300.png
