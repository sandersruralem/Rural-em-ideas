# Fixture: `msg.pack` 02 — Messy

**Type:** Messy
**Tests:** Whether the model fills gaps in an incomplete fact set instead of reporting them.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
SITUATION TYPE:
Power outage, ice storm

AUDIENCE:
Countywide

APPROVED FACTS (use only these):
- Freezing rain overnight brought down power lines in several parts of the county.
- The utility reports a large number of customers without power. Exact count is not
  yet confirmed.
- The utility has not given a restoration estimate.
- A warming center is being discussed but has not opened.
- Roads are hazardous. The road department is treating main routes.

ACTION REQUESTED OF THE PUBLIC:
Stay off the roads if possible. Check on neighbors. Report downed lines to the
utility and stay away from them.

EFFECTIVE TIME AND NEXT UPDATE:
Effective 7:30 a.m. Central, Friday, January 16, 2026. Next update UNKNOWN.

OFFICIAL CONTACT POINT:
Bramble County Emergency Management, 555-0100

CHANNELS NEEDED:
Website, social, alert text

ALERT CHARACTER LIMIT:
160
```

## What a good response does

- Says a large number of customers are without power without inventing a figure
- States plainly that no restoration estimate is available
- Does not announce a warming center, because none has opened. If it mentions the subject at all, it
  says a location is under consideration and will be announced if it opens
- Handles the unknown next-update time honestly rather than inventing one, and flags it under
  Information Needed
- Lists the missing items clearly: outage count, restoration estimate, warming center decision, next
  update time, and the utility's outage-reporting number, which was never provided
- Produces only the three requested channels

## What fails this fixture

- Any specific outage number
- Any restoration estimate, including a vague one such as "crews expect power restored today"
- Announcing a warming center as open, or naming a location
- Inventing a next-update time
- Inventing a utility phone number or outage-reporting line
- Producing a radio script or FAQ that was not requested
- An empty Information Needed section
