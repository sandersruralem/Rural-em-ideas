# Approved Tools

**Version:** 0.2 (draft)
**Owner:** Emergency Manager
**Review cycle:** Quarterly, or whenever a vendor changes its terms

Three tools are in scope. No other AI service is approved for county work under this playbook.

| Tool | Account | Primary use in this office | Highest data level |
| --- | --- | --- | --- |
| Microsoft Copilot | County enterprise (Microsoft Entra ID) | Drafting in Microsoft 365, meeting summaries, internal working documents | Yellow, once the confirmation checklist is complete |
| Claude Pro | Individual subscription | Long-form drafting, plans and annexes, structured outputs | Green |
| Gemini Pro | Individual subscription | Research-style synthesis, multimodal review | Green |

**Red data is never submitted to any of the three.** See
[Data Classification](data-classification.md).

---

## 1. Why the account matters more than the brand

The protections a tool provides come from the agreement behind the account, not from the product
name or the subscription price. The same vendor's consumer and enterprise offerings differ
substantially in retention, human review, model training, and administrative control.

That distinction is the reason this office can use one of these three tools differently from the
other two.

---

## 2. Microsoft Copilot — county enterprise account

This office uses Microsoft Copilot signed in with the **county's Microsoft Entra ID work account**,
inside the county's Microsoft 365 tenant. That places it under Microsoft's enterprise data
protection commitments, which generally means:

- Prompts and responses are not used to train Microsoft's foundation models
- Data stays within the tenant's service boundary and is covered by the county's Microsoft agreement
- Existing Microsoft 365 permissions and sensitivity labels are honored
- Interactions are subject to county administrative control, audit, and retention policy

This is a materially stronger position than a personal-account tool, and it is why Copilot is the
designated tool for Yellow data once the checklist in section 5 is complete.

It is not a reason to relax about Red data. See section 2.3.

### 2.1 Strengths for this office

- Works where county documents already live, which reduces copy-paste and therefore reduces the
  chance of pasting something that should not leave a controlled system
- Meeting summarization for EOC briefings, LEPC meetings, and commission sessions
- Familiar to staff and elected officials already using Microsoft 365
- Governed centrally: County IT can audit, retain, and restrict without depending on individual
  users configuring anything correctly

### 2.2 Cautions specific to an enterprise deployment

These are the risks that come with the enterprise version, not the ones it removes.

**Oversharing through inherited permissions.** Copilot can reach anything the signed-in user can
already open. In a county office one person often has broad access across shared drives — personnel
files, sheriff's office folders, health department material. Copilot will happily summarize a
poorly-permissioned folder into a tidy document that then gets emailed to a wider group. The tool is
not the failure; the permissions are, and Copilot makes existing permission problems visible fast.
A permissions review of the Emergency Manager's account is part of the checklist below.

**Records and discovery.** Copilot interactions are retained within the tenant and are subject to
county retention policy, audit, eDiscovery, and potentially state public-records law. Write every
prompt as though it may be read later by someone who was not in the room.

**Web grounding.** If Copilot is configured to search the web for grounding, some content leaves the
tenant boundary to service that search. Microsoft's position is that such queries are disassociated
from user and tenant identity, but a web-grounded prompt is more exposed than a tenant-only one.
County IT should record whether web grounding is enabled, and staff should assume it is until told
otherwise.

**Meeting summarization.** Copilot in Teams can transcribe and summarize. A meeting where someone
mentions a resident by name produces a record of that. Decide before the meeting whether it is
being summarized, and say so out loud to the participants.

**Agents and connectors.** Any agent, plugin, or connector added to the tenant may extend where data
travels. New ones are treated as new tools and go through section 7.

### 2.3 Red data is still prohibited

An enterprise tenant does not make protected categories permissible.

- **HIPAA** material requires that the county's business associate agreement actually cover the
  service in question, and that the use fits the agreement. Confirm with counsel, do not assume.
- **CJIS** material carries its own compliance requirements. Raw dispatch, records, and
  investigative content stays out.
- **Personal information about residents** stays out under this playbook regardless of tenant
  protections, because the operational benefit is small and the consequence of being wrong is not.

If the county later wants to reclassify a specific Red category for Copilot, that is a decision for
the Emergency Manager with legal counsel, documented in the change log, with the playbook version
bumped. It is not a judgment call made at a keyboard on a busy morning. Version 1.0 keeps Red
prohibited across all three tools.

---

## 3. Claude Pro

An individual subscription without a county enterprise agreement behind it. **Green only.**

Strengths for this office:

- Strong at long, structured documents such as annexes, exercise packages, and after-action reports
- Follows explicit output schemas reliably, which is what the prompt library depends on
- Handles large pasted source material in a single pass
- Comparatively willing to state uncertainty, which suits emergency management drafting

Cautions:

- A consumer subscription is not an enterprise agreement. Retention and training settings are
  configured per account and are not centrally administered by County IT.
- Verify that conversation history can be disabled or purged if something is submitted in error.
- Because it is Green-only, sanitize before prompting rather than after.

Best fits: `brief.morning`, `ex.tabletop`, `ex.aar`, `grant.narrative` — all working from public
inputs.

---

## 4. Gemini Pro

An individual subscription without a county enterprise agreement behind it. **Green only.**

Strengths for this office:

- Good at synthesizing several public sources into one readable summary
- Handles images and documents, useful for reading scanned plans or photographed whiteboards

Cautions:

- Consumer Google AI plans may retain conversations and, depending on activity settings, allow human
  review. Confirm the settings on the account in use.
- Google's own guidance advises against entering confidential information into its consumer
  products. Treat that as binding here.

Best fits: `msg.pack` drafting from approved public facts, public-source research, reading scanned
material.

---

## 5. Data routing

Which tool for which data. This is the table to remember.

| Data level | Microsoft Copilot (county enterprise) | Claude Pro | Gemini Pro |
| --- | --- | --- | --- |
| **Green** | Yes | Yes | Yes |
| **Yellow** | Yes, once section 6 is complete | No | No |
| **Red** | Never | Never | Never |

Practical effect: if the work involves draft plans, internal staffing, unconfirmed reports,
preliminary damage figures, vendor pricing, or anything else not yet public, it goes to Copilot.
Everything else can go wherever the prompt performs best.

If a job needs Claude's or Gemini's output quality on material that is Yellow, sanitize it into
Green form first. Do not route Yellow to a Green-only tool because the output reads better.

---

## 6. Copilot Yellow-data confirmation checklist

Copilot's enterprise footing makes this a confirmation rather than a full procurement review. It
still has to be completed and signed before Yellow data is submitted.

- [ ] License in use confirmed, and confirmed to carry enterprise data protection
- [ ] Confirmed that prompts and responses are not used to train foundation models under this
      license
- [ ] Retention policy for Copilot interactions set, documented, and known to staff
- [ ] Audit logging enabled and someone named as responsible for reviewing it
- [ ] Permissions review completed for the Emergency Manager's and deputy's accounts, with
      overbroad access to personnel, health, and law-enforcement material removed
- [ ] Sensitivity labeling in use for any Yellow material Copilot can reach, or a documented
      decision not to
- [ ] Web grounding configuration recorded, enabled or disabled
- [ ] Teams meeting summarization expectations recorded, including which meetings are never
      summarized
- [ ] Public-records implications reviewed with the county clerk or counsel
- [ ] Agents, plugins, and connectors inventoried

| Field | Value |
| --- | --- |
| Completed by (County IT) | |
| Date | |
| Approved by (Emergency Manager) | |
| Date | |
| Yellow data authorized for Copilot? | Not yet |

Until that last row says yes with a date beside it, **Copilot remains Green-only in practice**, the
same as the other two.

## 7. Claude Pro and Gemini Pro authorization record

Both remain Green-only. Raising either would require a county enterprise agreement, not a settings
change.

| Tool | Account type | Yellow authorized? | Reviewed by | Date | Notes |
| --- | --- | --- | --- | --- | --- |
| Claude Pro | Individual | No | | | Green-only; no county agreement in place |
| Gemini Pro | Individual | No | | | Green-only; no county agreement in place |

---

## 8. Account and access rules

- Use county-provided accounts. Personal accounts are not used for county work.
- Do not share logins. Each user signs in individually so activity is attributable.
- Enable multifactor authentication on all three tools.
- For Copilot, confirm you are signed in with the county work account, not a personal Microsoft
  account. The interface looks similar. The protections are not.
- When staff leave, County IT deactivates access as part of offboarding.
- Do not install browser extensions or plugins that relay county content to other services.

## 9. Requesting a new tool

1. Write down the job to be done and why the approved tools cannot do it.
2. Send the vendor's terms and privacy documentation to County IT for review.
3. Obtain the Emergency Manager's approval.
4. Test with Green data only, using the protocol in [`tests/README.md`](../tests/README.md).
5. Add the tool here with a version bump and a change-log entry.
