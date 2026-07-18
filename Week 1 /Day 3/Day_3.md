**GOOGLE DORK LIBRARY**

Day 3 Deliverable - 50 Search Operators for Public Document Discovery

| **What this is** | A reusable reference library of Google search operators (dorks) for finding public documents                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Date**         | July 4, 2026                                                                                                                               |
| **Categories**   | PDFs · Excel Sheets · Research Papers · Government Documents                                                                               |
| **Scope note**   | All entries here find publicly indexed, non-sensitive documents. None target exposed credentials, private data, or system vulnerabilities. |

# **How to Use This Library**

Each dork is a starting template - swap the quoted keywords or topic words for whatever you're actually researching. For example, dork #1 as written finds general annual reports; changing it to filetype:pdf "annual report" "Tesla" 2025 narrows it to one company.

_In plain terms: The site: operator accepts wildcards like \*.gov or \*.edu to search an entire category of websites at once, not just one specific domain._

# **1\. Finding PDFs**

| **#** | **Dork**                                   | **What it finds**                   |
| ----- | ------------------------------------------ | ----------------------------------- |
| 1     | filetype:pdf "annual report" 2025          | Company/organization annual reports |
| 2     | filetype:pdf intitle:"whitepaper" AI       | Technical whitepapers on AI         |
| 3     | site:un.org filetype:pdf                   | UN publications and reports         |
| 4     | filetype:pdf "user manual"                 | Product manuals and guides          |
| 5     | filetype:pdf "case study" marketing        | Marketing case studies              |
| 6     | filetype:pdf "market research" 2025        | Market research reports             |
| 7     | filetype:pdf inurl:brochure                | Company/product brochures           |
| 8     | filetype:pdf "meeting minutes"             | Published meeting minutes           |
| 9     | filetype:pdf "press release"               | Archived press releases             |
| 10    | filetype:pdf "financial statement" 2025    | Public financial statements         |
| 11    | filetype:pdf "syllabus" "computer science" | University course syllabi           |
| 12    | filetype:pdf "product catalog"             | Product catalogs                    |
| 13    | filetype:pdf "code of conduct"             | Organizational conduct policies     |

# **2\. Finding Excel Sheets**

| **#** | **Dork**                                | **What it finds**                 |
| ----- | --------------------------------------- | --------------------------------- |
| 14    | filetype:xlsx "budget" 2025             | Public budget spreadsheets        |
| 15    | filetype:xls "inventory list"           | Inventory tracking sheets         |
| 16    | filetype:xlsx "project timeline"        | Project planning sheets           |
| 17    | filetype:csv "open data" dataset        | Open datasets in CSV form         |
| 18    | filetype:xlsx "sales report" template   | Sales report templates            |
| 19    | filetype:xls "financial model" template | Financial modeling templates      |
| 20    | filetype:xlsx site:data.gov             | US government open datasets       |
| 21    | filetype:xlsx "survey results"          | Published survey data             |
| 22    | filetype:xlsx "price list"              | Public pricing sheets             |
| 23    | filetype:csv "population data"          | Demographic/population datasets   |
| 24    | filetype:xlsx "school enrollment" data  | Education enrollment statistics   |
| 25    | filetype:xlsx "audit report"            | Organizational audit spreadsheets |

# **3\. Finding Research Papers**

| **#** | **Dork**                                               | **What it finds**                  |
| ----- | ------------------------------------------------------ | ---------------------------------- |
| 26    | site:arxiv.org filetype:pdf "large language models"    | AI/ML preprints on arXiv           |
| 27    | intitle:"research paper" filetype:pdf "climate change" | Climate research papers            |
| 28    | site:researchgate.net "machine learning"               | Papers hosted on ResearchGate      |
| 29    | filetype:pdf "literature review" psychology            | Psychology literature reviews      |
| 30    | site:scholar.google.com "OSINT"                        | Academic citations on OSINT        |
| 31    | filetype:pdf "conference proceedings" 2025             | Academic conference papers         |
| 32    | intitle:"thesis" filetype:pdf cybersecurity            | Cybersecurity theses/dissertations |
| 33    | filetype:pdf "abstract" "methodology" economics        | Economics research papers          |
| 34    | site:ncbi.nlm.nih.gov "clinical trial"                 | Clinical trial publications (NIH)  |
| 35    | filetype:pdf "peer reviewed" "AI ethics"               | Peer-reviewed AI ethics papers     |
| 36    | site:\*.edu filetype:pdf "dissertation"                | University dissertations           |
| 37    | filetype:pdf "systematic review" healthcare            | Healthcare systematic reviews      |

# **4\. Finding Government Documents**

| **#** | **Dork**                                   | **What it finds**                  |
| ----- | ------------------------------------------ | ---------------------------------- |
| 38    | site:\*.gov filetype:pdf "annual report"   | US federal/state agency reports    |
| 39    | site:\*.gov.in filetype:pdf policy         | Indian government policy documents |
| 40    | site:data.gov filetype:csv                 | US open government datasets        |
| 41    | inurl:gov filetype:pdf "budget report"     | Government budget reports          |
| 42    | site:\*.gov filetype:pdf "public notice"   | Official public notices            |
| 43    | site:\*.gov.uk filetype:pdf "consultation" | UK government consultations        |
| 44    | site:europa.eu filetype:pdf regulation     | EU regulatory documents            |
| 45    | site:\*.gov filetype:xlsx statistics       | Government statistical datasets    |
| 46    | site:un.org filetype:pdf resolution        | UN resolutions                     |
| 47    | site:\*.gov filetype:pdf "meeting minutes" | Public agency meeting minutes      |
| 48    | site:\*.gov.au filetype:pdf report         | Australian government reports      |
| 49    | site:\*.gov filetype:pdf "press release"   | Government press releases          |
| 50    | site:\*.int filetype:pdf treaty            | International treaty documents     |

# **A Note on Ethics**

Every dork in this library only surfaces content that is already publicly indexed by Google - nothing here searches for exposed logins, private databases, leaked credentials, or misconfigured servers. That category of dorking (sometimes called 'Google Hacking' for vulnerability discovery) crosses from OSINT into security testing and requires proper authorization - it's a different discipline with different legal boundaries, and isn't something to practice against systems you don't own or have permission to test.