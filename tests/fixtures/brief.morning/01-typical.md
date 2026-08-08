# Fixture: `brief.morning` 01 — Typical

**Type:** Typical
**Tests:** Everyday performance on clean, well-formed input.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
OBSERVATION TIME:
Tuesday, April 14, 2026, 6:15 a.m. Central

NATIONAL WEATHER SERVICE PRODUCTS:
Area Forecast Discussion, Verlin WFO, issued 4:52 a.m. Central.
A cold front will cross the region this afternoon. Scattered thunderstorms are
expected between 2 p.m. and 8 p.m. A few storms could become strong, with gusts to
50 mph and pea-sized hail. The tornado threat is low but not zero along and south of
State Route 42. Rainfall of one half to one inch is expected, locally higher under
storms. No watches or warnings are in effect at this time.

Point forecast, Delphi Springs: High 74. South wind 10 to 15 mph, gusting 25.
Chance of precipitation 70 percent after 2 p.m. Low tonight 52.

RIVER AND STREAM GAUGES:
Wicket River at Kettle Ford: 9.4 feet at 6:00 a.m., steady. Flood stage 18 feet.
Sawyer Creek at Ashgrove: 3.1 feet at 6:00 a.m., steady. Flood stage 11 feet.

FIRE WEATHER AND DROUGHT:
None applicable.

ROAD AND INFRASTRUCTURE STATUS:
Road department reports no closures as of 6:00 a.m. Shoulder work continues on
County Road 9 near Mill Bend through Friday, one lane with flaggers, 7 a.m. to
4 p.m.

CARRIED-OVER ITEMS FROM YESTERDAY:
Generator service at the courthouse annex is scheduled for Thursday. The vendor has
not confirmed a time.

SCHEDULED EVENTS AND ACTIVITIES TODAY:
County Commission meets at 9 a.m. High school baseball at 4:30 p.m. at the county
high school.

OTHER NOTICES:
State Emergency Management District 4 weekly bulletin notes a statewide radio test
on Thursday at 10 a.m.
```

## What a good response does

- Leads with the afternoon storm timing and the wind and hail threat
- Notes that no watches or warnings are in effect, because that is what the input says
- Keeps both gauges in confirmed conditions with their 6:00 a.m. readings, well below flood stage
- Flags the 4:30 p.m. baseball game against the 2 p.m. to 8 p.m. storm window, since that is a real
  local decision point for today
- Notes the County Road 9 lane closure as a work zone, not as a road closure
- Carries the unconfirmed generator service time forward and lists it as an open item
- Actions name roles that exist in the fact pack

## What fails this fixture

- Any watch or warning stated as in effect
- Any gauge value other than 9.4 and 3.1 feet
- Describing County Road 9 as closed
- Dropping the generator item
- Generic advice such as "encourage residents to have a plan" with no local anchor
- Missing the conflict between the game time and the storm window
