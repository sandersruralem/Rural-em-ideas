# Fixture: `msg.pack` 01 — Typical

**Type:** Typical
**Tests:** Everyday performance and cross-channel consistency.

Use with [`_shared/test-fact-pack.md`](../_shared/test-fact-pack.md). All content is fictional.

---

## Inputs

```text
SITUATION TYPE:
Boil water advisory

AUDIENCE:
Delphi Springs water system customers only

APPROVED FACTS (use only these):
- A water main broke on North Street at about 3:00 a.m. Thursday, March 5, 2026.
- Repairs are complete. Water service has been restored.
- Because system pressure was lost, the state requires a precautionary boil water
  advisory for all Delphi Springs water system customers.
- The advisory does not apply to rural water district customers or to private wells.
- Water samples were collected Thursday morning. Results take about 24 hours.
- The advisory remains in effect until the county announces it has been lifted.

ACTION REQUESTED OF THE PUBLIC:
Bring water to a rolling boil for one minute and let it cool before drinking, making
ice, brushing teeth, washing dishes, or preparing food.

EFFECTIVE TIME AND NEXT UPDATE:
Effective 9:00 a.m. Central, Thursday, March 5, 2026. Next update by 5:00 p.m.
Central, Friday, March 6, 2026.

OFFICIAL CONTACT POINT:
Bramble County Emergency Management, 555-0100, brambleco.example.gov

CHANNELS NEEDED:
Website, social, alert text, radio script, FAQ

ALERT CHARACTER LIMIT:
160
```

## What a good response does

- Puts the boil instruction in the first two sentences of every version
- States clearly in every version that the advisory applies only to Delphi Springs water system
  customers, not to rural water or private wells
- Keeps the alert text within 160 characters and shows the count
- Uses the same effective time and next-update time everywhere, with the time zone
- Writes an FAQ covering the obvious questions: is the water safe for showering, for pets, what
  about ice already in the freezer, when will it be lifted
- Says the advisory remains until lifted, without predicting when

## What fails this fixture

- Predicting a lift time or saying results will be back "tomorrow morning"
- Omitting the rural water and private well exclusion from any version
- Alert text over 160 characters
- Adding a distribution point, bottled water site, or hotline that was never mentioned
- Stating a cause beyond the main break, or assigning blame
- Any version that contradicts another on times or who is affected
