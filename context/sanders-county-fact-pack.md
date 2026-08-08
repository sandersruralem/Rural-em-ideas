# County Fact Pack — Sanders County, Montana

**Version:** 0.1 (research draft — public sources only; verify with the Emergency Manager before operational use)
**Owner:** Emergency Manager
**Data level:** Green only
**Review cycle:** Quarterly, and after any plan change, election, or reorganization
**Base template:** `context/county-fact-pack.md` (copy filled for Sanders County)

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
- **UNKNOWN is preferred to invention.** Gaps below must be filled from county plans or staff
  knowledge before this pack is treated as complete.

---

## 1. Basics

- County name: Sanders County, Montana
- County seat: Thompson Falls
- Population: approximately 14,062 (July 1, 2025 Census estimate); 12,400 (2020 Census)
- Land area: approximately 2,760 square miles (2020 Census land area); roughly 4.5 people per
  square mile
- Incorporated towns: Thompson Falls (city; county seat), Plains (town), Hot Springs (town)
- Unincorporated communities commonly referenced: Paradise, Trout Creek, Noxon, Heron, Dixon
  (Sčilíp), Lonepine, Belknap, Camas, Old Agency, Perma, White Pine, and other Highway 200 /
  reservation-side places
- Adjacent counties: Lincoln (north), Flathead (northeast), Lake (east), Missoula (southeast),
  Mineral (south); Shoshone County, Idaho (west); Bonner County, Idaho (northwest)
- Time zone: Mountain Time; observes daylight saving time. Western border is near the Idaho /
  Pacific Time line; Idaho counties west of the line are on Pacific Time

## 2. Geography and infrastructure references

- Major highways and routes: Montana Highway 200 (main east–west corridor along the Clark Fork,
  from Missoula County through Plains, Paradise, Thompson Falls, Trout Creek, Noxon, and Heron
  toward Idaho); Montana Highway 28 (Plains north toward Hot Springs and on to the Flathead /
  Lake County area); Montana Highway 135 (south from near Paradise toward St. Regis / Mineral
  County); Montana Highway 77 / Hot Springs Road (from MT 28 to Hot Springs)
- Rivers, creeks, and lakes: Clark Fork River (main stem through the county); Flathead River
  (joins the Clark Fork near Paradise / Perma area); Thompson River; Bull River; Noxon Reservoir
  (behind Noxon Rapids Dam); Cabinet Gorge Reservoir area near the Idaho line; numerous mountain
  tributaries and forest drainages
- Named river or stream gauges used by this office: Clark Fork near Plains (AHPS/NWRFC PLNM8;
  USGS 12389000) — action stage 15 ft, flood stage 16 ft, moderate 18 ft, major 19.5 ft
  (NWS WFO Missoula). Flathead River at Perma (AHPS/NWRFC PERM8; USGS 12388700) — monitored
  locally; published NWS flood-stage thresholds not listed on the NWRFC summary used for this
  draft. Confirm any additional office-preferred gauges (Thompson River, Bull River, dam
  outflows) with staff — UNKNOWN beyond the two above
- Rail lines and crossings of concern: BNSF Railway main line along the Clark Fork / Highway 200
  corridor (historically operated in part under Montana Rail Link arrangements). At-grade and
  corridor wildfire / hazmat exposure along the river valley is a known planning concern
- Airports or airstrips: Thompson Falls Airport (public, county); Plains Airport; Hot Springs
  Airport. Nearest larger commercial service commonly referenced: Missoula Montana Airport
  (roughly 90–100 miles east via Highway 200)
- Terrain notes: Narrow river valley (Clark Fork) between the Cabinet Mountains (north) and
  Coeur d'Alene / Bitterroot-range foothills (south); steep forested slopes; WUI (wildland–urban
  interface) housing along the valley and side drainages; eastern county includes parts of the
  Flathead Indian Reservation / Bison Range vicinity; precipitation and vegetation shift from
  wetter west (Heron / Cabinet country) to drier east (Dixon area)
- Areas with a single access route: Many side-canyon and ridge communities depend on one county
  or forest road off Highway 200. Western corridor communities (Trout Creek, Noxon, Heron) are
  highly dependent on Highway 200 remaining open. Thompson River / Snider / Copper King–type
  drainages have limited outbound routes during wildfire. Describe tactically only in internal
  plans — not here

## 3. Hazards

From the Western Montana Regional Hazard Mitigation Plan (Sanders County participation), overall
significance rankings for Sanders County, ordered here by local operational relevance rather than
plan section order:

| Hazard | Season | Typical local impact |
| --- | --- | --- |
| Wildfire | Summer–early fall (can extend) | Evacuations, Highway 200 closures, structure loss, smoke, resource draw on volunteer fire; High significance in regional HMP |
| Drought | Summer–fall; multi-year | Elevated fire danger, forage and water stress for agriculture and livestock; High significance |
| Flooding (riverine / runoff) | Spring snowmelt; also rain-on-snow or intense rain | Clark Fork and Flathead bottoms, roads/bridges, infrastructure; Medium significance. Dec 2025 local emergency declaration for landslide/flood risk |
| Severe winter weather | November–March | Closures on Highway 200 and mountain laterals, power outages, delayed EMS/fire |
| High wind / severe summer weather | Spring–fall | Tree-down power outages countywide, road blockage, fire weather (red flag) |
| Dam-related flooding / regulated flows | Year-round (rare catastrophic failure); spring operations | Thompson Falls Dam (NorthWestern Energy), Noxon Rapids Dam and Cabinet Gorge Dam (Avista). HMP dam-failure significance for Sanders rated Low, but downstream awareness remains relevant |
| Hazardous materials (rail / highway / fixed) | Year-round | BNSF corridor and Highway 200 truck traffic; Tier II facilities coordinated through LEPC |
| Communicable disease / public health | Year-round | Coordinated with Sanders County Public Health; Medium significance in HMP |
| Earthquake | Year-round (rare) | Low significance in HMP for Sanders |
| Landslide / slope failure | Wet seasons; after burns | Road and bridge threat in steep drainages; Low–Medium context; referenced in Dec 2025 emergency meeting |
| Avalanche | Winter–spring | Low significance for incorporated places; mountain recreation drainages |
| Volcanic ash | Rare | Low significance (Cascade ashfall scenario) |

Notes on past significant events, publicly reported:

- August 2023 — River Road East Fire near Paradise: roughly 17,000+ acres, multiple homes /
  structures lost, Highway 200 segment closures, evacuations; Red Cross shelter opened at Church
  on the Move in Plains. Origin near the rail corridor remains a matter of public litigation and
  investigation reporting — do not assert cause in AI products unless confirmed by official
  inputs
- Thorne Creek Fire (public reporting): evacuations near Thompson Falls (Snider / Copper King
  area); Red Cross evacuation center at Thompson Falls Community Center
- December 2025 — Board of County Commissioners emergency declaration for potential landslides
  and flooding during intense rain; coincided with broader northwest Montana flood disaster
  activity
- Winter wind events (publicly discussed by Emergency Management): multi-community power outages
- Historic Clark Fork high water at Plains gauge: record stage 19.17 ft / 134,000 cfs on June 5,
  1948 (NWRFC station summary)

## 4. Emergency management organization

- Office staffing: one Emergency Management Coordinator (Office of Emergency Management). Prior
  public HMP participant lists also referenced a deputy OEM role; confirm current deputy /
  part-time support with the office — UNKNOWN for current secondary staffing
- EOC location and type: publicly identified candidate locations include the county courthouse,
  a DNRC facility, and at least one additional site (third site not fully named in the public
  LEPC minutes reviewed). Public LEPC discussion has stated the EOC has never been activated.
  Confirm primary / alternate EOC and layout with staff before treating as final
- Activation levels used: UNKNOWN from published materials reviewed for this draft. Do not invent
  ICS or county-specific level names
- Who declares a local emergency: principal executive officer of the political subdivision under
  MCA 10-3-402 / 10-3-403 — in practice the Board of County Commissioners by order or resolution
  (recent examples: fire-season and flood-related resolutions)
- Who authorizes public messaging: Office of Emergency Management / Emergency Management
  Coordinator for EM alert and preparedness messaging; Sheriff's Office commonly issues
  evacuation orders and field public safety notices. Confirm PIO arrangement — no dedicated
  full-time PIO is described in public materials reviewed

## 5. Response resources, described generally

- Fire: on the order of eleven fire departments / rural fire districts countywide (HIFLD / public
  listings), predominantly volunteer (examples publicly named: Thompson Falls Volunteer / Rural,
  Plains Volunteer, Plains-Paradise Rural, Trout Creek Rural, Noxon Rural, Heron Rural, Hot
  Springs Volunteer, Dixon Rural). Exact roster counts and combination status: verify locally
- EMS: Plains Community Ambulance — nonprofit BLS/ALS service for the Plains area with mutual-aid
  reach across the county; interfacility transport to/from Clark Fork Valley Hospital. Additional
  EMS capability is associated with some fire departments. Countywide 24/7 ALS coverage pattern:
  confirm with EMS leadership — do not invent unit counts or response-time averages
- Law enforcement: Sanders County Sheriff's Office (Thompson Falls) covers unincorporated areas
  and supports towns; municipal police departments publicly listed in Thompson Falls, Plains, and
  Hot Springs; Montana Highway Patrol on Highway 200 and related corridors
- Dispatch: county 911 / PSAP coordinated from the Thompson Falls area (Sheriff's Office public
  non-emergency line published as 406-827-3584). Confirm whether dispatch is solely county or
  shared — public scanner references describe Sanders County 911 Dispatch in Thompson Falls
- Public works and road department: Sanders County Road Department maintains county roads;
  municipal public works in incorporated places; Montana Department of Transportation for state
  highways. Equipment classes and staffing levels: UNKNOWN from Green sources reviewed
- Hospital: Clark Fork Valley Hospital, Plains — 16-bed critical access hospital; affiliated
  Family Medicine Network clinics in Plains, Thompson Falls, and Hot Springs; hospital-managed
  long-term care with 28 beds. Regional referral commonly to Missoula-area facilities for higher
  acuity (drive time roughly 1.5–2 hours in good conditions)
- Public health: Sanders County Public Health (Thompson Falls; published main line 406-827-6931),
  including WIC and related programs
- Emergency management volunteers: CERT / ARES / auxiliary status UNKNOWN from sources reviewed.
  Search and rescue capacity historically referenced in public EM hiring coverage; confirm
  current SAR affiliation and activation path with the Sheriff's Office / OEM

## 6. Facilities used in emergencies

Publicly known facilities only. Shelter designations change by incident — treat the table as
historical / typical uses from public reporting, not a standing open-shelter list.

| Facility | Type | Typical role |
| --- | --- | --- |
| Thompson Falls Community Center | Community center | Evacuation / Red Cross reception (used in Thorne Creek Fire reporting) |
| Church on the Move, Plains | Church | Evacuation shelter / Red Cross (used in River Road East Fire reporting); food bank ministry adjacent |
| Sanders County Fairgrounds, Plains (30 River Road) | Fairgrounds | Staging, large-animal / camping capacity; county has discussed emergency-use planning for the grounds |
| Clark Fork Valley Hospital campus, Plains | Hospital / LTC | Medical surge, continuity of care; not a general public shelter |
| Local schools (Thompson Falls, Plains, Hot Springs, Noxon, and other public schools) | Schools | Potential shelter / reunification — confirm MOUs before naming as open |
| Senior / community centers (Thompson Falls, Plains/Paradise, Trout Creek, Noxon, Heron, Hot Springs, Dixon) | Senior / community centers | Warming / cooling / information points when designated |

Notes: Generator availability, ADA detail, and capacity ranges for most facilities are UNKNOWN
from Green sources reviewed. Do not invent generator or bed counts.

## 7. Public warning and information channels

- Mass notification system: Hyper-Reach (county emergency notification). Community signup page
  linked from county Emergency Management; call-in signup number published on the county site as
  406-203-0082. Local reporting also describes texting "Alert" to a Hyper-Reach short code /
  number — confirm the current signup path on the county website before publishing instructions
- Alert character limit: UNKNOWN (confirm Hyper-Reach SMS vs. app/email limits with the vendor
  settings used by the county). Draft SMS as short and actionable
- Outdoor warning sirens: UNKNOWN / no countywide outdoor siren system identified in sources
  reviewed. Do not assume siren coverage
- County website: https://www.co.sanders.mt.us/ (Emergency Management:
  https://www.co.sanders.mt.us/202/Emergency-Management; Plans:
  https://www.co.sanders.mt.us/253/Plans)
- Official social media: Sanders County Emergency Management (Facebook); Fire Information–Sanders
  County (Facebook), per public EM outreach reporting. Confirm current official account names
  before directing the public
- Local radio: limited local over-the-air service. Publicly referenced options include KPLG 91.5
  FM (Plains translator / religious network) and regional country AM KERR 750 (Polson — Montana
  EAS primary entry point). A short-range Clark Fork River Radio effort in Plains has been
  reported; treat current status as UNKNOWN. Rely on Hyper-Reach and official social first
- Local newspaper: Sanders County Ledger (local coverage); Valley Press / Mineral Independent
  also covers county EM topics
- Regional television: Missoula market stations commonly carry Sanders County incidents (e.g.,
  KPAX and other Missoula news outlets)
- Official public contact point: Emergency Management published contacts via county directory /
  department page (coordinator office line published on the EM page; directory also lists
  Emergency Management at 406-827-6955). Sheriff non-emergency 406-827-3584. For life-threatening
  emergencies: 911
- Public information authority: Emergency Management Coordinator for EM/public alert messaging;
  Sheriff's Office for evacuations and law-enforcement notices; Board of County Commissioners for
  formal emergency/disaster declarations

## 8. Population considerations

Described in aggregate only. Never list individuals.

- Age profile: markedly older than the U.S. average — about 33–34% of residents are 65 and over
  (Census QuickFacts / 2020 Census age shares); median age around mid-50s
- Long-term care and assisted living facilities: Clark Fork Valley Hospital long-term care
  (Plains, 28 beds publicly stated by the hospital); Hot Springs Health & Rehabilitation;
  assisted living / adult foster care publicly listed in Thompson Falls and Plains (e.g., Cherry
  Hills Assisted Living, Mount Silcox Adult Foster Care, Mountain View Manor). Exact licensed
  bed totals beyond CFVH LTC: confirm with Public Health / DPHHS listings
- Residents dependent on electrically powered medical equipment: UNKNOWN aggregate count. Office
  has publicly discussed interest in building a special-needs database — do not invent numbers
- Households without reliable broadband or cell coverage: Census QuickFacts (2020–2024) —
  about 87.8% of households have a broadband subscription and 92.9% have a computer, implying
  roughly one in eight households without broadband. Cell coverage is widely described as patchy
  outside town centers and in mountain drainages
- Transportation-limited households: rural distances, limited public transit (Sanders County
  Public Transportation; CSKT Transit on the Flathead Reservation). Exact no-vehicle household
  share: confirm from ACS tables before stating a percentage
- Agricultural population and livestock operations: meaningful farm and ranch sector (hay and
  livestock oriented); agriculture, forestry, fishing, and hunting remain a top employment sector
- Seasonal population swings: summer recreation and reservoir tourism; hunting seasons; Sanders
  County Fair in Plains; huckleberry season / Trout Creek area events; temporary wildfire /
  incident personnel during large fires

## 9. Agriculture and economy

- Primary crops and livestock: hay and forage; cattle and other livestock; limited specialty
  crops. Forestry and related wood products are economically important alongside agriculture
- Grain storage, feedlots, dairies of note: no large industrial feedlot complex identified in
  Green sources reviewed; operations are generally dispersed ranch/farm scale
- Major employers (general): Clark Fork Valley Hospital and clinics; K–12 school districts;
  county government; hydroelectric operators (Avista; NorthWestern Energy at Thompson Falls Dam);
  retail and accommodation/food services along Highway 200; construction; agriculture and
  forestry employers
- Facilities with hazardous materials reporting obligations: LEPC coordinates Tier II reporting
  (public minutes reference facilities such as Cabinet-area sites and utility partners). List
  specifics only from current Tier II / E-Plan extracts held by the LEPC — not invented here

## 10. Mutual aid and partners

- Mutual aid agreements in place: fire mutual aid among county departments and with neighboring
  jurisdictions (exact agreement inventory UNKNOWN in this draft); EMS mutual aid extending
  Plains Community Ambulance coverage; law-enforcement cooperation with municipal PD and MHP
- Regional or district emergency management structure: participant in the Montana Western Region
  Hazard Mitigation Plan coordinated by Montana Disaster and Emergency Services (MT DES). State
  coordination path is through MT DES / State Emergency Coordination Center when activated
- State emergency management contact path: Montana DES (state duty officer / SECC process) —
  use current DES published duty procedures; do not embed personal cell numbers
- Tribal, federal, or military installations nearby: Confederated Salish and Kootenai Tribes
  (Flathead Reservation includes eastern Sanders County communities); USDA Forest Service (Lolo,
  Kootenai / Kaniksu areas); Montana DNRC; Bison Range (part); no major military installation
  inside the county identified for this draft
- Voluntary organizations active in disasters: American Red Cross (sheltering in recent fires);
  church and food-bank networks (e.g., Church on the Move / Plains Community Food Bank);
  Sanders County Council on Aging and senior-center network; LEPC partners including hospital
  emergency planning staff

## 11. Standing constraints the AI must respect

Write the honest version. This section prevents unusable recommendations more than any other.

- Very large geography (~2,760 sq mi land) with a small population and low density; travel times
  between Heron and Dixon are long even in good weather
- Fire response is predominantly volunteer and will thin on weekday mornings and during drawdown
  to large wildfires
- Highway 200 is the spine of the county; a closure can isolate western communities and disrupt
  EMS, fuel, and supply
- Cell and broadband gaps limit mass-notification reach; Hyper-Reach enrollment has been publicly
  described as far below county population
- No dedicated full-time PIO identified in public materials; EM coordinator and Sheriff's Office
  carry most public messaging
- EOC activation is rare to nonexistent historically; do not assume a standing EOC battle rhythm
- Critical access hospital only (16 beds); higher-acuity care requires out-of-county transport
- Rail and hydroelectric infrastructure create specialized hazmat / dam-awareness needs beyond
  typical rural counties
- Eastern county includes Flathead Reservation communities — coordination with CSKT is required
  for incidents affecting tribal lands or residents
- Winter storms, wildfire smoke, and wind-driven outages can coincide with fragile volunteer
  staffing
- Activation levels, full shelter MOU list, road-department plow counts, and special-needs
  registry totals are not fully documented in this Green draft — mark UNKNOWN rather than guess

## 12. Language for the model

```text
Do not invent road closures, shelter openings, gauge readings, outage counts, casualty
figures, damage estimates, or activation decisions. If a fact is not in this pack or in
the inputs I provide, write UNKNOWN and list it under Information Needed. Assume rural
constraints: volunteer response, long travel distances, and limited staffing. Treat
Highway 200 corridor continuity, wildfire evacuation, and Clark Fork / Flathead river
conditions as first-order local concerns when relevant. Prefer roles (Emergency Management
Coordinator, Sheriff, Board of County Commissioners, Fire Chief) over personal names.
```

---

## Maintenance log

| Date | Section changed | Changed by | Reason |
| --- | --- | --- | --- |
| 2026-08-08 | All sections (initial research draft) | Cloud agent research pass | First filled copy for Sanders County from public Green sources; pending EM verification |

---

## Sources used

All material above was drawn from publicly available Green sources. No non-public plans, CAD
data, or personally identifying details were used. URLs and titles as retrieved during research
(August 2026):

### Official county and state

1. Sanders County official website — https://www.co.sanders.mt.us/
2. Sanders County Emergency Management — https://www.co.sanders.mt.us/202/Emergency-Management
3. Sanders County Plans (EOP / RHMP / CWPP) — https://www.co.sanders.mt.us/253/Plans
4. Sanders County Staff Directory — https://www.co.sanders.mt.us/Directory.aspx
5. Sanders County Sheriff's Office — https://www.co.sanders.mt.us/212/Sheriffs-Office
6. Sanders County Airports — https://www.co.sanders.mt.us/194/Airports
7. Sanders County Fair / Fairgrounds — https://www.co.sanders.mt.us/200/County-Fair ;
   https://www.sanderscountyfair.com/facility-rentals
8. Sanders County Board of Commissioners minutes — Emergency Declaration Resolution 2025-28
   (Dec 8, 2025) — https://www.co.sanders.mt.us/AgendaCenter/ViewFile/Minutes/_12082025-178
9. Sanders County Commissioners minutes — OEM / fire declaration discussion (Jul 22, 2024) —
   https://www.co.sanders.mt.us/AgendaCenter/ViewFile/Minutes/_07222024-72
10. Sanders County LEPC minutes (Feb 12, 2026) —
    https://www.co.sanders.mt.us/AgendaCenter/ViewFile/Minutes/_02122026-198
11. Sanders County floodplain regulations (2016 revisions PDF) —
    https://co.sanders.mt.us/DocumentCenter/View/312/2016-Floodplain-Revisions-PDF
12. Montana Code Annotated 10-3-402 (local emergency declaration) —
    https://mca.legmt.gov/bills/mca/title_0100/chapter_0030/part_0040/section_0020/0100-0030-0040-0020.html
13. Montana Association of Counties — Guide for using model emergency proclamation / disaster
    declaration templates —
    https://www.mtcounties.org/wp-content/uploads/resources/model-policies-regulations-codes/guide-using-model-emergency-proclamation-disaster-declaration.pdf
14. Montana Disaster and Emergency Services — Western Montana Regional Hazard Mitigation Plan
    (FINAL, Oct 29, 2024), including Sanders County participation / risk rankings —
    https://des.mt.gov/Mitigation/Montana-Western-Region-Hazard-Mitigation-Plan-10.29.24-FINAL.pdf
15. Montana DES — Western Region base / related HMP PDF —
    https://des.mt.gov/mitigation/MT-Western-Region-Base-Plan-08.14.24.pdf

### Federal demographic, hydrologic, and aviation

16. U.S. Census Bureau QuickFacts: Sanders County, Montana —
    https://www.census.gov/quickfacts/sanderscountymontana
17. U.S. Census Bureau population / land-area figures as cited via QuickFacts and related Census
    products (2020 Census; July 1, 2025 estimate)
18. NOAA / NWRFC — Clark Fork near Plains (PLNM8) station summary (stages and record) —
    https://www.nwrfc.noaa.gov/river/station/flowplot/flowplot.cgi?PLNM8=
19. USGS NWIS — Clark Fork near Plains MT (12389000) —
    https://waterdata.usgs.gov/nwis/uv/?site_no=12389000
20. NOAA / NWRFC — Flathead River at Perma (PERM8) —
    https://www.nwrfc.noaa.gov/river/station/flowplot/flowplot.cgi?PERM8=
21. USGS NWIS — Flathead River at Perma MT (12388700) —
    https://waterdata.usgs.gov/nwis/uv/?site_no=12388700
22. AirNav — Thompson Falls Airport (KTHM) — http://www.airnav.com/airport/THM

### Local health, EMS, aging, and facility references

23. Clark Fork Valley Hospital — https://www.cfvh.org/
24. Plains Community Ambulance — https://www.plainsambulance.org/
25. Western Montana Area VI Agency on Aging — Sanders County Resources —
    https://www.westernmontanaagingservices.org/sanders-county-resources/
26. Montana State University Extension — Sanders County “need help?” resource sheet —
    https://www.montana.edu/extension/sanders/need%20help.pdf
27. MSU Extension / Ag Impact — Sanders County agriculture profile PDF —
    https://www.montana.edu/extension/agimpact/reports/sanders.pdf
28. Plains Community Food Bank / Church on the Move — https://www.plainsfoodbank.org/
29. Montana Courts self-help — Sanders County Resource Guide PDF —
    https://courts.mt.gov/external/selfhelp/resources/sanders.pdf

### News and contemporary incident reporting (used for publicly reported events and channels)

30. Sanders County Ledger — “County urges preparedness with smoke, fires” (Aug 6, 2026) —
    https://www.scledger.net/story/2026/08/06/news/county-urges-preparedness-with-smoke-fires/14123.html
31. Sanders County Ledger — “County declares flooding emergency” (Dec 11, 2025) —
    https://www.scledger.net/story/2025/12/11/news/county-declares-flooding-emergency/13165.html
32. Sanders County Ledger — “Sanders County radio station goes live” (Jul 11, 2024) —
    https://www.scledger.net/story/2024/07/11/news/sanders-county-radio-station-goes-live/11028.html
33. Valley Press / Mineral Independent — “New coordinator hired for Office of Emergency
    Management” (Apr 29, 2026) —
    https://vp-mi.com/news/2026/apr/29/new-coordinator-hired-for-office-of-emergency-management/
34. KPAX — “Wildfire evacuations ordered in Sanders County” (Thorne Creek / Community Center) —
    https://www.kpax.com/news/firewatch/evacuations-ordered-in-sanders-county
35. NBC Montana / related reporting — River Road East Fire closures and shelter references —
    https://nbcmontana.com/weather/wildfires/hwy-200-partial-closure-due-to-river-road-east-fire
36. Montana Public Radio — River Road East Fire / rail lawsuit coverage —
    https://www.mtpr.org/montana-news/2023-11-17/lawsuit-claims-fire-near-paradise-was-started-by-a-railcar
37. Daily Inter Lake — state joins River Road East Fire lawsuit (May 3, 2026) —
    https://dailyinterlake.com/news/2026/may/03/state-joins-lawsuit-blaming-railroads-for-2023-wildfire/
38. InciWeb / Northern Rockies fact sheet — River Road East Fire (Sep 1, 2023 PDF) —
    https://inciweb-prod-media-bucket.s3.us-gov-west-1.amazonaws.com/s3fs-public/2023-09/09012023_River%20Road%20East%20Fire%20Fact%20Sheet_final.pdf

### Reference / encyclopedia and secondary geographic context

39. Wikipedia — Sanders County, Montana — https://en.wikipedia.org/wiki/Sanders_County,_Montana
40. Wikipedia — Noxon Rapids Dam — https://en.wikipedia.org/wiki/Noxon_Rapids_Dam
41. Wikipedia — KERR (AM) — https://en.wikipedia.org/wiki/KERR
42. Wikipedia / highway references — Montana Highway 28 routing (Plains–Elmo)
43. Data USA — Sanders County, MT industry profile —
    https://datausa.io/profile/geo/sanders-county-mt
44. World Population Review — Sanders County / cities pages (cross-check only; Census preferred)
45. plainfiredata.com — Fire Departments in Sanders County, MT (HIFLD-derived department count) —
    https://plainfiredata.com/county/30089
46. Tour200 / regional tourism pages — Highway 200 corridor orientation (non-authoritative
    geography cross-check) — https://tour200.com/
47. NorthWestern Energy — Thompson Falls Hydroelectric Project pre-application / project
    description materials (dam ownership / location context)
48. FCC / radio station listings — KPLG 91.5 Plains; KERR 750 Polson public file references
49. Hyper-Reach community signup (linked from county EM page) —
    http://hyper-reach.com/mtsanderssignup.html

### Research notes / limitations

- The county Emergency Operations Plan PDF linked from the Plans page was not fully extracted in
  this pass; activation levels, formal shelter MOUs, and some resource counts remain UNKNOWN
  pending EM review of that document.
- Personal names of staff appear in some public news and minutes; this fact pack intentionally
  uses roles only.
- Litigation reporting about fire origin is cited only as public controversy context; AI outputs
  must not assert causation unless an official input says so.
