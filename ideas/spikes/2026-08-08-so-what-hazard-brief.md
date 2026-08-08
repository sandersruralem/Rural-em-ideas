# Spike brief — County “So What?” weather / hazard brief

**Status:** ready  
**Inbox source:** `ideas/inbox/2026-08-08-seed-friction-themes.md`  
**Owner:**  
**Cloud Agent PR:**

## Problem (rural-specific)

A 1–3 person county EM office gets the same regional NWS products and state alerts as everyone else, but still has to answer: *what does this mean for our roads, rivers, facilities, and partners?* That translation currently happens via memory, phone calls, and scrolling — slow when staffing is thin.

## User and stressful moment

EM coordinator (or on-call deputy) during a watch/warning, needing a one-page local brief before the next partner call.

## Hypothesis

If we generate a **county-specific one-page “so what” brief** from a small set of local assets + hazard inputs, then the coordinator can brief partners in under 5 minutes, measurable by time-to-first-brief in a tabletop.

## In scope

- Simple web (or static) form: hazard type + severity + free-text NWS synopsis paste
- Local asset checklist (roads/bridges, low-water crossings, shelters, facilities, vulnerable sites) driven by **synthetic county fixture data**
- Generated one-page brief (on-screen + printable) with suggested local actions and partner call-outs
- Export to PDF print or Markdown

## Out of scope

- Full EOC / CAD replacement
- Live NWS API integration (may stub; paste-in is OK for spike)
- Automated evacuation orders or dispatch recommendations
- Multi-county auth/SaaS

## Success criteria (demo definition of done)

- [ ] User can produce a printable one-page brief in under 5 minutes in the demo
- [ ] Works on a phone-sized viewport **and** prints cleanly
- [ ] Uses only synthetic demo data
- [ ] README or PR explains how to run with no special IT setup
- [ ] Screenshot or short recording attached

## Approach hints (optional)

Start with paste-in hazard text + checkbox local impacts → templated brief. Smart defaults beat complex GIS.

## Stack preferences

- Default: static or tiny local web app + print CSS
- Avoid: accounts, databases, live map servers

## Verification checklist (for the agent)

1. Open the demo locally
2. Load synthetic “Green County” fixtures
3. Enter a sample flash-flood watch synopsis
4. Select 3–5 local assets impacted
5. Generate brief; print-preview looks like one page
6. Confirm no real PII in fixtures

## Rural fit self-check

- [ ] Does not create babysitting work
- [ ] Degrades if connectivity drops (local/static OK)
- [ ] Understandable without training slides
- [ ] Mutual-aid friendly (shareable PDF/print) — or explicitly N/A

## Scoring (pre-spike)

| Pain | Rural fit | Novelty | Spikeability | Adoption | Total |
|------|-----------|---------|--------------|----------|-------|
| 4 | 5 | 3 | 5 | 4 | 21 |
