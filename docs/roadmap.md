# Build Roadmap

**Version:** 0.1 (draft)
**Owner:** Emergency Manager

How this repository gets from a draft to something the office actually relies on. Phases are
sequenced by dependency, not by calendar. Each phase has an exit condition; do not start the next
phase until the current one meets it.

The governing principle: **three tested prompts beat twelve untested ones.** The failure mode for a
project like this is a large library nobody trusts, built faster than it could be verified.

---

## Phase 0 — Scaffolding

**Status: complete.** Policy documents, three v1 prompts, fixtures, and the testing protocol exist
in this repository.

Exit condition met when the structure is in place and reviewable.

---

## Phase 1 — Local grounding

Nothing here is usable until the county fact pack is real.

- [ ] Fill in [`context/county-fact-pack.md`](../context/county-fact-pack.md) completely
- [ ] Verify every fact in it against a current source
- [ ] Confirm section 11, standing constraints, is honest rather than aspirational
- [ ] Confirm no line in it would be uncomfortable in a public-records release
- [ ] Emergency Manager approves it

**Exit condition:** a complete, verified, Green-only fact pack.

The temptation is to skip this and test with the fictional Bramble County pack. Do not. A prompt
tuned against a fictional county tells you nothing about how it behaves on yours.

---

## Phase 2 — Tool authorization

Runs in parallel with Phase 1. Does not block Green-only testing.

- [ ] Determine whether the office uses Microsoft Copilot with a personal account or a work or
      school account
- [ ] County IT reviews retention, training, and access terms for all three tools
- [ ] Complete the authorization table in [`docs/approved-tools.md`](approved-tools.md)
- [ ] Confirm multifactor authentication is enabled on all three
- [ ] Confirm county accounts are in use rather than personal ones
- [ ] Decide whether Yellow data is authorized anywhere, and record the decision

**Exit condition:** the authorization table is filled in, with a name and a date on each row.

Until then, everything stays Green-only. That is a workable constraint, not a blocker.

---

## Phase 3 — Golden-set testing

Requires Phase 1.

- [ ] Run all five `brief.morning` fixtures on Claude Pro
- [ ] Run all four `msg.pack` fixtures on Claude Pro and on Gemini Pro
- [ ] Run all three `ex.tabletop` fixtures on Claude Pro
- [ ] Run at least the typical and negative fixtures of each prompt on Microsoft Copilot, for
      comparison
- [ ] File a completed scorecard for every run
- [ ] Fill in the tool comparison table in [`tests/README.md`](../tests/README.md)
- [ ] Revise and re-version any prompt that fails, then re-run the full set

**Exit condition:** every fixture passes on at least one approved tool, and the prompt index status
moves from Draft to Tested.

Pay closest attention to the negative fixtures. A prompt that handles a routine morning well but
mishandles protected data is not a partial success.

---

## Phase 4 — Pilot

Requires Phase 3.

- [ ] Run `brief.morning` every working morning for two weeks
- [ ] Use `msg.pack` for the next three public messages
- [ ] Use `ex.tabletop` for one full exercise cycle, both design and after-action
- [ ] Log every run in [`tests/run-log.md`](../tests/run-log.md)
- [ ] Emergency Manager reviews the log weekly
- [ ] Have someone who did not write the playbook run the morning brief unaided, and note where they
      got stuck

**Exit condition:** the pilot success criteria in [`docs/ai-playbook.md`](ai-playbook.md), section
12, are met.

---

## Phase 5 — Version 1.0

Requires Phase 4.

- [ ] Update the playbook from what the pilot actually taught, not from what was assumed
- [ ] Promote passing prompts from Tested to Approved
- [ ] Retire or rewrite anything that failed
- [ ] Fill in the county fact pack gaps the pilot exposed
- [ ] Brief county leadership on what AI is used for here and what it is not used for
- [ ] Tag v1.0 and record it in the change log

**Exit condition:** v1.0 adopted, with leadership aware of the scope and the limits.

---

## Phase 6 — Expansion

Requires Phase 5. Build these one at a time, each earning its place through the full golden-set
process. Do not batch.

| Order | Prompt | Why this order |
| --- | --- | --- |
| 1 | `grant.narrative` | Highest time saving per use in a small office |
| 2 | `sop.jobaid` | Converts tribal knowledge into something that survives staff turnover |
| 3 | `ics.timeline` | Valuable during activations, but needs anonymized note samples first |
| 4 | `ex.aar` | Split out from `ex.tabletop` once its usage patterns are understood |
| 5 | `ops.mutualaid` | Requires a review of current agreements first |
| 6 | `msg.rumor` | Higher risk; needs stricter review rules than `msg.pack` |
| 7 | `train.micro` | Useful, not urgent |

Each addition repeats the same cycle: write acceptance criteria, write the prompt, build three to
five fixtures including a negative one, test, pilot, approve.

---

## Deferred, with reasons

| Item | Why it waits |
| --- | --- |
| Translation and multilingual output | Cannot verify translated output today. A qualified reviewer must be identified first, and emergency translation carries real liability. |
| Custom tools built with coding assistants | The text library must prove itself before the office takes on software it has to maintain. There is no in-house IT support to inherit it. |
| Automated evaluation of prompt outputs | Manual scoring is right at this volume. Revisit if the library exceeds roughly twenty prompts. |
| Any use touching Red data | Not deferred. Excluded. |
| AI in real-time incident decision-making | Excluded by design, not by schedule. |

---

## How to tell this is working

Signals that the effort is paying off:

- Median editing time in the run log falls week over week
- The Emergency Manager stops rewriting the morning brief from scratch
- A second person can run the workflows without help
- Products get made that previously did not get made at all, because there was no time

Signals that it is not:

- The run log is empty, which means nobody is actually using it
- The same defect keeps appearing and nobody has opened a new prompt version
- Someone is improvising prompts instead of using the library
- Review has become a formality
