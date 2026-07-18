# Day 11 -- Personal Dork Playbook

Author: \<Your Name\>\
Date: July 2026

------------------------------------------------------------------------

## Purpose

This playbook consolidates all search operators, techniques, workflows,
and lessons from Days 3--10 into a single searchable reference.

Everything here is intended for:

-   Passive OSINT
-   Publicly indexed information
-   Authorized security research
-   Ethical reconnaissance

It intentionally excludes exploitation, authentication attempts,
credential harvesting, or unauthorized testing.

------------------------------------------------------------------------

# Quick Navigation

1.  Basic Operators
2.  File Discovery
3.  Documentation Search
4.  Research Search
5.  Recon
6.  Files
7.  Credentials
8.  Infrastructure
9.  Internet Archives
10. Search Automation
11. Personal Workflow
12. Tag Reference
13. Ethics

------------------------------------------------------------------------

# 1. Basic Operators

  Operator      Purpose                        Example
  ------------- ------------------------------ -------------------------------------
  `site:`       Search one website             `site:example.com`
  `filetype:`   Find specific document types   `filetype:pdf`
  `intitle:`    Search page titles             `intitle:"whitepaper"`
  `inurl:`      Search URL paths               `inurl:docs`
  `intext:`     Search page text               `intext:"machine learning"`
  `cache:`      View cached page               `cache:example.com`
  `related:`    Find similar sites             `related:github.com`
  `*`           Wildcard                       `site:example.com * tutorial`
  `-`           Exclude results                `site:example.com -site:github.com`
  `AROUND(X)`   Nearby terms                   `"React Email" AROUND(5) SDK`

------------------------------------------------------------------------

# 2. File Discovery

## PDFs

-   `filetype:pdf "annual report"`
-   `filetype:pdf "financial statement"`
-   `filetype:pdf "whitepaper"`
-   `filetype:pdf "market research"`

## Excel / CSV

-   `filetype:xlsx budget`
-   `filetype:xlsx "sales report"`
-   `filetype:csv dataset`

## Government

-   `site:*.gov filetype:pdf`
-   `site:*.gov.in filetype:pdf`
-   `site:*.gov.uk filetype:pdf`
-   `site:europa.eu filetype:pdf`
-   `site:un.org filetype:pdf`

------------------------------------------------------------------------

# 3. Documentation Search

-   `site:example.com inurl:docs`
-   `site:example.com filetype:pdf documentation`
-   `site:example.com intitle:guide`
-   `site:example.com SDK`
-   `site:example.com API`

------------------------------------------------------------------------

# 4. Research Search

-   `site:arxiv.org`
-   `site:scholar.google.com`
-   `site:researchgate.net`
-   `filetype:pdf "systematic review"`
-   `filetype:pdf "conference proceedings"`
-   `intitle:thesis cybersecurity`

------------------------------------------------------------------------

# 5. Recon

-   `site:target.com`
-   `site:target.com inurl:blog`
-   `site:target.com "2025"`
-   `site:target.com "press release"`
-   `site:target.com filetype:pdf`
-   `site:target.com careers`

------------------------------------------------------------------------

# 6. Files

-   PDF
-   XLSX
-   CSV
-   DOC
-   PPT

Examples:

-   `filetype:pdf`
-   `filetype:xlsx`
-   `site:company.com filetype:pdf`

------------------------------------------------------------------------

# 7. Credentials

Safe searches only:

-   `site:example.com authentication`
-   `site:example.com OAuth`
-   `site:example.com SSO`
-   `site:example.com API key documentation`

**Avoid:** searching for passwords, secrets, private keys, or leaked
databases.

------------------------------------------------------------------------

# 8. Infrastructure

  Tool         Best For
  ------------ ----------------------------------------
  Google       Public webpages & documentation
  DuckDuckGo   APIs, config paths, directory listings
  Bing         Alternate cache
  Shodan       Internet-facing services
  Censys       Certificates & host discovery

------------------------------------------------------------------------

# 9. Internet Archives

-   Wayback Machine
-   Google Cache
-   CDX API

------------------------------------------------------------------------

# 10. Search Automation

Workflow:

`dorks.txt` → Python Script → Google Programmable Search API → Logs →
JSON

Advantages:

-   Repeatable
-   Fast
-   Consistent
-   ToS-compliant

------------------------------------------------------------------------

# 11. Personal Workflow

1.  Google
2.  Advanced Operators
3.  Bing
4.  DuckDuckGo
5.  Wayback
6.  Shodan
7.  Censys
8.  Organize Findings
9.  Confidence Rating
10. Documentation

------------------------------------------------------------------------

# 12. Tag Reference

-   **Recon**
-   **Files**
-   **Documentation**
-   **Research**
-   **Archives**
-   **Infrastructure**
-   **Automation**

------------------------------------------------------------------------

# 13. Ethics

## Always

-   Public information only
-   Passive collection
-   Respect Terms of Service
-   Verify findings
-   Record confidence

## Never

-   Login attempts
-   Credential guessing
-   Exploitation
-   Unauthorized reconnaissance
-   Private information

------------------------------------------------------------------------

**End of Playbook**
