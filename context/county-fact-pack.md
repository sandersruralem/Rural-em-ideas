# County Fact Pack

**Version:** 0.1 (template — not yet filled in)
**Owner:** Emergency Manager
**Data level:** Green only
**Review cycle:** Quarterly, and after any plan change, election, or reorganization

This is the shared local-context block pasted into every prompt. It is what stops a model from
producing advice that would fit any county in the country.

---

## Rules for this file

- **Green data only.** Nothing in this file may identify an individual or reveal a security detail.
- **Public facilities by name and type are fine.** Access codes, camera placements, key-holder
  names, cache contents, and security procedures are not.
- **Use roles, not people.** Write "Road Superintendent," not a person's name or cell number.
- **Publicly listed numbers only.** No personal cell numbers, even for staff.
- **If a line would be uncomfortable in a public-records release, delete it.**

Replace every bracketed placeholder below. Delete any line that does not apply. An honest short
fact pack beats a padded one.

---

## 1. Basics

- County name: `[County Name]`, `[State]`
- County seat: `[City]`
- Population: approximately `[number]` (`[year]` estimate)
- Land area: approximately `[number]` square miles
- Incorporated towns: `[list]`
- Unincorporated communities commonly referenced: `[list]`
- Adjacent counties: `[list]`
- Time zone: `[zone, and whether the county observes daylight saving time]`

## 2. Geography and infrastructure references

- Major highways and routes: `[list, using the numbers locals actually say]`
- Rivers, creeks, and lakes: `[list]`
- Named river or stream gauges used by this office: `[list with the names shown on AHPS]`
- Rail lines and crossings of concern: `[list]`
- Airports or airstrips: `[list]`
- Terrain notes: `[flood plain, bluffs, hollows, bottomland, ridge roads]`
- Areas with a single access route: `[list — describe generally, not tactically]`

## 3. Hazards

From the hazard mitigation plan, in the order this county actually experiences them.

| Hazard | Season | Typical local impact |
| --- | --- | --- |
| `[hazard]` | `[season]` | `[what it actually does here]` |

Notes on past significant events, publicly reported: `[year, event, general impact]`

## 4. Emergency management organization

- Office staffing: `[for example: one full-time emergency manager, one part-time deputy]`
- EOC location and type: `[general description]`
- Activation levels used: `[list the county's actual levels]`
- Who declares a local emergency: `[role]`
- Who authorizes public messaging: `[role]`

## 5. Response resources, described generally

- Fire: `[number]` departments, `[all volunteer / combination]`
- EMS: `[provider type, transport capability, typical response times]`
- Law enforcement: `[sheriff's office, municipal departments, approximate staffing posture]`
- Dispatch: `[county 911 center or shared regional center]`
- Public works and road department: `[capability, equipment classes, staffing]`
- Hospital: `[in-county facility, or nearest facility and drive time]`
- Public health: `[county or district health department]`
- Emergency management volunteers: `[CERT, ARES, auxiliary, or none]`

## 6. Facilities used in emergencies

Publicly known facilities only.

| Facility | Type | Typical role |
| --- | --- | --- |
| `[name]` | `[school / church / community center / fairgrounds]` | `[shelter, warming center, POD, staging]` |

Notes: `[generator availability in general terms, ADA accessibility, capacity ranges]`

## 7. Public warning and information channels

- Mass notification system: `[name of system]`
- Alert character limit: `[number]`
- Outdoor warning sirens: `[yes/no, coverage in general terms]`
- County website: `[URL]`
- Official social media: `[accounts]`
- Local radio: `[stations and call signs]`
- Local newspaper: `[name and publication schedule]`
- Regional television: `[stations]`
- Official public contact point: `[published number or page]`
- Public information authority: `[role]`

## 8. Population considerations

Described in aggregate only. Never list individuals.

- Age profile: `[for example: higher-than-average share of residents over 65]`
- Long-term care and assisted living facilities: `[count and general locations]`
- Residents dependent on electrically powered medical equipment: `[approximate count, if the
  county maintains an aggregate figure]`
- Households without reliable broadband or cell coverage: `[general description]`
- Transportation-limited households: `[general description]`
- Agricultural population and livestock operations: `[general description]`
- Seasonal population swings: `[hunting season, fair week, festivals, harvest labor]`

## 9. Agriculture and economy

- Primary crops and livestock: `[list]`
- Grain storage, feedlots, dairies of note: `[general description]`
- Major employers: `[list]`
- Facilities with hazardous materials reporting obligations: `[general description only]`

## 10. Mutual aid and partners

- Mutual aid agreements in place: `[list by type, not by document detail]`
- Regional or district emergency management structure: `[description]`
- State emergency management contact path: `[role and process, not personal contacts]`
- Tribal, federal, or military installations nearby: `[list]`
- Voluntary organizations active in disasters: `[Red Cross chapter, Salvation Army, church networks]`

## 11. Standing constraints the AI must respect

Write the honest version. This section prevents unusable recommendations more than any other.

- `[for example: no full-time PIO; the emergency manager writes all public messaging]`
- `[for example: fire response is entirely volunteer and thins sharply on weekday mornings]`
- `[for example: the county has no in-house GIS staff]`
- `[for example: overtime requires county board approval]`
- `[for example: shelter operations depend on a single church partner]`

## 12. Language for the model

```text
Do not invent road closures, shelter openings, gauge readings, outage counts, casualty
figures, damage estimates, or activation decisions. If a fact is not in this pack or in
the inputs I provide, write UNKNOWN and list it under Information Needed. Assume rural
constraints: volunteer response, long travel distances, and limited staffing.
```

---

## Maintenance log

| Date | Section changed | Changed by | Reason |
| --- | --- | --- | --- |
| | | | |
