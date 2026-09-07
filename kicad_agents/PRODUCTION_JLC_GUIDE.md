# JLCPCB production pipeline

Every project part has a Roboclick `run_python` action that calls
`kicad_agents/production_jlc_action.py`. The action reads
`data/kicad_file.kicad_pcb` by default and writes:

```text
data/production_auto_generate/
  gerbers_jlc.zip          # fabrication upload; BOM/CPL intentionally stay outside
  bom_jlc.csv              # Comment, Designator, Footprint, LCSC Part #
  cpl_jlc.csv              # Designator, Mid X, Mid Y, Rotation, Layer
  bom_missing_lcsc.csv     # explicit purchasing review queue
  data/
    gerbers/               # unpacked Gerbers, Excellon drills and drill maps
    components.json/.yaml # OOMP identity, supplier identity, placement and pad names
    kicad_position_raw.csv # unmodified KiCad position export for comparison
    drc.json               # KiCad DRC report
    manifest.json/.yaml    # source hash, commands, settings and output hashes
    generation_status.yaml
```

The Gerber ZIP is uploaded as the PCB fabrication file. Upload `bom_jlc.csv`
and `cpl_jlc.csv` separately for assembly. Always inspect the layers, drill
map, `data/drc.json`, missing-LCSC queue, rotations and JLCPCB's online preview
before ordering.

## Why the action uses KiCad CLI

[KiBot](https://github.com/INTI-CMNB/KiBot/) is an excellent automation layer
and informed this layout. Its installation guide still recommends Docker or
WSL for Windows, however, while this repository already requires KiCad and has
the supported `kicad-cli` executable. Calling that executable directly keeps
the local Roboclick action small, deterministic and native on Windows. Set the
`KICAD_CLI` environment variable only when automatic KiCad discovery is not
correct.

The export follows JLCPCB's documented file expectations:

- all board copper layers, paste, silkscreen, solder mask and Edge.Cuts use
  Protel extensions;
- drills use Excellon, millimetres, absolute origin and routed slots;
- BOM columns are Comment, Designator, Footprint and LCSC Part #;
- CPL columns are Designator, Mid X, Mid Y, Rotation and Layer, with both
  sides in the same file and counter-clockwise degrees.

Primary references:

- [JLCPCB Gerber preparation](https://jlcpcb.com/help/article/gerber-files-preparation)
- [JLCPCB BOM format](https://jlcpcb.com/help/article/bill-of-materials-for-pcb-assembly)
- [JLCPCB CPL format](https://jlcpcb.com/help/article/pick-place-file-for-pcb-assembly)
- [KiBot outputs](https://kibot.readthedocs.io/en/latest/configuration/outputs.html)
- [KiBot installation](https://kibot.readthedocs.io/en/latest/installation.html)

## Human-editable project settings

Put overrides beside the other version details in
`working_oomp_populate_project.py`. Empty lists and dictionaries are added by
default, so most boards need no production-specific declaration.

```python
{
    "version": "current",
    "project_file_basename": "my_board",
    "production_exclude_references": ["FID1", "TP1"],
    "production_lcsc_overrides": {
        "R1": "C4190",
    },
    "production_rotation_offsets": {
        "U1": 90,
    },
    "production_position_offsets_mm": {
        "J1": [0.0, 0.25],
    },
}
```

Available fields:

| Field | Meaning |
| --- | --- |
| `production_board_source` | Optional path relative to the project part. Empty means `data/kicad_file.kicad_pcb`. |
| `production_oomp_metadata_board` | Optional converted board used only to collect substituted OOMP footprint/pad names. The action otherwise discovers `data/oomp_design/<project_file_basename>.kicad_pcb`. |
| `production_exclude_references` | References deliberately omitted from both BOM and CPL. |
| `production_lcsc_overrides` | Verified reference-to-LCSC-number corrections. |
| `production_rotation_offsets` | Degrees added to individual CPL rotations after KiCad export. |
| `production_position_offsets_mm` | `[x, y]` millimetres added to an individual component centroid. |

The BOM and CPL always use the same final reference set. KiCad DNP,
exclude-from-BOM and exclude-from-position flags are honoured. LCSC identity is
resolved in this order: explicit project override, PCB property, then the
confirmed OOMP part's `working.yaml`. Missing identities stay visible in the
BOM and are also written to `bom_missing_lcsc.csv`; the generator never invents
a purchasing code.

When an OOMP design copy exists, `data/components.yaml` takes pad names from that
copy while the fabrication outputs continue to use the declared production
board. This makes semantic substituted names such as `VBUS`, `GND` and `CC1`
available for auditing without silently changing the board being manufactured.

Run one project through the normal pipeline:

```bat
action_generate.bat --filter oomp_project_github_user_repository_current
```

Or invoke the generated action payload through Roboclick as usual. Do not edit
the generated CSV, manifest or YAML as a substitute for editing the populate
settings: regeneration will replace generated production data.

`data/production_auto_generate/data/generation_status.yaml` is the action gate.
It is written last, after every public upload file and internal audit file is
complete, and the finished staging directory is then moved into place. The
Normal generation honours this gate and skips an already-complete production
bundle. Single-part and full regeneration deliberately ignore the gate and
rebuild the production bundle.
