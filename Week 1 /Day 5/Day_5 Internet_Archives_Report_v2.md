**INTERNET ARCHIVES REPORT**

Comparing Three Archived Websites: Spotify, Anthropic, Resend

| **What this is**    | A guide + template for comparing how three websites at very different company ages have changed over time                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Date**            | July 10, 2026                                                                                                                                                                      |
| **Covers**          | Wayback Machine · Cached Pages · Deleted Websites · Historical Analysis                                                                                                            |
| **Why these three** | A 20-year veteran (Spotify, 2006), a mid-stage AI lab (Anthropic, 2021), and an early-stage startup (Resend, 2022) - three completely different points on the company-age spectrum |

# **1\. What We Wanted to Find Out**

Our question: how have the public websites of Spotify, Anthropic, and Resend changed over time, and what do those changes reveal about each company's stage of growth?

# **2\. Key Concepts**

| **Term**            | **What it means**                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| Wayback Machine     | A free tool at web.archive.org that stores snapshots of public web pages going back to 1996                    |
| Cached page         | A short-lived copy kept by a search engine, useful for very recent changes, unlike Wayback's permanent archive |
| Deleted website     | A page or site no longer live at its original address, but potentially still viewable in an archive            |
| Historical analysis | Comparing snapshots across time to spot when and how something changed                                         |

# **3\. How to Actually Do This**

## **3.1 The simple way - browser only**

- Go to web.archive.org
- Type in a domain, e.g. spotify.com, anthropic.com, or resend.com
- Click any date on the calendar to view the site exactly as it looked then
- Repeat for a few different years per site and compare side by side

## **3.2 The faster way - check availability with one link**

<http://archive.org/wayback/available?url=resend.com>

Paste that into your browser address bar - it returns the closest saved snapshot instantly.

## **3.3 The power-user way - see every snapshot ever taken (CDX API)**

<http://web.archive.org/cdx/search/cdx?url=anthropic.com&from=2021&to=2026>

Swap the domain and year range for spotify.com or resend.com. Each result line gives a timestamp you can plug into a direct snapshot URL:

<http://web.archive.org/web/20210601000000/https://anthropic.com>

_In plain terms: The 14-digit number is just the date and time (YYYYMMDDHHMMSS) of the snapshot. Change those digits to jump to a different point in time._

_Source: archive.org/help/wayback_api.php_

# **4\. What's Already Documented - Background Before You Browse**

Each of these three sites has a very different documented history, which is worth knowing before you start comparing snapshots.

## **4.1 Spotify (founded 2006, site live since 2006-2008)**

Spotify has one of the most thoroughly documented website histories of any company, since design writers have tracked it year by year. Early sign-up pages (2006) were plain, text-heavy, and image-light, built to advertise the desktop app before public launch. The 2008 official launch added early product screenshots. By 2010, mobile app promotion and social login appeared. From roughly 2014 onward, the site adopted parallax scrolling, high-resolution photography, and a redesigned wordmark - a shift led by design agency Collins around 2015, moving Spotify's brand from 'music app' to 'entertainment brand.'

_In plain terms: Spotify's site history shows a company transitioning through recognizable phases: prove the product works (2006-2008) → drive downloads (2008-2011) → mobile-first (2011-2015) → broad lifestyle brand (2015 onward). That's 20 years of visual evolution to compare._

_Source: Prototypr - 'How Spotify's website UX has changed (2006 to 2016)'; Web Design Museum; Fast Company_

## **4.2 Anthropic (founded January 2021, site live since 2021)**

Anthropic's public site history is much shorter and more research-focused early on. The company finished training the first version of Claude in mid-2022 but deliberately delayed release, so the site's early snapshots (2021-early 2023) would show a research-lab framing without any consumer product - no sign-up flow, no pricing. Claude wasn't publicly introduced until March 2023, which is the point where the homepage's purpose would shift from 'about our research' to 'try our product.'

_In plain terms: This is a great one to actually check in the Wayback Machine: compare a snapshot from mid-2021 against one from April 2023. The shift from pure-research messaging to product-launch messaging should be one of the most visible mission-to-market transitions of the three sites, compressed into under two years._

_Source: Wikipedia - Anthropic; Timelines wiki - Timeline of Anthropic_

## **4.3 Resend (founded 2022, site live since ~2022-2023)**

Resend is the youngest and smallest of the three, so its Wayback history will be the thinnest - likely only a handful of snapshots, starting close to its 2023 seed round. Its site has always been narrowly focused on one message ('email API for developers'), unlike Spotify or Anthropic, which both broadened their messaging over time.

_In plain terms: A thin archive history is itself a finding, not a gap - it tells you a company is young enough that its public identity hasn't had time to shift yet. Comparing a company with 20 years of snapshots against one with maybe 2-3 years shows you what 'early-stage footprint' looks like directly in the archive record, not just in funding numbers._

# **5\. Comparison Template - Fill This In As You Browse**

| **Site**      | **Earliest snapshot (approx.)**           | **What to look for across snapshots**                                                   |
| ------------- | ----------------------------------------- | --------------------------------------------------------------------------------------- |
| spotify.com   | 2006 (pre-launch sign-up page)            | Product-proof → download drive → mobile-first → lifestyle brand; note the ~2015 rebrand |
| anthropic.com | 2021 (research-only framing)              | The shift from pure research messaging to product/pricing messaging around March 2023   |
| resend.com    | ~2022-2023 (product-focused from day one) | Whether messaging has broadened as funding/headcount grew, or stayed narrowly focused   |

_In plain terms: The most useful comparisons usually aren't about visual design - they're about messaging. Watch specifically for when a company's stated mission or focus shifts, since that's a real signal of strategic change, not just a redesign._

# **6\. Case Study: Why 'Deleted' Doesn't Always Mean Gone**

A 2025 investigation found that tens of thousands of ChatGPT conversations that users had shared via a public link were later discoverable through the Wayback Machine, even after being removed from search engines and the original hosting company's own visibility. Journalists reported the discovery but deliberately did not publish specific archive links or lookup methods, since the conversations contained sensitive content shared by real people who likely believed sharing was temporary or limited.

_In plain terms: This case captures the entire lesson of 'Deleted Websites' in one story: once something is publicly accessible on the internet, even briefly, an archive can preserve it independently of the original publisher's wishes._

_Source: Digital Digging, Aug 2025 - "ChatGPT Confessions gone? They are not!"_

# **7\. What We Can Conclude**

- Company age is directly visible in archive depth: Spotify's 20-year record shows multiple distinct brand eras, while Resend's short record shows a company that hasn't needed to reinvent its messaging yet.
- Mission-to-product transitions are the most valuable thing to look for - Anthropic's 2021-2023 window is likely the clearest example among the three, since it compresses a research-to-commercial pivot into less than two years.
- The Wayback Machine turns 'the current version of a website' into 'one frame in a long timeline' - most real intelligence value comes from comparing frames, not looking at just one.

# **8\. A Note on Ethics**

The Wayback Machine only archives content that was already publicly accessible at the time of the crawl. Browsing historical snapshots of any public website is a normal, legal research technique. The case study above intentionally avoids naming lookup methods for sensitive personal content, since publicly accessible does not automatically mean appropriate to surface or share further.