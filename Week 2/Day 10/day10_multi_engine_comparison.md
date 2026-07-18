# Day 10 – Advanced Search Techniques
## Multi-Engine Comparison: Bing, DuckDuckGo, Shodan & Censys

**Target:** OWASP Juice Shop demo instance (`demo.owasp-juice.shop`) — a deliberately vulnerable web app used for security training.

**Goal:** Run the same investigation across multiple search engines/tools and compare what each surfaced that a plain Google search missed.

---

## Side-by-Side Findings

| Engine / Tool | What It Surfaced | Notes / Value Add |
|---|---|---|
| **Google (baseline)** | Standard indexed pages: homepage, promo video page, general project description. | Mostly marketing/informational content. Did not surface API endpoints, backend responses, or infrastructure data. |
| **Bing** | Indexed a PDF-style cached snapshot of the storefront (with wallet/bonus point details), plus the same general project description as Google. | Slightly different cache/crawl of the same public pages. No unique technical exposure found beyond what Google showed. |
| **DuckDuckGo** | Surfaced live JSON API responses: `/api/Products`, `/rest/products/search`, `/api/Challenges`, `/assets/i18n/en.json`, `/api/Quantitys`, `/rest/languages`, `/metrics`, and directory-style paths (`/assets`, `/.env`, `/assets/public`, `/assets/.env`, `/ftp`). | Far more useful than Google/Bing — indexed raw application endpoints and even an open FTP directory listing (with files like `announcement_encrypted.md`, `incident-support.kdbx`, `package-lock.json.bak`, `suspicious_errors.yml`). This is where real dorking value showed up. |
| **Shodan** | No results found for hostname or SSL certificate search on `owasp-juice.shop`. | Demo/training instance likely isn't in Shodan's scan index, or sits behind infrastructure Shodan hasn't fingerprinted. Shows Shodan is better suited to IP/port-level infrastructure recon than a single demo hostname. |
| **Censys** | Legacy query syntax was rejected as invalid, but Censys auto-suggested the equivalent modern query for both "Hosts" and "Web Properties" search modes. | Highlights that search tools evolve their query language over time — useful for certificate/host discovery once the correct syntax is used, but returned no confirmed live match in this run. |

---

## Tool Purpose — Quick Reference

| Tool | Best Used For |
|---|---|
| Google | Broadest general index; good starting point but often filters/deprioritizes raw technical content. |
| Bing | Alternate crawl/cache of the same web content; occasionally surfaces older cached snapshots Google has dropped. |
| DuckDuckGo | Less aggressive filtering of "unstructured" content — good for finding raw API responses, config files, and exposed directories via dorks. |
| Shodan | Internet-wide device/service/port scanning by IP or banner — built for infrastructure recon, not single-domain content discovery. |
| Censys | Certificate transparency and host/service fingerprinting — strong for mapping infrastructure once correct query syntax is used. |

---

## Key Takeaways

- **Google was the weakest for technical exposure.** It mostly indexed polished, human-facing pages (homepage, promo video) and filtered out raw API/JSON responses.
- **DuckDuckGo was the standout.** It indexed live API endpoints (`/api/Products`, `/api/Challenges`, `/rest/products/search`), config-style paths (`/.env`, `/assets/.env`), and even an open FTP directory listing containing sensitive-sounding files (`incident-support.kdbx`, `announcement_encrypted.md`, `suspicious_errors.yml`).
- **Bing behaved similarly to Google** but occasionally showed a different cached snapshot (e.g., a PDF-style cache of the storefront with wallet/bonus point info) — a reminder that different crawlers cache different moments in time.
- **Shodan and Censys** target infrastructure (IPs, ports, TLS certificates) rather than page content, and returned no confirmed results for this specific demo hostname — showing these tools shine more for infrastructure-level recon than single-site content discovery.
- **Censys' rejection of the legacy query syntax** — and its auto-suggested modern equivalents — is a good reminder to always check a tool's current query syntax before assuming "no results" means "nothing there."
- **Lesson for future recon:** no single engine tells the whole story. Content-focused engines (Google/Bing/DuckDuckGo) reveal different slices of the same crawl, while infrastructure engines (Shodan/Censys) answer a completely different question — what's running, not what's published.

---

## Conclusion

Running the same target through multiple engines showed clear differences in coverage. DuckDuckGo's willingness to index raw application data and directory listings gave far more actionable findings than Google or Bing for this target, while Shodan and Censys — built for infrastructure fingerprinting — needed no results at all for this hostname, or in Censys' case, needed the corrected query syntax to be useful. The main takeaway is to treat each tool as covering a different layer of the target's exposure, and never rely on a single engine for a complete picture.
