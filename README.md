# County Emergency Management AI Playbook and Prompt Library

A working repository for a small rural county Emergency Management Office to use AI tools as a force
multiplier: more drafts, briefs, plans, and public messages produced by very few people, without
lowering accuracy or exposing protected information.

**Status:** v0.1 draft. Nothing here is adopted county policy yet, and no prompt has been tested.

| Setting | Value |
| --- | --- |
| Approved tools | Microsoft Copilot (county enterprise), Claude Pro, Gemini Pro |
| Reviewer of record | Emergency Manager or equivalent |
| Language | English only |
| Data routing | Green anywhere approved; Yellow to Copilot only, once its checklist is signed; Red nowhere |

---

## Start here

| If you are... | Read |
| --- | --- |
| New to this | [The playbook](docs/ai-playbook.md), then the [quick start](docs/ai-playbook.md#appendix-a--one-page-quick-start) |
| About to type something into an AI tool | [Data classification](docs/data-classification.md) |
| Unsure which tool to use | [Data routing](docs/approved-tools.md#5-data-routing) |
| About to release an AI-assisted product | [Review checklist](docs/review-checklist.md) |
| Doing a specific job | [Job playbooks](docs/job-playbooks/) |
| Looking for a prompt | [Prompt index](prompts/README.md) |
| Testing a prompt | [Testing protocol](tests/README.md) |
| Wondering what happens next | [Roadmap](docs/roadmap.md) |

---

## The three rules

1. **Match the data to the tool.** Green goes to any approved tool. Yellow goes to Microsoft Copilot
   only, because it runs on the county enterprise tenant. Red goes nowhere. When in doubt, it is
   Red. See [data classification](docs/data-classification.md).
2. **Everything is a draft.** The Emergency Manager reviews every operational and public-facing
   product before it goes anywhere.
3. **Official systems remain the source of truth.** The National Weather Service, dispatch, and the
   state system are authoritative. AI summarizes and packages; it does not decide.

---

## Repository layout

```text
docs/
  ai-playbook.md            how this office uses AI: principles, workflow, roles, pilot
  data-classification.md    Green / Yellow / Red, the decision rule, incident procedure
  approved-tools.md         Copilot, Claude Pro, Gemini Pro: strengths, cautions, authorization
  review-checklist.md       what the reviewer of record checks before anything is released
  roadmap.md                phased build plan with exit conditions
  job-playbooks/            one page per workflow: inputs, steps, review focus, failure modes
  governance/change-log.md  every change, promotion, and data-handling incident

prompts/
  README.md                 index, authoring standard, versioning rules, backlog
  _template.md              the standard every prompt follows
  brief.morning/v1.md       morning hazard digest and action checklist
  msg.pack/v1.md            public message pack across channels
  ex.tabletop/v1.md         tabletop design and after-action

context/
  county-fact-pack.md       local context pasted into every prompt — TEMPLATE, not yet filled in

tests/
  README.md                 golden fixtures, scoring, pass rules, regression policy
  run-log.md                real-world use during the pilot
  fixtures/                 fixed test inputs, including negative cases
  scorecards/               blank template and completed results
```

## What is currently in the three pilot workflows

| Job | Prompt | Status |
| --- | --- | --- |
| Morning hazard digest | `brief.morning` v1 | Draft — untested |
| Public message pack | `msg.pack` v1 | Draft — untested |
| Tabletop and after-action | `ex.tabletop` v1 | Draft — untested |

---

## Two things must happen before any of this is used

1. **Fill in [`context/county-fact-pack.md`](context/county-fact-pack.md).** It is a template. Until
   it describes the real county, every prompt will produce advice that would fit anywhere and help
   nowhere.
2. **Run the golden sets** in [`tests/README.md`](tests/README.md) and file the scorecards. A prompt
   is a draft until there is evidence behind it.

Details and sequencing are in the [roadmap](docs/roadmap.md).

---

## Notes on the test fixtures

Fixtures use a fictional county, Bramble County in the fictional State of Weldon, so they can live
in a repository safely. Some fixtures deliberately contain invented material that the prompts must
refuse to process, in order to test the safety rules. No fixture contains real resident, patient, or
law-enforcement information, and none should ever be created from real records.

## Contributing

- Never edit a tested or approved prompt in place. Copy it forward and bump the version.
- Any prompt change requires re-running the same golden set before it replaces its predecessor.
- Record every change in [the change log](docs/governance/change-log.md).
- Keep everything in this repository Green. Assume it may become public.

## License

GNU General Public License v3.0. See [LICENSE](LICENSE).
