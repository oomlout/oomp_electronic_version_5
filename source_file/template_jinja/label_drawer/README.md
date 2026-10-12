# Electronic drawer labels

Run `action_make_label_overwrite.bat` to force regeneration for all electronic
components. It can be launched from another directory. To select a family or
part, use `action_make_label_overwrite.bat --filter electronic_resistor_0805_`.

Each part receives:

| File | Inches | Millimetres |
| --- | --- | --- |
| `label_drawer_3x2.svg` | 3 x 2 | 76.2 x 50.8 |
| `label_drawer_1_5x1.svg` | 1.5 x 1 | 38.1 x 25.4 |

Print at **100% / actual size**. The black-and-white design uses Arial Narrow
Bold: type and package in a black header, the key value or part number in large
type, up to three supporting lines, and the existing three-word BIP39 name in
bold below a rule. Both sizes carry the same information at proportional scale.

## Details selected by type

| Type | Main detail | Supporting details, where recorded |
| --- | --- | --- |
| Resistor / resistor array | Resistance | Tolerance, power, array count, package |
| Capacitor | Capacitance | Voltage, dielectric, tolerance, polarity |
| Connector | Pin count | Family, pitch, mounting, orientation, socket/plug |
| Crystal | Frequency | Load capacitance, ESR, pins, package |
| Inductor / ferrite bead | Inductance / impedance | Current, tolerance, DCR, test frequency |
| LED | Colour | Driver/family, forward voltage/current, luminous intensity |
| IC | Part number | Function and available supply/output ratings |
| Transistor | Part number | Polarity, device type, voltage and current |
| Diode | Part number | Diode type, reverse/Zener voltage and current |
| Relay | Coil voltage | Contact arrangement, contact rating, part number |
| Switch | Switch type | Circuit, positions, current, voltage, part number |
| Fuse | Current or part number | Resettable/disposable type, voltage, package |
| Sensor / optical device | Part number | Sensing type, frequency/size, package |
| Potentiometer / NTC | Resistance | Trimmer style or current, part number |
| Display | Resolution or part number | Size, technology/interface, logic supply |
| Heatsink | Dimensions | Part number or supplier identifier |
| Prototyping / wire | Point count / length | Form, ends, colour or bundle quantity |
| Antenna / battery / buzzer / transformer | Part number | Available form, size, frequency or voltage |

The 29 current electronic types are covered. Navigation, project and mechanical
mounting-hole records do not represent electronic drawer contents and are
excluded. Missing ratings are not inferred. Supporting fields are selected in
priority order to fit the label; `data/label_drawer.yaml` records the complete
selected details and any omitted lines. Detailed source ratings remain in the
part record and datasheet. Manufacturer and LCSC identifiers use spare lines.

## Regeneration and Jinja

`working_oomp.py` registers an always-run drawer-label recipe before the web
manifest action. Therefore a standard `action_make_all.py` run redraws the
labels. The recipe runs `working_drawer_labels.py` to read current generated
metadata, `parts_source/<part>/working.yaml`, and optional per-part
`working_manual.yaml`, in that precedence order. Nested electrical values are
merged, so partial manual overrides preserve the other source ratings.

Preparation writes `data/label_drawer.yaml`. Two native `text_jinja_template`
actions then load this fresh YAML and render the two SVG templates in this
folder. Action definitions contain no frozen component values. `file_test` is
empty and `always_run_on_regeneration` is true. The web manifest stays last.
The batch updates these recipes without running unrelated CAD, AI or project
actions and preserves the other recipe definitions.

Both Jinja actions explicitly disable PDF and PNG conversion. Preparation and
the batch remove only `label_drawer_3x2.pdf`, `label_drawer_1_5x1.pdf` and their
PNG counterparts in the part root or its `data` folder. Datasheets and other
PDFs are unaffected.

Optional per-part overrides in `working_manual.yaml`:

```yaml
label_drawer_overrides:
  primary: 10 kOhm
  package: '0805'
  details:
    - +/-1% | 1/8 W
    - Preferred assembly resistor
```

`type` may also be overridden. An omitted override uses the type-specific
selection. Existing BIP39 identifiers are preserved; new identifiers use the
standard first three 11-bit words from the taxonomy ID's MD5.

Requirements: Python with PyYAML, Jinja2 and Pillow, plus **Arial Narrow Bold
(`ARIALNB.TTF`)**. The generator stops if the font is missing rather than sizing
text for a substituted font. Inkscape is not required for SVG regeneration.

Validation: `python -m pytest kicad_agents/tests/test_drawer_labels.py -q`.
Tests cover type priorities, dimensions and text fit across the generated
catalogue, action ordering and repeatability, native Python/Jinja execution
with changed source/manual data, and selective stale-render cleanup.
