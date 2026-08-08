# Review Checklist

**Version:** 0.1 (draft)
**Reviewer of record:** Emergency Manager or equivalent

No AI output is released, filed, or acted on until this checklist is worked. Review is a separate
pass from drafting. Do not review a draft in the same motion in which you generated it — the point
of the pass is to read it as a skeptic, not as its author.

---

## A. Universal checks

Applies to every AI-assisted product.

- [ ] **Every specific fact is verified against an authoritative source.** Gauge readings, road
      names and numbers, closures, shelter status, times, phone numbers, agency names, statutes.
      If it cannot be verified, it comes out or it is marked UNKNOWN.
- [ ] **Nothing was invented.** No closure, opening, activation, casualty count, damage figure, or
      quotation appears in the draft that did not appear in the input.
- [ ] **Local detail is correct.** Right county, right towns, right river, right routes. Neighboring
      jurisdictions are not confused with ours.
- [ ] **Confirmed and uncertain are visibly separated.** A reader can tell what is known from what
      is expected.
- [ ] **No protected information is present**, including anything that leaked back in from the
      operator's own paste.
- [ ] **Actions are specific to this county** and are things this office can actually do.
- [ ] **Tone is plain, calm, and non-alarming**, and matches how this office normally speaks.
- [ ] **Length fits the audience and channel.**
- [ ] **No AI hedging artifacts remain** — no "as an AI," no "it is important to note," no filler
      apologies, no placeholder text left in by accident.
- [ ] **The reviewer would sign their own name to it.**

## B. Public-facing products

Additional checks for anything reaching the public, media, or elected officials.

- [ ] Facts trace to an approved, releasable source. Nothing unconfirmed is stated as fact.
- [ ] No individual is identifiable, including indirectly through address, vehicle, or circumstance.
- [ ] No security-sensitive detail is disclosed.
- [ ] Instructions to the public are actionable and unambiguous.
- [ ] Contact points and links are current and were clicked or dialed to confirm.
- [ ] Timestamps and effective times are correct, including the time zone.
- [ ] Channel versions are consistent with each other — website, social, alert text, radio script
      do not contradict.
- [ ] Alert text fits the character limit of the system that will send it.
- [ ] Plain language throughout. No jargon or acronyms the public will not know.
- [ ] The Emergency Manager, and the PIO where that role exists, has approved release.

## C. Operational products

Briefs, checklists, ICS content, resource requests.

- [ ] Consistent with the current EOP, annexes, and SOPs.
- [ ] Uses correct ICS terminology and current position titles.
- [ ] Reflects actual local capability, not aspirational capability.
- [ ] Mutual aid assumptions are realistic and match existing agreements.
- [ ] Trigger points and thresholds match adopted criteria, not invented ones.
- [ ] Nothing in it substitutes for a decision that must be made by a person.

## D. Exercise and after-action products

- [ ] All people, businesses, and organizations in scenarios are clearly fictional.
- [ ] The scenario is plausible for this county's hazards, geography, and season.
- [ ] Objectives are measurable and match the intended core capabilities.
- [ ] Injects are realistically timed for the exercise length.
- [ ] After-action findings match what actually happened, not what the model assumed.
- [ ] Corrective actions have a named owner and a due date.
- [ ] No real incident is described in a way that identifies a real person.

## E. Grant and administrative products

- [ ] Every number was produced by a person and verified, not generated.
- [ ] Cited requirements were checked against the actual notice of funding opportunity.
- [ ] Claims about county capability and past performance are true and documentable.
- [ ] Deadlines, program names, and form numbers are current.
- [ ] No boilerplate remains from another county or another grant.

---

## Sign-off block

Attach or record this with the final product for public-facing and operational items.

```text
Product:
Prompt ID and version:
Tool used:
Operator:
Date generated:

Checklist sections applied:   [ ] A   [ ] B   [ ] C   [ ] D   [ ] E
Facts verified against:
Changes made in review:
Issues found (for the run log):

Approved by (Emergency Manager or equivalent): ______________________
Date: ____________
```

---

## If the draft fails review

1. Do not patch a fundamentally wrong draft. Regenerate it with better inputs.
2. Record what failed in [`tests/run-log.md`](../tests/run-log.md).
3. If the same failure occurs three times, the prompt is the problem. Open a revision, bump the
   version, and re-run the golden set before replacing the current version.
4. If the failure involved data handling, follow the incident procedure in
   [Data Classification](data-classification.md), section 5.
