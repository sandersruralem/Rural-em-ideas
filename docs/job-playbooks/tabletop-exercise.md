# Job Playbook: Tabletop Exercise and After-Action

**Prompt:** `ex.tabletop` v1
**Recommended tool:** Claude Pro
**Target time:** 45–60 minutes to a workable draft package, against a day or more unassisted
**Frequency:** Per exercise cycle
**Reviewer:** Emergency Manager, plus the exercise lead

---

## When to use

Designing a discussion-based tabletop for county staff, volunteer fire and EMS, road department,
schools, or the LEPC. Also useful for refreshing a scenario that has grown stale from repetition.

## When not to use

- For full-scale or functional exercises with live field play. Those need proper design support.
- For evaluated exercises tied to a grant deliverable, without first confirming the required format
  with the state exercise officer.

## Inputs to gather

| Input | Notes | Required |
| --- | --- | --- |
| Hazard and scenario premise | Drawn from the hazard mitigation plan | Yes |
| Exercise length | Typically 90–120 minutes for a tabletop | Yes |
| Participants and their roles | By position, not by name | Yes |
| Objectives | Two to four, or ask the prompt to propose them | Yes |
| Capabilities to exercise | Communications, mass care, warning, resource management | Yes |
| Season and time of day | Changes everything about a rural scenario | Yes |
| Known local constraints | Volunteer staffing, single access routes, no local hospital | Yes |
| Prior findings | Open corrective actions worth retesting | If any |
| County fact pack | `context/county-fact-pack.md` | Yes |

## Steps

1. Decide the hazard and what you actually want to learn. A tabletop that tests nothing is a meeting.
2. Open `prompts/ex.tabletop/v1.md`. Paste the system block, then the user block.
3. Generate the scenario, objectives, and timed injects.
4. Confirm every person, business, and organization in the scenario is clearly fictional.
5. Check plausibility against local geography and season. Wrong-season scenarios undermine the room.
6. Adjust inject timing to the real clock, allowing for discussion sprawl.
7. Exercise lead and Emergency Manager review and approve.
8. Run the exercise. Capture notes on the ICS 214 or a notepad.
9. Feed the notes back through the after-action portion of the prompt for a draft AAR.
10. Assign an owner and due date to every corrective action. Log the run.

## Expected output

- Scenario narrative, roughly 200–400 words
- Two to four measurable objectives mapped to capabilities
- Timed inject schedule fitting the stated exercise length
- Discussion questions per module
- Facilitator notes and expected discussion points
- A safety and artificiality statement
- After-action structure: findings, strengths, areas for improvement, corrective actions with owners
  and due dates

## Review focus for this job

Beyond the universal checks in the [Review Checklist](../review-checklist.md), section D applies in
full. Pay particular attention to:

- Fictional names throughout, with no real resident, business, or facility depicted in a harmful way
- Season, geography, and staffing realities matching this county
- Objectives measurable, not aspirational
- Inject timing that leaves room for discussion
- After-action findings that reflect what happened in the room, not what the model expected

## Known failure modes

| Failure | How to catch it |
| --- | --- |
| Urban assumptions in a rural county | Check for transit, multiple hospitals, large career departments |
| Uses a real business or resident name | Scan every proper noun |
| Too many injects for the time available | Count injects against minutes and cut |
| Objectives that cannot be measured | Rewrite until each has an observable outcome |
| Findings drift toward generic best practice | Compare each finding against the actual notes |
| Corrective actions with no owner | Reject the draft; every action gets a name and a date |

## Escalation

If the exercise supports a grant requirement or a state reporting obligation, confirm the required
format and documentation with the state exercise officer before building the package.
