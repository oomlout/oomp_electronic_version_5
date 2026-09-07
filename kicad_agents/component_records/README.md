# Component research records

One small YAML file records the browser-verified decision for each expansion
ledger item. These files are review inputs for
`kicad_agents/component_addition_agent.py`; generated component facts still
come from the applicable `working_oomp_populate_<family>.py` and
`working_oomp_populate_<family>_extra.py` files.

Keep the record plain and editable:

```yaml
format_version: 1
ledger_id: E0000
status: researched
family: transistor
part_id: electronic_example
exact_identity: true
package: sot_23
pin_count: 3
datasheet_required: true
project_references:
  - Q1
research:
  manufacturer: Example Manufacturer
  manufacturer_part_number: EXAMPLE-1
  lcsc_part_number: C123456
  lcsc_decision: Exact manufacturer, suffix and package confirmed.
  product_url: https://www.lcsc.com/product-detail/C123456.html
  datasheet_url: https://example.com/datasheet.pdf
  browser_sources:
    - https://www.lcsc.com/product-detail/C123456.html
    - https://example.com/product
  evidence_notes:
    - The fitted BOM, package and manufacturer suffix agree.
    - The manufacturer datasheet confirms the complete pinout and dimensions.
```

If no exact LCSC listing exists, leave `lcsc_part_number` blank and explain the
rejected candidate in `lcsc_decision`. Never use a code for a different suffix
or package merely because the base part number matches.

For a generic device family, use `exact_identity: false` and record its common
number as `research.generic_part_number` (and `part_number_generic` in populate
extra). Keep the manufacturer part number and LCSC number blank. If a supplier
datasheet is used as a representative reference, add a plain `datasheet_note`
in populate extra explaining that its manufacturer-specific limits are not a
guarantee for every member of the generic family.

The build also refreshes this part's navigation ancestors and repackages the
KiCad library. It does not rebuild any project README, board image, or explorer.
