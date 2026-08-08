# Job Playbook: Morning Hazard Digest

**Prompt:** `brief.morning` v1
**Recommended tool:** Claude Pro
**Target time:** 10–15 minutes, against roughly 45–60 minutes unassisted
**Frequency:** Each working morning, and twice daily during activation
**Reviewer:** Emergency Manager

---

## When to use

Every working morning, to produce a one-page situational brief for the Emergency Manager, the county
executive or judge, and department heads. Also useful before a board meeting or when a partner
agency asks "what are we watching?"

## When not to use

- During an active incident when the operational picture is changing faster than you can brief. Use
  ICS forms and the state system instead.
- As a substitute for reading the NWS forecast discussion yourself. You still read the source.

## Inputs to gather

All inputs are Green.

| Input | Source | Required |
| --- | --- | --- |
| NWS forecast, watches, warnings, advisories | weather.gov point forecast for the county | Yes |
| River or stream gauges | USGS / NWS AHPS, if the county has flood-prone waterways | If applicable |
| Fire weather or drought status | State forestry, NWS fire weather, drought monitor | Seasonally |
| Road status | County road department, state DOT public feed | Yes |
| Known scheduled events | County calendar | Yes |
| Ongoing issues carried from yesterday | Yesterday's brief | Yes |
| Regional or state notices | State EMA public bulletins | If any |
| County fact pack | `context/county-fact-pack.md` | Yes |

Copy the source text rather than paraphrasing it. Paraphrasing before the model sees it is where
detail gets lost.

## Steps

1. Pull the sources above into one scratch document. Note the time you pulled them.
2. Open `prompts/brief.morning/v1.md`. Paste the system block, then the user block.
3. Paste the county fact pack, then your gathered inputs, then the observation time.
4. Generate.
5. Read for obvious nonsense first: wrong county, invented closures, a river we do not have.
6. Verify every specific number, road, and time against the source. This is the real work.
7. Confirm the action checklist contains things this office can actually do today.
8. Emergency Manager reviews and approves.
9. Distribute through the normal channel and file it.
10. Log the run in `tests/run-log.md`.

## Expected output

A one-page brief containing:

- Bottom line up front, three sentences or fewer
- Confirmed conditions, with source and observation time
- Uncertain or developing conditions, stated as uncertain
- Watch items with trigger points
- County actions for today, three to seven items, each assignable
- What we do not know and how we will find out

## Review focus for this job

Beyond the universal checks in the [Review Checklist](../review-checklist.md):

- Gauge readings and forecast numbers match the source exactly
- No road is described as closed or open unless a source says so
- Trigger points match adopted criteria, not invented thresholds
- The uncertainty section is not empty when the forecast is genuinely uncertain

## Known failure modes

| Failure | How to catch it |
| --- | --- |
| Invents a closure or shelter opening | Cross-check every status claim against source |
| Blurs confirmed and forecast conditions | Require the two-section split; reject if merged |
| Generic actions that would fit any county | Reject and regenerate with a fuller fact pack |
| Overstates certainty in a marginal forecast | Compare against the NWS forecast discussion wording |
| Drops a carried-over issue from yesterday | Always paste yesterday's open items as input |

## Escalation

If the brief would drive an activation, evacuation, or shelter decision, the Emergency Manager makes
that decision from the source data, not from the brief.
