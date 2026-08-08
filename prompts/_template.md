# Prompt: `area.job`

| Field | Value |
| --- | --- |
| **ID** | `area.job` |
| **Version** | v1 |
| **Status** | Draft — untested |
| **Job** | One sentence describing the single job this prompt does |
| **Recommended tool** | Microsoft Copilot / Claude Pro / Gemini Pro. Note which tool for Green inputs and which if any input is Yellow |
| **Data level** | Green, or Yellow in Copilot once authorized. Never Red. |
| **Reviewer** | Emergency Manager or equivalent |

---

## When to use

Describe the situation that should trigger this prompt.

## When not to use

List the cases where a person must do the work instead, or where a different prompt applies.

## Required inputs

| Input | Source | Notes |
| --- | --- | --- |
| County fact pack | `context/county-fact-pack.md` | Always required |
| | | |

## Optional inputs

| Input | Effect |
| --- | --- |
| | |

---

## System block

Paste into the tool's system, instruction, or first message field.

```text
You are assisting a small rural county emergency management office in the United States.

Rules that apply to every response:
- Use only the information provided in this conversation. Do not add facts from memory.
- If a needed fact is missing, write UNKNOWN and list it under "Information Needed."
  Never invent road closures, shelter status, gauge readings, casualty counts, damage
  figures, activation decisions, or quotations.
- Separate what is confirmed from what is uncertain, and say which is which.
- Write in plain English at roughly an eighth-grade reading level. Short sentences.
- Do not include personal, medical, or law-enforcement information even if it appears
  in the input. If you see any, stop and say so instead of processing it.
- Everything you produce is a draft for human review, not an official product.
- Follow the output structure exactly. Do not add sections or commentary.
```

## User block

Fill every field before sending.

```text
[Job-specific instruction]

COUNTY FACT PACK:
<paste>

INPUTS:
<paste>

OUTPUT FORMAT:
<sections>
```

---

## Expected output schema

The output must contain exactly these sections, in this order:

1. Section one
2. Section two
3. Information Needed

## Acceptance criteria

Written before testing. A run passes only if all of these hold.

- [ ] Criterion
- [ ] No invented facts of any kind
- [ ] Missing information appears under Information Needed rather than being filled in
- [ ] Output matches the schema exactly

## Review checklist

Job-specific checks, applied in addition to the
[universal checklist](../docs/review-checklist.md).

- [ ] Check

## Known failure modes

| Failure | How to catch it |
| --- | --- |
| | |

## Change history

| Version | Date | Change | Author |
| --- | --- | --- | --- |
| v1 | YYYY-MM-DD | Initial draft | |
