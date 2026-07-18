# Day 13 -- Domains, WHOIS, Registrar, TLD

## Objective

Understand domain name structure, WHOIS lookups, registrars, and
Top-Level Domains (TLDs), then compare WHOIS information for five
domains.

## Domain Name Structure

Example: **www.google.com**

  Part       Meaning
  ---------- ---------------------------
  `www`      Subdomain
  `google`   Second-Level Domain (SLD)
  `.com`     Top-Level Domain (TLD)

## TLD Types

  Type       Meaning                         Examples
  ---------- ------------------------------- ----------------------------------
  gTLD       Generic Top-Level Domain        `.com`, `.org`, `.net`
  ccTLD      Country Code Top-Level Domain   `.uk`, `.in`, `.jp`, `.ai`
  New gTLD   Newer generic domains           `.app`, `.tech`, `.xyz`, `.shop`

## What is WHOIS?

WHOIS is a public database that provides registration information about
a domain name, including: - Registrar - Creation date - Expiry date -
Name servers - Registrant information (when not hidden by privacy
protection)

## Domains Selected

  Domain          TLD Type
  --------------- ----------------
  google.com      gTLD
  usa.gov         Government TLD
  wikipedia.org   gTLD
  bbc.co.uk       ccTLD
  abc.xyz         New gTLD

## WHOIS Report

  ------------------------------------------------------------------------------------------
  Domain          Registrar      Creation     Expiry Date  Privacy Status Exposed
                                 Date                                     vs. Redacted
  --------------- -------------- ------------ ------------ -------------- ------------------
  google.com      MarkMonitor    1997-09-15   2028-09-14   Privacy        Registrar, dates
                  Inc.                                     Protected      and nameservers
                                                                          visible;
                                                                          registrant details
                                                                          hidden.

  usa.gov         get.gov        1999-08-18   2027-08-18   Redacted       Domain details
                                                                          public;
                                                                          registrant/admin
                                                                          contacts redacted.

  wikipedia.org   MarkMonitor    2001-01-13   2028-01-13   Organization   Wikimedia
                  Inc.                                     Visible        Foundation
                                                                          visible; personal
                                                                          contact details
                                                                          protected.

  bbc.co.uk       British        1994-12-13   2034-12-13   Organization   Organization
                  Broadcasting                             Visible        shown; personal
                  Corporation                                             details not
                                                                          exposed.

  abc.xyz         MarkMonitor    2014-03-21   Varies by    Privacy        Registration
                  Inc.                        renewal      Protected      information
                                                                          visible;
                                                                          registrant contact
                                                                          details protected.
  ------------------------------------------------------------------------------------------

## Observations

-   Large organizations commonly use enterprise registrars such as
    MarkMonitor.
-   Government domains usually redact sensitive contact information.
-   Many organizations use WHOIS privacy protection to prevent public
    exposure of contact details.
-   WHOIS still reveals useful OSINT information such as registrar,
    creation date, expiry date, and nameservers.
-   Different TLDs serve different purposes: gTLDs are generic, ccTLDs
    belong to countries, and new gTLDs provide modern naming options.

## Conclusion

WHOIS is an important OSINT resource because it helps identify who
manages a domain, when it was registered, when it expires, and whether
ownership details are public or protected. Even when registrant
information is hidden, WHOIS remains valuable for understanding a
domain's registration history and technical details.
