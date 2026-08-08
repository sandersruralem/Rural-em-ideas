# Rural EM Ideas

A working system for inventing, testing, and building tools and workflows for **rural and county emergency management offices** — using Cursor (desktop) for framing and Cloud Agents for parallel spikes and prototypes.

## Why this exists

Rural and county EM offices are typically small teams covering large geography with limited budget, intermittent connectivity, multi-agency coordination, and paper/legacy-heavy processes. Most “smart city” or enterprise EM software assumes staffing, bandwidth, and IT support that these offices do not have.

This repo is an **idea → spike → prototype factory** tuned to those constraints.

## Operating loop (30-second version)

```
Capture friction → Frame a spike → Launch 2–4 Cloud Agents in parallel
→ Review demos/PRs → Pick one → Polish with follow-ups → Merge or archive
```

Full plan: [`docs/PLAN.md`](docs/PLAN.md)

## Repo layout

| Path | Purpose |
|------|---------|
| `ideas/inbox/` | Raw problem statements and opportunity notes |
| `ideas/spikes/` | Scoped spike briefs ready for a Cloud Agent |
| `ideas/prototypes/` | Winning spikes promoted to build briefs |
| `docs/PLAN.md` | How to use Cursor + Cloud Agents for this work |
| `docs/prompts/` | Copy-paste prompt templates |
| `AGENTS.md` | Standing instructions for Cloud Agents |

## Quick start

1. Drop a problem into `ideas/inbox/` (use the template).
2. In desktop Cursor, turn it into a spike brief under `ideas/spikes/`.
3. Launch Cloud Agents from [cursor.com/agents](https://cursor.com/agents) with a prompt from `docs/prompts/`.
4. Review artifacts (screenshots, recordings, PRs); promote winners to `ideas/prototypes/`.

## Design constraints (non-negotiable)

Every idea and prototype should respect:

- **Small staff** — often 1–3 people; tools must reduce work, not create dashboards to babysit
- **Intermittent connectivity** — offline-first or graceful degradation where possible
- **Low IT overhead** — no complex infra; prefer single-deploy or spreadsheet-adjacent tools
- **Multi-agency reality** — fire, EMS, law, public works, elected officials, mutual aid
- **Trust & plain language** — field-usable under stress; avoid jargon and alert fatigue
- **Budget realism** — free/cheap stack, open source preferred (this repo is GPL-3.0)

## Status

Bootstrap phase: plan + templates only. First spikes come next.
