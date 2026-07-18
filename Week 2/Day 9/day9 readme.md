# Day 9 — Search Automation

Runs a list of Google dorks automatically instead of typing each one into a
browser by hand, and logs every result to a file. Built around the official
**Google Programmable Search Engine (Custom Search JSON API)**.

## Files in this folder

| File | What it is |
|---|---|
| `search_automation.py` | The script |
| `dorks.txt` | The list of 10 dorks it runs (one per line) — currently the benign, content-discovery dorks from Day 3 |
| `sample_output.log` | A real output from running the script in `--demo` mode (no API key needed) |
| `sample_output.jsonl` | The same run's results in machine-readable JSON-lines format |
| `README.md` | This file |

## ⚠️ Important update — this API is being discontinued

I need to correct something from the original setup instructions: the
**Custom Search JSON API is now closed to new customers**, and Google has
announced it will be **fully discontinued on January 1, 2027**. If you
don't already have an existing Custom Search JSON API setup from before
the cutoff, you will not be able to sign up for one now — the steps below
won't work for a new account.

**What this means for this script:**

- If you already have a working `GOOGLE_API_KEY` / `GOOGLE_CSE_ID` pair
  from before Google closed new signups, the script still works exactly
  as documented below, until the January 2027 shutdown.
- If you're starting fresh, you have two realistic options:
  1. **Google's official recommendation: Vertex AI Search.** This is a
     larger, more enterprise-oriented Google Cloud product (not a drop-in
     API key swap) — worth it if you want to stay in the Google ecosystem
     long-term, but it's a heavier setup than the old CSE API.
  2. **A third-party SERP API** (e.g. SerpAPI, Serper.dev, or similar
     services) — these wrap real Google search results behind their own
     paid API, are usually a much closer drop-in replacement for the code
     structure below (swap the endpoint URL and auth header, keep
     everything else), and don't require a Google Cloud project at all.
     Pricing and specific providers change often, so it's worth checking
     current options rather than treating any one name here as a
     recommendation.

The rest of this README (and the script itself) is written against the
Custom Search JSON API, since that's what's runnable in `--demo` mode
without needing any credentials at all, and the underlying pattern (send
a query, get back title/link/snippet, log it) is the same regardless of
which provider you eventually point it at.

## Why the official API instead of `googlesearch-python`?

`googlesearch-python` (and similar libraries) work by scraping Google's
normal search results page directly. Two problems with that:

1. **It violates Google's Terms of Service** — Google's ToS prohibits
   automated querying of the regular search interface outside their
   supported APIs.
2. **It breaks unpredictably** — Google actively detects and rate-limits
   or blocks IPs that scrape search results this way, so a script built
   on it tends to work fine for a while and then silently stop working.

The **Custom Search JSON API** is Google's actual supported way to
automate search. It's free for up to 100 queries/day, and it returns
clean structured JSON instead of HTML you'd have to parse yourself.

## One-time setup (for real, live runs — existing CSE accounts only, see warning above)

1. Go to the [Google Cloud Console](https://console.cloud.google.com/),
   create a project, and enable the **Custom Search API**.
2. Create an API key under **APIs & Services → Credentials**.
3. Go to [Programmable Search Engine](https://programmablesearchengine.google.com/)
   and create a search engine. Set it to search the entire web (not just
   specific sites). Copy its **Search engine ID** (the `cx` value).
4. Set both as environment variables:

   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   export GOOGLE_CSE_ID="your-search-engine-id-here"
   ```

## Usage

**Demo mode** (no API key needed — uses simulated placeholder results, just
to test the script's logging and formatting works):

```bash
python search_automation.py --dorks-file dorks.txt --output sample_output.log --demo
```

**Live mode** (real results, requires the environment variables above):

```bash
python search_automation.py --dorks-file dorks.txt --output results.log
```

**Other options:**

```bash
--max-results N   # results per dork, default 5 (API max is 10 per request)
--delay N         # seconds between queries, default 2.0 (be a good citizen)
```

## How it works, step by step

1. **Load dorks** — reads `dorks.txt`, one query per line, skipping blank
   lines and lines starting with `#`.
2. **Loop through each dork** — for every query, it either:
   - calls the real Google Custom Search API (`requests.get(...)`), or
   - generates simulated placeholder results (`--demo` mode)
3. **Log every result** in two formats simultaneously:
   - a human-readable `.log` file (title, link, snippet, grouped by query)
   - a machine-readable `.jsonl` file (one JSON object per line — easy to
     load into pandas, jq, or any other tool for further analysis)
4. **Respect rate limits** — waits `--delay` seconds between each query so
   the script doesn't hammer the API (or the search engine, if you ever
   point similar logic at scraping instead — which this script deliberately
   does not do).
5. **Fail gracefully** — if one query errors out (bad syntax, quota
   exceeded, network issue), it logs the error and moves on to the next
   dork rather than crashing the whole run.

## Swapping in a different dork list

The script doesn't care what's in `dorks.txt` — it just runs whatever's
there. To reuse this automation for a different investigation, replace the
file's contents with a different set of dorks (e.g., a company-specific
list from Day 1, or the GHDB-style list from Day 8). Two things worth
keeping in mind if you do:

- **Authorization still applies.** Automating a search doesn't change the
  underlying ethics — a dork that's fine to run once by hand against an
  unauthorized real target doesn't become fine just because it's now
  running in a loop. The same boundaries from Days 3, 7, and 8 apply here.
- **API quotas are small.** The free tier caps out at 100 queries/day —
  automating a large dork list against many results-per-query will burn
  through that fast, so `--max-results` and `--delay` are there to help
  you stay within quota deliberately rather than by accident.
