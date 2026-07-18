# Day 7 - Advanced Google Dorking

**Date:** July 10, 2026  
**Target:** Resend (resend.com)

## Objective

Practice advanced Google search operators to improve search precision while remaining within passive OSINT. The objective was to discover publicly indexed information about Resend's digital footprint without interacting with any systems or attempting to access restricted resources.

## Advanced Queries Used

| Query                                                 | Purpose                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| site:resend.com filetype:pdf (documentation OR guide) | Locate publicly indexed PDF documentation or guides.         |
| site:resend.com intitle:blog intext:"React Email"     | Find official blog articles discussing React Email.          |
| site:resend.com inurl:docs filetype:pdf               | Search for documentation files.                              |
| site:resend.com "react-email" AROUND(5) SDK           | Find pages where React Email and SDK are discussed together. |
| site:resend.com -site:github.com resend               | Exclude GitHub results.                                      |
| cache:resend.com                                      | Check cached homepage.                                       |
| related:resend.com                                    | Observe similar websites.                                    |
| site:resend.com \* "email API"                        | Find variations of core messaging.                           |
| site:resend.com "2025" filetype:pdf                   | Find 2025 public documents.                                  |
| site:resend.com "login"                               | Observe indexed login pages only.                            |

## Operator Usage

- site:, filetype:, intitle:, inurl:, intext:, AROUND(X), wildcard (\*), cache:, related:, and minus (-) were combined to narrow results.

## High-Confidence Findings

- Public documentation is indexed.
- Official technical blog posts are discoverable.
- Messaging consistently emphasizes 'email API for developers'.
- Documentation pages are indexed.
- Developer resources dominate search results.

## Inferred Findings

- Search exposure is centered on technical documentation.
- Developer education appears prioritized.
- Indexed content aligns with the company's open-source identity.

## What Was Deliberately Not Pursued

- No login attempts.
- No authentication.
- No hidden directory exploration beyond indexed results.
- No vulnerability testing.
- No exploitation or access to non-public information.

## Search Engine Exposure Assessment

- The indexed footprint is focused, clean, and developer-oriented with little unrelated content.

## Conclusion

- Advanced Google operators improve precision while remaining within passive, ethical OSINT practices.