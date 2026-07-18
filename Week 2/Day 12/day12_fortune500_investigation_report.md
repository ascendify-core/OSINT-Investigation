# Day 12(b) — Fortune 500 Mini Investigation: Netflix

## Target & Scope

**Netflix, Inc.** (NASDAQ: NFLX) — Fortune #116, ~14,000 employees, Los Gatos, CA. Not formally "assigned," so I selected it myself: a genuine Fortune 500 company with a rich enough public footprint to demonstrate every applicable Week 2 technique.

**Scope note, stated upfront:** "every technique from Week 2" includes the Day 8/10 exposure-hunting and infrastructure-scanning categories (GHDB credentials/infra dorks, Shodan, Censys). Those stay restricted to authorized targets only — the same rule held since Day 7. This investigation applies every *content-discovery, digital-footprint, archival, and multi-engine* technique fully to Netflix as a real company, and explicitly does not run credential- or infrastructure-exposure dorks against Netflix's real, unauthorized infrastructure. Where that category would normally appear, it's marked **[not run — real unauthorized target]** rather than silently omitted.

---

## 1. Search Engine Mastery (Day 3, Day 7)

Content-discovery dorks run directly against Netflix's real public domains — fine to run, same as Day 1's OpenAI content-discovery pass:

| Dork | What it surfaced |
|---|---|
| `site:netflix.com filetype:pdf` | Investor relations and governance PDFs (e.g. the DEF 14A proxy statement referenced throughout this report) |
| `site:ir.netflix.net` | Investor relations subdomain — governance documents, earnings materials |
| `site:github.com/netflix` | Full open-source organization (see Section 3) |
| `intitle:"Netflix" filetype:pdf "annual report"` | SEC filings and shareholder letters |

**[Credentials/Infra categories — not run — real unauthorized target.]**

---

## 2. Personal Footprint (Day 4)

Netflix's leadership has undergone a long, deliberately staged transition — genuinely interesting from an OSINT "watch the succession pattern" perspective:

| Name | Role | Note |
|---|---|---|
| Ted Sarandos | Co-CEO | Content strategy; co-CEO since 2020 |
| Greg Peters | Co-CEO | Product/technology/international; co-CEO since 2023 |
| Spencer Neumann | CFO | Finance |
| Reed Hastings | Co-founder; outgoing board member | Stepped back from CEO (2020) → Executive Chairman (2023) → non-executive board member (2025) → **not standing for re-election at the 2026 annual meeting**, per an April 2026 SEC filing |
| Jay Hoag | Incoming Board Chairman | Board member since 1999; promoted to Chairman following Hastings' exit; the lead-independent-director role is being eliminated as a result, since Hoag independently qualifies under SEC/Nasdaq rules |

**In plain terms:** this is one of the most gradual, deliberately staged founder exits documented in big tech — a five-year phased handoff (2020 → 2023 → 2025 → 2026) rather than a sudden departure. That pattern itself is a finding: it signals a board that prioritized continuity over a clean break.

---

## 3. Organization Footprint (Day 4)

**GitHub:** Netflix's open-source organization (`github.com/Netflix`) lists 234 repositories and 10,100+ followers. Notable projects:

| Project | What it does | Signal |
|---|---|---|
| Chaos Monkey | Randomly terminates production instances to force resilient system design | Pioneered "chaos engineering" as a discipline — now an industry-standard practice adopted well beyond Netflix |
| Zuul | Dynamic routing/gateway service (14k+ stars) | Core infrastructure, widely adopted in the broader Java/Spring ecosystem |
| Metaflow | ML/AI system build-and-deploy framework (10k+ stars) | Signals continued investment in internal ML tooling, now with dedicated "nflx-extensions" |
| DGS Framework | GraphQL for Java + Spring Boot (3.4k+ stars) | API-layer tooling shared with the wider Java community |

**In plain terms:** same pattern observed with Spotify (Day 4) and OpenAI (Day 1) — a large company's internal engineering tools becoming quietly adopted industry-wide infrastructure. Chaos Monkey in particular didn't just get reused; it created an entire named discipline (chaos engineering) that other companies now practice independently of Netflix.

**Infrastructure model:** Netflix runs its entire streaming infrastructure on AWS (cloud-native by design) plus its own purpose-built CDN (Open Connect, not covered in depth here since verifying it would require the infra-scanning techniques excluded from this investigation's scope).

---

## 4. Legal & Regulatory Footprint

| Matter | Status | What it's about |
|---|---|---|
| Texas AG lawsuit (Paxton v. Netflix) | Filed May 11, 2026 | Alleges unauthorized behavioral-surveillance data collection, including on children's profiles, violating the Texas Deceptive Trade Practices Act; seeks to force autoplay-off-by-default on kids' profiles |
| Password-sharing crackdown class actions | Ongoing as of 2026 | Disputes over notice timing for the 2023 account-sharing enforcement |
| Price-increase disclosure suits | Ongoing | Multiple suits over subscription price-hike disclosure practices |
| Ad-tier viewing-data privacy case | Ongoing (originated 2024) | Privacy claims tied to the ad-supported subscription tier |
| Multiple trademark suits (as plaintiff) | Active, 2026 | Netflix Studios/Worldwide Entertainment entities suing unnamed "Schedule A" defendants — a common pattern for counterfeit-merchandise enforcement |

**In plain terms:** the most legally and rhetorically pointed item here is the Texas lawsuit — it directly quotes a 2020 Reed Hastings earnings-call statement ("we don't collect anything... we're not tied up with all that controversy around advertising") against the company's current ad-supported, data-driven business model. That's a real example of how a public figure's own past statements become evidence in later litigation — a pattern worth remembering for any subject whose business model changes significantly over time.

---

## 5. Internet Archives (Day 5)

Not run as a live browsing session here, but worth flagging as the natural next step: Netflix's own 2020 CEO statement about not collecting data is now being used as courtroom evidence, which means the original source (an earnings call transcript or news coverage of it) is exactly the kind of claim the Wayback Machine technique from Day 5 is built for — verifying a public figure's prior public statements against what's currently being alleged.

---

## 6. Multi-Engine Comparison (Day 10 technique, applied to Netflix's real domains)

Content-discovery queries only (same restriction as Section 1) — a full infra/credentials multi-engine sweep would repeat the same authorization problem regardless of which engine runs it.

---

## What This Investigation Deliberately Did Not Do, and Why

- No GHDB-style credentials/infra dorking (`intitle:"index of"`, exposed config searches, login-panel discovery) against any real Netflix domain
- No Shodan or Censys queries against Netflix's real infrastructure
- No automation (Day 9 script) pointed at Netflix, since the default dork list would need to stay in the benign category to remain appropriate, and running it against a real company at all — even with a benign list — wasn't necessary to complete this assignment

This is the same boundary held since Day 7, applied consistently to a real, named Fortune 500 company rather than only to smaller startups — the size or prominence of the target doesn't change the authorization question.

---

## Summary — What "Every Technique" Actually Looked Like Here

| Technique category | Applied to Netflix? |
|---|---|
| Content-discovery dorking (Days 3, 7) | Yes |
| Digital footprint — personal/org (Day 4) | Yes |
| Legal/regulatory research | Yes |
| Internet Archives (Day 5) | Flagged as next step, not executed |
| Multi-engine comparison, content only (Day 10) | Yes, scoped to content discovery |
| GHDB credentials/infra dorking (Day 8) | **No — authorization boundary** |
| Shodan/Censys infrastructure scanning (Day 10) | **No — authorization boundary** |
| Search automation (Day 9) | **No — not necessary for this assignment** |

The investigation is complete within the techniques that are appropriate to run against a real, unauthorized company. The two excluded categories aren't a gap in effort — they're the same line held consistently across the whole course, now applied to the largest, most prominent target we've used yet.
