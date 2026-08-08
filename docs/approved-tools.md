# Approved Tools

**Version:** 0.1 (draft)
**Owner:** Emergency Manager
**Review cycle:** Quarterly, or whenever a vendor changes its terms

Three tools are in scope for the pilot. No other AI service is approved for county work under this
playbook.

| Tool | Plan | Primary use in this office | Default data level |
| --- | --- | --- | --- |
| Microsoft Copilot | Paid | Drafting inside Microsoft 365 documents and email; summarizing meetings | Green |
| Claude Pro | Paid | Long-form drafting, plan and annex work, structured outputs, document analysis | Green |
| Gemini Pro | Paid | Research-style synthesis, multimodal review, Google-ecosystem drafting | Green |

**All three are Green-only until County IT confirms otherwise in writing.** See
[Data Classification](data-classification.md).

---

## 1. Why the default is Green-only

The protections a tool provides depend on the account it is used with, not on the brand name or the
subscription price. Consumer and enterprise versions of the same product can differ substantially in
how conversations are retained, whether they may be reviewed by humans, and whether they may be used
to improve models.

Vendor terms also change. A determination made once is not permanent, which is why this document is
reviewed quarterly and why the authorization column below must be filled in locally rather than
assumed.

---

## 2. Microsoft Copilot

**Important distinction.** "Copilot" refers to several different products:

- **Microsoft Copilot (consumer)** — signed in with a personal Microsoft account
- **Microsoft 365 Copilot** — licensed within a Microsoft 365 tenant, signed in with a work or
  school account (Microsoft Entra ID), with access to tenant data through Microsoft Graph
- **GitHub Copilot** — a code-completion product, out of scope for this playbook

This office uses **Microsoft Copilot**. Before any use beyond Green data, County IT must confirm
which of the first two the office is actually signed into, because the data handling differs. Work
or school account sign-in generally carries commercial data protection terms that a personal account
does not.

Strengths for this office:

- Works where documents already live, which reduces copy-paste and therefore reduces exposure risk
- Useful for meeting summaries, email drafting, and document rewriting
- Familiar interface for staff and elected officials already using Microsoft 365

Cautions:

- Copilot can reach into files the signed-in user can already access. Verify that the user's
  permissions do not expose Yellow or Red material into a summary.
- Confirm whether Copilot output is retained in the tenant and whether it is discoverable under
  records law.

Best fits: `sop.jobaid`, meeting minutes, email and memo drafting, document cleanup.

---

## 3. Claude Pro

Strengths for this office:

- Strong at long, structured documents such as annexes, after-action reports, and exercise packages
- Follows explicit output schemas reliably, which matters for the prompt library
- Handles large pasted source material in a single pass
- Comparatively conservative about stating uncertainty, which suits emergency management drafting

Cautions:

- A consumer subscription is not an enterprise agreement. Confirm current retention and
  model-training settings for the account in use, and confirm they can be administered centrally.
- Verify whether account history can be disabled or purged if Red data is ever submitted in error.

Best fits: `brief.morning`, `ex.tabletop`, `ex.aar`, `grant.narrative`, `ics.timeline`.

---

## 4. Gemini Pro

Strengths for this office:

- Good at synthesizing several public sources into one readable summary
- Handles images and documents, useful for reading scanned plans or photographed whiteboards
- Integrates with Google Workspace if the county uses it

Cautions:

- Consumer Google AI plans may retain conversations and, depending on activity settings, allow human
  review. Confirm the current settings for the account in use.
- Google's own guidance advises against entering confidential information into consumer products.
  Treat that as binding here.

Best fits: `msg.pack` variants, public-source research, reading scanned or photographed material.

---

## 5. Local authorization record

County IT or legal counsel completes this table. Until a row says "Yes," that tool remains
Green-only regardless of what its vendor documentation claims.

| Tool | Account type in use | Yellow data authorized? | Authorized by | Date | Notes |
| --- | --- | --- | --- | --- | --- |
| Microsoft Copilot | _(consumer / work-school)_ | No | | | Pending IT review |
| Claude Pro | _(individual / team)_ | No | | | Pending IT review |
| Gemini Pro | _(consumer / Workspace)_ | No | | | Pending IT review |

Questions to put to IT or the vendor:

1. Are prompts and outputs used to train or improve models? Can that be turned off, and by whom?
2. How long is conversation history retained, and who can delete it?
3. Can county administrators audit or export usage?
4. Does the agreement include commercial or enterprise data protection terms?
5. Is county data processed or stored outside the United States?
6. Does any existing county contract or cyber-insurance policy restrict this use?

---

## 6. Account and access rules

- Use county-provided accounts. Personal accounts are not used for county work.
- Do not share logins. Each user signs in individually so activity is attributable.
- Enable multifactor authentication on all three tools.
- When staff leave, County IT deactivates their access as part of offboarding.
- Do not install third-party browser extensions or plugins that relay county content to other
  services.

---

## 7. Requesting a new tool

1. Write down the job to be done and why the approved tools cannot do it.
2. Send the vendor's terms and privacy documentation to County IT for review.
3. Obtain the Emergency Manager's approval.
4. Test with Green data only, using the golden-set protocol in [`tests/README.md`](../tests/README.md).
5. Add the tool to this document with a version bump and a change-log entry.
