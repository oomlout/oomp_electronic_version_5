# Second-pass JLC integration worker

The canonical instructions are now [JLC_PART_INTEGRATION_AGENT.md](../JLC_PART_INTEGRATION_AGENT.md).
Read that entire guide and follow its numbered steps. This file remains a
compatibility entry point for older prompts; do not maintain a second workflow here.

Select one item with `python -m kicad_agents.jlc_house_parts_agent next --stage full`
using the repository's Python environment. Work slowly, verify each fact, and
record this stage's completion or precise deferral before selecting another item.

See [WORKER.md](WORKER.md) for the two-stage dispatch prompts.
