# Run Log

Lightweight record of real-world prompt use during the pilot. One line per run. The point is to see
whether the editing burden falls over time and whether the same defect keeps recurring.

Keep it fast to fill in. A log nobody completes tells you nothing.

| Date | Prompt ID and version | Tool | Minutes editing | Errors caught | Auto-fail? | Keep / change |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

---

## How to fill this in

- **Minutes editing** — time from receiving the draft to a version you would sign, not including
  gathering inputs.
- **Errors caught** — what review found, briefly. "Invented gauge reading." "Wrong route number."
  "Contradiction between the alert text and the website version."
- **Auto-fail?** — yes if any condition in the [testing protocol](README.md), section 3, occurred.
  Any yes is reported to the Emergency Manager the same day.
- **Keep / change** — your judgment on whether the prompt is working as written.

## Escalation rule

If the same defect appears three times, the prompt is the problem, not the operator. Open a new
version, fix it, and re-run the golden set before replacing the current version.

If any run involves protected data reaching a tool, follow the incident procedure in
[Data Classification](../docs/data-classification.md), section 5, before anything else.

## Weekly review

Once a week during the pilot, the Emergency Manager reviews this log and records:

| Week ending | Runs | Median minutes editing | Recurring defects | Decision |
| --- | --- | --- | --- | --- |
| | | | | |
