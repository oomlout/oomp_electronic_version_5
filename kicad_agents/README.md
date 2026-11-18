# Component generation tools

Research, validate, and generate the records behind the OOMP component catalogue.
These tools connect editable population data to component pages, diagrams,
labels, and KiCad libraries.

**[Back to OOMP Electronics](../README.md)** · **[Add a component](../ADDING_COMPONENTS.md)** · **[Full workflow](AGENT_GUIDE.md)**

## Choose a starting point

| Task | Guide |
| --- | --- |
| Add or amend a component definition | [Adding components](../ADDING_COMPONENTS.md) |
| Add cable crimp contacts and empty housings | [Crimp connector pilot and worker instructions](CRIMP_CONNECTOR_AGENT.md) |
| Verify a supplier part and capture evidence | [JLC part intake](JLC_PART_INTAKE_AGENT.md) |
| Complete pins, dimensions, drawings, and KiCad assets | [JLC part integration](JLC_PART_INTEGRATION_AGENT.md) |
| Record a research decision | [Component record format](component_records/README.md) |
| Work through the house-parts queue | [House-parts workflow](jlc_house_parts/README.md) |
| Review symbol and footprint sources | [KiCad library guide](KICAD_LIBRARY_GUIDE.md) |

## How the pipeline fits together

```text
Population definitions → parts_source → component records → generated assets
```

`working_oomp.py` prepares records and generation actions. The output includes
diagrams, previews, READMEs, web manifests, and category navigation.

| Tool | Responsibility |
| --- | --- |
| `component_addition_agent.py` | Validate the research record and build a targeted component. |
| `kicad_library_agent.py` | Build symbols and footprints from installed official KiCad masters, with captured fallback evidence. |
| `pipeline_audit_agent.py` | Check the generation sources and saved action lists. |

IC definitions use **function → subtype → package → manufacturer → part number**.
The [component workflow](AGENT_GUIDE.md) documents the taxonomy and validation gates.

## Check changes

Run from the repository root:

```powershell
python tools/run_component_tests.py -q --noconftest --rootdir=. kicad_agents/tests/test_ic_taxonomy.py
python -m pytest kicad_agents/tests
python -m kicad_agents.pipeline_audit_agent --fail-on-error
```

The first command runs the naming regressions with project-checkout access blocked.
The second runs the broader component suite. The audit writes its reports under
`kicad_agents/generated/`.

Board processing, source imports, explorers, and fabrication belong to the
independent [project tools](https://github.com/oomlout/oomp_electronic_project_version_5/tree/main/kicad_agents).
