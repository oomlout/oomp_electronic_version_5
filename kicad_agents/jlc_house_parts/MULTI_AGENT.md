# Multi-agent fan-out for the intake queue

One worker at a time is still the default (`next` → research →
complete/defer). This document adds a second mode: N workers process the
queue in parallel, one part per worker at a time, without conflicts.

## Why plain `next` is not enough

`next` does not claim or lock a task; two workers handed the same code would
duplicate work or overwrite each other. The CLI now provides local
coordination primitives (files under `kicad_agents/jlc_house_parts/`):

| Primitive | File | Guarantee |
| --- | --- | --- |
| Claim | `claims/<stage>_<code>.json` | Exclusive create; exactly one worker wins a code |
| Family lock | `locks/family_<family>.lock` | Serialises populate-file edits within one OOMP family |
| Registry lock | `locks/reviewed_choices.lock` | Taken automatically by `promote-intake` |
| Staged capture | `browser_staging/<code>.json` | Live-page facts recorded once by the browser reader; workers never need the browser |

Claims are cleared automatically by `intake-complete` and `defer`. A worker
that dies mid-part leaves its claim behind; clear abandoned state with:

```powershell
python -m kicad_agents.jlc_house_parts_agent claims          # list active claims
python -m kicad_agents.jlc_house_parts_agent release --code C123
python -m kicad_agents.jlc_house_parts_agent release --stale --hours 6
```

## The browser reader handoff

The ZCode in-app browser is **main-agent only** — spawned subagents get
"Browser is not available in subagent". The fan-out therefore splits each
part into two roles:

1. **Browser reader** (main agent, or a human with
   [browser_capture_bridge.py](browser_capture_bridge.py)): reads live JLC
   product pages and records every visible fact into
   `browser_staging/C<number>.json` via `stage-capture`. It decides nothing.
   See [BROWSER_READER_AGENT.md](BROWSER_READER_AGENT.md).
2. **Pool workers** (subagents, no browser needed): claim only codes that
   already have a fresh staged capture with
   `next --stage intake --claim --staged-only --worker W1`, then either
   `defer --stage intake --code <C> --from-capture` (non-house class) or the
   full intake flow (house class). Everything else — populate edits under
   the family lock, scaffolding, gates, generation — is browser-free.

## Plan a pool

```powershell
python -m kicad_agents.jlc_house_parts_agent plan --workers 10
```

prints, per worker, a balanced category slice and the exact claim command to
paste into that worker's prompt. Oversized categories are shared between
workers on purpose: claims arbitrate individual codes, and the family lock
serialises the rare populate-file edit. Change N any time; claims are
per-code, so workers can change slices between batches. A worker with no
categories may claim anything pending and acts as a free helper at the tail.

## Worker loop (no browser required)

1. Claim exactly one staged item:

   ```powershell
   python -m kicad_agents.jlc_house_parts_agent next --stage intake --claim --staged-only --worker W1
   ```

   `task: null` means no fresh staged capture is waiting; stop and ask the
   reader for another batch. Never work a code you did not claim.
2. Read the staged capture in `browser_staging/<code>.json`.
3. `tier_label` is Extended (or otherwise not a house class): defer with the
   staged facts in one command:

   ```powershell
   python -m kicad_agents.jlc_house_parts_agent defer --stage intake --code <C> --from-capture
   ```

   It refuses to defer a capture that shows a house class.
4. `tier_label` is Basic/Preferred/Promotional and matches the queue class:
   full intake per `../JLC_PART_INTAKE_AGENT.md`. Build the observation from
   the staged capture (`intake_from_capture.py`), hold the family lock around
   any populate edit:

   ```powershell
   python -m kicad_agents.jlc_house_parts_agent lock --family diode --worker W1
   # edit ONLY working_oomp_populate_diode.py / _extra.py for this part
   # ... scaffold-intake, promote-intake, intake-check, intake-complete ...
   python -m kicad_agents.jlc_house_parts_agent unlock --family diode --worker W1
   ```

5. Finish with `intake-complete` or `defer`; both release the claim. Report
   the code, the outcome and one line of evidence to the batch log.

## Conflict rules

- Only the claiming worker writes `progress/<code>.json`, the component
  record, the page capture or `parts_source/<part_id>/` for its code.
- Edit only populate family files for the part you claimed, and only while
  holding that family's lock. Never bulk-rewrite populate files.
- `reviewed_choices.json` is protected by the promote-intake lock; do not
  edit it by hand while a pool is running.
- Never weaken a gate to pass; defer instead. Deferral is a first-class
  result and is reviewed after the sweep.

## Constraints observed in practice (2026-09-26)

- The ZCode in-app browser is main-agent only; the reader role must run
  there. A worker that cannot verify the live page must NOT defer and must
  NOT guess: `release --code <C>` and report blocked.
- A user plan runs roughly three agents concurrently; larger pools are
  rejected with "user concurrency limit exceeded". Launch pool members in
  groups of three or fewer, and let each worker loop over several staged
  parts instead of spawning one agent per part.

## Solo mode

`next` without `--claim` keeps its original behaviour and additionally skips
codes already claimed by a pool. Working solo while a pool runs: use
`--claim --worker solo` so the pool skips your item too.
