# Adding boards and components

Edit the small lists and dictionaries in `working_oomp_populate_*.py`, then run
one generation command. These Python files are the source of truth. You do
**not** need to hand-write YAML/JSON, Markdown pages, navigation links,
Roboclick actions, SVGs or HTML for a normal addition to a supported family.

## The short version

| What you are adding | Where to enter the details |
| --- | --- |
| Another board or version | The `projects` list in [working_oomp_populate_project.py](working_oomp_populate_project.py) |
| A resistor value or size | The lists in [working_oomp_populate_resistor.py](working_oomp_populate_resistor.py) |
| A capacitor value or size | The lists in [working_oomp_populate_capacitor.py](working_oomp_populate_capacitor.py) |
| Another connector, IC, LED, crystal, etc. | The matching `working_oomp_populate_<family>.py` |
| Manufacturer details, supplier IDs, pins, exact dimensions or KiCad masters | A simple `if current in extras_dict:` block in that family's `working_oomp_populate_<family>_extra.py` |
| A confirmed project-to-part match | The board version's `match_overrides` dictionary in the project populator |

From this repository directory, run:

```bat
action_generate.bat --filter YOUR_OOMP_ID
```

For example:

```bat
action_generate.bat --filter electronic_resistor_0603_2000_ohm
action_generate.bat --filter oomp_project_github_hanqaqa_easyduino_atmega328p_arduino_uno_current
```

In PowerShell use `./action_generate.bat ...`. The equivalent Python command is
`python action_generate.py --filter YOUR_OOMP_ID`.

This regenerates populate definitions, compiles the selected records through
`working_oomp`, runs their deterministic Roboclick actions, refreshes navigation
and packages the KiCad libraries. Browser/AI actions are skipped. It uses the
system-installed Git for board repositories. It creates missing PNGs and
300-pixel previews but retains existing PNGs.

The filter is a **substring** of the OOMP ID, not a wildcard. A full ID is safest;
`--filter _2000_ohm` builds that resistor value in all defined sizes. A broad
family prefix intentionally generates all matching parts and can take longer.

## 1. Add a board

Open `working_oomp_populate_project.py`. Add one dictionary to `projects`, using
the same indentation as its neighbours. This is the real Easyduino entry:

```python
{
    "github_user": "hanqaqa",
    "github_repository": "easyduino",
    "github_url": "https://github.com/Hanqaqa/Easyduino",
    "repository_url": "https://github.com/Hanqaqa/Easyduino.git",
    "versions": [
        {
            "board": "atmega328p_arduino_uno",
            "board_name": "ATmega328P Arduino Uno",
            "board_url": "https://github.com/Hanqaqa/Easyduino/tree/master/Atmega328p%20Arduino%20Uno",
            "version": "current",
            "git_ref": "master",
            "sparse_checkout": True,
            "project_file_folder": "Atmega328p Arduino Uno",
            "project_file_basename": "Easyduino_Atmega",
            "project_file_path": "Atmega328p Arduino Uno/Easyduino_Atmega",
            "match_overrides": {
                "J2": "electronic_connector_header_2_54_mm_pitch_through_hole_2_pin",
            },
        },
    ],
},
```

This is already present; do not add it twice. Copy the pattern for another
board and replace the values with that board's actual details.

| Field | What to type |
| --- | --- |
| `github_user`, `github_repository` | Lowercase taxonomy names; replace spaces and hyphens with underscores. |
| `github_url`, `repository_url` | Actual upstream URLs. Preserve their real spelling, case and hyphens. |
| `board` | Optional extra taxonomy level for a repository containing several boards. Lowercase with underscores. Omit for a single-board repository. |
| `board_name` | Readable board title, including distinguishing model/revision details. |
| `board_url` | Link to this board's folder on GitHub; used by the generated project page. |
| `version` | `current` for the moving latest version; defaults to `current`. Use a stable name such as `rev_a` for a historical version. |
| `git_ref` | Actual upstream branch, tag or commit. `current` pulls that branch; historical versions check out the specified ref without pulling. Defaults to `main`, so specify `master` when appropriate. |
| `sparse_checkout` | `True` to check out only the selected board folder and root files. Useful for multi-board repositories. |
| `project_file_folder` | Directory inside the repository, with original case and spaces. Use `/`, and `""` if files are at repository root. |
| `project_file_basename` | Common filename stem, without an extension. |
| `project_file_path` | Folder plus filename stem; keep consistent with the previous two fields. |
| `match_overrides` | Optional reference-to-OOMP-ID matches that you have verified. Use `{}` initially. |

The source must contain modern `.kicad_pcb`, `.kicad_sch` and `.kicad_pro` files.
Legacy Eagle or old `.sch` projects must be converted with KiCad first. Followed
hierarchical sheets are copied automatically; unrelated schematics elsewhere
in the repository are not imported as extra boards.

### Taxonomy and versions

Single-board repository:

```text
oomp / project / github / user / repo / current
```

Multi-board repository:

```text
oomp / project / github / user / repo / board / current
```

The Easyduino ID is:

```text
oomp_project_github_hanqaqa_easyduino_atmega328p_arduino_uno_current
```

For another board in the **same** repository, append another entry to `versions`
with a different `board`, source folder and file stem. For a previous version,
copy that board's entry, keep `board` unchanged, change `version` and `git_ref`,
and adjust the file path only if it differed in that revision. This produces
another part, rather than overwriting `current`.

### Generate and check the board

1. Run `action_generate.bat --filter <full-project-id>`.
2. Open `parts/<id>/README.md` and `data/generated_data/board_explorer.html`.
3. Review `data/generated_data/unmatched_parts.yaml` (or JSON) and the browser
   research queue. Do not accept a near match just to remove a warning.
4. Add any missing components through their populate files. Build those
   components first. Put confirmed mappings in the board's `match_overrides`,
   then rerun the same project command.

For example, after verifying a connector's pitch, row count and mounting style:

```python
"match_overrides": {
    "J2": "electronic_connector_header_2_54_mm_pitch_through_hole_2_pin",
},
```

Overrides are declarations of an exact match, not search hints. Never force an
IC, USB connector or crystal onto a similar-looking but electrically different
part. Unknown parts still appear in structured data and the explorer with their
actual PCB pads; they do not get an invented OOMP definition.

The action also generates InteractiveHtmlBom and a guarded OOMP KiCad design
copy. Read `data/oomp_design/conversion_report.yaml` and `validation.yaml`.
Only symbols/footprints that match official KiCad defaults are replaced.
Custom or changed items are retained and reported. Original files are preserved
in `data/original/`; the ignored checkout is under `data/git/`.

## 2. Add a resistor or capacitor

### Resistor value

In `working_oomp_populate_resistor.py`, append a number in ohms to
`additional_resistance_values`:

```python
additional_resistance_values = [200, 510, 2000, 5100, 102000, 133000, 510000]
```

The existing nested loops pair these values with `sizes`. For example, `2000`
and `0603` produce `electronic_resistor_0603_2000_ohm`. Do not duplicate a value
already generated by the base-value/multiplier lists.

To add only a specific size/value pair, append a row to `low_value_resistors`
instead of expanding the entire grid; despite its name, this is the existing
explicit-pair list. Use a decimal underscore for sub-ohm values, e.g.
`["2512", "0_2_ohm"]`.

### Capacitor value

In `working_oomp_populate_capacitor.py`, find the block with the required
`sizes` and add the capacitance to that block's `capacitance_values`:

```python
sizes = ["0603"]
capacitance_values = [
    "22_pico_farad",
    "10_nano_farad",
    "100_nano_farad",
    "1_micro_farad",
    "4_7_micro_farad",
    "10_micro_farad",
]
```

These are existing entries, shown as a template. Do not use `100_nano_farad`
for 10 nF: the human-readable name is generated from the actual value.
For polarized/tantalum/electrolytic capacitors use the relevant style, package
and voltage block, not the generic ceramic grid.

Run the generation command with the new full ID. Common supported sizes already
have diagram and KiCad defaults. Adding a value does not require drawing code.

## 3. Add an exact component

Use an existing family file, not a new standalone agent. Inside its `main`
function, add a dictionary to `options` or copy an adjacent row in its explicit
component list. The following is an existing SOT-23-5 IC expressed as a simple
dictionary; use its pattern with your verified part details:

```python
options.append({
    "taxonomy_2": "ic",
    "taxonomy_3": "sot_23_5",
    "taxonomy_4": "amplifier",
    "taxonomy_5": "operational_single_rail_to_rail_input_output",
    "taxonomy_14": "gainsil",
    "taxonomy_15": "lmv321_tr",
})
```

`taxonomy_1` defaults to `electronic`. Non-empty taxonomy levels are joined in
number order to make the ID. Exact ICs and USB connectors include manufacturer
at level 14 and normalized MPN at level 15. Generic passives normally do not put
a manufacturer or MPN in their taxonomy. Single-row headers use `6_pin`, not
`1x6`; dual-row headers use a form such as `40_pin_dual_row`.

### Extra details, pins and dimensions

In `working_oomp_populate_ic_extra.py`, add or edit a matching block. Here is a
shortened real example; there is already a longer entry for this device:

```python
current = "electronic_ic_sot_23_5_amplifier_operational_single_rail_to_rail_input_output_gainsil_lmv321_tr"
if current in extras_dict:
    part = extras_dict[current]
    part["part_number_manufacturer"] = "LMV321-TR"
    part["part_number_manufacturer_gainsil"] = "LMV321-TR"
    part["part_number_lcsc"] = "C362273"
    part["name_readable_override"] = "IC LMV321-TR SOT-23-5"

    pin_rows = [
        ["1", "in_positive", "input"],
        ["2", "vss", "power"],
        ["3", "in_negative", "input"],
        ["4", "output", "output"],
        ["5", "vdd", "power"],
    ]
    part["pins"] = {}
    for number, name, pin_type in pin_rows:
        part["pins"][f"pin_{number}"] = {
            "number": number, "name": name, "type": pin_type,
        }

    part["dimensions_mm"] = {"length": 2.92, "width": 2.8}
    part["ic_dimensions_mm"] = {
        "body_length": 2.92,
        "body_width": 1.6,
        "body_height": 1.15,
        "overall_width": 2.8,
        "pin_pitch": 0.95,
        "pin_width": 0.4,
        "pin_length": 0.45,
    }
```

Use the actual datasheet's pin numbers and dimensions, not this example's values
for a different part. `name_readable_override` is optional; omit it to use the
automatic readable name. Explicit dimension dictionaries survive repeat
generation rather than being replaced by family defaults.

Other supported families use `connector_dimensions_mm` or
`header_dimensions_mm`; copy the keys from the nearest **same package/style**
example. The drawing code remains in `working_svg.py`, not in the extra file.

### MPNs, distributors and datasheets

- Preserve the real manufacturer's spelling/punctuation in
  `part_number_manufacturer`. Normalize only taxonomy tokens.
- Add `part_number_lcsc = "C..."` when verified. The link is generated for you.
  `part_number_digikey`, `part_number_mouser` and `part_number_farnell` are also
  supported. An optional `<field>_url` sets an exact supplier URL.
- A manufacturer-specific alternative can use
  `part_number_manufacturer_uni_royal` or `part_number_manufacturer_yxc` without
  changing the generic taxonomy. Use the common distributor field for the
  primary linked listing.
- Leave unknown fields out; do not invent MPNs or LCSC numbers. Research and
  PDF downloads use the available browser, never direct Python HTTP requests.

A datasheet PDF is a source asset, not metadata that Python can create. If you
already downloaded one, store it in `source_file/datasheets/<id>.pdf` and declare
the copy in the same populate-extra block:

```python
part["file_copy"] = [{
    "file_source": f"source_file/datasheets/{current}.pdf",
    "file_destination": "datasheet.pdf",
}]
```

The generated action puts it at `parts/<id>/data/datasheet.pdf` and links it in
the README. Do not declare a file copy until the source file exists. Existing
parts may use `parts_source/<id>/datasheet.pdf`; those input PDFs remain valid.
No hand-authored research YAML is required for this ordinary populate workflow;
the more rigorous expansion-ledger workflow is optional and documented in the
[agent guide](kicad_agents/AGENT_GUIDE.md).

### KiCad symbol and footprint selections

Passives and common headers have defaults in `working_oomp_populate_kicad.py`.
To override them, add `part["kicad"]` in the same extra block with these fields:

```python
part["kicad"] = {
    "symbol": "Device:R_Small",
    "machine_solder": "Resistor_SMD:R_0603_1608Metric",
    "hand_solder": "",  # Choose an actual official HandSolder master if available.
}
```

This example is **for a resistor**, not the IC above. Select the correct official
KiCad library IDs for the device, including pin numbering and package variant.
Empty entries are reported for review; they do not cause invented geometry.
Through-hole hand/machine versions may intentionally share a master. SMT
hand-solder pads must come from a verified master, not automatic pad enlargement.

Generate the component, then rerun any affected project. Per-part files go under
`data/kicad/`; the combined libraries go under `kicad_libraries/`.

## Component categories

Category defaults are plain arrays in `working_oomp_populate_category.py`.
Resistors and resistor arrays share `resistor`; IC functions become categories
such as `mcu`, `memory`, `logic`, `amplifier` and `power_management`.
Every electronic/mechanical part gets `category` and `category_name` in both
its source and generated `working.yaml`. Categories do not change the OOMP ID.

For a specific component, enter an override in its populate dictionary:

```python
option["category"] = "logic"
```

Or in its existing populate-extra `if current in extras_dict:` block:

```python
part["category"] = "memory"
```

Use lowercase underscore-separated names. Custom categories are supported.
Run the component generation command, then rerun affected projects to refresh
their copied metadata and explorer hierarchy. No HTML edits are needed.

In the explorer, category checkboxes select **all members on both sides**, even
while searching. Individual component checkboxes let you refine or combine
selections. **Highlight all selected nets** highlights the union of their nets,
including other connected pins; common nets are only drawn once. It defaults
off. **Zoom to net** also works on this combined highlight. Clicking a pin/net
returns to following that single net; Escape clears net highlighting without
discarding the component selection. **Clear selection** clears the components.

Unmatched board items get a coarse, labelled KiCad category hint until an OOMP
match exists; this never constitutes an accepted catalogue match.

## What generation writes

```text
working_oomp_populate_<family>.py + *_extra.py     <- edit these
  -> parts_source/<id>/working.yaml              <- generated
  -> parts/<id>/working.yaml                     <- generated action definitions
  -> parts/<id>/README.md                        <- generated
  -> parts/<id>/data/                            <- diagrams, PDFs, KiCad assets
  -> navigation/.../README.md                    <- generated category links
```

Project `data/` additionally contains copied KiCad inputs, original snapshots,
`generated_data` JSON/YAML, per-component records, board images, explorer HTML,
InteractiveHtmlBom and the guarded OOMP design. `git/` and `project_source/`
remain ignored. Nothing is committed or pushed automatically.

## When you intentionally want new PNGs

After changing a drawing's dimensions or styling, use:

```bat
action_regenerate_all.bat --filter YOUR_OOMP_ID
```

Omit the filter only for a deliberate full-repository rebuild. This regenerates
existing PNGs and previews as well as other outputs; browser actions are still
skipped. Normal `action_generate.bat` keeps the low-churn PNG default.

## Final checks and limits

- Check the part README, pin labels, dimensioned SVG and 300-pixel preview.
- For boards, check both sides, mounting holes, net colours and optional
  **Zoom to net**, plus unmatched-part and KiCad-conversion reports.
- Missing files usually mean the branch, case-sensitive path, stem or file
  extension in the project entry is wrong. Fix that entry, not the generated
  copies.
- An unknown family or genuinely new package drawing needs a reusable renderer
  added once to the framework. Merely typing a new package name cannot establish
  its dimensions, pin arrangement or solder geometry. After that support exists,
  additional components again need only populate data.
- Tests: `python -m unittest discover -s kicad_agents/tests -v` and
  `python -m kicad_agents.pipeline_audit_agent --fail-on-error`.
