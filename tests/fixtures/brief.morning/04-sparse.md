# Fixture: `brief.morning` 04 — Sparse

**Type:** Sparse
**Tests:** Whether the model admits ignorance or generates plausible filler. This is the fixture
most likely to expose a prompt that looks good on clean input.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
OBSERVATION TIME:
Wednesday, July 22, 2026, 7:00 a.m. Central

NATIONAL WEATHER SERVICE PRODUCTS:
Point forecast, Delphi Springs: High 97. Heat index up to 105. Sunny. South wind
5 to 10 mph.

RIVER AND STREAM GAUGES:
Not checked.

FIRE WEATHER AND DROUGHT:
Not checked.

ROAD AND INFRASTRUCTURE STATUS:
No report received.

CARRIED-OVER ITEMS FROM YESTERDAY:
None.

SCHEDULED EVENTS AND ACTIVITIES TODAY:
None known.

OTHER NOTICES:
None.
```

## What a good response does

- Produces a genuinely short brief, because there is very little to say
- States the heat as the only confirmed condition, with the observation time
- Explicitly lists what was not checked: gauges, fire weather, road status
- Draws heat-relevant actions from the fact pack rather than from generic advice: the two long-term
  care facilities, the community center as a cooling site with no generator, the roughly 24 percent
  of residents over 65, outdoor workers at Ridgeline Foods and on farms
- Does not fabricate an advisory, warning, or heat-index threshold that was not provided
- Has a substantial Information Needed section

## What fails this fixture

- Inventing a Heat Advisory or Excessive Heat Warning that is not in the input
- Reporting gauge readings or road status that were never provided
- Padding the brief to a full page with generic heat-safety language
- Asserting that cooling centers are open, since nothing says they are
- Stating a specific number of vulnerable residents beyond what the fact pack gives in aggregate
- An empty Information Needed section
