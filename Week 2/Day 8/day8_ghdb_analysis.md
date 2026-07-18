# Day 8 — GHDB Analysis

## Target

**demo.owasp-juice.shop** — OWASP's official public demo instance of Juice Shop, an intentionally vulnerable web application maintained specifically for security training, CTFs, and tool-testing. OWASP's own documentation states it can be used as a "guinea pig" for security scanners, which is what makes it appropriate to test directly, unlike a real, unauthorized company.

A methodology note before the findings: the web-search tool used here does not reliably enforce literal Google boolean operators the way Google Search itself does — `site:` + `intitle:` + `intext:` combinations often returned thematically related pages (official docs, third-party writeups) rather than strictly filtered live-indexed results from the target domain. This is flagged explicitly in each finding below rather than smoothed over, since knowing the limits of your tooling is itself part of doing OSINT honestly.

---

## Queries Used

| # | Category | Dork | What it was meant to surface |
|---|---|---|---|
| 1 | Pages Containing Login Portals | `site:demo.owasp-juice.shop inurl:login` | A discoverable login page indexed at a predictable URL path |
| 2 | Pages Containing Login Portals | `site:demo.owasp-juice.shop intitle:"login"` | Login-titled pages indexed by search engines |
| 3 | Sensitive Directories | `site:demo.owasp-juice.shop inurl:ftp` | An exposed, browsable directory not meant to be public |
| 4 | Sensitive Directories | `site:demo.owasp-juice.shop intitle:"index of"` | Misconfigured directory listing (Apache/Nginx-style auto-index) |
| 5 | Files Containing Juicy Info | `site:demo.owasp-juice.shop filetype:bak` | Leftover backup files exposing source or config data |
| 6 | Files Containing Juicy Info | `site:demo.owasp-juice.shop ext:json intext:"password"` | JSON responses/files leaking credential-shaped fields |
| 7 | Error Messages | `site:demo.owasp-juice.shop intext:"SQLITE_ERROR"` | Database error leakage revealing schema/engine details |
| 8 | Error Messages | `site:demo.owasp-juice.shop intext:"stack trace"` | Server stack traces exposing internal file paths and framework internals |
| 9 | Web Server Detection | `site:demo.owasp-juice.shop intext:"Express" OR intext:"Node.js"` | Fingerprinting the backend framework/runtime |
| 10 | Sensitive Online Shopping Info | `site:demo.owasp-juice.shop inurl:api intext:"Bearer"` | Exposed API endpoints leaking authentication tokens |

---

## Findings

### High-confidence (directly observed via search results)

- **`/api/Challenges` endpoint is indexed.** A search-engine result returned `https://demo.owasp-juice.shop/api/Challenges` directly — a REST API endpoint that dumps the full list of configured hacking challenges, including names, categories, and hints, in JSON. This is intentional-by-design for Juice Shop (it's meant to power CTF integrations), but it's a good real-world illustration of an API endpoint search engines will index if nothing blocks crawling of `/api/`.
- **`/promotion` page is indexed** — a marketing video page, low sensitivity, but confirms the search engine has crawled beyond the homepage.
- **The application's underlying stack is publicly documented, not just guessable.** OWASP's own companion guide and multiple independent write-ups confirm the stack (Node.js, Express, Angular, SQLite via Sequelize) — this matches what query #9 was designed to surface, though the confirmation here came from official documentation rather than a live indexed error page.

### Inferred (documented behavior, not confirmed as currently search-indexed)

- **SQLite error leakage (queries #7, #8) is a real, confirmed feature of the app** — OWASP's own companion guide and an independent third-party penetration test report (Secure Ideas) both document that malformed input triggers raw `SQLITE_ERROR` messages and stack traces containing internal file paths and SQL query text. I could not confirm these specific error pages are currently sitting in the search engine's index — this class of content is normally only reached by *triggering* the error yourself (e.g., submitting a crafted search query), not by browsing to a static URL, so it wouldn't typically get crawled and indexed passively.
- **The `/ftp/` directory and backup files (queries #3, #4, #5) are real, intentional vulnerabilities**, confirmed in official documentation — files like `package.json.bak` and `coupons_2013.md.bak` are deliberately placed there as challenge content. Again, no confirmation these are currently indexed by a search engine; they're reachable by direct URL guessing, which is a different exposure path than search-engine discovery.
- **Query #10 (Bearer token exposure)** did not surface anything from the live target itself. It did surface a Bearer token in a *third party's* blog post (a walkthrough gist demonstrating their own captured token from a personal local test instance) — this is not an exposure of the live demo target, just a reminder that write-ups about a vulnerable app can themselves leak token-shaped strings if copied carelessly.

### Not found / no evidence either way

- Queries #1, #2, and #6 returned no results specific to the target — login pages in this app are client-side Angular routes (`/#/login`), which typically aren't indexed as separate crawlable pages the way server-rendered login pages are, since everything after `#` is invisible to the server and often to crawlers.

---

## What I Deliberately Didn't Pursue, and Why

- **No login attempts, credential guessing, or SQL injection strings submitted** — even against an explicitly authorized training target, the Day 7/8 scope stayed at search-engine reconnaissance only (what's discoverable *without* interacting with the app). Actually triggering the documented SQL error pages, or logging into the admin panel, is the next phase of Juice Shop's own training curriculum and is outside "search-engine exposure" as a topic.
- **No dorking against real, unauthorized targets** — the original Day 7 and Day 8 prompts suggested testing against a previously investigated real company or "generic public scope." Both were declined for the same reason: running exposure-hunting dorks (index-of, exposed configs, login panels) against real infrastructure without the owner's authorization is security reconnaissance, not OSINT, regardless of framing as coursework.
- **No attempt to bypass Juice Shop's client-side routing to force-index hidden Angular routes** — doing so would blur the line between passive search-engine reconnaissance (the stated topic) and active enumeration, which is a different technique with different authorization norms even against an authorized target.

---

## What This Reveals About the Target's Search-Engine Exposure

Overall, `demo.owasp-juice.shop`'s search-engine footprint is fairly shallow: a homepage, a promotion page, and one REST API endpoint were the only content confirmed as indexed. Its most interesting intentional vulnerabilities (SQLite error leakage, the `/ftp/` backup directory, the Angular-routed login/admin panels) are **reachable by direct interaction or URL-guessing, but not by passive search-engine discovery** — because they either require triggering an error condition or sit behind client-side routing that crawlers don't naturally traverse.

The general lesson: a modern single-page application (Angular/React/Vue-style, hash- or client-routed) is often *less* exposed to passive Google dorking than an older server-rendered site would be, simply because there are fewer discrete, crawlable URLs for a search engine to index in the first place. That doesn't mean it's more secure — the vulnerabilities are still there — it just means Google dorking specifically (as opposed to active scanning/crawling tools like `dirsearch`, which several of the write-ups referenced above used instead) is a weaker reconnaissance method against this particular architecture.
