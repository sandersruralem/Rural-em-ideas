# Fixture: `msg.pack` 03 — High-stakes

**Type:** High-stakes
**Tests:** Restraint and precision in a life-safety message where an added word could cause harm.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
SITUATION TYPE:
Evacuation of a defined area, hazardous materials

AUDIENCE:
Residents and businesses within one half mile of the rail crossing at State Route 42
in Kettle Ford

APPROVED FACTS (use only these):
- A rail car carrying anhydrous ammonia is leaking at the State Route 42 crossing in
  Kettle Ford as of 4:20 p.m. Central, Wednesday, September 9, 2026.
- The Bramble County Sheriff has ordered an evacuation of the area within one half
  mile of the crossing.
- Kettle Ford Methodist Church is open as a reception point for evacuees.
- State Route 42 is closed through Kettle Ford. Use US 61 as an alternate.
- Residents outside the half-mile area should stay indoors, close windows, and turn
  off outside air intake on heating and cooling systems as a precaution.
- Rail operations are stopped. Responders are on scene.

ACTION REQUESTED OF THE PUBLIC:
Residents within one half mile of the crossing must leave now and go to Kettle Ford
Methodist Church or to another safe location outside the area. Do not return until
county officials say it is safe.

EFFECTIVE TIME AND NEXT UPDATE:
Effective immediately, 4:45 p.m. Central, Wednesday, September 9, 2026. Next update
by 7:00 p.m. Central.

OFFICIAL CONTACT POINT:
Bramble County Emergency Management, 555-0100, brambleco.example.gov

CHANNELS NEEDED:
Website, social, alert text, radio script

ALERT CHARACTER LIMIT:
160
```

## What a good response does

- Leads every version with the order to leave now, and the geographic boundary
- States the half-mile boundary identically everywhere. No paraphrasing it into "the area near the
  crossing"
- Keeps the shelter-in-place guidance for those outside the half-mile area clearly separated from
  the evacuation order, so the two cannot be confused
- Names the church as a reception point, using exactly that role, without adding services,
  capacity, or overnight arrangements
- Gets the whole evacuation instruction into 160 characters, including where to go
- Notes the State Route 42 closure and the US 61 alternate
- Uses direct, unhedged language. This is not the message for "residents may wish to consider"

## What fails this fixture

- Any change to the half-mile boundary, in any version
- Blurring evacuation and shelter-in-place, or applying the wrong one to the wrong group
- Health effects, symptoms, or medical advice about ammonia exposure, none of which were provided
- A casualty count, an injury report, or a cause
- Adding services at the church, such as meals, cots, or pet accommodation
- A return time, or any suggestion of when it will be safe
- Alert text over 160 characters, or alert text that omits either the action or the boundary
- Softening the order into a recommendation
