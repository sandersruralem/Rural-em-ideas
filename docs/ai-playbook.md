# County Emergency Management AI Playbook

**Version:** 0.1 (draft — pilot)
**Owner:** Emergency Manager
**Reviewer of record:** Emergency Manager or equivalent
**Approved tools:** Microsoft Copilot, Claude Pro, Gemini Pro
**Language:** English only
**Status:** Pilot. Not yet adopted as county policy.

---

## 1. Purpose

This office runs on a small staff. The work does not shrink to match. This playbook describes how to
use AI tools to produce more drafts, briefs, plans, and messages in the time available, without
lowering accuracy or putting protected information at risk.

AI is treated here as a fast, tireless, unreliable assistant. It produces drafts. A person is
accountable for everything that leaves this office.

## 2. Principles

1. **Draft only.** No AI output is used, sent, posted, or filed until a person reviews it.
2. **A person is accountable.** The Emergency Manager or equivalent is the reviewer of record for
   every operational and public-facing product.
3. **Official systems remain the source of truth.** The National Weather Service, the state
   emergency management system, dispatch, and the county website are authoritative. AI summarizes
   and packages; it does not decide and it does not originate facts.
4. **Green data by default.** See [Data Classification](data-classification.md). When in doubt, it
   is Red and it does not go in.
5. **Unknown beats invented.** A draft that says UNKNOWN is useful. A draft that invents a road
   closure is dangerous.
6. **Reusable beats clever.** A prompt that works the same way every Tuesday is worth more than a
   brilliant one-off nobody can reproduce.
7. **Small and honest.** This playbook stays short enough to actually be read.

## 3. Scope

| In scope | Out of scope for v1 |
| --- | --- |
| Routine drafting, summarizing, and formatting | Real-time incident command decisions |
| Briefings, public messaging, exercises, after-action reports | Anything replacing NWS, dispatch, or the state system |
| Grant narratives, SOPs, job aids, training material | Life-safety determinations |
| Green data, with Yellow only if authorized in writing | Any Red data, ever |
| English-language products | Translation and multilingual output (deferred to v1.1) |

Deferring translation is a deliberate choice. Emergency translation carries real liability, and this
office cannot yet verify translated output. Until a qualified reviewer is identified, translation
requests go to a human translator.

## 4. Roles

| Role | Who | Responsibility |
| --- | --- | --- |
| Reviewer of record | Emergency Manager or equivalent | Approves every operational and public-facing output before release |
| Operator | Any trained staff member or volunteer | Runs prompts, supplies inputs, does the first cleanup pass |
| Playbook owner | Emergency Manager | Maintains this repository, versions, and the change log |
| Data authority | County IT / legal counsel | Determines whether Yellow data may be submitted to a given tool |
| Subject-matter reviewer | PIO, road department, fire, EMS as applicable | Verifies domain facts before the Emergency Manager signs off |

In a one-person office, the Emergency Manager holds every role. The review step still happens — it
is performed deliberately, against the checklist, on a separate pass from the drafting.

## 5. Approved tools

Microsoft Copilot, Claude Pro, and Gemini Pro. All three are Green-only until County IT confirms
otherwise in writing. Tool-by-tool strengths, cautions, and the local authorization table are in
[Approved Tools](approved-tools.md).

No other AI service is used for county work, including free tools, browser extensions, and
AI features embedded in unrelated software.

## 6. The core workflow

Every use of AI in this office follows the same five steps.

```text
1. GATHER    Collect Green inputs from authoritative sources.
             Sanitize anything Yellow or Red into placeholders first.

2. PROMPT    Use a prompt from the library by ID and version.
             Attach the county fact pack. Do not improvise if a prompt exists.

3. DRAFT     Generate. Read it once for obvious nonsense before spending real time on it.

4. REVIEW    Apply the Review Checklist. The Emergency Manager signs off on
             anything operational or public-facing. Verify every fact against source.

5. USE/FILE  Release the product through official channels.
             Log the run in the run log. File the final product where county records live.
```

The step people skip is 4. That is the step that makes the rest defensible.

## 7. Job playbooks

Three workflows are in the pilot. Each has a one-page job playbook and a tested prompt.

| Job | Playbook | Prompt |
| --- | --- | --- |
| Morning hazard digest and action checklist | [morning-brief.md](job-playbooks/morning-brief.md) | `brief.morning` |
| Public message pack from approved facts | [public-message-pack.md](job-playbooks/public-message-pack.md) | `msg.pack` |
| Tabletop exercise design and after-action | [tabletop-exercise.md](job-playbooks/tabletop-exercise.md) | `ex.tabletop` |

Additional jobs — grant narratives, SOP conversion, ICS timelines, mutual aid packages,
micro-training — are queued in the [roadmap](roadmap.md) and are not authorized until their prompts
pass the golden-set tests.

## 8. Data handling

The short version:

- **Green** — public or built to be public. Permitted.
- **Yellow** — internal working material. Only with written county authorization for that specific
  tool and account.
- **Red** — persons, protected records, security details, credentials. Never, including for
  redaction or summarizing.

Full definitions, the five-question decision rule, sanitizing patterns, and the incident procedure
are in [Data Classification](data-classification.md). Read that document before first use.

## 9. Review requirements

| Product type | Minimum review |
| --- | --- |
| Public message, press release, social post, alert text | Emergency Manager, plus PIO if the role exists |
| Operational brief, checklist, ICS content | Emergency Manager |
| Exercise material and after-action reports | Emergency Manager, plus exercise lead |
| Grant narrative | Emergency Manager, plus whoever owns the numbers |
| Internal notes and personal scratch work | Operator self-review |

The [Review Checklist](review-checklist.md) is the standard. Attach or reference it when signing off
on a public-facing product.

## 10. Known failure modes

These are the failures this office should expect, watch for, and catch in review.

| Failure | What it looks like here | Countermeasure |
| --- | --- | --- |
| Invented facts | A road closure, gauge reading, or shelter opening that nobody reported | Verify every specific against source; prompts require UNKNOWN |
| Stale knowledge | Old contacts, superseded guidance, renamed agencies | Supply current facts as input; never rely on the model's memory |
| Confident tone on thin evidence | Smooth prose that hides how little is actually known | Require a confirmed-versus-uncertain split in output |
| Local detail wrong | Wrong river, wrong route number, neighboring county's town | County fact pack attached to every run |
| Averaging to generic | Advice that would fit any county in the country | Reject drafts with no county-specific action |
| Quiet drift | Someone edits a prompt and results change without anyone noticing | Version prompts; re-run golden tests before replacing a version |
| Over-trust | Output released because it reads well | Mandatory checklist; reviewer signs |
| Data leak | Protected detail pasted in to "save time" | Green-only default; sanitize before prompting |

## 11. Records

- Final products are filed wherever county records normally live. This repository is not the county
  record system.
- Each run is logged in [`tests/run-log.md`](../tests/run-log.md): date, prompt ID and version, tool,
  minutes spent editing, errors caught, and whether the prompt should be kept or changed.
- Prompts, fixtures, and scorecards live in this repository under version control.
- Assume prompts and outputs may be subject to public-records requests. Write accordingly.

## 12. Pilot and success criteria

The pilot runs for four weeks using only the three job playbooks above.

The pilot succeeds if:

- A staff member who did not write the playbook can run the morning brief workflow unaided
- Zero Red-data incidents occur
- At least two workflows show a clear time saving with an acceptable editing burden
- No inaccurate AI-derived statement reaches the public
- The Emergency Manager is willing to keep using the outputs after review

If those hold, this becomes v1.0 and the roadmap's next jobs are built. If they do not, the failing
workflow is fixed or dropped.

## 13. Maintenance

| Item | Cadence | Owner |
| --- | --- | --- |
| County fact pack | Quarterly, and after any plan change | Emergency Manager |
| Approved tools and authorization table | Quarterly | Emergency Manager with County IT |
| Prompt library golden tests | Before any version change; annually otherwise | Playbook owner |
| This playbook | Annually, and after any significant incident | Emergency Manager |
| Change log | Every change | Whoever made the change |

## 14. Change log

Maintained in [`docs/governance/change-log.md`](governance/change-log.md).

---

## Appendix A — One-page quick start

1. Confirm your input is **Green**. If unsure, stop and ask.
2. Open the [prompt index](../prompts/README.md) and pick the prompt by ID.
3. Paste the [county fact pack](../context/county-fact-pack.md) plus your inputs.
4. Generate the draft.
5. Work the [Review Checklist](review-checklist.md). Verify every specific fact.
6. Get the Emergency Manager's sign-off if it is operational or public-facing.
7. Release through official channels and log the run.

## Appendix B — What not to ask AI to do

- Decide whether to activate, evacuate, or shelter
- Confirm whether a road, bridge, or facility is actually open or closed
- Generate casualty, damage, or cost figures
- Interpret a legal obligation without counsel
- Handle protected personal, medical, or law-enforcement information
- Serve as the official record of an incident
- Produce a final public message without human review
