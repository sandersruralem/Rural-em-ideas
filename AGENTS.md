# Cloud Agent instructions — Rural EM Ideas

You are working in a repo that invents and spikes tools for **rural and county emergency management** offices (small staff, large geography, limited IT/budget, intermittent connectivity).

## Mission

Implement the spike or prototype brief you were given. Optimize for field usefulness under stress, not feature completeness.

## Non-negotiable rural constraints

- Prefer tools a 1–3 person EM office can run without a dedicated IT department
- Prefer offline-capable, printable, phone-friendly, CSV/Excel-friendly designs
- Do not assume metro staffing, always-on broadband, or enterprise GIS/CAD integrations
- Do not invent legal/policy claims (HIPAA, FOIA, NIMS compliance). If needed, add a clear “needs local counsel / EM director review” note
- Do not build a full EOC platform unless the brief explicitly says so
- Plain language only — no vendor jargon

## How to work

1. Read `README.md`, the assigned brief under `ideas/`, and this file
2. Stay inside the brief’s in-scope list
3. Implement the smallest demo that meets success criteria
4. Verify using the brief’s checklist; fix failures before finishing
5. Open a PR with:
   - What a rural EM user would do in 60 seconds
   - Screenshots or a short recording of the demo
   - Known limitations and offline/IT assumptions
   - How to run locally

## Stack defaults (unless brief overrides)

- Static HTML/CSS/JS or a tiny local web app
- SQLite or localStorage if state is needed
- CSV import/export over custom databases
- Printable CSS for anything used in an EOC/briefing
- No heavy frameworks unless required for the demo

## Safety / ethics

- Use only synthetic or clearly fake demo data (no real PII, no real vulnerable-population lists)
- Do not scrape or store real personal data
- If a feature would be dangerous if trusted blindly in an incident (e.g., automated dispatch advice), make it advisory and label it clearly

## When blocked

Document the blocker in the PR description and stop. Do not silently expand scope or fake a successful verification.
