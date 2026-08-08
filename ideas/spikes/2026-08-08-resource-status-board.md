# Spike brief — Printable resource status board

**Status:** ready  
**Inbox source:** `ideas/inbox/2026-08-08-seed-friction-themes.md`  
**Owner:**  
**Cloud Agent PR:**

## Problem (rural-specific)

During activation, shelter/generator/fuel/staff status lives in whiteboards, group texts, and individual memories. Across a large county, partners cannot see the same truth, and the EM becomes a human router.

## User and stressful moment

EM coordinator updating status between radio calls; fire/public works checking what’s available before driving 40 minutes.

## Hypothesis

If we provide a **phone-updatable status board that also prints as one sheet**, then partners can share a common picture without new accounts, measurable by successful tabletop updates in under 1 minute per change.

## In scope

- Status board for: shelters, generators, fuel, key facilities, staff on-duty (synthetic)
- Mobile-friendly edit
- One-click printable snapshot
- Optional CSV export
- Local-only persistence for the spike (localStorage or file)

## Out of scope

- Full EOC / CAD replacement
- Realtime multi-user cloud sync (note as future; spike may simulate)
- Auth/roles beyond a simple “editor” demo
- Live generator telemetry

## Success criteria (demo definition of done)

- [ ] Update a status in under 1 minute on a phone-sized viewport
- [ ] Printable snapshot is readable on one page
- [ ] Synthetic data only
- [ ] Zero-IT run instructions in PR
- [ ] Screenshot or recording attached

## Approach hints (optional)

Think “digital whiteboard that prints,” not “ops center product.”

## Stack preferences

- Static/tiny web app + print CSS + CSV export
- Avoid: mandatory logins for viewers

## Verification checklist (for the agent)

1. Open demo
2. Edit 3 resource rows on a narrow viewport
3. Export CSV
4. Open print preview — fits one page / readable
5. Confirm synthetic labels only

## Rural fit self-check

- [ ] Does not create babysitting work
- [ ] Useful even if sync is “screenshot/PDF share”
- [ ] Understandable without training slides
- [ ] Mutual-aid friendly (print/PDF share without accounts)

## Scoring (pre-spike)

| Pain | Rural fit | Novelty | Spikeability | Adoption | Total |
|------|-----------|---------|--------------|----------|-------|
| 5 | 5 | 2 | 5 | 5 | 22 |
