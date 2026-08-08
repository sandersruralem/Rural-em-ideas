# Prompt Library

Reusable, versioned prompts for county emergency management work. Each prompt does one job, states
its required inputs, and produces a predictable structure that a person can review quickly.

**Approved tools:** Microsoft Copilot, Claude Pro, Gemini Pro
**Language:** English only
**Data level:** Green only — see [Data Classification](../docs/data-classification.md)

---

## How to use a prompt

1. Confirm your inputs are Green.
2. Open the prompt file and copy the **System block** into the tool's system, instruction, or first
   message field.
3. Copy the **User block** and fill in every field. Do not leave a field implied.
4. Paste the [county fact pack](../context/county-fact-pack.md) where the prompt asks for it.
5. Generate, then run the [Review Checklist](../docs/review-checklist.md).
6. Log the run in [`tests/run-log.md`](../tests/run-log.md).

Do not improvise a prompt when one exists. If the existing prompt is wrong, revise it as a new
version so the fix survives.

---

## Status of the library

| ID | Job | Version | Status | Recommended tool |
| --- | --- | --- | --- | --- |
| [`brief.morning`](brief.morning/v1.md) | Morning hazard digest and action checklist | v1 | Draft — untested | Claude Pro |
| [`msg.pack`](msg.pack/v1.md) | Public message pack across channels | v1 | Draft — untested | Claude Pro / Gemini Pro |
| [`ex.tabletop`](ex.tabletop/v1.md) | Tabletop scenario, injects, and after-action | v1 | Draft — untested | Claude Pro |

**Status meanings**

| Status | Meaning |
| --- | --- |
| Draft — untested | Written but not yet run against the golden set. Not authorized for county products. |
| Tested | Passed the golden set on at least one approved tool. Usable in the pilot. |
| Approved | Passed the golden set and survived live pilot use. Authorized for routine use. |
| Deprecated | Superseded. Retained for reference for 90 days. |

All three prompts are **Draft — untested** until the golden-set runs in
[`tests/README.md`](../tests/README.md) are completed and scored.

---

## Backlog

Not authorized until written and tested. Ordered by expected value to a small office.

| ID | Job | Why it waits |
| --- | --- | --- |
| `grant.narrative` | Grant narrative from bullet notes | High value, but needs the first three proven first |
| `sop.jobaid` | Turn an SOP into a laminate-ready job aid | Needs example SOPs gathered |
| `ics.timeline` | Messy notes into an ICS-style chronology | Needs real anonymized note samples |
| `ex.aar` | Standalone after-action report | Partially covered inside `ex.tabletop` v1 |
| `ops.mutualaid` | Structured mutual aid request package | Needs current agreements reviewed |
| `msg.rumor` | Rumor-control statement | Higher risk; needs stricter review rules |
| `train.micro` | Ten-minute role-specific training outline | Lower urgency |

Deliberately excluded from the roadmap: anything that decides, anything touching protected data, and
translation until a qualified reviewer exists.

---

## Prompt authoring standard

Every prompt file uses [`_template.md`](_template.md) and contains these sections in order.

1. **Header** — ID, version, status, job, recommended tool, data level
2. **When to use / when not to use**
3. **Required inputs** and **optional inputs**
4. **System block** — role, constraints, refusal rules
5. **User block** — fill-in fields
6. **Expected output schema** — exact headings the output must contain
7. **Acceptance criteria** — what "good enough" means, written before the prompt is tested
8. **Review checklist** — job-specific checks beyond the universal ones
9. **Known failure modes**
10. **Change history**

### Authoring rules

- **One prompt, one job.** A prompt that does three things fails in three ways.
- **Structure in the schema, not the instructions.** Say what sections the output needs; do not
  narrate how to write them.
- **Every prompt refuses to invent.** Required line: unknown information is marked UNKNOWN and
  never filled in.
- **Every prompt is Green-only** and says so in its system block.
- **Every prompt reports what it needed and did not get.** The gap list is often the most valuable
  part of the output.
- **Short beats long.** Long prompts drift. Cut anything the output schema already implies.

---

## Versioning

- Versions are whole numbers: `v1`, `v2`. Files live at `prompts/<id>/v<n>.md`.
- Never edit a tested or approved version in place. Copy it forward and bump.
- Any change to the system block, user block, or output schema requires a new version.
- Fixing a typo that cannot change output is the only in-place edit allowed, and it is noted in the
  prompt's change history.
- A new version must pass the same golden set before it replaces its predecessor in the index above.
- Deprecated versions stay in the repository for 90 days, marked Deprecated at the top of the file.

## Naming

`area.job`, lowercase, dot-separated.

| Area | Meaning |
| --- | --- |
| `brief` | Situational awareness products |
| `msg` | Public information and warning |
| `ex` | Exercises and after-action |
| `ops` | Operations and coordination |
| `grant` | Grants and administration |
| `sop` | Procedures and job aids |
| `ics` | ICS documentation support |
| `train` | Training material |
