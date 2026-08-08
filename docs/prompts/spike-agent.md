# Prompt: Cloud Agent spike

Replace `{{SPIKE_PATH}}`. Launch from https://cursor.com/agents

For parallel variants, keep the same spike path but add an Approach override line.

---

## Goal

Implement the spike described in `{{SPIKE_PATH}}`.

## Context

Read and follow:
- `AGENTS.md`
- `README.md` (rural design constraints)
- The spike brief end-to-end

## Deliverables

1. Working demo that meets the spike success criteria
2. Branch + PR against `main`
3. Screenshots or short screen recording of the happy path
4. PR description including:
   - 60-second “how a rural EM would use this”
   - How to run (zero special IT preferred)
   - Limitations / offline assumptions
   - What you deliberately did *not* build

## Approach override (optional)

{{e.g. Prefer printable PDF rollup over interactive map}}

## Verification

Run every item in the spike brief’s verification checklist. If something fails, fix it or document the blocker — do not claim success.

## Constraints

- Synthetic demo data only (no real PII)
- Do not expand into a full EOC platform
- Prefer static/tiny local web app + CSV/print
- Plain language UI
- If blocked on policy/legal questions, note “needs EM director review” and continue with a safe advisory design

## Definition of done

Spike success criteria checkboxes are honestly met, or the PR clearly states which could not be met and why.
