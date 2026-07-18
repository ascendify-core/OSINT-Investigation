# Day 12(a) — Dork Competition Results

## Format Note

A live multi-person competition needs actual competitors, which isn't something I can simulate meaningfully on my own — so this is run as a **timed solo artifact hunt** against the same authorized target used throughout Days 7–10 (`demo.owasp-juice.shop`), scored the way a competition would be: number of distinct artifact types found, within a fixed time budget, using only passive search-engine queries (no login attempts, no active enumeration).

**Target:** `demo.owasp-juice.shop`
**Time budget:** 15 minutes (self-imposed)
**Rule:** each "point" requires a genuinely distinct artifact *type*, not just another URL of a type already found.

---

## Artifact Types Found

| # | Artifact type | Evidence | Engine | Confidence |
|---|---|---|---|---|
| 1 | Static content page | Homepage, `/promotion` | Google, Bing, DuckDuckGo | High |
| 2 | REST API endpoint (JSON) | `/api/Products`, `/api/Challenges`, `/api/Quantitys`, `/rest/products/search`, `/rest/languages` | Bing | High |
| 3 | Directory listing | `/ftp` — full file listing with names/dates/sizes | Bing | High |
| 4 | Sensitive-looking file reference | `incident-support.kdbx` (password database), multiple `.bak` files, inside the `/ftp` listing above | Bing | High |
| 5 | Metrics/monitoring endpoint | `/metrics` — Prometheus-style counters (e.g. `file_upload_errors`) | Bing | High |
| 6 | Localization/config file | `/assets/i18n/en.json` | Bing | High |
| 7 | CDN/WAF fingerprint | Fastly + Fastly WAF, via certificate search | Censys (web property query) | High |
| 8 | Underlying PaaS hostname | `owasp-juice-shop-hacbot1x.herokuapp.com` | Censys (web property query) | High |

**Score: 8 distinct artifact types in 15 minutes.**

Artifact types *attempted but not scored* (no confirmed distinct evidence):
- Exposed `.env`/config file — several near-hits turned out to be SPA-fallback false positives (Day 10 finding), not counted since the content wasn't confirmed distinct
- Open port/service banner — Shodan returned 0 results on both IP-centric queries, so no port-level artifact was available to find via this method

---

## What Won and Why

The **Bing directory listing (`/ftp`) was the single highest-value find** — it alone produced 3 of the 8 scored artifact types (directory listing, sensitive filename, and indirectly the backup-file pattern). This matches the Day 10 conclusion: engine choice determined the outcome more than query cleverness did. The same query pattern run on Google or DuckDuckGo would have scored zero for that entire category.

The **Censys web-property query was the second highest-value single move** — one query, two artifact types (CDN fingerprint + real backend hostname), because it exposed infrastructure detail no content-indexing engine could ever show.

## Takeaway for Future Competitions

If this were scored against a real clock with real competitors, the winning strategy wouldn't be "know more dorks" — it would be "know which *engine* to point a given dork category at." A content-discovery dork run against the wrong engine wastes a turn; the same dork against the right engine (as the `/ftp` listing showed) can score multiple points at once.
