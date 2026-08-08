# Job Playbook: Public Message Pack

**Prompt:** `msg.pack` v1
**Recommended tool:** Claude Pro or Gemini Pro
**Target time:** 15–20 minutes, against roughly 60–90 minutes unassisted
**Frequency:** As needed
**Reviewer:** Emergency Manager, plus the PIO where that role exists

---

## When to use

When one set of approved facts needs to reach the public through several channels at once: county
website, Facebook, mass-notification text, radio read script, and a short FAQ. Writing five versions
by hand is where a small office loses an hour it does not have.

## When not to use

- When the facts are not yet approved. The prompt does not decide what is true.
- For anything involving a named individual, casualty, or law-enforcement matter.
- For translation. English only in v1; translation goes to a human translator.

## Inputs to gather

| Input | Notes | Required |
| --- | --- | --- |
| Approved fact set | Bullet points, already verified and releasable | Yes |
| Situation type | Outage, flood, winter storm, boil water, road closure, shelter opening | Yes |
| Audience | Whole county, a specific town, a specific road corridor | Yes |
| Action requested of the public | What people should actually do | Yes |
| Effective time and expected update time | Include the time zone | Yes |
| Official contact point | Published number or page, not a personal cell | Yes |
| Channels needed | Which of the five variants are actually going out | Yes |
| Alert character limit | From the notification system in use | If sending an alert |
| County fact pack | `context/county-fact-pack.md` | Yes |

Write the fact set as short declarative bullets. Ambiguity in the input becomes confident nonsense in
the output.

## Steps

1. Confirm with the Emergency Manager which facts are approved for release.
2. Open `prompts/msg.pack/v1.md`. Paste the system block, then the user block.
3. Fill in every field. Leave nothing implied.
4. Generate.
5. Check the variants against each other for contradictions. This is the most common defect.
6. Confirm the alert version fits the character limit by pasting it into the system, not by trusting
   the count in the output.
7. Read the radio script aloud. If it does not read cleanly, fix it.
8. Verify links and phone numbers by clicking and dialing.
9. Emergency Manager approves release.
10. Post and send. File the final versions and log the run.

## Expected output

- Website update, roughly 150–250 words
- Social post, roughly 50–80 words
- Mass-notification text within the stated character limit
- Radio read script, roughly 30 seconds when read aloud
- Three to six FAQ entries
- A list of facts the draft needed but did not have

## Review focus for this job

Beyond the universal checks in the [Review Checklist](../review-checklist.md), section B applies in
full. Pay particular attention to:

- Consistency across variants, especially times and instructions
- No fact appearing in any variant that was not in the approved input
- Plain language, no jargon, no acronyms the public will not know
- Correct effective time and time zone in every variant
- The action requested is unambiguous

## Known failure modes

| Failure | How to catch it |
| --- | --- |
| Variants contradict each other | Read them side by side before approving |
| Alert text exceeds the character limit | Paste into the actual system to check |
| Adds reassurance not supported by facts | Compare each sentence against the input bullets |
| Invents a hotline, hours, or shelter | Verify every contact point |
| Radio script reads as written text | Read it aloud |
| Buries the action in the last sentence | Require the action in the first two sentences |

## Escalation

If a fact is missing, the prompt must say so rather than fill the gap. If the output lists a needed
fact, get it before releasing anything.
