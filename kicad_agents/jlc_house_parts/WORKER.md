# Two-stage JLC house-parts worker

Give a smaller AI **one code and one stage at a time**. First run the detailed
[intake agent](../JLC_PART_INTAKE_AGENT.md) across the entire queue. Later run the
[integration agent](../JLC_PART_INTEGRATION_AGENT.md) for only parts whose intake passed. One writer
owns the population files and progress ledger; `next` is not a lock.

## First pass: add and classify

Copy this prompt into the worker's session:

> Read `kicad_agents/JLC_PART_INTAKE_AGENT.md`. Run
> `.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage intake`.
> Follow the guide in order, taking time to verify each step.
> Work on that one code only. Verify its official JLC page in a browser,
> classify/reuse/add its OOMP identity, save a webpage text capture and a
> browser-downloaded datasheet if possible, then pass `intake-check` and
> `intake-complete`. If a fact needed for a safe identity is missing, defer
> with a specific reason. Report only the code, ID, result and blocker.

The PDF is **optional in intake**; record its absence. Do not hold up the
queue for a datasheet, exact pin geometry, SVG, KiCad footprint, rendered
artifacts or project-wide build. Do not claim full validation at this stage.

LCSC is an approved first choice for datasheets in either stage. Load the
matching product page, check the exact identity and follow its real download
link; browser automation is allowed. Keep JLC page verification for house
status. Save the PDF with provenance and verify its contents locally.

## Second pass: complete the ecosystem work

After intake coverage, use a separate run:

> Read `kicad_agents/JLC_PART_INTEGRATION_AGENT.md`. Run
> `.venv/Scripts/python.exe -m kicad_agents.jlc_house_parts_agent next --stage full`.
> Follow the guide in order. Use written pin and dimension tables,
> not assumptions about similar parts. Work on that one intake-complete code only. Finish datasheet provenance, electrical
> and mechanical evidence, pins, package SVG, verified KiCad masters, targeted
> generation and visual review. Pass `full-check` and `full-complete`, or
> defer the full stage with a specific reason.

The stage ledger is `progress/C<number>.json`. `status` reports pending,
complete and deferred counts **separately** for intake and full validation.
Revisit a code with `next --code C<number> --stage intake|full`.

These are reusable instruction agents, not unattended research scripts. The
model needs browser access, local file tools and (for full integration) image
viewing. It must read command output, resolve routine errors, and preserve
unrelated edits. Missing evidence gets a precise handoff, never a guessed value.
For a batch, repeat the same guide only after each code has a ledger outcome;
do not mix stages or run concurrent writers against the shared population files.
