# Data Classification for AI Use

**Version:** 0.1 (draft)
**Owner:** Emergency Manager
**Review cycle:** Annually, or after any change in approved tools, county policy, or state/federal guidance

This document defines what information may and may not be entered into an AI tool. It applies to
every prompt, attachment, screenshot, pasted note, and voice transcript submitted to any AI service,
including requests that only ask the tool to summarize, translate, redact, or reformat.

**Default posture:** Until County IT or legal counsel confirms otherwise in writing,
**all approved tools are treated as Green-only.**

---

## 1. Why classification comes first

A paid subscription is not an authorization. Whether information may be submitted depends on the
contract, retention terms, training terms, access controls, and applicable law that govern the
specific account being used — not on the price of the plan.

Three additional realities apply to a county office:

- **Public records.** County records, including some AI prompts and outputs, may be subject to state
  public-records law. Assume anything typed into a tool could later be disclosed.
- **Irreversibility.** Once submitted, information cannot be recalled. There is no undo.
- **Aggregation.** Individually harmless facts can become sensitive in combination (for example, a
  shelter location plus an occupant roster plus a medical need).

---

## 2. The three levels

### Green — permitted

Information that is already public, or that was created to be public, and that identifies no
individual.

Examples:

- Published National Weather Service forecasts, watches, warnings, and products
- Adopted plans, ordinances, and other published county documents
- Public road status, public facility lists, published shelter locations
- Census, demographic, and published hazard-mitigation data
- Blank ICS forms, generic checklists, and template language
- Press releases and social posts that have already been issued
- Training and exercise material using clearly fictional people and organizations

Green data may be used in approved tools, subject to human review of the output.

### Yellow — restricted

Non-public working information whose disclosure would cause limited harm, confusion, or
embarrassment, but that does not identify individuals in a protected way and does not compromise
security.

Examples:

- Draft plans, draft press releases, and unreleased messaging
- Internal staffing rosters, shift schedules, and availability
- Internal (non-published) agency contact lists
- Preliminary or unverified damage estimates
- Vendor quotes, cost estimates, and in-progress grant narratives
- Unconfirmed incident reports and early situational notes
- Detailed resource and equipment inventories

Yellow data may be submitted **only** when both conditions are met:

1. County IT or legal counsel has confirmed in writing that the specific tool **and the specific
   account** provide acceptable retention, training, and access protections; and
2. The Emergency Manager has approved that category of use.

If either condition is unmet, anonymize the material into Green form or treat it as Red.

### Red — prohibited

Information whose disclosure could harm a person, compromise operations or infrastructure, violate
law or contract, or expose county systems. Red data is never submitted to any AI tool under this
playbook.

Examples:

- Names or identifying details of victims, patients, minors, evacuees, or shelter occupants
- Medical, disability, medication, behavioral-health, or access-and-functional-needs information
- Social Security numbers, dates of birth, driver's license numbers, financial or banking data
- Raw CAD, 911, EMS, dispatch, or law-enforcement records
- Criminal justice information (CJIS) or active investigative material
- Passwords, API keys, radio programming or encryption keys, and system credentials
- Security plans, vulnerability assessments, camera placements, alarm or access codes
- Locations of protected persons, evidence, or sensitive caches
- Unpublished critical-infrastructure vulnerabilities
- School security, evacuation, reunification, or tactical response detail
- Anything restricted by HIPAA, CJIS, FERPA, state statute, contract, or county policy

Red data must not be entered even to ask the tool to remove, mask, or summarize it. Redaction is
performed by a person, before the tool sees the material.

---

## 3. Decision rule

Before submitting anything, answer these five questions:

1. Is this already public?
2. Does it identify, or allow identification of, a specific person?
3. Could disclosure compromise responders, facilities, systems, or an investigation?
4. Is it protected by law, contract, or county policy?
5. Has the county approved this tool and this account for this class of data?

If any answer creates doubt, do not submit it. Ask the Emergency Manager.

**When in doubt, it is Red.**

---

## 4. Sanitizing to Green

Most Yellow or Red material can be rewritten by a person into Green form that still produces a
useful draft. Replace specifics with placeholders and restore them after review.

```text
[RESIDENT A]
[PATIENT 1]
[SHELTER 1]
[CRITICAL FACILITY]
[VENDOR A]
[UNCONFIRMED DAMAGE COUNT]
[ROAD SEGMENT 1]
```

Example — not acceptable:

> Draft a welfare-check list. Jane Doe, 412 Oak St, on home oxygen, daughter's cell 555-0134.

Example — acceptable:

> Draft a welfare-check call script for residents who depend on electrically powered medical
> equipment during an extended outage. Leave blanks for name, address, and callback number.

The script comes back as a Green product. Staff fill in the protected details offline.

---

## 5. Incident handling

If Red data is submitted to an AI tool, whether intentionally or not:

1. Stop using that conversation. Do not continue the thread.
2. Notify the Emergency Manager the same day.
3. Notify County IT, and legal counsel if the material is regulated (HIPAA, CJIS, FERPA).
4. Delete the conversation and account history if the tool allows it, and record that you did.
5. Record the event in `docs/governance/change-log.md` with date, tool, data class, and action taken.
6. The Emergency Manager determines whether notification obligations apply.

The purpose of this process is correction, not punishment. Reporting promptly is expected.

---

## 6. Quick reference

| Question | Green | Yellow | Red |
| --- | --- | --- | --- |
| Already public? | Yes | No | No |
| Identifies a person in a protected way? | No | No | Yes |
| Could compromise security or an investigation? | No | No | Yes |
| May be submitted to an approved tool? | Yes | Only with written county authorization | Never |
| Requires Emergency Manager review of output? | Yes | Yes | N/A |
