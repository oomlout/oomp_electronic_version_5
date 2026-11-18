# Launch prompt for GPT-6.1 Terra

Select GPT-6.1 Terra in the new agent's model selector, open the electronics
checkout as its workspace, and paste the text below. The instructions do not
change the selected model themselves. This prompt is for the next render batch;
it does not resume component ingestion or the paused duplicate audit.

```text
Continue the display-render pipeline in C:\gh\oomp_electronic_version_5.
If the checkout is elsewhere, use the actual workspace root throughout.

Read in this order:
1. Applicable AGENTS.md instructions, if any.
2. ADDING_COMPONENTS.md.
3. kicad_agents/DISPLAY_RENDER_AGENT.md.
4. kicad_agents/DISPLAY_RENDER_TERRA_RUNBOOK.md.
5. source_file/display_render/recipes.json and studio.json.
Then inspect the renderer, marking policy and publisher listed in the runbook.

The approved pilot is electronic_resistor_0603_10000_ohm. Preserve its appearance.
Your assignment is up to FIVE additional existing 0603 resistor catalogue parts
that can use the reviewed chip-resistor adapter and whose selected manufacturer,
exact MPN, tolerance and marking policy you can verify. Prefer the same UNI-ROYAL
series as the pilot. Discover eligible parts from actual local source records;
do not invent IDs, MPNs, supplier matches or printed codes. Skip already completed
renders. If I supply exact IDs with this prompt, use only those IDs instead.

Record the exact selected IDs and evidence before editing recipes. Then work
through each selected part: evidence review, recipe, --check, scratch preview,
visual inspection, final render, artifact validation, selected-part publication.
Keep a resumable batch note using the runbook template. Proceed autonomously
within this scope; you do not need approval between successful stages.

Use actual KiCad geometry, manufacturer-backed markings, the existing materials
and studio, and only PNG/WebP/provenance outputs. Reuse local datasheets and models.
Do not guess markings from a procurement suffix or apply E96 just because a value
fits. Unsupported values or missing evidence are blockers for that candidate.
Do not expand into another package or family, implement a new adapter, change the
shared studio, or weaken validation to complete the batch.

Preserve unrelated edits. Do not resume duplicate repair or ingestion, modify the
project repository, run whole-catalogue generation, commit, push, export persistent
CAD/meshes, or rerender the approved pilot unnecessarily. Use the render virtual
environment for rendering and normal repository Python for publishing/tests.

Inspect images with an available image-viewing tool. A successful command alone
is not visual approval. Never publish an uninspected image. Do not claim files,
downloads, test passes, or visual checks that you did not observe. If blocked on
one candidate, record why and continue independently with another eligible one;
finish with fewer than five if evidence does not support five.

At completion report exact IDs, printed markings, preview links/images, tests,
artifact sizes, evidence limitations and any unfinished stages. Link the batch
note so another agent can resume without repeating completed work. Do not imply
local changes are already on GitHub.
```
