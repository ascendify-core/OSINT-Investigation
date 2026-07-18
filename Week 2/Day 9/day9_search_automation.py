#!/usr/bin/env python3
"""
search_automation.py — Day 9: Search Automation

Runs a list of Google dorks automatically using the official Google
Programmable Search Engine (Custom Search JSON API), instead of manual
one-by-one searching. Logs every result to a timestamped file.

Why the official API instead of scraping Google directly?
-----------------------------------------------------------
Libraries like `googlesearch-python` work by scraping Google's HTML search
results page directly. That has two problems: (1) it violates Google's
Terms of Service, and (2) Google actively rate-limits and blocks IPs that
do this, so it breaks unpredictably. The Custom Search JSON API is the
supported, ToS-compliant way to automate search — you just need a free
API key and a Programmable Search Engine ID. See the README for setup.

Usage
-----
    # Real run (requires GOOGLE_API_KEY and GOOGLE_CSE_ID env vars):
    python search_automation.py --dorks-file dorks.txt --output results.log

    # Demo run (no API key needed — uses simulated example data so you
    # can see the log format and test the script before getting credentials):
    python search_automation.py --dorks-file dorks.txt --output results.log --demo
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    requests = None  # only required for real (non-demo) runs


GOOGLE_CSE_ENDPOINT = "https://www.googleapis.com/customsearch/v1"

# Google Custom Search API free tier allows 100 queries/day; be a good
# citizen and space requests out even within that limit.
DEFAULT_DELAY_SECONDS = 2.0
DEFAULT_MAX_RESULTS_PER_DORK = 5


def load_dorks(path):
    """Read one dork per line from a text file, skipping blanks/comments."""
    dorks = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            dorks.append(line)
    return dorks


def run_real_query(dork, api_key, cse_id, max_results):
    """Call the real Google Custom Search JSON API for one dork."""
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": dork,
        "num": min(max_results, 10),  # API max is 10 per request
    }
    resp = requests.get(GOOGLE_CSE_ENDPOINT, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    items = data.get("items", [])
    return [
        {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "snippet": item.get("snippet", "").replace("\n", " "),
        }
        for item in items
    ]


def run_demo_query(dork, max_results):
    """
    Simulate a search result set without hitting any network or API.
    Lets you test the script's logging/formatting before you have
    real API credentials.
    """
    time.sleep(0.05)  # tiny pause, just to make the demo feel realistic
    fake_results = []
    for i in range(1, min(max_results, 3) + 1):
        fake_results.append(
            {
                "title": f"[DEMO] Example result {i} for: {dork}",
                "link": f"https://example.com/demo-result-{i}",
                "snippet": "This is simulated placeholder text — no real "
                "search was performed. Run without --demo and with valid "
                "API credentials to get live results.",
            }
        )
    return fake_results


def main():
    parser = argparse.ArgumentParser(
        description="Run a list of Google dorks automatically and log results."
    )
    parser.add_argument(
        "--dorks-file", default="dorks.txt", help="Path to file with one dork per line"
    )
    parser.add_argument(
        "--output", default=None, help="Path to output log file (default: timestamped)"
    )
    parser.add_argument(
        "--max-results", type=int, default=DEFAULT_MAX_RESULTS_PER_DORK,
        help="Max results to fetch per dork (default: %(default)s)",
    )
    parser.add_argument(
        "--delay", type=float, default=DEFAULT_DELAY_SECONDS,
        help="Seconds to wait between queries, to respect rate limits (default: %(default)s)",
    )
    parser.add_argument(
        "--demo", action="store_true",
        help="Run with simulated results — no API key or network needed",
    )
    args = parser.parse_args()

    if not args.demo:
        if requests is None:
            print("ERROR: the 'requests' library is required for real runs. "
                  "Install it with: pip install requests --break-system-packages", file=sys.stderr)
            sys.exit(1)
        api_key = os.environ.get("GOOGLE_API_KEY")
        cse_id = os.environ.get("GOOGLE_CSE_ID")
        if not api_key or not cse_id:
            print("ERROR: set GOOGLE_API_KEY and GOOGLE_CSE_ID environment variables, "
                  "or re-run with --demo to test without credentials. See README.md.", file=sys.stderr)
            sys.exit(1)

    dorks = load_dorks(args.dorks_file)
    if not dorks:
        print(f"No dorks found in {args.dorks_file}", file=sys.stderr)
        sys.exit(1)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = args.output or f"results_{timestamp}.log"
    jsonl_path = output_path.rsplit(".", 1)[0] + ".jsonl"

    mode_label = "DEMO (simulated data, no live search)" if args.demo else "LIVE (Google Custom Search API)"

    all_records = []
    with open(output_path, "w", encoding="utf-8") as log:
        header = (
            f"Search Automation Run\n"
            f"Mode: {mode_label}\n"
            f"Started: {datetime.now(timezone.utc).isoformat()}\n"
            f"Dorks file: {args.dorks_file} ({len(dorks)} queries)\n"
            f"{'=' * 70}\n\n"
        )
        log.write(header)
        print(header)

        for i, dork in enumerate(dorks, start=1):
            print(f"[{i}/{len(dorks)}] Running: {dork}")
            try:
                if args.demo:
                    results = run_demo_query(dork, args.max_results)
                else:
                    results = run_real_query(dork, api_key, cse_id, args.max_results)
            except Exception as exc:  # noqa: BLE001 — log and continue on any single-query failure
                error_block = f"Query #{i}: {dork}\n  ERROR: {exc}\n\n"
                log.write(error_block)
                print(f"  -> ERROR: {exc}")
                all_records.append({"query_num": i, "dork": dork, "error": str(exc)})
                time.sleep(args.delay)
                continue

            block_lines = [f"Query #{i}: {dork}", f"  Results returned: {len(results)}"]
            for r in results:
                block_lines.append(f"  - {r['title']}")
                block_lines.append(f"    {r['link']}")
                block_lines.append(f"    {r['snippet']}")
            block_lines.append("")  # blank line between queries
            log.write("\n".join(block_lines) + "\n")

            all_records.append({"query_num": i, "dork": dork, "results": results})
            print(f"  -> {len(results)} result(s) logged")

            if i < len(dorks):
                time.sleep(args.delay)

        footer = f"\n{'=' * 70}\nFinished: {datetime.now(timezone.utc).isoformat()}\n"
        log.write(footer)

    with open(jsonl_path, "w", encoding="utf-8") as jf:
        for record in all_records:
            jf.write(json.dumps(record) + "\n")

    print(f"\nDone. Human-readable log: {output_path}")
    print(f"Machine-readable log (JSON lines): {jsonl_path}")


if __name__ == "__main__":
    main()
