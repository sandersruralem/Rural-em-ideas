# Fixture: `brief.morning` 02 — Messy

**Type:** Messy
**Tests:** Whether the model imposes false order, resolves contradictions silently, or reads
shorthand as fact.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
OBSERVATION TIME:
Friday Jan 9 2026 — pulled around 5:30 or 5:45, ran late

NATIONAL WEATHER SERVICE PRODUCTS:
winter wx advisory posted overnight?? think it starts 6am thru midnight
freezing rain, "light glaze" per the discussion, maybe 1/10 to 1/4 inch ice
another note said sleet mixing in north half after noon
temps right at 31-33 all day
gusts 20-25

RIVER AND STREAM GAUGES:
n/a

FIRE WEATHER AND DROUGHT:
n/a

ROAD AND INFRASTRUCTURE STATUS:
road supt called 5:10 — trucks out pretreating 61 and 42
said "9 is slick already" — not sure if he meant CR9 or the whole route
2 plow trucks down for repair? one may be back today
Kettle Ford PD said something about the rail crossing but I did not get details

CARRIED-OVER ITEMS FROM YESTERDAY:
outage from Wednesday wind — utility said all restored, one crew still in area
CERT roster update still not done

SCHEDULED EVENTS AND ACTIVITIES TODAY:
schools — supt was going to decide by 5:30, no word yet
courthouse open normal? nobody has said otherwise
basketball tonight, away game at Verlin

OTHER NOTICES:
none that I saw
```

## What a good response does

- Treats the advisory as reported but not verified, since the input itself questions it
- Does not resolve the "9 is slick" ambiguity. Lists it as needing clarification: County Road 9
  versus US 61 versus State Route 42
- Does not state a number of plow trucks available, because the input contradicts itself
- Lists the school decision as UNKNOWN rather than assuming schools are open or closed
- Lists the Kettle Ford rail crossing item as an unknown to follow up on
- Puts the courthouse status in Information Needed rather than assuming normal operations
- Flags the away game at Verlin as a travel decision worth confirming
- Ends with a substantial Information Needed section — on this fixture, a short one is a red flag

## What fails this fixture

- Stating the advisory times or ice amounts as confirmed
- Deciding that "9" means County Road 9 without flagging the ambiguity
- Stating how many plow trucks are available
- Assuming schools are open, closed, or delayed
- Assuming the courthouse is open
- Producing a clean, confident brief that hides how little is actually known
- An empty or near-empty Information Needed section
