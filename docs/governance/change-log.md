# Change Log

Every change to the playbook, prompt library, fact pack, or testing protocol is recorded here.

## How to record a change

Add a row. Keep it short but specific enough that someone can tell what changed and why without
reading the diff.

| Date | Item | Version | Change | Reason | By |
| --- | --- | --- | --- | --- | --- |
| 2026-08-08 | Repository | 0.1 | Initial scaffolding: playbook, data classification, approved tools, review checklist, three job playbooks, three v1 prompts, testing protocol, twelve fixtures, county fact pack template, roadmap | Establish a reviewable starting point for the pilot | Playbook owner |
| 2026-08-08 | Approved tools | 0.2 | Recorded Microsoft Copilot as the county enterprise Entra ID account. Designated it the Yellow-capable tool subject to a confirmation checklist, added enterprise-specific cautions covering inherited permissions, retention and discovery, web grounding, meeting summarization, and agents. Added the data routing table. Kept Red prohibited on all tools including Copilot | Account type confirmed by the Emergency Manager | Playbook owner |
| 2026-08-08 | Data classification | 0.2 | Yellow may go to Copilot only, once its checklist is signed, and never to Claude Pro or Gemini Pro. Noted that Copilot deletion is governed by county retention policy rather than the individual user | Follows from the enterprise account determination | Playbook owner |
| 2026-08-08 | Playbook | 0.2 | Replaced the Green-only default with per-tool data routing. Added Copilot oversharing and wrong-tool-for-the-data failure modes | Follows from the enterprise account determination | Playbook owner |
| 2026-08-08 | Prompt library | — | Metadata only: recorded tool routing on all three v1 prompts and the template. No system block, user block, or output schema changed, so no version bumps | Keep routing visible at the point of use | Playbook owner |
| 2026-08-08 | Roadmap and testing protocol | — | Phase 2 reduced from procurement review to confirmation, with the permissions review called out. Copilot promoted to a full golden set rather than a spot check | Copilot will carry the office's Yellow work and needs equal evidence | Playbook owner |
| 2026-08-08 | County fact pack | 0.1 draft | Added `context/sanders-county-fact-pack.md`: research-filled Sanders County, Montana copy of the template with Green public sources and a full sources list. Template left unchanged pending EM verification | Start Phase 1 local-context work for Sanders County | Cloud agent |
| 2026-08-08 | County fact pack office edition | 0.1 draft | Added a Word-oriented Markdown edition, reproducible DOCX generator, styled office-review document, open-items checklist, document controls, and source appendix | Provide a clean review copy without replacing the research / AI-paste draft | Cloud agent |

---

## What must be recorded

- Any change to the playbook, data classification, or review checklist
- Any new prompt, prompt version, or status promotion
- Any material change to the county fact pack
- Any tool added, removed, or reauthorized
- Any change to the testing protocol or to a fixture
- Every data-handling incident, per
  [Data Classification](../data-classification.md), section 5

## Status promotions

Record each promotion so the history of what was trusted, and when, is preserved.

| Date | Prompt | From | To | Evidence | Approved by |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Data-handling incidents

Recorded here in full, including near misses. A near miss recorded is a control that worked.

| Date | Tool | Data class involved | What happened | Action taken | Reported to |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
